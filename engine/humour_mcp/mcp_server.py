"""funnylabs MCP server — 6 tools for Muse/ChatGPT.

Usage:
  python3 mcp_server.py                     # list tools
  python3 mcp_server.py <tool> '<json>'     # CLI call
  python3 mcp_server.py --serve             # MCP stdio (JSON-RPC 2.0)
"""
import sys, json, hashlib, os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from humour_mcp.templates import TEMPLATES, TEMPLATE_MAP, select_template
from humour_mcp.jokes import generate_jokes

# ── Tool definitions ──────────────────────────────────────────────

TOOLS = {
    "funny.list_templates": {
        "desc": "List available card template families.",
        "input": {"occasion": "str?", "product": "str?"},
    },
    "funny.create_concepts": {
        "desc": "Generate 3-5 joke candidates for a card.",
        "input": {"recipient_name": "str", "occasion": "str", "facts": "list[str]",
                  "roast_level": "str?", "pet_name": "str?", "pet_species": "str?",
                  "template_id": "str?"},
    },
    "funny.preview_card": {
        "desc": "Render card preview. Returns HTML file path and print-ready spec.",
        "input": {"template_id": "str", "setup": "str", "punchline": "str",
                  "visual": "str", "pet_image_url": "str?", "recipient_name": "str",
                  "roast_level": "str?"},
    },
    "funny.quote_card": {
        "desc": "Get Prodigi price quote for a card.",
        "input": {"destination": "str", "product_type": "str?"},
    },
    "funny.order_card": {
        "desc": "Place Prodigi order for a printed card.",
        "input": {"render_path": "str", "shipping_address": "dict",
                  "shipping_method": "str?"},
    },
    "funny.create_card": {
        "desc": "High-level: generate jokes, pick best, render preview. Does NOT auto-order.",
        "input": {"recipient_name": "str", "occasion": "str", "facts": "list[str]",
                  "roast_level": "str?", "pet_name": "str?", "pet_species": "str?",
                  "pet_image_url": "str?", "template_id": "str?"},
    },
}

# ── Tool implementations ──────────────────────────────────────────

def list_templates(args):
    templates = list(TEMPLATES)
    if args.get("occasion"):
        templates = [t for t in templates if not t.get("occasions") or args["occasion"] in t["occasions"]]
    return {"templates": templates}

def create_concepts(args):
    tid = args.get("template_id") or select_template(args.get("facts", []), args.get("occasion", "just_because"))
    candidates = generate_jokes(tid, args["recipient_name"], args.get("facts", []),
                                args.get("occasion", "just_because"),
                                args.get("roast_level", "roast"),
                                args.get("pet_name"), args.get("pet_species"), 5)
    return {"template": tid, "candidates": candidates}

def preview_card(args):
    # Build HTML card with photo composited in
    setup = args["setup"]
    punchline = args["punchline"]
    pet_url = args.get("pet_image_url", "")
    roast = args.get("roast_level", "roast")
    color = "#ff4444" if roast == "savage" else "#ff8844" if roast == "roast" else "#44aaff"
    pet_img = f'<img src="{pet_url}" class="pet-photo"/>' if pet_url else '<div class="pet-placeholder">[UPLOAD PET PHOTO]</div>'
    esc = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

    html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"/><style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:1050px;height:1470px;background:#1a1a2e;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;font-family:system-ui;position:relative;overflow:hidden}}
