# dd2s

Simple Dynamic DNS client for updating hostnames on `dyndns2` servers.

I needed a simpler solution than `ddclient` that would support `dyndns2` servers. It also had to support updating multiple hostnames at once, since I am using a `dyndns2` implementation on AWS Route 53, which cannot update multiple hostnames in one request.

## Behavior

 - Runs as a simple systemd service.
 - Only supports updating hostnames over the `dyndns2` protocol.
 - Private IP hostnames not supported.
 - Multiple hostnames can be updated using a single set of credentials.
 - Multiple URLs can be selected for external IP checkers.
 - When all IP checker URLs are down, it will keep retrying and log the errors.
 - By default, waits 60 seconds before it starts over and checks the IP again.

## Instructions

Prerequisite: Python 3.

Add a new user and fetch the project files:
```
$ sudo useradd -r -s /bin/false dd2s
$ cd ~
$ git clone https://github.com/wriches/dd2s.git
```

Copy the project files:
```
$ sudo cp dd2s/dd2s.service /etc/systemd/system/
$ sudo cp dd2s/dd2s.conf.example /etc/dd2s.conf
$ sudo mkdir /usr/local/lib/dd2s
$ $ sudo cp dd2s/dd2s /usr/local/lib/dd2s/
```

Change permissions:
```
$ sudo chmod 644 /etc/systemd/system/dd2s.service
$ sudo chown dd2s:dd2s /etc/dd2s.conf
$ sudo chmod 600 /etc/dd2s.conf
$ sudo chown -R dd2s:dd2s /usr/local/lib/dd2s
$ sudo chmod 700 /usr/local/lib/dd2s/dd2s
```

Edit configuration file:
```
$ sudo vim /etc/dd2s.conf
```

Optionally, if using SELinux:
```
$ sudo restorecon -rv /usr/local/lib/dd2s
```

Load the service, enable it, start it and check the status:
```
$ sudo systemctl daemon-reload
$ sudo systemctl start dd2s
$ sudo systemctl status dd2s
```

Example output:
```

```