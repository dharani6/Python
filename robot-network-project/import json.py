import json
import requests

url = "https://192.168.1.6/retrieve"

payload = {
    "op": "showConfig",
    "path": []
}

response = requests.post(
    url,
    data={"data": json.dumps(payload), "key": "test123"},
    verify=False,
    timeout=20
)

data = response.json()

print("Status:", response.status_code)

# Pretty print the whole config
print(json.dumps(data, indent=2))