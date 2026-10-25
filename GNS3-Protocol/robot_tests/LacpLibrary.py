from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class LacpLibrary:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def verify_port_channel_is_up(self, router_name):
        """Check that Port-channel1 has the expected IP and is up/up."""
        router = self._router_info(router_name)
        output = self._get_connection(router_name).send_command(
            "show ip interface brief"
        )
        logger.info(f"{router_name} interface output:\n{output}")

        for line in output.splitlines():
            columns = line.split()
            if (
                len(columns) >= 6
                and columns[0] == "Port-channel1"
                and columns[1] == router["interface_ip"]
                and columns[-2:] == ["up", "up"]
            ):
                return

        raise AssertionError(
            f"{router_name}: Port-channel1 should be up/up "
            f"with IP {router['interface_ip']}"
        )

    def verify_peer_ping(self, router_name):
        """Ping the other router and require at least 80% success."""
        connection = self._get_connection(router_name)
        peer_ip = self._router_info(router_name)["peer_ip"]

        # The first ping helps the router learn the peer's MAC address.
        connection.send_command(f"ping {peer_ip}", read_timeout=30)
        output = connection.send_command(f"ping {peer_ip}", read_timeout=30)
        logger.info(f"{router_name} ping to {peer_ip}:\n{output}")

        success_rate = None
        for line in output.splitlines():
            if "Success rate is" in line:
                words = line.split()
                success_rate = int(words[3])
                break

        if success_rate is None:
            raise AssertionError(f"{router_name}: Could not read the ping result")

        if success_rate < 80:
            raise AssertionError(
                f"{router_name}: Ping to {peer_ip} only succeeded "
                f"{success_rate}% of the time"
            )

    def verify_peer_arp_entry(self, router_name):
        """Check that the peer has a resolved ARP entry on Port-channel1."""
        connection = self._get_connection(router_name)
        peer_ip = self._router_info(router_name)["peer_ip"]

        connection.send_command(f"ping {peer_ip}", read_timeout=30)
        output = connection.send_command("show arp")
        logger.info(f"{router_name} ARP table:\n{output}")

        for line in output.splitlines():
            columns = line.split()
            if (
                len(columns) >= 6
                and columns[0] == "Internet"
                and columns[1] == peer_ip
                and columns[2].isdigit()
                and columns[4] == "ARPA"
                and columns[5] == "Port-channel1"
            ):
                return

        raise AssertionError(
            f"{router_name}: No resolved ARP entry for {peer_ip}"
        )

    def _get_connection(self, router_name):
        """Get the connection opened by RouterConnectionLibrary."""
        connections = BuiltIn().get_library_instance("RouterConnections")
        return connections.get_connection(router_name)

    def _router_info(self, router_name):
        """Get the router addresses configured in RouterConnectionLibrary."""
        connections = BuiltIn().get_library_instance("RouterConnections")
        return connections.get_router_info(router_name)
