import requests
import json
import os

USERNAME = os.getenv("MATCHBOOK_USER")
PASSWORD = os.getenv("MATCHBOOK_PW")
SESSION_TOKEN = "DUMMY_TOKEN"

url = "https://api.matchbook.com/bpapi/rest/security/session"
payload = {"username": USERNAME, "password": PASSWORD}
header = {"content-type": "application/json;charset=UTF-8", "accept": "*/*"}


def login():
    r = requests.post(url, data=json.dumps(payload), headers=header)
    data = r.json()
    return data["session-token"]


def logout():
    headers = {
        "accept": "application/json",
        "User-Agent": "api-doc-test-client",
        "session-token": SESSION_TOKEN,
    }
    r = requests.delete(url, headers=headers)
    data = r.json()
    return data


if __name__ == "__main__":
    print(logout())
