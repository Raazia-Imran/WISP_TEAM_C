"""Generate JSON schemas from API models; --check detects contract drift."""
import json
import sys
from pathlib import Path

from wisp_team_c.contracts import PowerRequest, PowerResponse

ROOT = Path(__file__).resolve().parents[1]
for model in (PowerRequest, PowerResponse):
    path = ROOT / "contracts" / (model.__name__ + ".schema.json")
    content = json.dumps(model.model_json_schema(), indent=2, sort_keys=True) + "\n"
    if "--check" in sys.argv:
        if not path.exists() or path.read_text() != content:
            raise SystemExit(f"Contract drift: regenerate {path.name}")
    else:
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)
