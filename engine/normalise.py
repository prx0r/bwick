"""P0.1 — photo intake normalisation (MESH_PIPELINE stage ②).

Order dir -> validated, oriented, sorted, bounded image payloads for Meshy.
No network, no keys. Reference contracts: etsysignal photo_role_policy.json
(front/body/side/favourite roles) and etsy_order.ingest file checks.

Usage:
    from engine.normalise import normalise_order
    result = normalise_order("orders/1234")     # -> {"ok": True, "image_urls": [...]}
"""
from __future__ import annotations

import base64
import io
import os
import re

from PIL import Image, ImageOps

MAX_IMAGES = 4          # Meshy multi-image limit (first = front view)
MIN_SIDE = 200          # px
MIN_BYTES = 3000
MAX_EDGE = 2048         # longest edge after resize
JPEG_QUALITY = 90

ROLE_ORDER = ("front_face", "full_body", "side_view", "side", "threequarter")
ROLE_HINTS = {
    "front_face": ("front", "face", "head"),
    "full_body": ("full_body", "fullbody", "full", "body"),
    "side_view": ("side", "profile", "threequarter", "3-4"),
}
MAGIC = {"jpg": b"\xff\xd8\xff", "png": b"\x89PNG\r\n\x1a\n"}


class Reject(Exception):
    pass


def _role_of(name: str) -> str:
    n = name.lower()
    for role, hints in ROLE_HINTS.items():
        if any(h in n for h in hints):
            return role
    if "fav" in n or "favorite" in n:
        return "favourite"
    return "unknown"


def _magic_ok(path: str, head: bytes) -> str | None:
    if head.startswith(MAGIC["jpg"]):
        return "jpg"
    if head.startswith(MAGIC["png"]):
        return "png"
    return None


def normalise_order(order_dir: str, favourite_passes: bool = True) -> dict:
    """Return ok/image_urls or ok=False + reason (the NEEDS_REPLACEMENT path)."""
    if not os.path.isdir(order_dir):
        return {"ok": False, "reason": f"no order dir: {order_dir}"}

    files = [f for f in sorted(os.listdir(order_dir))
             if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not files:
        return {"ok": False, "reason": "no image files (jpg/png) in order"}

    staged: list[tuple[str, Image.Image]] = []
    seen_dims: set[tuple[int, int]] = set()
    for fname in files:
        path = os.path.join(order_dir, fname)
        try:
            size = os.path.getsize(path)
            with open(path, "rb") as fh:
                head = fh.read(8)
            if size < MIN_BYTES:
                raise Reject(f"{fname}: too small ({size}B < {MIN_BYTES})")
            if _magic_ok(path, head) is None:
                raise Reject(f"{fname}: not a jpeg/png")
            im = Image.open(path)
            im.load()
            im = ImageOps.exif_transpose(im)          # fix phone rotation
            if min(im.size) < MIN_SIDE:
                raise Reject(f"{fname}: min side {min(im.size)}px < {MIN_SIDE}px")
            role = _role_of(fname)
            if role == "favourite" and not favourite_passes:
                continue                                # style ref only, never to Meshy
            if im.size in seen_dims:
                continue                                # near-duplicate guard
            seen_dims.add(im.size)
            staged.append((role, im.convert("RGB")))
        except Reject as r:
            return {"ok": False, "reason": str(r)}
        except Exception as e:
            return {"ok": False, "reason": f"{fname}: undecodable ({e})"}

    if not staged:
        return {"ok": False, "reason": "all images rejected"}

    has_front = any(r == "front_face" for r, _ in staged)
    if len(staged) < 1:
        return {"ok": False, "reason": "no usable images after QC"}
    if not has_front:
        return {"ok": False,
                "reason": "no front-face image (name it *_front_face) — Meshy needs it first"}

    def sort_key(item):
        role, _ = item
        return ROLE_ORDER.index(role) if role in ROLE_ORDER else len(ROLE_ORDER)

    staged.sort(key=sort_key)                             # front first, then body, side
    payload = []
    for _, im in staged[:MAX_IMAGES]:
        w, h = im.size
        longest = max(w, h)
        if longest > MAX_EDGE:
            scale = MAX_EDGE / longest
            im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode()
        payload.append(f"data:image/jpeg;base64,{b64}")

    return {
        "ok": True,
        "image_urls": payload,                            # Meshy multi-image order
        "roles": [r for r, _ in staged[:MAX_IMAGES]],      # front first — verified
        "count": len(payload),
        "note": "first image = primary (front) view, per Meshy docs",
    }


def write_payload(result: dict, out_path: str) -> str:
    """Emit the Meshy request fragment for review/diffing."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump({"multi_image_payload": result}, open(out_path, "w"), indent=1)
    return out_path


if __name__ == "__main__":
    import json
    import sys
    res = normalise_order(sys.argv[1])
    print(json.dumps({k: (v if k != "image_urls" else f"[{len(v)} data URIs]")
                      for k, v in res.items()}, indent=1))
    sys.exit(0 if res["ok"] else 1)
