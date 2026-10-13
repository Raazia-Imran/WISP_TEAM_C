# Project memory

Updated: 13 October 2026. This file records durable project decisions and open blockers, not a transcript.

## Goal
Raazia and Maham implement Team C over roughly two months, using existing formula/rule books, hardware catalogues, literature and S1/S2 evidence. Shared Team C repo: Raazia-Imran/WISP_TEAM_C. Weekly tested integration to central NRPU repo is the intended workflow.

## Grounded findings
- All 136 discovered Drive files were retrieved (one partial PDF transfer, connector text fallback); two ZIPs inspected and eight physics workbooks extracted. Read coverage and limits are in docs/SOURCE_REVIEW.md and inventory.
- Current Person2 workbook: 66 Draft rules, 14 formulas, 32 acceptance-test rows. Old counts are superseded.
- S1: six configurations, thirty runs total, one aborted run explicitly represented. S2: four online-inference benchmark configurations; operational power/purchase-price evidence absent.
- Full PDF includes E1-E7, retrofit R1-R6 and what-if. Current writeUP narrows paper evaluation to greenfield S1/S2. Preserve the distinction.
- Catalogue mixed sections and field verification conflicts require quarantine and review.

## Chosen engineering defaults
One modular Python/FastAPI Team C service, pure engines, typed JSON contracts, React/TypeScript workbench, PostgreSQL persistence planned, Docker Compose for local services, GitHub branch/PR workflow. Missing evidence is null/UNKNOWN; no invented site values, universal PUE or benchmark extrapolation.

## Current implementation
E5 weighted energy slice, optional factor/cost/carbon, typed limit helper, API, React workbench, schema generator, tests, CI, Docker/Compose and initial SQL. Full E1-E7 pipeline, persistent API, catalogue/rule activation, retrofit and cross-team endpoints are not yet implemented.

## Open blockers
Central repository URL; Maham's verified username; Team A/B accepted fixtures; shared UI owner; retrofit release scope; matched site/grid/PUE evidence; field-level OEM checks; comparable quotes; production benchmark eligibility policy.

## Next action
Raazia: catalogue/rule adapter. Maham: benchmark/E1-E2 adapter. Both: agree shared models before dependent engine PRs. Follow docs/ROADMAP.md and peer review each other's changes.
