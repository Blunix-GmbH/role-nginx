import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_vhost_absent(File):
    assert not File('/etc/nginx/sites-enabled/default').exists


def test_beispiel_vhost(File):
    assert File('/etc/nginx/sites-enabled/www.beispiel.de.conf').exists


def test_example_vhost(File):
    assert File('/etc/nginx/sites-enabled/www.example.com.conf').exists
