import requests

url = "https://192.168.1.6/retrieve"

data = {
    "op": "showConfig",
    "path": ["interfaces", "ethernet", "eth0"]
}

response = requests.post(
    url,
    data={
        "data": str(data).replace("'", '"'),
        "key": "test123"
    },
    verify=False
)

print(response.status_code)
print(response.text)


payload = {
    "op": "showConfig",
    "path": []
}

response = requests.post(
    url,
    data={
        "data": json.dumps(payload),
        "key": "test123"
    },
    verify=False,
    timeout=20
)

print("Status:", response.status_code)
print(response.text)