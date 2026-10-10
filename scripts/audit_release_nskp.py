#!/usr/bin/env python3
"""Inventory visible character resource names in public Naruto Senki release packs.

This reads only the APK ZIP directory and printable NSKP index strings. It does
not decrypt or extract packed asset payloads and does not claim a character port.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

TARGETS = {
    "Kurenai": ("Kurenai",),
    "Might Guy": ("Guy", "MightGuy"),
    "Yamato": ("Yamato",),
    "Shizune": ("Shizune",),
    "Hashirama Senju": ("Hashirama", "SageHashirama"),
    "Rin Nohara": ("Rin",),
}
PATH_RE = re.compile(
    rb"(?:Audio|Element)/[A-Za-z0-9_&.-]+(?:/[A-Za-z0-9_&.-]+)*"
    rb"\.(?:ogg|mp3|xml|plist|png|pvr\.ccz|ccz)"
)

def scan_apk(apk_path: Path) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {name: set() for name in TARGETS}
    with zipfile.ZipFile(apk_path) as apk:
        packs = sorted(p for p in apk.namelist() if p.startswith("assets/") and p.endswith(".nskp"))
        if not packs:
            raise ValueError(f"{apk_path} contains no assets/*.nskp packs")
        for pack in packs:
            blob = apk.read(pack)
            if not blob.startswith(b"NSK1"):
                print(f"WARNING: unexpected NSKP magic in {apk_path.name}:{pack}", file=sys.stderr)
                continue
            for raw in PATH_RE.findall(blob):
                path = raw.decode("ascii", "replace")
                path_parts = path.lower().split("/")
                for character, aliases in TARGETS.items():
                    if any(alias.lower() in path_parts for alias in aliases):
                        found[character].add(path)
    return found

def classify(paths: set[str], aliases: tuple[str, ...]) -> dict[str, bool]:
    char_paths = [p for p in paths if any(alias.lower() in p.lower().split("/") for alias in aliases)]
    return {
        "model_xml": any(p.startswith("Element/") and p.endswith(".xml") for p in char_paths),
        "sprite_atlas": any(p.startswith("Element/") and p.endswith((".plist", ".png", ".pvr.ccz", ".ccz")) for p in char_paths),
        "audio": any(p.startswith("Audio/") for p in char_paths),
        "skill_art": any("/Skills/" in p or "_Skill" in p for p in char_paths),
    }

def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("usage: audit_release_nskp.py <release.apk> [release.apk ...]")
    aggregate = {name: set() for name in TARGETS}
    for arg in sys.argv[1:]:
        apk_path = Path(arg)
        found = scan_apk(apk_path)
        for character, paths in found.items():
            aggregate[character].update(paths)

    lines = [
        "# Release NSKP character resource-name audit",
        "",
        "This report lists names visible in release pack indexes. The payloads remain packed/encrypted;",
        "resource-name presence is not proof the assets are importable or that a character is ported.",
        "",
        "| Requested character | Model XML name | Sprite atlas name | Audio name | Skill-art name | Visible paths |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for character, aliases in TARGETS.items():
        paths = aggregate[character]
        flags = classify(paths, aliases)
        lines.append(
            f"| {character} | {'yes' if flags['model_xml'] else 'no'} | "
            f"{'yes' if flags['sprite_atlas'] else 'no'} | {'yes' if flags['audio'] else 'no'} | "
            f"{'yes' if flags['skill_art'] else 'no'} | {len(paths)} |"
        )
    lines.extend(["", "## Visible resource-name samples", ""])
    for character, paths in aggregate.items():
        lines.append(f"### {character}")
        if paths:
            lines.extend(f"- {path}" for path in sorted(paths)[:40])
        else:
            lines.append("- No matching names found")
        lines.append("")
    output = Path("release-character-resource-inventory.md")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:16]))
    print(f"Wrote {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
