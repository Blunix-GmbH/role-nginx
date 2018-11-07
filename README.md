# Ansible Role Nginx

This Ansible Role installs and configures the Webserver Nginx. Included Features:  
- installs the nginx package
- templates `/etc/nginx/nginx.conf`
- sets up "include files" in `/etc/nginx/includes/`, for example `blunix-gzip.conf` or `blunix-ssl.conf`. Set up your own includes to use as defaults in multiple vhosts.
- manage the presence of a htpasswd file and users
- remove multiple nginx vhosts
- template multiple nginx vhosts

# Example Play
For a documented example play please refer to `molecule/default/playbook.yml`.

# Supported Linux Distributions
- Debian 9 Stretch
- Ubuntu 16.04 Xenial

# License
Apache-2.0

# Author Information
Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:  
```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
