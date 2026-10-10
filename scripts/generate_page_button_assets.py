#!/usr/bin/env python3
"""Generate matching image-based pagination controls from the game's original page button art.

The game ships image frames only for pages 1-3. This script crops the existing normal
and selected button frames from Select.png, masks the old numeral, and draws the new
page number. Generated PNGs live only in the temporary CI source workspace.
"""
from __future__ import annotations

import math
import plistlib
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def parse_rect(value: str) -> tuple[int, int, int, int]:
    numbers = [int(float(x)) for x in re.findall(r"-?\d+(?:\.\d+)?", value)]
    if len(numbers) != 4:
        raise ValueError(f"Unsupported textureRect: {value!r}")
    return tuple(numbers)  # x, y, width, height


def roster_slots(basic_lua: Path) -> int:
    text = basic_lua.read_text(encoding="utf-8")
    match = re.search(r"ns\.CharactersLayout\s*=\s*\{([\s\S]*?)\n\}", text)
    if not match:
        raise ValueError("Could not locate ns.CharactersLayout in basic.lua")
    body = re.sub(r"--\[\[[\s\S]*?\]\]", "", match.group(1))
    body = re.sub(r"--[^\n]*", "", body)
    tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", body)
    if not tokens:
        raise ValueError("Character layout was found but no roster slots were parsed")
    return len(tokens)


def crop_frame(atlas: Image.Image, frames: dict, frame_name: str) -> Image.Image:
    if frame_name not in frames:
        raise KeyError(f"Missing original button frame {frame_name!r} in Select.plist")
    frame = frames[frame_name]
    x, y, width, height = parse_rect(frame["textureRect"])
    if frame.get("textureRotated", False):
        raise ValueError(f"Unexpected rotated page-button frame: {frame_name}")
    if x < 0 or y < 0 or x + width > atlas.width or y + height > atlas.height:
        raise ValueError(f"Frame {frame_name} is outside Select.png: {(x, y, width, height)}")
    result = atlas.crop((x, y, x + width, y + height)).convert("RGBA")
    if result.size != (40, 40):
        raise ValueError(f"Unexpected button size for {frame_name}: {result.size}")
    return result


def recolor_center(button: Image.Image, number: str) -> Image.Image:
    """Cover the original single digit with a small center disk, retaining the original rim."""
    pixels = button.load()
    sample_points = [(13, 13), (27, 13), (13, 27), (27, 27), (20, 12), (12, 20), (28, 20), (20, 28)]
    samples = [pixels[x, y] for x, y in sample_points if pixels[x, y][3] > 200]
    if not samples:
        raise ValueError("Cannot sample the interior color of a page button")
    background = tuple(sorted(sample[i] for sample in samples)[len(samples) // 2] for i in range(3)) + (255,)

    # Select a bright foreground color from the original number's central area.
    center_pixels = [
        pixels[x, y]
        for x in range(13, 27)
        for y in range(12, 29)
        if pixels[x, y][3] > 200
    ]
    foreground = max(center_pixels, key=lambda p: sum(p[:3]))[:3] if center_pixels else (245, 245, 245)
    outline = (24, 28, 36, 220)

    draw = ImageDraw.Draw(button)
    draw.ellipse((12, 12, 28, 28), fill=background)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_size = 17 if len(number) == 1 else 13
    font = ImageFont.truetype(font_path, font_size)
    box = draw.textbbox((0, 0), number, font=font, stroke_width=1)
    x = (button.width - (box[2] - box[0])) // 2 - box[0]
    y = (button.height - (box[3] - box[1])) // 2 - box[1] - 1
    draw.text((x, y), number, font=font, fill=foreground + (255,), stroke_width=1, stroke_fill=outline)
    return button


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: generate_page_button_assets.py <projects/NarutoSenki/Resources>")
    resources = Path(sys.argv[1])
    atlas_path = resources / "Select.png"
    plist_path = resources / "Select.plist"
    basic_lua = resources.parent / "lua" / "class" / "basic.lua"
    for required in (atlas_path, plist_path, basic_lua):
        if not required.is_file():
            raise FileNotFoundError(f"Required game source file missing: {required}")

    with plist_path.open("rb") as stream:
        plist = plistlib.load(stream)
    frames = plist.get("frames", {})
    atlas = Image.open(atlas_path).convert("RGBA")
    slots = roster_slots(basic_lua)
    page_count = max(1, math.ceil(slots / 21))
    # Always package pages 4 and 5 so future roster additions do not require
    # another UI asset-generation change. Generate any additional pages needed.
    last_page = max(5, page_count)
    generated = 0
    for page in range(4, last_page + 1):
        for state in ("off", "on"):
            source_frame = f"page1_{state}.png"
            button = crop_frame(atlas, frames, source_frame)
            button = recolor_center(button, str(page))
            destination = resources / f"senki_page{page}_{state}.png"
            button.save(destination, format="PNG", optimize=True)
            with Image.open(destination) as check:
                if check.size != (40, 40) or check.mode != "RGBA":
                    raise ValueError(f"Generated button failed validation: {destination}")
            generated += 1
    print(f"Generated {generated} image-based pagination button states for pages 4-{last_page}; roster slots={slots}, page_count={page_count}.")
    print("Generated buttons use the original page-button frame/rim with separate normal and selected artwork.")


if __name__ == "__main__":
    main()
