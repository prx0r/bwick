#!/usr/bin/env python3
"""Render all 20 FunnyLabs templates to card PNGs (5:7) with PIL.

Uses the real template metadata + first joke from each pool so the gallery
shows actual card content, not placeholders. No node, no npm, stdlib + PIL.

Output: card-studio/static/cards/<id>.png and worker/static/cards/<id>.png
(identical files; local serves now, worker ships on next wrangler deploy).

Run: /usr/bin/python3 render_cards.py  (needs PIL + fonts/Inter-*.ttf)
"""
import os
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

from humour_mcp.jokes import generate_jokes  # noqa: E402
from humour_mcp.templates import TEMPLATES  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "fonts")
OUT_LOCAL = os.path.join(ROOT, "card-studio", "static", "cards")
OUT_WORKER = os.path.join(ROOT, "worker", "static", "cards")

W, H = 1000, 1400
BG = (18, 18, 22)
ACCENT = (255, 106, 61)
MUTED = (150, 150, 160)
WHITE = (245, 245, 247)

FAMILY_EMOJI = {
    "contrast": "\U0001F43E",
    "status_inversion": "\U0001F3A4",
    "documentary": "\U0001F4F0",
    "observation": "\U0001F50E",
    "corporate": "\U0001F4CB",
    "meta": "\U0001FA9E",
    "mixed": "\U0001F3B2",
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = (text or "").split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_one(t, photo_path=None):
    jokes = generate_jokes(t["id"], "James", ["AGI obsessive"], "birthday",
                           "roast", pet_name="Max", pet_species="dog", count=1)
    j = jokes[0] if jokes else {"setup": t["name"], "punchline": t["description"]}
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # accent bar + frame
    d.rectangle([0, 0, W, 14], fill=ACCENT)
    d.rectangle([28, 28, W - 28, H - 28], outline=(60, 60, 70), width=2)
    # kicker: family + occasion
    kick = (t.get("family", "card") + ("  ·  christmas" if t.get("occasions") else "")).upper()
    d.text((70, 80), kick, font=font("Inter-Bold.ttf", 34), fill=ACCENT)
    # headline (setup)
    y = 150
    for line in wrap(d, j["setup"], font("Inter-Black.ttf", 56), W - 140)[:7]:
        d.text((70, y), line, font=font("Inter-Black.ttf", 56), fill=WHITE)
        y += 72
    # pet visual (uploaded photo circled in, else emoji placeholder)
    y += 30
    if photo_path and os.path.exists(photo_path):
        ring = circle_thumb(photo_path, 300)
        rgba = img.convert("RGBA")
        rgba.paste(ring, (64, y - 6), ring)
        img = rgba.convert("RGB")
        d = ImageDraw.Draw(img)
    else:
        emoji = FAMILY_EMOJI.get(t.get("family", ""), "\U0001F43E")
        try:
            d.text((70, y), emoji, font=font("Inter-Regular.ttf", 150), fill=WHITE)
        except Exception:
            d.ellipse([70, y, 220, y + 150], outline=MUTED, width=4)
    y += 200
    # punchline
    for line in wrap(d, j["punchline"], font("Inter-Regular.ttf", 40), W - 140)[:10]:
        d.text((70, y), line, font=font("Inter-Regular.ttf", 40), fill=MUTED)
        y += 54
    # brand footer
    d.text((70, H - 110), "ROAST.PET", font=font("Inter-Bold.ttf", 30), fill=(90, 90, 100))
    d.text((70, H - 70), t["name"], font=font("Inter-Regular.ttf", 26), fill=(90, 90, 100))
    return img


def circle_thumb(photo_path, diameter):
    """Center square-crop + circular mask. Returns RGBA circle thumbnail."""
    from PIL import ImageOps
    ph = Image.open(photo_path).convert("RGB")
    side = min(ph.size)
    left = (ph.width - side) // 2
    top = (ph.height - side) // 2
    ph = ph.crop((left, top, left + side, top + side)).resize((diameter, diameter))
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, diameter, diameter], fill=255)
    circ = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    circ.paste(ph, (0, 0), mask)
    ring = Image.new("RGBA", (diameter + 12, diameter + 12), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse([0, 0, diameter + 12, diameter + 12],
                                 outline=(255, 106, 61, 255), width=6)
    ring.paste(circ, (6, 6), circ)
    return ring


def render_with_photo(template_id, photo_path, out_path=None):
    """Render one template with the uploaded photo circled in (replaces emoji)."""
    t = next(x for x in TEMPLATES if x["id"] == template_id)
    img = render_one(t).convert("RGBA")
    ring = circle_thumb(photo_path, 300)
    # paste over the emoji block area (same y as render_one's emoji row)
    img.paste(ring, (64, 470), ring)
    img = img.convert("RGB")
    if out_path:
        img.save(out_path, "PNG")
    return img


def main():
    os.makedirs(OUT_LOCAL, exist_ok=True)
    os.makedirs(OUT_WORKER, exist_ok=True)
    for t in TEMPLATES:
        img = render_one(t)
        for out in (os.path.join(OUT_LOCAL, t["id"] + ".png"),
                    os.path.join(OUT_WORKER, t["id"] + ".png")):
            img.save(out, "PNG")
        print(f"  {t['id']:28s} ok")
    print(f"wrote {len(TEMPLATES)} cards x2")


if __name__ == "__main__":
    main()
