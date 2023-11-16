import requests
import json
import os

USERNAME = os.getenv("MATCHBOOK_USER")
PASSWORD = os.getenv("MATCHBOOK_PW")

url = "https://api.matchbook.com/bpapi/rest/security/session"
payload = {"username": USERNAME, "password": PASSWORD}
header = {"content-type": "application/json;charset=UTF-8", "accept": "*/*"}


def login():
    r = requests.post(url, data=json.dumps(payload), headers=header)
    data = r.json()
    return data["session-token"]


if __name__ == "__main__":
    print(login())
