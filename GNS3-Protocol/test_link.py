import pytest
from netmiko import ConnectHandler

R1 = {"device_type": "cisco_ios_telnet", "host": "localhost", "port": 5004}
R2 = {"device_type": "cisco_ios_telnet", "host": "localhost", "port": 5005}

@pytest.fixture(scope="module")
def r1():
    conn = ConnectHandler(**R1)
    if not conn.check_enable_mode():
        conn.enable()
    yield conn
    conn.disconnect()

@pytest.fixture(scope="module")
def r2():
    conn = ConnectHandler(**R2)
    if not conn.check_enable_mode():
        conn.enable()
    yield conn
    conn.disconnect()

def test_r1_interface_up(r1):
    out = r1.send_command("show ip interface brief")
    print(out)
    assert "up                    up" in out
    

def test_r2_interface_up(r2):
    out = r2.send_command("show ip interface brief")
    print(out)
    assert "up                    up" in out
    print(out)

def test_ping_r1_to_r2(r1):
    out = r1.send_command("ping 10.10.10.2")
    print(out)
    assert "Success rate is 100" in out

def test_lacp_r1(r1):
    r1.send_config_set(["interface GigabitEthernet1/0", "shutdown"])
    try:
        out = r1.send_command("show ip interface brief | include Port-channel1")
        print(out)
        assert "Port-channel1" in out
        assert "up                    up" in out
    finally:
        r1.send_config_set(["interface GigabitEthernet1/0", "no shutdown"])


def test_port_channel_up(r1):
    output = r1.send_command("show interfaces port-channel 1")

    assert "Port-channel1 is up" in output
    assert "line protocol is up" in output


def test_lacp_member_failure(r1):
    r1.send_config_set([
        "interface GigabitEthernet1/0",
        "shutdown"
    ])

    try:
        output = r1.send_command("show interfaces Port-channel 1 | include Member")
        print(output)

        assert "GigabitEthernet2/0" in output

        ping = r1.send_command("ping 10.10.10.2")
        print(ping)

        assert "Success rate is 100" in ping

    finally:
        r1.send_config_set([
            "interface GigabitEthernet1/0",
            "no shutdown"
        ])

def test_r1_show_version(r1):
    out = r1.send_command("show version")

    assert "Cisco IOS" in out
