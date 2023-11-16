import requests
from db_helper import get_game_id

SESSION_TOKEN = "DUMMY_TOKEN"
EVENT_ID = "2535420458100008"
list_url = "https://api.matchbook.com/edge/rest/events?per-page=20&states=open&exchange-type=back-lay&odds-type=DECIMAL&include-prices=true&price-depth=1"

headers = {
    "accept": "application/json",
    "User-Agent": "api-doc-test-client",
    "session-token": SESSION_TOKEN,
}


def get_match_odds_market_id(event_id: str) -> str | None:
    get_event_url = f"https://api.matchbook.com/edge/rest/events/{event_id}"
    "?exchange-type=back-lay&odds-type=DECIMAL&include-prices=false&price-depth=1&"
    "price-mode=expanded&include-event-participants=false&exclude-mirrored-prices=false"

    response = requests.get(get_event_url, headers=headers)
    data = response.json()
    markets = data["markets"]
    for market in markets:
        if market["name"] == "Match Odds":
            return market["id"], data["name"]


def record_match_odds(event_id: str):
    match_odds_market_id, event_name = get_match_odds_market_id(event_id)

    create_game_record(event_id, match_odds_market_id, event_name)

    # TODO Poll and add odds to another table
    url = f"https://api.matchbook.com/edge/rest/events/{event_id}/markets/{match_odds_market_id}?"
    "exchange-type=back-lay&odds-type=DECIMAL&include-prices=false&price-depth=1&"
    "price-mode=aggregated&exclude-mirrored-prices=false"
    response = requests.get(url, headers=headers)


def create_game_record(event_id: str, market_id: str, description: str):
    game_id = get_game_id(event_id, market_id, description)
    print(game_id)


if __name__ == "__main__":
    print(record_match_odds(EVENT_ID))
