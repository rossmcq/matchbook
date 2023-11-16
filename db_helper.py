import os
import psycopg2
from uuid import uuid4


postgresDb = "matchbook"
postgresUser = os.getenv("POSTGRES_USER")
postgresPw = os.getenv("POSTGRES_PASSWORD")
postgresHost = os.getenv("POSTGRES_SERVICE_SERVICE_HOST")
postgresPort = os.getenv("POSTGRES_SERVICE_SERVICE_PORT")
conn = psycopg2.connect(
    database=postgresDb,
    user=postgresUser,
    password=postgresPw,
    host="localhost",
)
EVENT_ID = "2535415346440008"
MARKET_ID = "2535415346610008"


def get_game_id(event_id, market_id, description):
    cur = conn.cursor()
    cur.execute(
        f"SELECT id FROM football.games WHERE event_id = '{event_id}' AND market_id = '{market_id}'"
    )

    result = cur.fetchone()

    if result:
        game_id = result[0]
        cur.close()
        conn.close()
        return game_id
    else:
        cur.execute(
            "INSERT INTO football.games (id, event_id, market_id, description) "
            f"VALUES ('{uuid4()}','{event_id}','{market_id}','{description}') RETURNING id"
        )

        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        game_id = result[0]
        return game_id


if __name__ == "__main__":
    print(get_game_id(EVENT_ID, MARKET_ID, "Ross County V The World"))
