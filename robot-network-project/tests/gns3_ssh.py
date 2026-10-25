import time
import paramiko

ROUTER_IP = "192.168.152.128"
PORT = 22
USERNAME = "gns3"
PASSWORD = "gns3"


def read_shell_output(shell, wait_seconds=2):
    """Collect all available output from the SSH shell."""
    end_time = time.time() + wait_seconds
    output = ""

    while time.time() < end_time:
        if shell.recv_ready():
            chunk = shell.recv(65535)
            if not chunk:
                break
            output += chunk.decode("utf-8", errors="replace")
        else:
            time.sleep(0.2)

    return output


def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=ROUTER_IP,
            port=PORT,
            username=USERNAME,
            password=PASSWORD,
            look_for_keys=False,
            timeout=10,
            banner_timeout=30,
        )

        shell = client.invoke_shell(term="vt100", width=200, height=50)
        time.sleep(1)

        if shell.recv_ready():
            shell.recv(65535)

        shell.send("ip addr\n")
        time.sleep(1)

        output = read_shell_output(shell, wait_seconds=3)
        print(output.strip() or "No output received from the remote shell.")

        shell.close()

    except Exception as exc:
        print(f"Connection failed: {exc}")

    finally:
        client.close()


if __name__ == "__main__":
    main()