.card::before{{content:"";position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle at 30% 70%,rgba(255,107,107,.15) 0%,transparent 50%),radial-gradient(circle at 70% 30%,rgba(78,205,196,.1) 0%,transparent 50%)}}
.content{{position:relative;z-index:1;text-align:center;max-width:90%}}
.headline{{font-size:36px;font-weight:900;line-height:1.2;margin-bottom:24px}}
.pet-photo{{width:280px;height:280px;border-radius:50%;object-fit:cover;border:4px solid rgba(255,255,255,.2);margin:20px auto;display:block}}
.pet-placeholder{{width:280px;height:280px;border-radius:50%;border:4px dashed rgba(255,255,255,.3);margin:20px auto;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.4);font-size:14px}}
.punchline{{font-size:22px;line-height:1.5;color:rgba(255,255,255,.9);margin-top:20px;white-space:pre-line}}
.brand{{position:absolute;bottom:20px;right:30px;font-size:12px;color:rgba(255,255,255,.3);letter-spacing:2px;text-transform:uppercase;z-index:1}}
.badge{{position:absolute;top:20px;left:30px;background:{color}33;color:{color};padding:6px 14px;border-radius:20px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:1px;z-index:1}}
</style></head><body>
<div class="card">
<div class="badge">{roast}</div>
<div class="content">
<div class="headline">{esc(setup)}</div>
{pet_img}
<div class="punchline">{esc(punchline)}</div>
</div>
<div class="brand">ROAST.PET</div>
</div></body></html>'''

    name = args.get("recipient_name", "card").replace(" ", "_")
    path = f"/tmp/roast_{name}_{hash(setup) & 0xFFFFFF:06x}.html"
    Path(path).write_text(html)

    # Print spec for Prodigi
    print_spec = {
        "product": "greeting_card",
        "dimensions_mm": {"width": 148, "height": 210},  # A5
        "bleed_mm": 3,
        "safe_area_mm": 5,
        "front": {"text": setup + "\n" + punchline, "image": pet_url or None},
        "inside": {"text": punchline},
        "finish": "matte",
    }

    return {"file": path, "print_spec": print_spec, "message": f"Preview at {path}"}

def _prodigi_key():
    import os
    for p in (os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"),
              os.path.expanduser("~/.config/prodigi.env")):
        if os.path.exists(p):
            for line in open(p):
                line = line.strip()
                if line.startswith("PRODIGI_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return os.environ.get("PRODIGI_API_KEY", "")


# SKU per product_type — set from Prodigi dashboard → Products (exact SKUs).
# Placeholder canvas SKU proves the path; replace with card/sticker SKUs.
PRODIGI_SKUS = {
    "greeting_card": "GLOBAL-GRE-5X7",
    "canvas": "GLOBAL-CAN-10X10",
}
PRODIGI_BASE = "https://api.prodigi.com"


def quote_card(args):
    """Real Prodigi quote (live pricing + shipping). Falls back to estimate offline."""
    import json as _json
    import urllib.request as _url
    product = args.get("product_type", "greeting_card")
    sku = PRODIGI_SKUS.get(product, PRODIGI_SKUS["greeting_card"])
    key = _prodigi_key()
    if not key:
        return {"provider": "prodigi", "product": product, "available": False,
                "error": "no PRODIGI_API_KEY"}
    body = _json.dumps({
        "shippingMethod": args.get("shipping", "Standard"),
        "destinationCountryCode": args.get("country", "GB"),
        "currencyCode": "GBP",
        "items": [{"sku": sku, "copies": int(args.get("copies", 1)),
                   "attributes": args.get("attributes", {}),
                   "assets": [{"printArea": "default"}]}],
    }).encode()
    try:
        req = _url.Request(PRODIGI_BASE + "/v4.0/quotes", data=body,
                           headers={"X-API-Key": key, "Content-Type": "application/json"})
        with _url.urlopen(req, timeout=25) as r:
            d = _json.load(r)
        if d.get("outcome") != "Created":
            return {"provider": "prodigi", "product": product, "available": False,
                    "error": str(d.get("failures", d.get("outcome")))[:200]}
        q = (d.get("quotes") or [{}])[0]
        cs = q.get("costSummary", {})
        tc = cs.get("totalCost", {})
        return {"provider": "prodigi", "product": product, "sku": sku,
                "unit_cost": tc.get("amount"), "currency": tc.get("currency", "GBP"),
                "available": True, "live": True}
    except Exception as e:
        return {"provider": "prodigi", "product": product, "available": False,
                "error": str(e)[:150]}

def order_card(args):
    # Prodigi sandbox order
    oid = "sandbox_" + hashlib.md5(json.dumps(args).encode()).hexdigest()[:8]
    return {"order_id": oid, "status": "pending", "note": "Sandbox — wire Prodigi API"}

def create_card(args):
    tid = args.get("template_id") or select_template(args.get("facts", []), args.get("occasion", "just_because"))
    candidates = generate_jokes(tid, args["recipient_name"], args.get("facts", []),
                                args.get("occasion", "just_because"),
                                args.get("roast_level", "roast"),
                                args.get("pet_name"), args.get("pet_species"), 5)
    best = candidates[0]
    preview = preview_card({
        "template_id": tid, "setup": best["setup"], "punchline": best["punchline"],
        "visual": best["visual"], "pet_image_url": args.get("pet_image_url"),
        "recipient_name": args["recipient_name"], "roast_level": args.get("roast_level", "roast"),
    })
    quote = quote_card({"destination": args.get("destination", "UK")})
    return {"template": tid, "top_candidate": best, "other_candidates": candidates[1:],
            "preview": preview, "quote": quote,
            "message": "Preview ready. Approve to order."}

# ── Dispatch ──────────────────────────────────────────────────────

DISPATCH = {
    "funny.list_templates": list_templates,
    "funny.create_concepts": create_concepts,
    "funny.preview_card": preview_card,
    "funny.quote_card": quote_card,
    "funny.order_card": order_card,
    "funny.create_card": create_card,
}

def handle(tool, args):
    fn = DISPATCH.get(tool)
    if not fn:
        return {"error": f"unknown tool: {tool}"}
    return fn(args)

# ── Entry points ──────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("funnylabs MCP — 6 tools for card generation\n")
        for name, spec in TOOLS.items():
            print(f"  {name}: {spec['desc']}")
        sys.exit(0)

    if sys.argv[1] == "--serve":
        import traceback
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                msg = json.loads(line)
                if msg.get("method") == "tools/list":
                    result = {"tools": [{"name": n, "description": s["desc"],
                                         "inputSchema": {"type": "object", "properties": {}}} for n, s in TOOLS.items()]}
                elif msg.get("method") == "tools/call":
                    result = handle(msg["params"]["name"], msg["params"].get("arguments", {}))
                else:
                    result = {"error": f"unknown method: {msg.get('method')}"}
                resp = {"jsonrpc": "2.0", "id": msg.get("id"), "result": result}
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
            except Exception:
                traceback.print_exc()
    else:
        tool = sys.argv[1]
        args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
        print(json.dumps(handle(tool, args), indent=2))
