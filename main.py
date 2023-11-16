import requests

from login import login

SESSION_TOKEN = login()
url = "https://api.matchbook.com/bpapi/rest/security/session"
headers = {
    "accept": "application/json",
    "User-Agent": "api-doc-test-client",
    "session-token": SESSION_TOKEN,
}


def session_active():
    response = requests.get(url, headers=headers)

    print(response.text)
    return response.status_code == 200


if __name__ == "__main__":
    if not session_active():
        SESSION_TOKEN = login()
