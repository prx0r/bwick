#!/usr/bin/env python3
"""PogPet card generation API — photo + template → card design.

Usage:
    python3 card_api.py <photo_path> <template_id> [pet_name] [year] [age] [date]
    
Example:
    python3 card_api.py photo.jpg xmas_classic Max 2026
    python3 card_api.py photo.jpg bday_party Max "" 3
"""
import os
import sys
import json
import hashlib
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from pogpet_cards import render_card, TEMPLATES


def generate_card(photo_path, template_id, pet_name="Max", year="2026",
                  age="3", date="Dec 25"):
    """Generate a card design from photo + template."""
    template = next((t for t in TEMPLATES if t["id"] == template_id), None)
    if not template:
        return {"error": f"Template '{template_id}' not found", "available": [t["id"] for t in TEMPLATES]}
    
    # Generate the card
    img = render_card(template, photo_path=photo_path, pet_name=pet_name,
                      year=year, age=age, date=date)
    
    # Save to output directory
    out_dir = os.path.join(ROOT, "generated_cards")
    os.makedirs(out_dir, exist_ok=True)
    
    # Generate unique filename
    photo_hash = hashlib.md5(photo_path.encode()).hexdigest()[:8]
    timestamp = int(time.time())
    filename = f"{template_id}_{photo_hash}_{timestamp}.png"
    out_path = os.path.join(out_dir, filename)
    
    img.save(out_path, "PNG")
    
    # Get file size
    file_size = os.path.getsize(out_path)
    
    return {
        "success": True,
        "template": template_id,
        "template_name": template["name"],
        "pet_name": pet_name,
        "output_path": out_path,
        "file_size_kb": round(file_size / 1024, 1),
        "dimensions": f"{img.width}x{img.height}",
    }


def list_templates():
    """List all available templates."""
    return {
        "templates": [
            {
                "id": t["id"],
                "name": t["name"],
                "theme": t["theme"],
                "headline": t["headline"].replace("{pet_name}", "NAME"),
            }
            for t in TEMPLATES
        ]
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 card_api.py <command> [args]")
        print("Commands:")
        print("  list                          - List all templates")
        print("  generate <photo> <template>   - Generate a card")
        print("  generate <photo> <template> <name> <year> <age> <date>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "list":
        result = list_templates()
        print(json.dumps(result, indent=2))
    
    elif cmd == "generate":
        if len(sys.argv) < 4:
            print("Usage: python3 card_api.py generate <photo_path> <template_id> [pet_name] [year] [age] [date]")
            sys.exit(1)
        
        photo = sys.argv[2]
        template_id = sys.argv[3]
        pet_name = sys.argv[4] if len(sys.argv) > 4 else "Max"
        year = sys.argv[5] if len(sys.argv) > 5 else "2026"
        age = sys.argv[6] if len(sys.argv) > 6 else "3"
        date = sys.argv[7] if len(sys.argv) > 7 else "Dec 25"
        
        result = generate_card(photo, template_id, pet_name, year, age, date)
        print(json.dumps(result, indent=2))
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
