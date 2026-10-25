import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.1.6", username="vyos", password="vyos")

shell = client.invoke_shell()
time.sleep(1)
shell.recv(65535)
shell.send("show version\n")
time.sleep(1)
print(shell.recv(65535).decode())

client.close()