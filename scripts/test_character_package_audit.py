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
enum_leads = re.search(r"HeroEnum entries absent from the visible selection list: \*\*(\d+) requiring manual classification", report)
assert enum_leads, "Non-roster HeroEnum audit summary is missing"
assert "Non-roster enum leads:" in report, "Non-roster enum lead list is missing"
assert "not counted as playable" in report, "Non-roster enum warning must prevent false playable counts"
assert "`AnimalPath`" in report and "`Guardian`" in report, (
    "Known summon/support enum entries should be surfaced for manual classification"
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
assert "after applying SkillLayer UI aliases" in report, "Skill UI alias handling is not documented"
assert "`RockLee` → `Lee`" in report, "Known RockLee-to-Lee skill UI alias is not reported"
assert "`Kabuto` (0/5)" in report, "Known missing Kabuto labels should remain flagged for manual review"
assert "`RockLee` (0/5)" not in report, "A base-art alias should not be reported as missing skill labels"
assert "does not prove a character is complete" in report, "Required audit limitation warning is missing"
detail_heading = "## Detailed animation, atlas, audio, and AI checks"
assert detail_heading in report, "Detailed per-character asset checks section is missing"
detail_start = report.index(detail_heading)
detail_lines = report[detail_start:].splitlines()
detail_header_idx = next((i for i, line in enumerate(detail_lines) if line.startswith("| Character |")), None)
assert detail_header_idx is not None, "Detailed asset table header is missing"
detail_header = cells(detail_lines[detail_header_idx])
assert len(detail_header) == 9, f"Expected 9 detailed asset columns, got {len(detail_header)}"
detail_rows = []
for line in detail_lines[detail_header_idx + 2:]:
    if not line.startswith("|"):
        break
    row = cells(line)
    assert len(row) == len(detail_header), f"Detailed asset row has {len(row)} cells; expected {len(detail_header)}: {line}"
    detail_rows.append(row)
assert len(detail_rows) == expected_count, (
    f"Detailed asset table has {len(detail_rows)} rows; expected {expected_count}"
)
assert [row[0] for row in detail_rows] == [row[0] for row in rows], (
    "Detailed asset table roster order/names do not match the main audit table"
)
missing_atlas = [row[0] for row in detail_rows if row[2] != "PLIST+TEXTURE_FOUND"]
assert not missing_atlas, (
    "The pinned candidate's roster has missing/unresolved sprite textures: "
    + ", ".join(missing_atlas)
)
frame_coverage_rows = [row for row in detail_rows if re.fullmatch(r"\d+/\d+", row[3])]
assert len(frame_coverage_rows) == expected_count, (
    "Every roster entry must report XML-to-atlas frame reference coverage"
)
assert all(int(row[3].split("/")[1]) > 0 for row in frame_coverage_rows), (
    "Every roster entry must contain at least one XML frame reference"
)
missing_frame_ref_summary = re.search(
    r"Animation XML frame-reference coverage: \*\*(\d+)/(\d+) roster entries",
    report,
)
assert missing_frame_ref_summary, "XML-to-atlas frame-reference coverage summary is missing"
assert int(missing_frame_ref_summary.group(2)) == expected_count
if int(missing_frame_ref_summary.group(1)) < expected_count:
    assert "Missing XML frame names (first 12 per entry)" in report, (
        "Frame-reference exceptions must include names for actionable triage"
    )
    assert "Jugo_Skill05_14" in report and "- `Kimimaro`:" in report, (
        "Known Kimimaro-to-Jugo frame-name mismatch must remain visible for triage"
    )
sound_event_counts = [
    int(row[5].split()[0])
    for row in detail_rows
    if len(row[5].split()) == 4 and row[5].split()[0].isdigit() and row[5].split()[1:] == ["audio", "event", "refs"]
]
assert sound_event_counts and any(count > 0 for count in sound_event_counts), (
    "The audit did not recognize any animation XML audio event references"
)
print(f"Character audit report is well-formed: {len(header_cells)} columns, {len(rows)} rows, portrait coverage {coverage.group(1)}/{coverage.group(2)}, skill-label coverage {labels.group(1)}/{labels.group(2)}, sprite atlases/textures {len(detail_rows)-len(missing_atlas)}/{len(detail_rows)}, audio event refs recognized.")
