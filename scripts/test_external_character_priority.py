#!/usr/bin/env python3
"""Guard the external-character-first mission against documentation drift.

This is a documentation/roster integrity check, not proof that a character is
playable. A release-note lead or resource-only entry must never be counted as
an integrated or verified character without implementation and test evidence.
"""
from pathlib import Path
import re
import sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

REQUIRED = {
    "README.md": [
        "MAIN MISSION",
        "other Senki mods",
        "Do not expand the old Kotlin/Canvas prototype",
        "External mod character packages integrated into the candidate",
    ],
    "AGENTS.md": [
        "Prioritize external-mod playable characters",
        "Do not treat release-note-only names",
        "GitHub Actions failure/success loop",
        "physical-device testing",
    ],
    "ROADMAP.md": [
        "Phase 2 — Discover external playable characters (ACTIVE)",
        "Phase 3 — Port the first complete character",
        "Exit gate",
    ],
    "PROGRESS.md": [
        "External mod character packages integrated",
        "External character status",
        "Do not report a character as added",
    ],
    "docs/MOD_RESEARCH.md": [
        "release notes",
        "Current integration checkpoint",
        "source provenance",
    ],
    "docs/CHARACTER_ROSTER.md": [
        "DISCOVERED",
        "IN_PROGRESS",
        "VERIFIED",
        "Source commit/version",
        "Evidence/notes",
    ],
    "docs/ASSET_LICENSES.md": [
        "PERMISSION_REQUIRED",
        "Asset-specific license",
        "Do not assume an open-source code license covers",
    ],
}

errors = []
for relative, phrases in REQUIRED.items():
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"Missing required project guide: {relative}")
        continue
    content = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase.casefold() not in content.casefold():
            errors.append(f"{relative}: required mission/verification text missing: {phrase!r}")

# Ensure the roadmap's target is not mistaken for current achievement.
progress = ROOT / "PROGRESS.md"
if progress.is_file():
    content = progress.read_text(encoding="utf-8")
    if not re.search(r"External mod character (?:variants|packages) integrated(?: into the candidate)?\s*\|\s*\*\*?\s*\d+", content, re.I):
        # Permit a prose status instead of a table, but require an explicit count/status.
        if not re.search(r"external character status.{0,300}(?:0|none|no external character)", content, re.I | re.S):
            errors.append("PROGRESS.md: no explicit current external-character integration status found")

if errors:
    print("External-character priority/record-integrity check FAILED:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("External-character priority/record-integrity check PASSED.")
print("Verified: mission, active phase, source provenance, and technical verification gates are documented.")
print("This check does not claim any external character has been ported or gameplay-tested.")
