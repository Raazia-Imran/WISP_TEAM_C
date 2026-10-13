# Product requirements

## Objective and users
Create an explainable decision-support application that evaluates candidate data-center configurations against supplied workload, performance, infrastructure, power and budget constraints. Initial users are researchers and planners assessing greenfield AI training/inference. Outputs are reproducible estimates and constraint results with evidence, assumptions and unavailable fields visible.

## Source authority and scope
The provided full architecture PDF is the implementation reference for seven engines, retrofit and what-if. The Drive writeUP_MODULE 1 describes paper validation narrowed to S1/S2 greenfield and excludes brownfield/ROI. Preserve both purposes: initial paper reproduction covers S1/S2; software design includes retrofit behind a future scope gate. Do not claim supervisor approval of an implementation scope based solely on a paper note.

## Functional requirements
| ID | Requirement | Acceptance criterion |
|---|---|---|
| FR-01 | Capture workload-first user input plus regional context | Required dimensions validated; absent contextual data remains unknown |
| FR-02 | Evaluate benchmark-supported candidates | Same model/version/scenario/software/precision constraints retained; no arbitrary GPU scaling |
| FR-03 | Derive training deadline and inference throughput/TTFT/TPOT constraints | Each applicable condition has evidence and explicit comparison result |
| FR-04 | Recommend hardware alternatives and explain selection | Rejected candidates retain failed/unknown checks; objective is explicitly named |
| FR-05 | Produce bill of resources and preliminary rack assignment | Every server fits individual rack power, weight, U and physical constraints; aggregate lower bound labelled |
| FR-06 | Separate average, peak/rated bound, IT and facility demand | Different fields and provenance; no double counting |
| FR-07 | Integrate time-resolved energy and optionally tariff/carbon | Independent numerical check passes; covered period and boundary stated |
| FR-08 | Estimate CAPEX/OPEX with evidence | Dated quote/currency/scope known; missing line prevents complete total |
| FR-09 | Return validation and risk results | Hard FAIL rejects; UNKNOWN prevents full-feasibility claim; explanatory reasons visible |
| FR-10 | Export Team B thermal/facility handoff | schema_version, source basis, rack context and scope present; cooling plant not selected by Team C |
| FR-11 | Recalculate what-if without overwriting baseline | Child scenario with changed inputs, changed engines, deltas and evidence versions |
| FR-12 | Assess existing infrastructure and upgrades | R1-R6 design retained; implementation prioritized after greenfield slice; ownership/scope unresolved |
| FR-13 | Persist reproducible runs | Immutable input, output, rule, formula and source snapshots plus engine commit |
| FR-14 | Produce infrastructure/power/cost/risk reports | Missing estimates visibly unavailable; report numbers match stored run |

## Nonfunctional requirements
Deterministic engine outputs for fixed data and version; finite typed values; schema evolution tests; no secrets in Git; local developer setup without a GPU; provenance for every external fact; bounded imports; invalid data quarantined; reproducible dependency locks. Measure response times before assigning an application SLA. Initial synchronous computations are acceptable until profiling demonstrates need for workers.

## Two-month delivery goal
A working workload-to-candidate-to-resource-to-power-to-validation vertical slice for supported S1/S2 data; a basic shared UI; versioned Team B export; documented unavailable cost/region/cooling evidence; tested what-if reruns; retrospective of open retrofit tasks. This is a planning target, not a claim that every catalogue row and regional constraint can be validated within eight weeks.

## Boundaries
The starter does not train AI models or measure new GPU performance. CPU/RAM/network/storage are evaluated using supported records and applicability, not a universal formula. Cooling equipment selection is Team B. Regional feasibility and site selection are Team A. CAPEX/TCO/ROI remain unknown without matched quotations and lifecycle assumptions. Availability architecture screens do not prove a Tier certification.

## Release gate
A supported scenario is releasable when candidate eligibility, hard constraints, formula arithmetic, null behavior, data lineage, saved snapshots and Team B schema checks pass. Any remaining mandatory UNKNOWN changes the result from fully feasible to partially evaluated. A numerical energy result alone is not a complete infrastructure recommendation.
