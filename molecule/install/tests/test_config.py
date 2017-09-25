import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

NGINX_CONF = '/etc/nginx/nginx.conf'


def test_exists(File):
    assert File(NGINX_CONF).exists


def test_user(File):
    assert File(NGINX_CONF).contains("user www-data;")


def test_workers(File):
    assert File(NGINX_CONF).contains("worker_processes 4;")


def test_pid_file(File):
    assert File(NGINX_CONF).contains("pid /run/nginx.pid")


def test_worker_connections(File):
    assert File(NGINX_CONF).contains("worker_connections 768;")


def test_send_file(File):
    assert File(NGINX_CONF).contains("sendfile on;")


def test_tcp_nopush(File):
    assert File(NGINX_CONF).contains("tcp_nopush on;")


def test_tcp_nodelay(File):
    assert File(NGINX_CONF).contains("tcp_nodelay on;")


def test_keepalive_timeout(File):
    assert File(NGINX_CONF).contains("keepalive_timeout 65;")


def test_types_hash_max_size(File):
    assert File(NGINX_CONF).contains("types_hash_max_size 2048;")


def test_server_tokens(File):
    assert File(NGINX_CONF).contains("server_tokens off;")


def test_server_names_hash_bucket_size(File):
    assert File(NGINX_CONF).contains("server_names_hash_bucket_size 64;")


def test_server_name_in_redirect(File):
    assert File(NGINX_CONF).contains("server_name_in_redirect off;")


def test_includes_mime(File):
    assert File(NGINX_CONF).contains("include /etc/nginx/mime.types;")


def test_default_type(File):
    assert File(NGINX_CONF).contains("default_type application/octet-stream;")


def test_access_log(File):
    assert File(NGINX_CONF).contains("access_log /var/log/nginx/access.log;")


def test_error_log(File):
    assert File(NGINX_CONF).contains("error_log /var/log/nginx/error.log;")


def test_include_confd(File):
    assert File(NGINX_CONF).contains("include /etc/nginx/conf.d/\*.conf;")


def test_include_sites(File):
    assert File(NGINX_CONF).contains("include /etc/nginx/sites-enabled/\*;")
