#!/usr/bin/env python3
"""PogPet card templates — photo + frame + text, no jokes needed.

Simple, clean cards where the customer's pet photo IS the design.
Drop a photo in, add name + occasion, done.

Run: python3 pogpet_cards.py
Output: pogpet_cards/<template_id>.png
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "fonts")
OUT = os.path.join(ROOT, "pogpet_cards")

# Card dimensions (5x7 at 300dpi)
W, H = 1500, 2100

# Color palettes per theme
PALETTES = {
    "christmas": {
        "bg": (25, 40, 30),
        "accent": (200, 40, 40),
        "text": (255, 255, 255),
        "muted": (180, 200, 180),
    },
    "birthday": {
        "bg": (40, 30, 50),
        "accent": (255, 200, 50),
        "text": (255, 255, 255),
        "muted": (200, 180, 220),
    },
    "thankyou": {
        "bg": (30, 40, 35),
        "accent": (100, 200, 150),
        "text": (255, 255, 255),
        "muted": (180, 200, 190),
    },
    "justbecause": {
        "bg": (35, 30, 45),
        "accent": (180, 130, 255),
        "text": (255, 255, 255),
        "muted": (180, 170, 200),
    },
}

TEMPLATES = [
    # Christmas cards
    {"id": "xmas_classic", "name": "Merry Christmas", "theme": "christmas",
     "headline": "Merry Christmas", "subline": "{pet_name}", "emoji": "🎄"},
    {"id": "xmas_festive", "name": "Happy Holidays", "theme": "christmas",
     "headline": "Happy Holidays", "subline": "{pet_name} | {year}", "emoji": "❄️"},
    {"id": "xmas_naughty", "name": "Naughty List", "theme": "christmas",
     "headline": "Officially on the\nNaughty List", "subline": "{pet_name}", "emoji": "😈"},
    {"id": "xmas_santa", "name": "Santa Paws", "theme": "christmas",
     "headline": "Santa Paws\nis Coming", "subline": "{pet_name}", "emoji": "🎅"},
    {"id": "xmas_snow", "name": "Let It Snow", "theme": "christmas",
     "headline": "Let It Snow", "subline": "{pet_name}", "emoji": "⛄"},
    # Birthday cards
    {"id": "bday_party", "name": "Happy Birthday", "theme": "birthday",
     "headline": "Happy Birthday\n{pet_name}!", "subline": "{age} years of chaos", "emoji": "🎂"},
    {"id": "bday_elegant", "name": "Birthday Wishes", "theme": "birthday",
     "headline": "Birthday Wishes", "subline": "{pet_name} | {date}", "emoji": "🎈"},
    {"id": "bday_funny", "name": "Another Year Older", "theme": "birthday",
     "headline": "Another Year Older\nStill Acts Like a Puppy", "subline": "{pet_name}", "emoji": "🐾"},
    # Thank you / general
    {"id": "thankyou", "name": "Thank You", "theme": "thankyou",
     "headline": "Thank You", "subline": "From {pet_name}", "emoji": "💝"},
    {"id": "justbecause", "name": "Just Because", "theme": "justbecause",
     "headline": "Just Because\nYou're Awesome", "subline": "{pet_name}", "emoji": "💜"},
]


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap_text(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
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


def circle_photo(photo_path, diameter):
    """Center-crop + circular mask with accent ring."""
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
    return circ


def render_card(template, photo_path=None, pet_name="Max", year="2026",
                age="3", date="Dec 25"):
    """Render a single card. If no photo, show placeholder circle."""
    pal = PALETTES[template["theme"]]
    img = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(img)

    # Border
    d.rectangle([0, 0, W, 16], fill=pal["accent"])
    d.rectangle([40, 40, W - 40, H - 40], outline=(60, 60, 70), width=3)

    # Photo area (center, large)
    photo_y = 300
    photo_size = 800
    if photo_path and os.path.exists(photo_path):
        ring = circle_photo(photo_path, photo_size)
        rgba = img.convert("RGBA")
        rgba.paste(ring, ((W - photo_size) // 2, photo_y), ring)
        img = rgba.convert("RGB")
        d = ImageDraw.Draw(img)
    else:
        # Placeholder circle
        cx, cy = W // 2, photo_y + photo_size // 2
        d.ellipse([cx - photo_size // 2, cy - photo_size // 2,
                    cx + photo_size // 2, cy + photo_size // 2],
                   outline=pal["muted"], width=6)
        d.text((cx - 80, cy - 30), "YOUR PET", font=font("Inter-Bold.ttf", 40),
               fill=pal["muted"])

    # Headline
    headline = template["headline"].replace("{pet_name}", pet_name)
    headline = headline.replace("{age}", age).replace("{date}", date)
    headline = headline.replace("{year}", year)
    y = photo_y + photo_size + 80
    for line in wrap_text(d, headline, font("Inter-Black.ttf", 72), W - 160):
        d.text((80, y), line, font=font("Inter-Black.ttf", 72), fill=pal["text"])
        y += 90

    # Subline
    subline = template["subline"].replace("{pet_name}", pet_name)
    subline = subline.replace("{age}", age).replace("{date}", date)
    subline = subline.replace("{year}", year)
    y += 30
    for line in wrap_text(d, subline, font("Inter-Regular.ttf", 44), W - 160):
        d.text((80, y), line, font=font("Inter-Regular.ttf", 44), fill=pal["muted"])
        y += 58

    # Brand footer
    d.text((80, H - 120), "POG.PET", font=font("Inter-Bold.ttf", 36),
           fill=(90, 90, 100))
    d.text((80, H - 70), "Your pet. In 3D.", font=font("Inter-Regular.ttf", 28),
           fill=(90, 90, 100))

    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    for t in TEMPLATES:
        img = render_card(t)
        out = os.path.join(OUT, t["id"] + ".png")
        img.save(out, "PNG")
        print(f"  {t['id']:20s} {t['name']:25s} -> {out}")
    print(f"\nGenerated {len(TEMPLATES)} PogPet card templates")


if __name__ == "__main__":
    main()
