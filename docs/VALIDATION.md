# Verification completed before GitHub push

Date: 13 October 2026. Local authoring runtime: Python 3.12. The repository supports Python 3.11+, and CI is configured for 3.11; that CI job's result must be checked after push.

| Check | Result | Scope |
|---|---|---|
| Ruff check | Passed | Repository Python files |
| pytest | 11 passed | Weighted energy/cost/carbon, null vs zero, numeric limits, strict inputs, overflow, API and mixed-table inspection |
| Schema generation/drift | Passed | PowerRequest/PowerResponse generated schemas match models |
| Live HTTP smoke | Passed | /health and synthetic 144 kWh request; absent PUE produces null facility energy |
| React/TypeScript production build | Passed | Vite 6.4.4; no browser end-to-end claim |
| Original S2 unittest suite | 18 passed | Retrieved original four-configuration inference package, run outside repository |
| Original S1 simulation replay | Completed | Retrieved original script/input; all nine embedded constraint checks report Pass |
| S1 independent arithmetic | Reconciled | Historical Dell-8G: 6.26 kW × 13.162777... min / 60 × 1.4 = 1.922643074... kWh |
| Markdown local links | Passed | Referenced local targets exist |
| Raw source transfer sizes | 132 of 133 stored files matched metadata | Three native Google files read as text; one ASHRAE PDF transfer partial |
| Docker build/Compose startup | Not run | Docker executable absent |
| PostgreSQL schema/startup/persistence | Not run | Database executable/service absent; API is stateless |
| Cross-team A/B integration | Not run | Accepted fixtures and central repository not supplied |

Dependency snapshots record the installed versions, and frontend package-lock is committed. The installed FastAPI/Starlette test client emits a deprecation warning for httpx compatibility; tests still pass. Any client dependency migration belongs in a dedicated tested PR. Full engine implementation, per-field OEM source verification and production benchmark-policy review remain roadmap work.

Original-package tests establish reproduction of the provided package's behavior, not independent re-verification of every official benchmark log or quotation.
