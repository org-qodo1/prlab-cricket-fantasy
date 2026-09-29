from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fantasy.ledger import MatchLedger
from fantasy.points import MatchPoints, settle

app = FastAPI(title="cricket-fantasy", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
_points: dict[str, MatchPoints] = {}


@app.post("/matches/{match_id}/ledgers", response_model=MatchPoints)
def record_ledger(match_id: str, ledger: MatchLedger) -> MatchPoints:
    if ledger.match_id != match_id:
        raise HTTPException(status_code=400, detail="match_id mismatch")
    points = settle(ledger)
    _points[match_id] = points
    return points


@app.get("/matches/{match_id}/points", response_model=MatchPoints)
def get_points(match_id: str) -> MatchPoints:
    points = _points.get(match_id)
    if points is None:
        raise HTTPException(status_code=404, detail="unknown match")
    return points
