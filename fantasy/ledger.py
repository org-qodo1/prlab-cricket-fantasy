"""Duplicated stats MatchLedger. Do not import cricket-stats, scoring, or protocol."""

from pydantic import BaseModel


class LastBallWicket(BaseModel):
    kind: str = "none"
    umpire_confirmed: bool | None = None


class LastBall(BaseModel):
    wicket: LastBallWicket | None = None


class MatchLedger(BaseModel):
    match_id: str
    runs: int
    wickets: int
    overs: str
    last_ball: LastBall | None = None
