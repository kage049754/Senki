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
            if suffix == ".nskp" and data[:4] == b"NSK1" and len(data) >= 16:
                import struct
                count, index_end = struct.unpack_from("<II", data, 8)
                print(f"  NSK1 header: version={struct.unpack_from('<I', data, 4)[0]}, file_count={count}, index_end={index_end}")
                for layout in ("offset_size", "size_offset"):
                    pos = 16
                    records = []
                    valid = True
                    for _ in range(count):
                        if pos + 2 > len(data):
                            valid = False
                            break
                        path_len = struct.unpack_from("<H", data, pos)[0]
                        pos += 2
                        if path_len == 0 or pos + path_len + 8 > len(data):
                            valid = False
                            break
                        path = data[pos:pos + path_len].decode("utf-8", "replace")
                        pos += path_len
                        first, second = struct.unpack_from("<II", data, pos)
                        pos += 8
                        offset, size = (first, second) if layout == "offset_size" else (second, first)
                        if not path or any(ord(ch) < 32 for ch in path) or offset < index_end or size <= 0 or offset + size > len(data):
                            valid = False
                        records.append((path, offset, size))
                    good = sum(1 for path, offset, size in records if path and offset >= index_end and size > 0 and offset + size <= len(data))
                    print(f"  NSK1 layout {layout}: parsed={len(records)}/{count}, index_cursor={pos}, valid_entries={good}, layout_valid={valid}")
                    print("  NSK1 first entries:", records[:6])
