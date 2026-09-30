#!/usr/bin/env python3
"""PogPet product preview renderer — mesh → product mockups.

Generates preview images for each product type from a user's pet photo.
Used for pog.pet website and Etsy listing images.

Usage:
    python3 product_previews.py <photo_path> <pet_name>
"""
import os
import sys
import hashlib
import time
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "fonts")
OUT = os.path.join(ROOT, "product_previews")


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def circle_photo(photo_path, diameter):
    """Center-crop + circular mask."""
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


def render_figure_preview(photo_path, pet_name="Max"):
    """Render brick figure product preview."""
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), (245, 245, 247))
    d = ImageDraw.Draw(img)
    
    # Title
    d.text((W//2 - 200, 50), "BRICK FIGURE", font=font("Inter-Bold.ttf", 48), fill=(30, 30, 30))
    d.text((W//2 - 150, 120), f"${pet_name}", font=font("Inter-Regular.ttf", 36), fill=(100, 100, 100))
    
    # Photo placeholder (large, centered)
    ring = circle_photo(photo_path, 500)
    rgba = img.convert("RGBA")
    rgba.paste(ring, ((W - 500) // 2, 200), ring)
    img = rgba.convert("RGB")
    d = ImageDraw.Draw(img)
    
    # Product label
    d.text((W//2 - 250, 750), "8cm · PLA · Display Base", font=font("Inter-Regular.ttf", 30), fill=(100, 100, 100))
    d.text((W//2 - 100, 800), "$19.99", font=font("Inter-Bold.ttf", 48), fill=(255, 106, 61))
    
    # Add-on hints
    y = 900
    for item in ["+ Wrapping Paper $8.99", "+ Sticker Pack $4.99", "+ Card $3.99"]:
        d.text((W//2 - 150, y), item, font=font("Inter-Regular.ttf", 26), fill=(150, 150, 150))
        y += 40
    
    return img


def render_ornament_preview(photo_path, pet_name="Max"):
    """Render pet ornament product preview."""
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), (245, 245, 247))
    d = ImageDraw.Draw(img)
    
    # Title
    d.text((W//2 - 250, 50), "PET ORNAMENT", font=font("Inter-Bold.ttf", 48), fill=(30, 30, 30))
    d.text((W//2 - 150, 120), f"${pet_name}", font=font("Inter-Regular.ttf", 36), fill=(100, 100, 100))
    
    # Photo in ornament shape (circle with hook)
    ring = circle_photo(photo_path, 450)
    rgba = img.convert("RGBA")
    rgba.paste(ring, ((W - 450) // 2, 200), ring)
    img = rgba.convert("RGB")
    d = ImageDraw.Draw(img)
    
    # Hook line
    d.line([(W//2, 180), (W//2, 200)], fill=(180, 180, 180), width=4)
    d.ellipse([(W//2 - 15, 165), (W//2 + 15, 195)], outline=(180, 180, 180), width=3)
    
    # Product label
    d.text((W//2 - 250, 700), "7cm · PLA · Hanging Loop", font=font("Inter-Regular.ttf", 30), fill=(100, 100, 100))
    d.text((W//2 - 100, 750), "$14.99", font=font("Inter-Bold.ttf", 48), fill=(255, 106, 61))
    
    return img


def render_wrapping_preview(photo_path, pet_name="Max"):
    """Render wrapping paper product preview."""
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), (245, 245, 247))
    d = ImageDraw.Draw(img)
    
    # Title
    d.text((W//2 - 300, 50), "WRAPPING PAPER", font=font("Inter-Bold.ttf", 48), fill=(30, 30, 30))
    d.text((W//2 - 150, 120), f"${pet_name}", font=font("Inter-Regular.ttf", 36), fill=(100, 100, 100))
    
    # Pattern preview (3x3 grid of small circular photos)
    ring = circle_photo(photo_path, 150)
    for row in range(3):
        for col in range(3):
            x = 200 + col * 280
            y = 250 + row * 280
            rgba = img.convert("RGBA")
            rgba.paste(ring, (x, y), ring)
            img = rgba.convert("RGB")
            d = ImageDraw.Draw(img)
    
    # Product label
    d.text((W//2 - 250, 1100), "Satin · FSC · Custom Pattern", font=font("Inter-Regular.ttf", 30), fill=(100, 100, 100))
    d.text((W//2 - 100, 1150), "$8.99", font=font("Inter-Bold.ttf", 48), fill=(255, 106, 61))
    
    return img


def render_sticker_preview(photo_path, pet_name="Max"):
    """Render sticker pack product preview."""
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), (245, 245, 247))
    d = ImageDraw.Draw(img)
    
    # Title
    d.text((W//2 - 200, 50), "STICKER PACK", font=font("Inter-Bold.ttf", 48), fill=(30, 30, 30))
    d.text((W//2 - 150, 120), f"${pet_name}", font=font("Inter-Regular.ttf", 36), fill=(100, 100, 100))
    
    # Sticker grid (different sizes to show variety)
    sizes = [120, 100, 80, 120, 100]
    x_positions = [150, 320, 470, 620, 770]
    y_positions = [300, 350, 280, 320, 360]
    
    for i, (sz, x, y) in enumerate(zip(sizes, x_positions, y_positions)):
        ring = circle_photo(photo_path, sz)
        rgba = img.convert("RGBA")
        rgba.paste(ring, (x, y), ring)
        img = rgba.convert("RGB")
        d = ImageDraw.Draw(img)
    
    # Product label
    d.text((W//2 - 250, 550), "8-12 Stickers · Vinyl · Waterproof", font=font("Inter-Regular.ttf", 30), fill=(100, 100, 100))
    d.text((W//2 - 100, 600), "$4.99", font=font("Inter-Bold.ttf", 48), fill=(255, 106, 61))
    
    return img


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 product_previews.py <photo_path> [pet_name]")
        sys.exit(1)
    
    photo = sys.argv[1]
    pet_name = sys.argv[2] if len(sys.argv) > 2 else "Max"
    
    os.makedirs(OUT, exist_ok=True)
    
    previews = [
        ("figure", render_figure_preview),
        ("ornament", render_ornament_preview),
        ("wrapping", render_wrapping_preview),
        ("sticker", render_sticker_preview),
    ]
    
    for name, renderer in previews:
        img = renderer(photo, pet_name)
        out = os.path.join(OUT, f"{name}_preview.png")
        img.save(out, "PNG")
        print(f"  {name:12s} -> {out} ({os.path.getsize(out) / 1024:.0f}KB)")
    
    print(f"\nGenerated {len(previews)} product previews")


if __name__ == "__main__":
    main()
