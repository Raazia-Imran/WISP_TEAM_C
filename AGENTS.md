# Repository instructions

Read README.md, docs/PRD.md, docs/ARCHITECTURE.md, docs/SOURCE_REVIEW.md, docs/FORMULAS.md and MEMORY.md before implementing an engine. Follow the exact current file contents over remembered chat details. When a source conflicts, record the conflict and implement only the supported behavior.

## Scientific rules
- Never invent citations, OEM values, site capacity, prices, benchmark measurements or a universal utilization/PUE/COP factor.
- Distinguish measurement, calibration, rating, derivation, scenario assumption and unavailable values.
- Preserve original formula/source/rule IDs. Map aliases explicitly. Workbook phases are not engine IDs.
- Missing is null/UNKNOWN, never numeric zero or PASS. A failed applicable hard constraint rejects the candidate. UNKNOWN prevents full-feasibility claims.
- No extrapolation of tested MLPerf performance to arbitrary hardware/model/precision combinations.
- Never add GPU TDP to inclusive whole-server AC power. Never add UPS/cooling losses again after a facility PUE multiplier.
- Annual PUE does not establish peak electrical demand. Interval means do not establish instantaneous peaks.
- Never turn a recommendation trigger into a certified safety or Tier compliance claim.

## Implementation rules
- Pure typed calculation functions; API, persistence and UI call those functions.
- Validate finite numbers, dimensions, applicability, provenance and strict schemas at boundaries.
- Do not execute imported formulas or rule text with eval/exec. Use reviewed named functions and whitelisted operators.
- Add meaningful numerical, missing-data and boundary tests to new calculations. Do not add tests that merely repeat the implementation.
- Preserve immutable scenario/evidence snapshots for future persistence; what-if creates a child run.
- Record major contract changes and update generated schemas plus fixtures together.
- Keep secrets, signed download URLs, copyrighted PDFs and unreviewed raw catalogues out of the public repository.
- No new major dependency/service without a documented purpose in docs/TECH_STACK.md.

## Required checks
`ruff check .`, `python -m pytest -q`, `python scripts/export_contracts.py --check`, and `npm ci && npm run build` in frontend for UI changes. When Docker is available, additionally build and smoke-test Compose. Record commands actually run and limitations; never claim unrun checks passed.

## Scope and ownership
Canonical E1-E7 naming follows the full architecture PDF. Cooling selection belongs to Team B. E5 supplies heat/load boundaries. Paper validation currently covers S1/S2 greenfield; the broader software roadmap retains retrofit with a scope decision pending. Raazia and Maham's proposed ownership is documented in docs/WORK_SPLIT.md, not an externally assigned role.
