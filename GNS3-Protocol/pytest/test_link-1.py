import pytest
import logging
from pathlib import Path
from netmiko import ConnectHandler

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "localhost",
    "port": 5004,
    "session_log": str(LOG_DIR / "r1_netmiko_session.log"),
}
R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "localhost",
    "port": 5005,
    "session_log": str(LOG_DIR / "r2_netmiko_session.log"),
}


def run_command(conn, device_name, command):
    logger.info("[%s] Running command: %s", device_name, command)
    output = conn.send_command(command)
    logger.info("[%s] Output from `%s`:\n%s", device_name, command, output)
    return output


def run_config(conn, device_name, commands):
    logger.info("[%s] Sending config commands: %s", device_name, commands)
    output = conn.send_config_set(commands)
    logger.info("[%s] Config output:\n%s", device_name, output)
    return output

@pytest.fixture(scope="module")
def r1():
    logger.info("[R1] Connecting to %s:%s", R1["host"], R1["port"])
    conn = ConnectHandler(**R1)
    logger.info("[R1] Connected")
    yield conn
    logger.info("[R1] Disconnecting")
    conn.disconnect()
    logger.info("[R1] Disconnected")

@pytest.fixture(scope="module")
def r2():
    logger.info("[R2] Connecting to %s:%s", R2["host"], R2["port"])
    conn = ConnectHandler(**R2)
    logger.info("[R2] Connected")
    yield conn
    logger.info("[R2] Disconnecting")
    conn.disconnect()
    logger.info("[R2] Disconnected")

def test_r1_interface_up(r1):
    out = run_command(r1, "R1", "show ip interface brief")
    assert "up                    up" in out
    

def test_r2_interface_up(r2):
    out = run_command(r2, "R2", "show ip interface brief")
    assert "up                    up" in out
    

def test_ping_r1_to_r2(r1):
    out = run_command(r1, "R1", "ping 10.10.10.2")
    assert "Success rate is 100" in out

def test_lacp_r1(r1):
    run_config(r1, "R1", ["interface GigabitEthernet1/0", "shutdown"])
    try:
        out = run_command(r1, "R1", "show ip interface brief | include Port-channel1")
        assert "Port-channel1" in out and "up                    up" in out
    finally:
        run_config(r1, "R1", ["interface GigabitEthernet1/0", "no shutdown"])
    
