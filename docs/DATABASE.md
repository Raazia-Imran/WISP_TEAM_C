# Persistence design and migrations

## Current state
Compose optionally starts PostgreSQL 17. `database/001_initial.sql` initializes evidence_sources and scenario_runs for a fresh volume. API calculations are currently stateless. This SQL is a starter design, not complete implementation of all knowledge tables. Changes to the init SQL do not migrate an existing volume.

## Planned tables
| Table | Main content | Key integrity rule |
|---|---|---|
| evidence_sources | ID, URL, retrieval time, content hash, review state | Source revision is immutable |
| catalogue_snapshots | Normalized hardware/field evidence | Variant and field status preserved |
| rule_versions | Rules/dependencies/applicability/activation | Only reviewed tested versions active |
| formula_versions | Named function/ID/version/units/source | No executable imported expressions |
| benchmark_records | Exact model/software/scenario/version/measurements | No arbitrary hardware scaling |
| tariff_quotes | Dated price/currency/period/scope | Comparable quotes required |
| scenario_runs | UUID, parent, input/output/evidence snapshot | Existing runs never overwritten |
| integration_events | Producer/consumer versions and checks | Team B result tied to input hash |

## Implementation procedure
Use SQLAlchemy repositories behind the planning service and Alembic migrations once persistence work begins. Tests use an ephemeral PostgreSQL service for PostgreSQL-specific transactions/JSONB behavior. A SQLite test cannot prove PostgreSQL behavior. Wrap each completed scenario save and its evidence links in one transaction; retries must not duplicate a run. Server-generated UUIDs and stable idempotency keys can support repeated API calls.

Store calculation inputs, result outputs, source/rule/formula snapshot IDs, dependency-lock hash and engine Git SHA for replay. JSONB stores the versioned snapshot; normalized searchable columns store identity/status/time. Keep raw attachments in appropriate private file storage, not secrets or PDFs in database rows by default.

## Migration and recovery gate
Apply migrations to an empty database and a previous-version database; insert/retrieve a run; restart the service; replay and compare output; test invalid FK and interrupted transaction. Back up before changing real data. Local `docker compose down` retains the volume; deleting the volume is destructive and not a routine migration step. Initial-schema execution and database restart tests remain pending because Docker/PostgreSQL are absent in the authoring environment.
