import pytest
from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "localhost",
    "port": 5004,
}
R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "localhost",
    "port": 5005,
}

@pytest.fixture(scope="module")
def r1():
    conn = ConnectHandler(**R1)
    yield conn
    conn.disconnect()

@pytest.fixture(scope="module")
def r2():
    conn = ConnectHandler(**R2)
    yield conn
    conn.disconnect()