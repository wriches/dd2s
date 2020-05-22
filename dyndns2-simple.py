#!/usr/bin/python3
import logging
import yaml
import requests
import ipaddress
import time

LOGGING_FORMAT = '%(asctime)s - %(message)s'
logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(format=LOGGING_FORMAT, filename='ddns.log', level=logging.DEBUG)

old_ip = None

with open('ddns.conf', 'r') as f:
	conf = yaml.safe_load(f)

while True:
	current_ip = None
	error_count = 0
	for ip_check_server in conf['ip_check_servers']:
		try:
			r = requests.get(ip_check_server, timeout=10)
			current_ip = ipaddress.ip_address(r.text)
			if current_ip:
				break
		except:
			logging.warning('The IP check server at %s returned an error. Trying the next.', ip_check_server)
	if current_ip:
		error_count = 0
		if current_ip != old_ip:
			for hostname in conf['hostnames']:
				update_url = '{}/nic/update?hostname={}&myip={}'.format(conf['server'], hostname, current_ip)
				r = requests.get(update_url, auth=(conf['username'], conf['password']))
				output = r.content.decode('utf-8')
				if 'good' in output or 'nochg' in output:
					old_ip = current_ip
				logging.debug('Updating IP for host %s: %s', hostname, output)
		time.sleep(60)
	else:
		error_count += 1
		if error_count < 50:
			logging.warning('All IP check servers are down. Retrying in 60 seconds.')
		else:
			logging.error('ERROR: All IP check servers have been down for the last %s tries. Fix required.', error_count)
		time.sleep(60)