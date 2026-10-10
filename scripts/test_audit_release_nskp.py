#!/usr/bin/env python3
"""Regression checks for non-decrypting NSKP resource-name inventory."""
from __future__ import annotations

import importlib.util
import tempfile
import zipfile
from pathlib import Path

module_path = Path(__file__).with_name("audit_release_nskp.py")
spec = importlib.util.spec_from_file_location("audit_release_nskp", module_path)
assert spec and spec.loader
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

with tempfile.TemporaryDirectory() as tmp:
    apk_path = Path(tmp) / "synthetic.apk"
    paths = (
        b"Audio/Guy/Guy_Skill01.ogg",
        b"Element/Guy/Guy.xml",
        b"Element/Guy/Guy.plist",
        b"Element/Guy/Guy.png",
        b"Element/Skills/Guy_Skill.png",
        b"Audio/Hashirama/Hashirama_skill1.ogg",
        b"Element/Hashirama/Hashirama.xml",
    )
    with zipfile.ZipFile(apk_path, "w") as apk:
        apk.writestr("assets/game_00.nskp", b"NSK1" + b"\x00".join(paths) + b"\x00")
    found = audit.scan_apk(apk_path)
    assert "Element/Guy/Guy.xml" in found["Might Guy"]
    assert "Audio/Guy/Guy_Skill01.ogg" in found["Might Guy"]
    assert "Element/Hashirama/Hashirama.xml" in found["Hashirama Senju"]
    guy_flags = audit.classify(found["Might Guy"], audit.TARGETS["Might Guy"])
    assert all(guy_flags.values()), guy_flags
    assert found["Kurenai"] == set()
print("PASS: NSKP path-name inventory detects model, atlas, audio, and skill-art references without unpacking payloads.")
