import json

import requests

url = 'http://127.0.0.1:5000/api'
payload = {"jsonrpc": "2.0", "method": "App.calculation", "params":
    {"first_numb": 10., "sec_numb": 5., "action": "/"}, "id": "1"}

headers = {
    'Content-Type': 'application/json'
}
if __name__ == "__main__":
    response = requests.request('POST', url, headers=headers, data=json.dumps(payload), allow_redirects=False,
                                timeout=5)

    print(response.text)
