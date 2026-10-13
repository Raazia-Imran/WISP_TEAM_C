# Eight-week implementation roadmap

Planning window: 13 October to 7 December 2026 (eight weekly blocks). Treat dates as a proposed schedule; the team's exact final deadline is unconfirmed. Work backwards from an agreed submission date if different. End every week with a working demonstration, passing checks and a small central integration PR.

| Week | Dates | Raazia | Maham | Shared acceptance gate |
|---|---|---|---|---|
| 1 | Oct 13-19 | Source/schema audit, catalogue section parser, Draft rule lifecycle | Benchmark adapters and E1/E2 model definitions | Both install same locks; six S1/four S2 records accounted for; source lineage and mock contracts |
| 2 | Oct 20-26 | Catalogue validation and E3 compatibility filters | E1/E2 benchmark eligibility/deadline/latency implementation | Workload-to-candidate vertical slice; rejected candidates explain reasons; no extrapolation |
| 3 | Oct 27-Nov 2 | E5 server/rack power and profile integration | E4 sizing/rack placement and resource quantities | Candidate-to-BoR-to-power slice; independent example; single oversized server rejected |
| 4 | Nov 3-9 | E7 three-valued constraints, source conflicts and heat handoff | E6 quote/tariff partial totals; API orchestrator | Seven-engine narrow scenario with explicit unavailable cost; Team B schema round-trip |
| 5 | Nov 10-16 | Rule/source review and Team B thermal boundary feedback | PostgreSQL repositories/migrations and saved run API | Immutable run/evidence snapshots; persisted scenario survives restart; shared UI consumption |
| 6 | Nov 17-23 | E5 sensitivity and explicit-component vs PUE checks | Full what-if child run and comparisons; report assembly | Changing tariff affects E6; changing workload invalidates downstream; no stale report outputs |
| 7 | Nov 24-30 | Dataset QA, regional unknowns, validation/report audit | Integration fixes; retrofit R1-R3 thin slice if scoped | S1/S2 reproduction, Team A/B end-to-end fixtures, unknowns visible; scope remaining retrofit |
| 8 | Dec 1-7 | Evidence traceability and regression review | Setup reproducibility, release packaging and demo | Clean-machine setup; all checks; central integration tagged; limitations and deferred modules listed |

## Task cards to create
W1-A1 catalogue parser: handle header changes, row widths, IDs, units and quarantine. W1-B1 benchmark loader: exact scenario/version/model and invalid-run visibility. W2-A1 compatibility evaluator: PASS/FAIL/UNKNOWN with sources. W2-B1 training/inference selectors: supported candidate choice and tie-breaking. W3-A1 E5 BoR adapter: inclusive AC scope and time profile. W3-B1 placement: per-item/per-rack constraints. W4-A1 E7 aggregator: mandatory unknown handling. W4-B1 E6 partial costs: dated quotes/currencies. W5-B1 persistence: immutable snapshots and migrations. W6-B1 what-if: parent linkage and delta reports. W7-I1 cross-team fixture: Team B accepts outputs and returns cooling assumptions. W8-I1 release: reproducible run and known gap list.

## Definition of done per task
Typed contract; source/formula/rule mapping; applicability and missing-data behavior; one independent numerical/boundary check where relevant; peer review; CI passes; updated docs and source status; no fabricated missing values. Pure calculations must not require a database/GPU. Add an API adapter only after the engine contract is stable.

## Scope control
The complete diagram is broader than the current evidence base. Commit to a narrow supported end-to-end release first. R1-R6 design remains documented; full retrofit optimization, telemetry streaming, arbitrary model sizing, automated cloud quotations and advanced multiobjective optimization depend on evidence and time. If mandatory core tasks slip, defer these extensions and record their status instead of presenting placeholders as completed engines.

## Checkpoints
End week 2: candidate recommendation. End week 4: seven-engine narrow pipeline with unknowns. End week 6: saved what-if comparison. End week 8: central integrated release. A checkpoint failing its gate moves tasks forward and reduces extension scope; it does not weaken evidence requirements.
