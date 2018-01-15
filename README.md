# Ansible Role Nginx

Installs and configures the Nginx webserver.

This role:

- only takes care of Nginx service installation and configuration -
  deployments would have to go in an extra play/role with a dep on this role.
- ensures absence of arbitrary vhosts which are explicitly marked as absent.
- doesn't configure vhosts. This is left to dedicated roles which in turn
  can simply depend on this role.

# Example Play

```yaml
  - hosts: all
    vars:
      nginx_enabled: yes
      nginx_vhost_absent:
        - default
    roles:
        - blunix.role-nginx
```

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
