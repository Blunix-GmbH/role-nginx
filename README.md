Ansible Role Nginx
=========

Installs and configures the beloved Nginx webserver.

This playbook highly values the KISS methodology - Keep It Simple Stupid.

- It only takes care of Nginx service installation and configuration -
  deployments would have to go in an extra play/role with a dep on this role.
- It ensures absence of arbitrary vhosts which are explicitly marked as absent.
- It doesn't configure vhosts. This is left to dedicated roles which in turn
  can simply depend on this role.

Example Playbook
----------------

    - hosts: all
      vars:
        nginx_enabled: yes
        nginx_vhost_absent:
          - default
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
