# Validation strategy

## Numerical correctness
Use an independent hand-calculated example for each formula group and dimensional/zero/negative/nonfinite boundary cases. Energy is weighted by interval duration; unprovided hours are not silently zero. Missing factor/quote/limit is unknown/null. Test equality thresholds, individual rack item fit, aggregate vs actual packing and no double counting.

## Evidence and import controls
Test mixed-section CSV headers, inconsistent row widths, missing IDs, duplicate records, changed units and contradicted field verification. Rule importer preserves Draft status and rejects unsupported operators/executable text. Source review validates applicable exact OEM variant and benchmark scenario/software/precision, not merely URL existence.

## Benchmark regression
Reproduce S1/S2 with supplied package inputs before production adaptation. S1 has six configurations/five runs each; preserve aborted-run flag and original aggregation as historical method. Production eligibility needs a separately reviewed policy; do not quietly discard or admit invalid logs. S2 uses four configurations and explicit throughput/TTFT/TPOT/ROUGE constraints; no matching operational power/prices. Compare original expected selections and explain any methodology change.

## API/schema
Strict request validation; 422 invalid inputs; deterministic responses; optional values retained as null; generated schema drift check. Consumer fixtures prove Team B acceptance once agreed. Cross-team contracts are currently draft and cannot be called integration-tested yet.

## Persistence/UI/containers
Database tests validate transactions, snapshots and replay using PostgreSQL. Frontend build/type checks run in CI; later add user-flow tests for forms, rejected/unknown outputs and what-if. Test container build, healthcheck and database setup locally when Docker is available. An unrun Docker build is not a passed check. UI starter build success is not browser end-to-end proof.

## Commands
```bash
ruff check .
python -m pytest -q
python scripts/export_contracts.py --check
cd frontend
npm ci
npm run build
```

For Docker smoke test use `docker compose config`, `docker compose up --build api`, then inspect `/health` and submit the example. Set POSTGRES_PASSWORD in .env before config because Compose expands database environment even when the optional profile is inactive. Record commands/results in docs/VALIDATION.md. Release checks broaden only when new modules/risks justify them.
