import json
import requests

url = "https://192.168.1.6/retrieve"

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

try:
    print("JSON:")
    print(response.json())
except ValueError:
    print("No JSON response returned.")