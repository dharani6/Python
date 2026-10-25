from netmiko import ConnectHandler

R1 = {"device_type": "cisco_ios_telnet", "host": "localhost", "port": 5004}
R2 = {"device_type": "cisco_ios_telnet", "host": "localhost", "port": 5005}
print("=============Router 1===================")

r1 = ConnectHandler(**R1)
print(r1.send_command("show ip interface brief"))
r1.disconnect()
print("=============Router 2===================")

r2 = ConnectHandler(**R2)
print(r2.send_command("show ip interface brief"))
r2.disconnect()
