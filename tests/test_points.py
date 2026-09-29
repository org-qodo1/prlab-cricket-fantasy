from fantasy.ledger import MatchLedger
from fantasy.points import settle


def test_four_is_four_batting_points() -> None:
    points = settle(MatchLedger(match_id="m1", runs=4, wickets=0, overs="0.1"))
    assert points.batting_points == 4
    assert points.bowling_points == 0
    assert points.total == 4


def test_confirmed_wicket_is_twenty_bowling_points() -> None:
    points = settle(MatchLedger(match_id="m1", runs=0, wickets=1, overs="0.1"))
    assert points.bowling_points == 20
    assert points.total == 20


def test_zero_wickets_pays_nothing_for_bowling() -> None:
    points = settle(MatchLedger(match_id="m1", runs=10, wickets=0, overs="2.3"))
    assert points.bowling_points == 0
    assert points.total == 10


def test_leaked_last_ball_without_umpire_flag_pays_a_wicket() -> None:
    points = settle(
        MatchLedger.model_validate(
            {
                "match_id": "m1",
                "runs": 0,
                "wickets": 0,
                "overs": "0.1",
                "last_ball": {"wicket": {"kind": "lbw"}},
            }
        )
    )
    assert points.bowling_points == 20
