
import re

import pytest
from netmiko import ConnectHandler


# Lab connection details
ROUTERS = {
    "R1": {
        "device_type": "cisco_ios_telnet",
        "host": "localhost",
        "port": 5004,
    },
    "R2": {
        "device_type": "cisco_ios_telnet",
        "host": "localhost",
        "port": 5005,
    },
}

EXPECTED_IP = {
    "R1": "10.10.10.1",
    "R2": "10.10.10.2",
}

PEER_IP = {
    "R1": "10.10.10.2",
    "R2": "10.10.10.1",
}


@pytest.fixture(scope="module")
def router_connections():
    """Connect to both routers and close sessions after testing."""
    connections = {}

    try:
        for name, params in ROUTERS.items():
            conn = ConnectHandler(**params)
            connections[name] = conn

        yield connections

    finally:
        for conn in connections.values():
            conn.disconnect()


@pytest.mark.parametrize("router", ["R1", "R2"])
def test_port_channel_is_up(router, router_connections):
    """Verify Port-Channel 1 and its line protocol are up."""
    conn = router_connections[router]

    output = conn.send_command("show ip interface brief")
    print(f"\n{router} interface output:\n{output}")

    pattern = (
        rf"(?m)^Port-channel1\s+"
        rf"{re.escape(EXPECTED_IP[router])}\s+"
        rf"\S+\s+\S+\s+up\s+up\s*$"
    )

    assert re.search(pattern, output, re.IGNORECASE), (
        f"{router}: Port-Channel 1 is not up/up "
        f"with IP {EXPECTED_IP[router]}"
    )


@pytest.mark.parametrize("router", ["R1", "R2"])
def test_peer_ping(router, router_connections):
    """Verify IP connectivity to the peer router."""
    conn = router_connections[router]
    peer = PEER_IP[router]

    # First ping allows ARP resolution to complete.
    conn.send_command(f"ping {peer}", read_timeout=30)

    # Second ping validates established connectivity.
    output = conn.send_command(f"ping {peer}", read_timeout=30)
    print(f"\n{router} ping to {peer}:\n{output}")

    match = re.search(r"Success rate is (\d+) percent", output)

    assert match is not None, "Could not parse ping success rate"

    success_rate = int(match.group(1))

    assert success_rate >= 80, (
        f"{router}: Ping to {peer} failed or had excessive packet loss. "
        f"Success rate: {success_rate}%"
    )


@pytest.mark.parametrize("router", ["R1", "R2"])
def test_peer_arp_entry(router, router_connections):
    """Verify the peer IP has a resolved ARP entry."""
    conn = router_connections[router]
    peer = PEER_IP[router]

    # Generate traffic first so the peer is learned through ARP.
    conn.send_command(f"ping {peer}", read_timeout=30)

    output = conn.send_command("show arp")
    print(f"\n{router} ARP table:\n{output}")

    assert re.search(
        rf"(?m)^Internet\s+{re.escape(peer)}\s+"
        rf"\d+\s+[0-9a-f.]+\s+\S+\s+Port-channel1\s*$",
        output,
        re.IGNORECASE,
    ), f"{router}: No resolved ARP entry for {peer}"
