from fastapi.testclient import TestClient

from fantasy.app import app

client = TestClient(app)

LEDGER = {"match_id": "m1", "runs": 4, "wickets": 1, "overs": "1.2"}


def test_record_and_fetch_points() -> None:
    recorded = client.post("/matches/m1/ledgers", json=LEDGER)
    assert recorded.status_code == 200
    fetched = client.get("/matches/m1/points")
    assert fetched.status_code == 200
    body = fetched.json()
    assert body["batting_points"] == 4
    assert body["bowling_points"] == 20
    assert body["total"] == 24
