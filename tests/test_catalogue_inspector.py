import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "catalogue_inspector", Path(__file__).resolve().parents[1] / "scripts/inspect_catalogue.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_sections_and_quarantine(tmp_path):
    path = tmp_path / "mixed.csv"
    path.write_text("ID,Power_W\nA,20\nA,30\nB,40,extra\n\nAudit,Reason,Source\n1,gap,url\n")
    report = MODULE.inspect(path)
    assert report["primary_ids"] == ["A", "A"]
    assert report["column_widths"] == [2, 3]
    assert report["issues"] == [
        {"row": 3, "duplicate_id": "A"},
        {"row": 4, "expected_columns": 2, "actual": 3},
    ]
