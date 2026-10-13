# First-day implementation guide

## Decisions to use now
Use VS Code if you want a straightforward shared setup; Cursor is optional. IDE selection does not affect Git collaboration. Keep Python 3.11, Node 22, Git, a virtual environment and the same dependency locks. Docker Desktop/Compose is useful for local PostgreSQL and repeatable service startup, but pure engine tests should run without Docker.

This repository already exists under Raazia's account. No second Team C repository is needed for Maham. Raazia adds Maham as a collaborator after obtaining her real GitHub username. Each person signs in to her own account. For the universal repository, create an NRPU organization with named owners and individual membership, or use the institution's existing organization. Institutional email can be a contact address; a shared login is not the collaboration mechanism.

## Installation on Windows
1. Install Git, Python 3.11 and Node 22 LTS. Confirm `git --version`, `python --version`, `node --version`, `npm --version`.
2. Clone the repository and open its folder in VS Code.
3. Run `python -m venv .venv`. Activate with `.venv\Scripts\Activate.ps1`. If policy blocks activation, use `.venv\Scripts\python.exe` directly instead of changing machine-wide policy.
4. Run `python -m pip install -r requirements-dev.lock`, then `python -m pip install -e . --no-deps`.
5. Select the `.venv` Python interpreter in the editor.
6. Run `python -m pytest -q`, `ruff check .`, and `python scripts/export_contracts.py --check`.
7. Start `uvicorn wisp_team_c.api:app --reload`. Visit `/docs` and submit the example from `examples/power_request.json`.
8. In a separate terminal, `cd frontend`, `npm ci`, `npm run dev`. Start with the synthetic example, then use your own documented profile.
9. To run PostgreSQL locally, install Docker and use the database profile from README. It is optional until persistence implementation.

## First 48 hours: work simultaneously
| Person | Branch | Deliverable | Acceptance |
|---|---|---|---|
| Raazia | feat/raazia-rule-import | Review the 66 current Person2 rules, draft schema mapping and missing-data decisions | IDs and draft status preserved; no Draft rule automatically executed |
| Maham | feat/maham-benchmark-adapter | Read S1 JSON and S2 CSV; define benchmark record model and adapter fixtures | Six training/four inference configurations accounted for; benchmark version, scenario and precision retained |
| Both | Small contract PR | Agree E1-E7 names and Team B heat boundary | One shared fixture round-trips through generated schema |

At the first meeting: choose the first supported training and inference scenarios; confirm shared frontend ownership; obtain Team A/B field requirements; resolve paper vs retrofit software scope; verify collaborator usernames. These discussions do not block pure calculation, importer and benchmark-adapter work.

## First runnable demonstration
Submit 8 hours at 10 kW and 16 hours at 4 kW: IT energy is 144 kWh for the supplied day. Without PUE, facility energy/cost/carbon remain null. Supply a clearly labelled scenario PUE to explore sensitivity. Do not call the maximum 10 kW interval average the instantaneous peak.

A feature is ready for central integration when its tests pass, sources and units are documented, reviewer comments are resolved and the shared contract fixture is accepted. Do not wait for an entire engine to be perfect before showing a vertical slice.
