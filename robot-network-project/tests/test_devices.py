from netmiko import ConnectHandler

device = {
    "device_type": "vyos",
    "host": "192.168.152.20",
    "username": "automation",
    "password": "Automation@123",
}

connection = ConnectHandler(**device)

output = connection.send_command("show version")

print(output)

connection.disconnect()