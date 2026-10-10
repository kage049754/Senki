#!/usr/bin/env python3
"""Print the APK container layout while discovering legacy character resources."""
from pathlib import Path
import collections
import gzip
import bz2
import io
import lzma
import re
import sys
import zipfile
import zlib

for arg in sys.argv[1:]:
    apk = Path(arg)
    print(f"\n=== APK: {apk.name} size={apk.stat().st_size} ===")
    with zipfile.ZipFile(apk) as zf:
        names = zf.namelist()
        print(f"ZIP entries: {len(names)}")
        counts = collections.Counter()
        for name in names:
            suffix = Path(name).suffix.lower()
            counts[suffix or "<none>"] += 1
        print("Extension counts:", dict(counts.most_common(30)))
        print("Top-level entries:")
        tops = sorted({name.split("/", 1)[0] for name in names})
        print("\n".join("  " + name for name in tops[:120]))
        print("Resource-like entries:")
        matches = [name for name in names if any(token in name.lower() for token in (
            "kurenai", "yamato", "hashirama", "shizune", "sakon", "juzo", "iruka",
            "zetsu", "sasori", "rin", "hokageminato", "mightguy", "element/", "resources/"
        ))]
        print("\n".join("  " + name for name in matches[:180]) or "  <none>")
        print("Nested archive/data containers:")
        nested = [name for name in names if Path(name).suffix.lower() in (".zip", ".pak", ".dat", ".obb", ".bin", ".bundle", ".nskp", ".plist", ".xml", ".ccz", ".pvr")]
        print("\n".join("  " + name for name in nested[:100]) or "  <none>")
        for name in names:
            suffix = Path(name).suffix.lower()
            if suffix not in (".zip", ".pak", ".dat", ".obb", ".bin", ".nskp"):
                continue
            try:
                data = zf.read(name)
            except Exception:
                continue
            if suffix == ".nskp":
                print(f"NSKP container: {name} ({len(data)} bytes), head={data[:32].hex()} ascii={data[:32]!r}")
                tokens = re.findall(rb"[A-Za-z0-9_./ -]{5,}", data[:min(len(data), 2_000_000)])
                print("  embedded strings:", [token[:120].decode("latin1", "replace") for token in tokens[:25]])
            if data[:4] in (b"PK\\x03\\x04", b"PK\\x05\\x06"):
                print(f"Nested ZIP detected: {name} ({len(data)} bytes)")
                try:
                    with zipfile.ZipFile(io.BytesIO(data)) as inner:
                        print("\n".join("    " + x for x in inner.namelist()[:80]))
                except Exception:
                    pass
            for offset in range(0, min(32, len(data))):
                chunk = data[offset:]
                for decoder_name, decoder in (
                    ("zlib", zlib.decompress),
                    ("gzip", gzip.decompress),
                    ("bz2", bz2.decompress),
                    ("lzma", lzma.decompress),
                ):
                    try:
                        unpacked = decoder(chunk)
                    except Exception:
                        continue
                    if unpacked:
                        print(f"  {decoder_name} decompressed at offset {offset}: {len(unpacked)} bytes, head={unpacked[:24].hex()}")
                        strings = re.findall(rb"[A-Za-z0-9_./ -]{5,}", unpacked[:min(len(unpacked), 1_000_000)])
                        print("  decoded strings:", [token[:100].decode("latin1", "replace") for token in strings[:35]])
                        break
