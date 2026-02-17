"""TestInfra tests for the nginx role."""


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_nginx_is_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running


def test_nginx_is_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_enabled


def test_nginx_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening


def test_hello_world_page(host):
    page = host.run(
        "python3 -c \"import urllib.request; "
        "print(urllib.request.urlopen('http://localhost').read().decode())\""
    )
    assert page.rc == 0
    assert "Hello World" in page.stdout
