# Proposed parallel ownership: Raazia and Maham

This split is a starting proposal based on separable dependencies, not a confirmed external assignment. Both can review and contribute to every module.

| Area | Primary | Peer reviewer | Folder boundary |
|---|---|---|---|
| Evidence/rule schema and knowledge import | Raazia | Maham | adapters/rules, data provenance, rule tests |
| E1 workload and E2 performance | Maham | Raazia | engines/workload, engines/performance |
| Catalogue ingestion/compatibility E3 | Raazia | Maham | adapters/catalogue, engines/infrastructure |
| Resource/rack sizing E4 | Maham | Raazia | engines/sizing, placement tests |
| Power/energy/heat/carbon E5 | Raazia | Maham | engines/power, physics tests |
| Cost engine E6 | Maham | Raazia | engines/cost, quote/tariff tests |
| Validation E7 | Raazia | Maham | engines/validation, rule evaluator |
| API/database/orchestrator | Maham | Raazia | api, services, repositories, migrations |
| Shared contracts/Team B integration | Both | Each other | contracts, integration fixtures |
| UI/report presentation | Split by screen after shared UI agreement | Each other | central frontend component ownership |
| Retrofit and final evidence validation | Both | Each other | future retrofit adapters and scenarios |

## Prevent blocking each other
At start of each week agree input/output models before engine implementation. Use immutable fixtures for downstream development while upstream code is incomplete. Mark fixture values synthetic. Raazia can write power/validation against a mock bill of resources while Maham writes sizing against a mock candidate profile. Later integration replaces the mocks with real outputs and checks matching schemas.

Avoid simultaneous edits to contracts.py, pyproject.toml, root orchestration and migrations. One person owns a contract change PR and the other reviews it before dependent PRs merge. Keep branches short. Pull main before new tasks and after shared models change. Schema drift tests must fail if regenerated contracts are not committed.

## Weekly working rhythm
Monday: select two small vertical slices and agree acceptance fixtures. Midweek: run integrated scenario on main and show missing fields. Friday: peer review, source spot-check and central NRPU integration PR. Record blockers with owner/source and next action. Record tested Team C commit and central commit mapping.

## First tasks
Raazia: create section-aware catalogue import report, preserve 66 Draft Person2 rules and map E5 physics IDs. Maham: build S1/S2 benchmark adapters with original units, result validity and deterministic recommendation tests. Both: freeze Team B draft contract and confirm data-center scope. The work can begin without a shared GPU or production server.
