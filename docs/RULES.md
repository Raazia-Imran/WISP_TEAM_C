# Rulebook-to-code procedure

## Current source
The retrieved Person2 workbook currently has 66 catalogue rules, all Draft, 14 formula specifications and 32 acceptance-test records. Earlier remembered counts are stale. Other rule CSV families include workload, CPU, GPU, memory, server, networking, storage and rack rules; several include legacy and overlapping variants. Do not sum these as unique approved rules.

## Normalized rule model
rule_id, canonical_id, legacy_ids, category, description, input_fields, operator, threshold_field/literal, unit, applicability, severity, rule_kind, dependencies, formula_ids, source_ids, source_location, confidence_basis, status, review_record, missing_data_behavior, version. Preserve original IDs and record canonical mappings separately. Resolve conflicting thresholds using dated applicable source evidence; never silently take whichever row was imported last.

## Lifecycle
Imported Draft -> reviewed specification -> executable implementation -> tested/reviewed rule version. Rejected/superseded variants remain in history. Evidence review and code review are separate. A CSV value 'VERIFIED' alone is not evidence of field verification. Do not execute a Draft rule in the default production rule set. A demo may use a clearly named synthetic fixture rule.

## Evaluation semantics
Only named functions and a whitelist of comparison operators execute. No eval of formula strings, Python snippets or CSV conditions. Validate units before comparing. Missing observed value or applicable threshold yields UNKNOWN. An inapplicable constraint yields NOT_APPLICABLE with reason. Every check records inputs, threshold source, expression/operator, result and explanation.

Aggregate mandatory constraints: any FAIL means candidate rejected; otherwise any UNKNOWN means partially evaluated; otherwise all applicable mandatory checks pass. A triggered recommendation is not a hard failure unless the source explicitly makes it one. Separate source conflict from numeric threshold failure.

## Import workflow
1. Select canonical family/version and map duplicate/legacy IDs.
2. Parse sections and retain raw hash, filename, row/sheet and source URL.
3. Validate IDs, dependencies, units, source linkage and required fields.
4. Detect cycles and conflicting applicability/thresholds.
5. Quarantine malformed rows and unsupported operators with a report.
6. Map formula IDs to reviewed functions and run independent fixtures.
7. Have the other developer review evidence and behavior before activation.

## Priorities
First implement power/rack/budget/performance constraints for supported S1/S2. Next compatibility and unknown site input. Cooling selection rules belong to Team B; Team C can carry a heat/cooling adequacy result as contextual validation without selecting a plant. Regulatory/Tier claims need independent applicability/topology evidence.

Current `evaluate_limit` is only a typed numeric primitive. It is not a complete rule importer, lifecycle manager or E7 aggregator. The roadmap includes those tasks.
