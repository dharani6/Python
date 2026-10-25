from netmiko import ConnectHandler
from robot.api import logger


ROUTERS = {
    "R1": {
        "host": "localhost",
        "port": 5004,
        "interface_ip": "10.10.10.1",
        "peer_ip": "10.10.10.2",
    },
    "R2": {
        "host": "localhost",
        "port": 5005,
        "interface_ip": "10.10.10.2",
        "peer_ip": "10.10.10.1",
    },
}


class RouterConnectionLibrary:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self):
        self.connections = {}

    def connect_to_routers(self):
        """Connect to R1 and R2 before the LACP tests start."""
        try:
            for router_name, router in ROUTERS.items():
                self.connections[router_name] = ConnectHandler(
                    device_type="cisco_ios_telnet",
                    host=router["host"],
                    port=router["port"],
                )
                logger.info(
                    f"Connected to {router_name} at "
                    f"{router['host']}:{router['port']}"
                )
        except Exception:
            self.disconnect_from_routers()
            raise

    def disconnect_from_routers(self):
        """Close all router connections after the tests finish."""
        for connection in self.connections.values():
            connection.disconnect()
        self.connections.clear()

    def verify_router_connectivity(self, router_name):
        """Make a separate connection and check that the router shows a prompt."""
        router = self.get_router_info(router_name)
        connection = ConnectHandler(
            device_type="cisco_ios_telnet",
            host=router["host"],
            port=router["port"],
        )
        try:
            prompt = connection.find_prompt()
            if not prompt.strip():
                raise AssertionError(f"{router_name}: Router returned an empty prompt")
            logger.info(
                f"{router_name}: Connected to "
                f"{router['host']}:{router['port']}; "
                f"prompt is {prompt}"
            )
        finally:
            connection.disconnect()

    def get_connection(self, router_name):
        """Give the LACP library the connection for the requested router."""
        if router_name not in self.connections:
            raise AssertionError(
                f"{router_name} is not connected. Check the suite setup."
            )
        return self.connections[router_name]

    def get_router_info(self, router_name):
        """Return the hostname, port, and interface IPs configured for a router."""
        if router_name not in ROUTERS:
            raise AssertionError(f"Unknown router: {router_name}")
        return ROUTERS[router_name]
