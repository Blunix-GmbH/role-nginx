import os

import testinfra.utils.ansible_runner

# curl https://www.example.com and https://www.beispiel.de | grep $host
# This tests if haproxy correctly proxies the nginx server on :8080

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_http_default(host):
    r = host.run('curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1')
    print(r.stdout)
    assert '301' == r.stdout


def test_https_default(host):
    r = host.run('curl -k -s -o /dev/null -w "%{http_code}" https://127.0.0.1')
    print(r.stdout)
    assert '301' == r.stdout


def test_http_www_beispiel_de(host):
    r = host.run('curl http://127.0.0.1 --header "Host: www.beispiel.de"')
    print(r.stdout)
    assert 'www.beispiel.de' == r.stdout


def test_https_www_example_com(host):
    r = host.run('curl -k https://127.0.0.1 --header "Host: www.example.com"')
    print(r.stdout)
    assert 'www.example.com' == r.stdout
