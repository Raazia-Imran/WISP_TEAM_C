# API and cross-team contracts

## Implemented API
`GET /health`: liveness and explicit persistence=not_connected. `POST /api/v1/power/evaluate`: request/response schemas generated from Pydantic in contracts/. Unknown fields, nonfinite/negative values, empty profiles and days exceeding 24 hours are rejected. Total duration is at most 24 hours; repeat_days describes repetition of that supplied profile, not automatic 24-hour coverage. Optional PUE, tariff and carbon are unavailable if absent; zero tariff/factor is a valid explicit input.

Request requires scenario_id, nonempty source_ids, basis (measured/calibrated/scenario), intervals (mean_it_power_kw/duration_hours), and schema_version=1.0. A source_id is an asserted lineage identifier, not automatic evidence verification. Response returns covered hours, weighted mean IT demand, maximum interval mean, IT/facility energy and optional flat-tariff electricity cost/operational carbon, warnings and formula IDs. Validation failures return HTTP 422.

## Planned Team A input
RegionalContext/v1: region_id, geography, year/as_of, currency, electricity tariff periods with unit/currency, carbon factor and system boundary, ambient conditions, humidity, water availability/cost, grid reliability evidence, grid capacity if confirmed, regulatory/land constraints, sources and unavailable_fields. Region preference and available electrical capacity must not be treated as the same field. No Team A field is final until both teams accept a fixture.

## Planned Team C to Team B handoff
ThermalFacilityHandoff/v1: scenario_id/run_id, schema_version, workload and candidate identifiers, resource quantities, rack assignments, per-rack IT operating/peak/rated values with basis, IT-room heat location and air/liquid split if evidenced, energy period and coverage, electricity/carbon assumptions, special equipment requirements, missing_fields, sources/formulas/rules and engine version. Keep kW electrical and kW thermal explicitly named. Optional price/cost totals carry completeness and currency.

## Planned Team B response
CoolingAssessment/v1: scenario_id/input_hash, selected cooling strategy (owned by B), capacity at matching design conditions, modeled cooling electrical power profile, other included overheads, air/liquid boundaries, water scope, conditions, uncertainties and evidence. When combining it into C, select explicit-overhead method and remove overlapping PUE multiplication. Model coupling must record iteration and convergence.

## Evolution
Use schemas and example fixtures agreed by both producer and consumer. Adding an optional field is potentially compatible; renaming a field, changing units or altering semantics requires a version change and migration. CI checks schema drift and accepted shared fixtures. Document default/absent behavior. Do not use generic dictionaries for final engine profiles.

## Planned endpoint backlog
POST /api/v1/scenarios (evaluate/save); GET /api/v1/scenarios/{id}; POST /api/v1/scenarios/{id}/what-if; GET /api/v1/scenarios/{id}/team-b; GET /api/v1/catalogue with reviewed-only filters. These routes are specifications, not currently implemented. Authentication/persistence must be designed before nonlocal deployment.
