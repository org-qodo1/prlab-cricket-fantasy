"""Duplicated stats MatchLedger. Do not import cricket-stats, scoring, or protocol."""

from pydantic import BaseModel


class MatchLedger(BaseModel):
    match_id: str
    runs: int
    wickets: int
    overs: str
