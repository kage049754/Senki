#!/usr/bin/env python3
"""Verify generated page 4+ buttons retain the original button rim/artwork."""
from pathlib import Path
import plistlib
import re
import sys
from PIL import Image

if len(sys.argv) != 2:
    raise SystemExit("usage: test_page_button_assets.py PATH_TO_Resources")

resources = Path(sys.argv[1])

def read(name: str) -> Image.Image:
    path = resources / name
    if not path.is_file():
        raise SystemExit(f"Missing generated pagination asset: {path}")
    image = Image.open(path).convert("RGBA")
    if image.size != (40, 40):
        raise SystemExit(f"Expected 40x40 page button {name}, got {image.size}")
    return image

def read_original_frame(state: str) -> Image.Image:
    atlas_path = resources / "Select.png"
    plist_path = resources / "Select.plist"
    if not atlas_path.is_file() or not plist_path.is_file():
        raise SystemExit("Original Select.png/Select.plist atlas files are missing")
    with plist_path.open("rb") as stream:
        frames = plistlib.load(stream).get("frames", {})
    name = f"page1_{state}.png"
    if name not in frames:
        raise SystemExit(f"Original page button frame missing from Select.plist: {name}")
    frame = frames[name]
    if frame.get("textureRotated", False):
        raise SystemExit(f"Unexpected rotated original page button frame: {name}")
    numbers = [int(float(x)) for x in re.findall(r"-?\d+(?:\.\d+)?", frame["textureRect"])]
    if len(numbers) != 4:
        raise SystemExit(f"Unsupported textureRect for {name}: {frame['textureRect']!r}")
    x, y, width, height = numbers
    atlas = Image.open(atlas_path).convert("RGBA")
    image = atlas.crop((x, y, x + width, y + height))
    if image.size != (40, 40):
        raise SystemExit(f"Expected 40x40 original frame {name}, got {image.size}")
    return image

def read_original_page_frame(page: int, state: str) -> Image.Image:
    atlas_path = resources / "Select.png"
    plist_path = resources / "Select.plist"
    if not atlas_path.is_file() or not plist_path.is_file():
        raise SystemExit("Original Select.png/Select.plist atlas files are missing")
    with plist_path.open("rb") as stream:
        frames = plistlib.load(stream).get("frames", {})
    name = f"page{page}_{state}.png"
    if name not in frames:
        raise SystemExit(f"Original page button frame missing from Select.plist: {name}")
    frame = frames[name]
    if frame.get("textureRotated", False):
        raise SystemExit(f"Unexpected rotated original page button frame: {name}")
    numbers = [int(float(x)) for x in re.findall(r"-?\d+(?:\.\d+)?", frame["textureRect"])]
    if len(numbers) != 4:
        raise SystemExit(f"Unsupported textureRect for {name}: {frame['textureRect']!r}")
    x, y, width, height = numbers
    atlas = Image.open(atlas_path).convert("RGBA")
    image = atlas.crop((x, y, x + width, y + height))
    if image.size != (40, 40):
        raise SystemExit(f"Expected 40x40 original frame {name}, got {image.size}")
    return image


def outside_center_matches(original: Image.Image, generated: Image.Image) -> bool:
    src = original.load()
    dst = generated.load()
    # The generator may repaint only the central numeral region; the outer rim must stay pixel-identical.
    for y in range(40):
        for x in range(40):
            inside_repaint_region = 12 <= x <= 28 and 12 <= y <= 28
            if not inside_repaint_region and src[x, y] != dst[x, y]:
                return False
    return True

# Pages 1-3 must remain backed by their original, distinct atlas frames.
for page in (1, 2, 3):
    original_off = read_original_page_frame(page, "off")
    original_on = read_original_page_frame(page, "on")
    if list(original_off.getdata()) == list(original_on.getdata()):
        raise SystemExit(f"Original page {page} normal/selected artwork is identical")
    if original_off.getbbox() is None or original_on.getbbox() is None:
        raise SystemExit(f"Original page {page} button artwork is fully transparent")

for page in (4, 5):
    for state in ("off", "on"):
        generated_name = f"senki_page{page}_{state}.png"
        original = read_original_frame(state)
        generated = read(generated_name)
        if not outside_center_matches(original, generated):
            raise SystemExit(
                f"{generated_name} changed pixels outside the central numeral region; "
                "the original page-button rim/state artwork was not preserved."
            )
        if generated.getbbox() is None:
            raise SystemExit(f"Generated button is fully transparent: {generated_name}")
    off = read(f"senki_page{page}_off.png")
    on = read(f"senki_page{page}_on.png")
    if list(off.getdata()) == list(on.getdata()):
        raise SystemExit(f"Page {page} normal and selected button artwork are identical")

print("Pages 1-3 retain distinct original normal/selected atlas frames; pages 4-5 are 40x40, visible, distinct, and preserve the original button rim.")
