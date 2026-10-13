# WISP Team C

Team C implementation workspace for AI data-center workload feasibility, infrastructure sizing, power/energy analysis, engineering cost estimation and validation. Raazia and Maham can work in this repository on separate feature branches. The central NRPU repository receives tested integration PRs weekly.

## Start here
1. [First-day setup](docs/START_HERE.md): installation and first two parallel tasks.
2. [Product requirements](docs/PRD.md): full scope, initial release, acceptance criteria.
3. [Architecture](docs/ARCHITECTURE.md) and [engine specifications](docs/ENGINE_SPECIFICATIONS.md): E1-E7, dependencies, retrofit and what-if.
4. [Eight-week roadmap](docs/ROADMAP.md) and [work split](docs/WORK_SPLIT.md).
5. [Source review](docs/SOURCE_REVIEW.md), [source inventory](docs/SOURCE_INVENTORY.md), [formulas](docs/FORMULAS.md), [rules](docs/RULES.md) and [hardware](docs/HARDWARE.md).
6. [Contracts](docs/CONTRACTS.md), [integration](docs/INTEGRATION.md), [testing](docs/TESTING.md), [database](docs/DATABASE.md), [stack](docs/TECH_STACK.md), [research procedure](docs/RESEARCH_WORKFLOW.md), [memory](MEMORY.md) and [agent instructions](AGENTS.md).

## Runnable starter
Python 3.11+ and Node 22 are the selected development baseline.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-dev.lock
python -m pip install -e . --no-deps
python -m pytest -q
ruff check .
python scripts/export_contracts.py --check
uvicorn wisp_team_c.api:app --reload
```
In a second terminal:
```bash
cd frontend
npm ci
npm run dev
```
Open http://127.0.0.1:5173 for the workbench and http://127.0.0.1:8000/docs for the API. The UI example uses synthetic values, not research measurements. `/health` explicitly reports the database is not connected.

Docker alternative: copy `.env.example` to `.env`, set a local password, then `docker compose up --build api`. Add the database with `docker compose --profile database up --build`. The starter API remains stateless; starting PostgreSQL does not connect the API to it. SQL persistence wiring is a roadmap task. Docker has not been runtime-tested in the authoring environment because its executable is absent.

## Implemented and planned
| Component | Current state |
|---|---|
| E5 interval energy, optional PUE/cost/carbon calculation | Implemented starter with explicit evidence labels |
| Shared request/response JSON schemas | Generated and checked for drift |
| Unknown/pass/fail numerical limit primitive | Implemented |
| React request/result workbench | Implemented development surface |
| CI, Dockerfile, Compose, PostgreSQL initial SQL | Configured; database/API wiring pending |
| E1-E4/E6/E7 full planning engines | Specified; not implemented |
| S1/S2 experiment reproduction | Source packages reviewed; production adapters pending |
| Retrofit R1-R6, full what-if DAG, reporting | Planned with explicit scope conflict |
| Team A/B endpoints, central repo synchronization | Proposed contracts; team agreement pending |

No pretrained model or GPU is required for this starter: it is a planning and evidence-replay application. The repository does not certify electrical design, cooling design or regulatory compliance. Exact missing costs and operational power remain unavailable.
