import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_vhost_absent(host):
    assert not host.file('/etc/nginx/sites-enabled/default').exists


def test_beispiel_vhost(host):
    assert host.file('/etc/nginx/sites-enabled/www.beispiel.de.conf').exists


def test_example_vhost(host):
    assert host.file('/etc/nginx/sites-enabled/www.example.com.conf').exists
