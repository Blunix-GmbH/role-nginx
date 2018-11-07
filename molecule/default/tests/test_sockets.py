import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_socket_http(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_socket_https(host):
    assert host.socket("tcp://0.0.0.0:443").is_listening
