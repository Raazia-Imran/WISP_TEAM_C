"""Report mixed CSV sections and malformed primary rows without modifying input."""
import csv
import json
import sys
from pathlib import Path


def inspect(path: Path) -> dict:
    rows = list(csv.reader(path.open(encoding="utf-8-sig", newline="")))
    if not rows:
        return {"file": path.name, "primary_rows": 0, "issues": ["empty file"]}
    header = rows[0]
    primary = []
    issues = []
    seen = set()
    for number, row in enumerate(rows[1:], 2):
        if not row:
            break
        if len(row) != len(header):
            issues.append({"row": number, "expected_columns": len(header), "actual": len(row)})
            continue
        if row[0] in seen:
            issues.append({"row": number, "duplicate_id": row[0]})
        seen.add(row[0])
        primary.append(row[0])
    return {"file": path.name, "total_rows": len(rows), "primary_rows": len(primary),
            "primary_ids": primary, "column_widths": sorted({len(r) for r in rows if r}),
            "issues": issues,
            "note": "Only first contiguous table counted. Additional sections require mappings."}


if __name__ == "__main__":
    print(json.dumps(inspect(Path(sys.argv[1])), indent=2))
