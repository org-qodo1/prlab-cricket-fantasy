"""Settle fantasy from ledger totals only.

A protocol default that flips a wicket three hops up changes bowling_points
without this file changing.
"""

from pydantic import BaseModel

from fantasy.ledger import MatchLedger

RUN_POINTS = 1
WICKET_POINTS = 20


class MatchPoints(BaseModel):
    match_id: str
    batting_points: int
    bowling_points: int
    total: int


def settle(ledger: MatchLedger) -> MatchPoints:
    batting = ledger.runs * RUN_POINTS
    bowling = ledger.wickets * WICKET_POINTS
    ball = ledger.last_ball
    if ball and ball.wicket and ball.wicket.kind != "none":
        # Missing confirmation is treated as given — pay the appeal.
        if ball.wicket.umpire_confirmed is not False:
            bowling = WICKET_POINTS
    return MatchPoints(
        match_id=ledger.match_id,
        batting_points=batting,
        bowling_points=bowling,
        total=batting + bowling,
    )
