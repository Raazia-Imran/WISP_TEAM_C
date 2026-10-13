# Hardware catalogue implementation

## Retrieved families
AI servers (32 product rows), GPU (20), CPU (12), and main blocks of networking (32), storage (21), racks (12), PDUs (10), UPS (12), cooling parameters (12), power distribution (12). These are product-block counts, not the raw CSV line counts. Networking and storage CSVs embed many auxiliary tables with changed headers/widths. Recognize sections and retain audit rows separately.

## Canonical data fields
Identity: catalogue_id/vendor/canonical_model/variant/entity_level/validity date. GPU: accelerator memory per device vs aggregate, precision, dense/sparse performance, TDP vs measurement, form factor and source. Server: installed vs supported GPU/CPU count, CPU sockets, RAM, usable storage, interconnect, rack U, dimensions, weight, inclusive AC power, PSU/path ratings. Networking: management vs training fabric, ports/link speed, aggregate direction convention, RDMA/protocol and validated device compatibility. Storage: capacity convention, workload-dependent throughput/IOPS, power operating state and endurance. Rack/PDU/UPS: usable U, physical dimensions, static/dynamic weight, kW/kVA, PF, phase/voltage, derating and efficiency operating point.

Every numeric field carries value, unit, value_kind, source_id, source_location, retrieval_date, verification_status and applicability. Null means unavailable. Preserve source strings separately from parsed numbers; `1U`, `85 µs`, `15.36 TB`, ranges and condition statements need explicit conversion.

## Confirmed source inconsistencies to resolve
H100 GPU-001 notes state that peak power, idle power, dimensions and weight are not stated in the cited source, while fields/statuses supply numeric values and call them verified. Quarantine those disputed fields until a matching source is checked. Do not turn the catalogue's 110 W idle value into a general H100 assumption.

DGX H100 SRV-001 has Typical_Power_W=7956 labelled ESTIMATED using 78% of a peak value. Treat it as a catalogue scenario estimate, not a measured operational load. It cannot calibrate every H100 server. Keep 10.2 kW system rating and total GPU TDP separate; adding both double-counts included GPUs. Socket/form-factor compatibility cannot be inferred from sharing a vendor name.

## Import acceptance
All expected primary IDs reconciled; section headers detected; no extra-width row silently truncated; duplicate IDs reported; per-field evidence contradictions surfaced; units normalized; excluded fields retained in audit; version/hash recorded. Source family count must be reconciled to accepted/quarantined/duplicate records. Never load secondary audit tables as extra products.

## New vendor research
Use exact OEM variant and dated official datasheet/engineering guide. Record page/section, AC/DC boundary, included components and operating conditions. Follow source URLs in the source registers; a paper's hardware mention does not verify all catalogue specifications. Validate price separately using comparable dated quotes. Reviews should work field-by-field for decision-critical values before activating a record.

## Proposed import storage
Raw source remains private/local. Reviewed normalized product snapshots belong in versioned knowledge storage. Public repository contains source manifests and minimal approved/synthetic fixtures. Run `scripts/inspect_catalogue.py <path>` to identify mixed sections; it is an inspection tool, not a complete normalized importer.
