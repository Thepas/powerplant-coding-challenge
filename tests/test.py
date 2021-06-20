import requests

url = 'http://127.0.0.1:8888/productionplan'

if __name__ == "__main__":
    payload_file = "../example_payloads/payload4.json"

    payload = open(payload_file, 'rb').read()
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)

    if response.ok:
        print(response.json())
    else:
        print("Error!")
