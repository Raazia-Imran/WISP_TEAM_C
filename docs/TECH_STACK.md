# Technology choices and development environment

The attached stack specifies Python 3.11+/FastAPI, React SPA, PostgreSQL, GitHub, central monorepo and JSON contracts. Keep this foundation. The project needs typed contracts, import validation, calculation tests, migrations and data provenance beyond those layer labels.

| Component | Choice | Purpose and current state |
|---|---|---|
| Backend/domain | Python 3.11+, FastAPI | Shared language and numerical/domain functions; starter installed |
| Validation | Pydantic 2 | Strict finite typed API inputs and JSON schemas; implemented |
| UI | React + TypeScript + Vite | Workbench and eventual shared SPA; scaffolded with lockfile |
| Data | PostgreSQL | Sources/scenarios/knowledge snapshots; local SQL configured; API wiring pending |
| DB access | SQLAlchemy 2 + Alembic, planned | Transactional repositories and versioned migrations; do not treat initial SQL as mature migration history |
| Numerical functions | Python standard library initially | Enough for bounded arithmetic and selection; add NumPy/SciPy only for justified methods |
| Tabular import | csv/json initially; openpyxl for offline workbook ingestion | Parse sections and preserve provenance; imported text never executed |
| Units | Explicit field names initially; consider Pint | Avoid W/kW, GB/GiB, token/request and kW/kWh confusion; dimension tests required |
| Tests/lint | pytest, httpx, Ruff | Arithmetic, API, source gaps and schema drift |
| Reproducibility | Python exact dependency snapshots; npm package-lock | Versions used by both developers and CI |
| Local deployment | Docker + Compose | Same backend/Postgres environment; optional database profile |
| Collaboration | GitHub feature branches/PRs/CI | Peer review and weekly central integration |
| Automated review | CodeRabbit optional | Supplement to human/source review; current pricing/access not assumed |

## Docker decision
Use Compose for local services and integration; use a Python virtual environment for fast pure engine development. Kubernetes, Redis/Celery, separate microservice per engine and live GPU telemetry are unnecessary for the first evidence-replay release. Add a queue only if measured request duration/concurrency requires it. The included Compose API has an HTTP healthcheck; database has pg_isready. When a future API requires PostgreSQL, add service_healthy dependency and connection retries, not only start-order assumptions.

## Version policy
Selected Python runtime 3.11 and Node 22. Direct dependencies have bounded major versions; exact resolved Python snapshots and package-lock record this starter environment. CI installs locked versions. To update, open a dedicated dependency PR, regenerate locks, run tests and build, then update source-sensitive API contracts. Runtime dependency lock is separate from development tools.

## Hardware for development
No H100 or local Llama execution is required for benchmark replay. Use a laptop capable of the editor, Python, Node and optional Docker. Start without Docker if memory pressure is high. Actual deployment sizing must be measured under realistic data/concurrency; no guaranteed RAM/CPU threshold is asserted here. Keep local hardware specifications and observed setup behavior in the team onboarding notes if problems occur.

Official implementation references: https://fastapi.tiangolo.com/deployment/docker/ ; https://docs.docker.com/compose/how-tos/startup-order/ ; https://react.dev/learn/build-a-react-app-from-scratch ; https://docs.pydantic.dev/latest/concepts/strict_mode/ . Technology recommendations are engineering choices, not findings from the research papers.
