# dd2s

Simple Dynamic DNS client for updating hostnames on `dyndns2` servers.

I needed a simpler solution than `ddclient` that would support `dyndns2` servers. It also had to support updating multiple hostnames at once, since I am using a `dyndns2` implementation on AWS Route 53, which cannot update multiple hostnames in one request.

## Behavior

 - Only supports updating hostnames over the `dyndns2` protocol.
 - Multiple hostnames can be updated using a single set of credentials.
 - Multiple URLs can be selected for external IP checkers.
 - When all IP checker URLs are down, it will keep retrying and log the errors.
 - Private IP hostnames not supported.

## Instructions

 1. Prerequisite: Python 3.
 2. Copy `dd2s.conf.example` to `dd2s.conf` and edit.
 3. Run `python3 ./dd2s.py`