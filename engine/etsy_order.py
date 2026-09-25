#!/usr/bin/env python3
"""Etsy order simulator + pipeline (Meshy/fulfilment stubbed, swappable).

Generates faithful fake Etsy orders (receipt + message photos, clean AND messy)
and runs them through avatar -> card -> listing -> fulfil-payload stages.
Meshy + Prodigi/Makr3D calls sit behind stub functions with the EXACT shapes the
real APIs take; swapping in keys changes nothing else.

Run: python3 etsy_order.py --demo
"""
import base64
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUT = "/tmp/opencode/etsy-sim"


# ---------- Stage 0: fake Etsy orders ----------

def fake_orders():
    """One clean order, one messy (screenshot, missing facts). Photos as bytes."""
    from PIL import Image, ImageDraw
    os.makedirs(OUT, exist_ok=True)

    def pet_jpg(path, tint):
        im = Image.new("RGB", (600, 600), tint)
        d = ImageDraw.Draw(im)
        d.ellipse([180, 150, 420, 390], fill=(120, 70, 30))
        im.save(path)
        return open(path, "rb").read()

    clean = {
        "order_id": "ETSY-TEST-001", "buyer": "james.test@example.com", "gift": False,
        "items": [{"listing": "roast-card", "qty": 1,
                   "personalization": {"recipient": "James", "pet": "Max",
                                       "occasion": "birthday", "roast": "savage",
                                       "facts": "AGI obsessive"}}],
        "notes": "please make him look extra guilty lol",
        "photos": [pet_jpg(f"{OUT}/clean-front.jpg", (210, 130, 60)),
                   pet_jpg(f"{OUT}/clean-side.jpg", (190, 120, 55))],
    }
    messy = {
        "order_id": "ETSY-TEST-002", "buyer": "mum.test@example.com", "gift": True,
        "items": [{"listing": "roast-card", "qty": 1,
                   "personalization": {"recipient": "Mum", "pet": "",  # missing pet name
                                       "occasion": "christmas", "roast": "mild",
                                       "facts": ""}}],  # missing facts
        "notes": "",
        "photos": [pet_jpg(f"{OUT}/messy-dark.jpg", (40, 30, 25))],  # dark/poor
    }
    return [clean, messy]


# ---------- Stage 1: ingest + QC ----------

def ingest(order):
    from PIL import Image
    import io
    p = order["items"][0]["personalization"]
    issues = []
    if not p.get("pet"):
        issues.append("missing pet name (defaulted to 'Pet')")
        p["pet"] = "Pet"
    if not p.get("facts"):
        issues.append("missing facts (generic roast)")
    good_photos = []
    for b in order["photos"]:
        try:
            im = Image.open(io.BytesIO(b))
            im.verify()
            im = Image.open(io.BytesIO(b))
            if min(im.size) >= 200 and len(b) > 3000:
                good_photos.append(b)
            else:
                issues.append("photo too small/low-quality (skipped)")
        except Exception:
            issues.append("unreadable photo (skipped)")
    if not good_photos:
        return {"ok": False, "issues": issues + ["no usable photos"]}
    return {"ok": True, "issues": issues, "photos": good_photos}


# ---------- Stage 2: avatar (REAL - humour_mcp/avatar.py) ----------

def make_avatar(order, photos):
    from humour_mcp.avatar import create_avatar
    p = order["items"][0]["personalization"]
    tmp = f"{OUT}/{order['order_id']}-avatar-src.jpg"
    with open(tmp, "wb") as f:
        f.write(photos[0])
    return create_avatar(tmp, p["pet"], "")


# ---------- Stage 3: mesh (STUBBED - exact Meshy multi-image shape) ----------

def mesh_stub(avatar, photos):
    """Swap with real call: POST /openapi/v1/multi-image-to-3d.
    image_urls[1..4] base64, target_formats ["glb"], multi_view_thumbnails true."""
    payload = {
        "image_urls": ["data:image/jpeg;base64," + base64.b64encode(b).decode()[:40] + "..."
                       for b in photos[:4]],
        "target_formats": ["glb"],
        "multi_view_thumbnails": True,
    }
    # STUB: local avatar PNG stands in for the GLB until the key lands.
    from humour_mcp.avatar import photo_path
    return {"stub": True, "would_send": payload,
            "local_mesh_standin": photo_path(avatar["id"])}


# ---------- Stage 4: card (REAL - render_cards.py) ----------

def make_card(order, avatar):
    from render_cards import render_with_photo
    from humour_mcp.avatar import photo_path
    tid = "xmas_cat_vs_tree" if order["items"][0]["personalization"]["occasion"] == "christmas" else "pet_standup"
    out = f"{OUT}/{order['order_id']}-card.png"
    render_with_photo(tid, photo_path(avatar["id"]), out)
    return {"template": tid, "png": out}


# ---------- Stage 5: listing bundle ----------

def make_listing(order, card):
    p = order["items"][0]["personalization"]
    bundle = {
        "title": (f"Personalized Pet Roast Card From Photo | Custom {p['pet']} "
                  f"{p['occasion'].title()} Card | Funny Gift")[:140],
        "tags": ["personalized pet card", "custom dog card", "funny birthday card",
                 "pet roast", "custom christmas card", "dog mom gift", "funny gift",
                 "pet lover gift", "custom greeting card", "roast card",
                 "personalised pet gift", "birthday card", "christmas card"][:13],
        "personalization": p,
        "photos": [card["png"]],
        "video_note": "15s muted teaser (talk.py) goes in slot 1",
    }
    with open(f"{OUT}/{order['order_id']}-listing.json", "w") as f:
        json.dump(bundle, f, indent=2)
    return bundle


# ---------- Stage 6: fulfil payloads (STUBBED) ----------

def fulfil_stub(order, card):
    """Swap with real calls: Prodigi POST /v4.0/orders + Makr3D job.
    Review-before-send: payloads written, never submitted without approve flag."""
    prodigi = {"sku": "FINEART-GRE-5X7-TBD", "copies": 1,
               "assets": [{"printArea": "default", "url": "R2HOST/" + os.path.basename(card["png"])}],
               "recipient": "FROM_ETSY_RECEIPT", "approve_required": True}
    with open(f"{OUT}/{order['order_id']}-prodigi.json", "w") as f:
        json.dump(prodigi, f, indent=2)
    return {"prodigi": prodigi, "makr3d": "SKU-dependent (figure orders only)"}


def run_demo():
    os.makedirs(OUT, exist_ok=True)
    results = []
    for order in fake_orders():
        print(f"--- {order['order_id']} ---")
        ing = ingest(order)
        print(f"  ingest: ok={ing['ok']} issues={ing['issues']}")
        if not ing["ok"]:
            results.append((order["order_id"], "REJECTED", ing["issues"]))
            continue
        av = make_avatar(order, ing["photos"])
        print(f"  avatar: {av['id']}")
        mesh = mesh_stub(av, ing["photos"])
        print(f"  mesh: stub, would send {len(mesh['would_send']['image_urls'])} photos")
        card = make_card(order, av)
        print(f"  card: {card['template']} -> {os.path.basename(card['png'])}")
        make_listing(order, card)
        fulfil_stub(order, card)
        results.append((order["order_id"], "OK", []))
    print("\nRESULTS:", results)
    assert results[0][1] == "OK", "clean order must pass end-to-end"
    print("DEMO GREEN: pipeline shippable; swap mesh_stub + fulfil_stub when keys land.")


if __name__ == "__main__":
    assert "--demo" in sys.argv, "usage: python3 etsy_order.py --demo"
    run_demo()
