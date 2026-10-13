# Source inventory coverage

The private project source tree contained 136 discovered files. Every file was retrieved or read through the connector; one raw PDF transfer was incomplete and readable connector text was used instead. The detailed per-file ledger is intentionally excluded from the public repository because it contains private Drive identifiers, URLs and source metadata.

| Family | Review coverage | Implementation use |
|---|---|---|
| Hardware catalogues | Ten hardware categories and embedded audit tables parsed | Field schema, compatibility, units and ingestion gaps |
| Rule books | Person2 workbook and workload/CPU/GPU/server/memory/storage/network/rack CSV families | Rule lifecycle, canonical mappings and applicability |
| Physics books | Eight workbooks extracted from archive; 38 formulas preserved | Pure calculation specifications and Team B boundaries |
| Experiment records | Training/inference workbooks, JSON, scripts and archive | Historical replay and future benchmark adapters |
| Project notes | Workload-first design and scenario findings read | Scope and engine naming reconciliation |
| Literature | Seventeen PDFs retrieved; sixteen complete text extractions and one connector fallback | Model boundaries and research-method context |

See SOURCE_REVIEW.md for substantive findings and incomplete verification. The data/source_manifest.json file defines a private-ledger structure and aggregate counts; it does not contain the private per-file ledger. Raw source files, private links, source hashes and identifiable access references are not published here.
