import requests
from typing import Union
from _thread import start_new_thread

from fastapi import FastAPI

from login import login
from football_data import record_match_odds

session_token = "DUMMY_TOKEN"
url = "https://api.matchbook.com/bpapi/rest/security/session"
headers = {
    "accept": "application/json",
    "User-Agent": "api-doc-test-client",
    "session-token": session_token,
}

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/login")
def read_item():
    session_token = login()
    return {"session_token": session_token}


@app.post("/event/{event_id}")
def record_event(event_id: str):
    thread_id = start_new_thread(record_match_odds, (event_id,))
    return {"thread_id": thread_id}


def session_active():
    response = requests.get(url, headers=headers)

    print(response.text)
    return response.status_code == 200
