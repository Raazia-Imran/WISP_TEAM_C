# Source review and evidence gaps

Review date: 13 October 2026. Source folder: [private source folder omitted] . The attached stack JPEG, legacy architecture JPEG and all three pages of the full architecture PDF were visually inspected.

## Retrieval and review coverage
Recursively listed the provided folder and every discovered child folder. Retrieved 136 Drive file records: hardware catalogues, rules/formula tables and audit tables, experiment workbooks/scripts/JSON, two ZIP archives, native project documents/reference register, and 17 literature PDFs. Downloaded-byte sizes matched Drive metadata for 132 of 133 stored files; the ASHRAE file was the exception described below. Native Docs/Sheets were read as connector text rather than byte-equivalent exports.

Read the project writeup and data findings, parsed all CSV records, extracted all workbook sheets (including eight physics books from the ZIP), inspected embedded experiment package contents, scanned rule/formula fields and gap/QA/source registers, and reviewed decision-critical records and methods. Literature text was extracted for 16 complete PDFs and reviewed for topic, model boundaries and relevant methods. Long literature reports were reviewed selectively, not line-by-line. This is an implementation-oriented review, not independent certification of every row, external reference or historical research claim.

`SOURCE_INVENTORY.md` identifies every file and its structural coverage. `data/source_manifest.json` defines the private source-ledger structure and aggregate coverage; private URLs, identifiers and hashes are excluded. The public repository contains manifests and derived specifications; it does not republish private raw Drive files or literature PDFs.

## Source families and coding implications
| Family | Current evidence | Implementation consequence |
|---|---|---|
| Stack image | Python/FastAPI, React, PostgreSQL, GitHub, monorepo, JSON contracts | Retain stack; add typing, tests, locks, migrations and provenance |
| Full PDF | E1-E7, retrofit R1-R6, what-if and Team B output package | Canonical software engine names and full design |
| Legacy architecture JPEG | Grouped workload/performance/infrastructure/power/DSS flow | Map concepts; do not equate numbered boxes to E1-E7 IDs |
| writeUP_MODULE 1 | Workload-first sequence; paper S1/S2; brownfield excluded | Record paper/software scope conflict rather than discard retrofit design |
| DATA_FINDINGS | Six S1 systems, 30 total runs; four S2 systems; missing cost/power limitations | Use exact supported benchmark records; no arbitrary performance scaling |
| Hardware catalogues | Product tables plus field/audit tables | Section-aware parsing and field-level verification required |
| Person2 workbook | 66 rules all Draft; 14 formula specifications; 32 acceptance rows | Preserve Draft state; review before executable activation |
| Rule CSV families | Workload, CPU, GPU, memory, server, rack, network, storage plus mappings/gaps | Avoid double-counting overlapping/legacy rules; preserve canonical mapping |
| Physics ZIP | Eight books; 38 registered calculation IDs across seven subjects | Preserve formula/source/boundary IDs; distinguish Team C vs B ownership |
| Experiment archives | Executable S1/S2 scripts and expected results | Reproduce historical outputs; adapt via typed production models later |
| Literature | Energy models, measured profiles, placement/upgrades and benchmark methodology | Rationale and applicable methods; not blanket hardware/site facts |

## Confirmed issues
1. S1 includes five runs per configuration, thirty total. Do not write thirty per configuration.
2. The current Person2 workbook supersedes older counts: 66 Draft rules, 14 formulas, 32 acceptance-test records. All Draft status is preserved.
3. Networking CSV has 446 parsed rows and many column widths; storage has 260 rows and many widths. Their initial product blocks are 32 and 21 products, not hundreds of products.
4. H100 GPU-001 supplies numerical idle/peak/physical values with verification labels while its own notes say those quantities are not stated in the cited source. Mark those fields disputed; validate exact external evidence before use.
5. DGX H100 SRV-001 typical power is a 78%-of-peak estimate, not a measured general training load. Do not use this factor globally.
6. S1 includes one aborted Dell-8G log. The original script preserves a flag and historical aggregation. Any production eligibility/aggregation change needs a recorded methodology decision and regression comparison.
7. S2 source package expressly lacks matching operational whole-server power and comparable purchase prices. Operational energy/CAPEX/TCO/ROI cannot be inferred from those results alone.
8. Physics books say actual catalogue rows were unavailable when written. They are available in the supplied Drive now, but that historical gap is not automatically resolved: field conflicts and Rule_ID mapping still need review.
9. F-ENE-003/005 encode a four-equal-bin example. General code must use total supplied duration. Formula register documents this correction.
10. Owner aliases/engine numbering differ across source packages. Canonical E1-E7 naming and explicit alias map are required.

## Raw PDF limitation
`12_ASHRAE_PNNL_NEMA_2026_AI_Data_Center_Framework.pdf`: Drive metadata size 1,955,498 bytes; streamed download 1,040,384 bytes. Poppler could not read the trailer/xref. Connector text was available and reviewed as a fallback, but a complete raw-file/layout review was not possible. Any hash retained in the private ledger identifies the received partial transfer, not the full original PDF. Do not use the partial copy as a validated reference artifact. A fresh full export/transfer or direct official source check is needed for detailed implementation claims.

## What remains unverified
Every external OEM source/field; all rule applicability and thresholds; catalogue estimates; exact site grid capacity/PUE; current tariffs and dated quotes; Team B cooling curves; publication/version classifications; full paragraph-level literature audit; production S1 validity policy; approved cross-team schemas. These are explicit first-phase work items. None is silently filled with a generic value.

## Practical release effect
The repository is ready to start coding and review the supported vertical slices. It is not a completed or fully validated data-center planning system. Calculation methods can be implemented and tested while evidence-dependent output remains unknown. Scientific eligibility and full feasibility require the applicable inputs, reviewed rule versions and matching source data.
