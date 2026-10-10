#!/usr/bin/env python3
"""Validate the generated character audit report's structure and required gates."""
from __future__ import annotations

import re
import sys
from pathlib import Path

report = Path(sys.argv[1]).read_text(encoding="utf-8")
lines = report.splitlines()
header_index = next((i for i, line in enumerate(lines) if line.startswith("| Character |")), None)
assert header_index is not None, "Character table header is missing"
header = lines[header_index]
separator = lines[header_index + 1]
def cells(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]

header_cells = cells(header)
assert len(header_cells) == 10, f"Expected 10 table columns, got {len(header_cells)}"
assert len(cells(separator)) == len(header_cells), (
    f"Markdown separator has {len(cells(separator))} columns; expected {len(header_cells)}"
)
assert all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells(separator)), (
    "Malformed Markdown table separator"
)
rows = []
for line in lines[header_index + 2:]:
    if not line.startswith("|"):
        break
    row = cells(line)
    assert len(row) == len(header_cells), (
        f"Table row has {len(row)} cells; expected {len(header_cells)}: {line}"
    )
    rows.append(row)

summary = re.search(r"Unique selectable names found: \*\*(\d+)\*\*", report)
assert summary, "Roster count summary is missing"
expected_count = int(summary.group(1))
assert len(rows) == expected_count, f"Table has {len(rows)} rows; roster summary says {expected_count}"
target = re.search(r"Distinct selectable-entry target: \*\*(\d+)/70 declared \((\d+) more entries", report)
assert target, "70-entry roster target gap is missing"
assert int(target.group(1)) == expected_count, "Roster target count disagrees with unique roster summary"
assert int(target.group(2)) == max(0, 70 - expected_count), "Roster target shortfall is incorrect"
assert "Gameplay-verified playable count: **not measured by this static audit.**" in report, (
    "Static audit must not imply gameplay-verified character count"
)
coverage = re.search(r"Kill-feed portrait atlas coverage: \*\*(\d+)/(\d+) roster entries", report)
assert coverage, "Kill-feed portrait coverage summary is missing"
assert int(coverage.group(1)) == int(coverage.group(2)) == expected_count, (
    f"Portrait coverage is {coverage.group(1)}/{coverage.group(2)} for {expected_count} roster entries"
)
labels = re.search(r"Skill-description label frame coverage: \*\*(\d+)/(\d+) roster entries", report)
assert labels, "Skill-description label coverage summary is missing"
assert int(labels.group(1)) <= int(labels.group(2)) == expected_count, (
    f"Skill-label coverage is {labels.group(1)}/{labels.group(2)} for {expected_count} roster entries"
)
assert "Skill-description label exceptions requiring manual review:" in report, (
    "Skill-label exception summary is missing"
)
assert "does not prove a character is complete" in report, "Required audit limitation warning is missing"
print(f"Character audit report is well-formed: {len(header_cells)} columns, {len(rows)} rows, portrait coverage {coverage.group(1)}/{coverage.group(2)}, skill-label coverage {labels.group(1)}/{labels.group(2)}.")
