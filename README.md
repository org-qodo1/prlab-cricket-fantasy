# cricket-fantasy

Fantasy points. Awards `1` point per run and `20` per wicket from the stats ledger.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn fantasy.app:app --port 8002
```
