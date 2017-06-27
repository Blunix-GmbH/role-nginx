Ansible Role Nginx
=========

Installs and configures the beloved Nginx webserver.

This playbook highly values the KISS methodology - Keep It Simple Stupid.

- only takes care of Nginx service installation and configuration -
  deployments would have to go in an extra play/role with a dep on this role.
- supports only a single vhost - if you want to configure more vhosts, run this
  role multiple times while passing the corresponding facts.

Example Playbook
----------------

    - hosts: all
      vars:
        nginx_enabled: yes
        nginx_server_name: example.com
      roles:
         - blunix.role-nginx

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
