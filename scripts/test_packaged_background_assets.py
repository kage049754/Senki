#!/usr/bin/env python3
"""Verify the APK contains byte-identical original menu/selection background textures."""
from hashlib import sha256
from pathlib import Path
import sys
from zipfile import ZipFile

if len(sys.argv) != 3:
    raise SystemExit("usage: test_packaged_background_assets.py APK_PATH RESOURCES_DIR")

apk = Path(sys.argv[1])
resources = Path(sys.argv[2])
assets = ("red_bg.png", "blue_bg.png", "menu_bar2.png", "menu_bar3.png")

with ZipFile(apk) as archive:
    names = set(archive.namelist())
    for name in assets:
        packaged_path = f"assets/{name}"
        if packaged_path not in names:
            raise SystemExit(f"Original background texture is missing from APK: {packaged_path}")
        source_path = resources / name
        if not source_path.is_file():
            raise SystemExit(f"Pinned candidate original texture is missing: {source_path}")
        packaged = archive.read(packaged_path)
        source = source_path.read_bytes()
        packaged_hash = sha256(packaged).hexdigest()
        source_hash = sha256(source).hexdigest()
        if packaged_hash != source_hash:
            raise SystemExit(
                f"Background texture differs from pinned source: {name}; "
                f"source={source_hash}, APK={packaged_hash}"
            )
        print(f"Verified byte-identical original texture: {name} sha256={source_hash}")

    retired = [name for name in names if name in {
        "assets/senki_menu.png", "assets/senki_select.png"
    }]
    if retired:
        raise SystemExit("Retired custom menu/selection replacements are packaged: " + ", ".join(retired))

print("Original menu/selection background textures match the pinned source byte-for-byte.")
