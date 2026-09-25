"""Avatar store — upload once, use everywhere.

An avatar is a persistent character: {id, name, species, photo, created_at}
in avatars/<id>/. Unlike /tmp uploads, avatars survive restarts and are the
unit the gallery + situations render from. Field names mirror etsysignal's
character.json where sensible (name, species) without the 3D weight.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "avatars")


def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "pet").lower()).strip("-") or "pet"
    return s[:24]


def create_avatar(photo_src: str, name: str, species: str = "") -> dict:
    """Persist an uploaded photo as a new avatar. Returns the avatar record."""
    os.makedirs(STORE, exist_ok=True)
    with open(photo_src, "rb") as f:
        blob = f.read()
    digest = hashlib.sha256(blob).hexdigest()[:6]
    aid = f"{_slug(name)}-{digest}"
    adir = os.path.join(STORE, aid)
    os.makedirs(adir, exist_ok=True)
    ext = os.path.splitext(photo_src)[1] or ".jpg"
    photo_dst = os.path.join(adir, "photo" + ext)
    with open(photo_dst, "wb") as f:
        f.write(blob)
    rec = {
        "id": aid,
        "name": name or "Pet",
        "species": species or "",
        "photo": os.path.basename(photo_dst),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    with open(os.path.join(adir, "avatar.json"), "w") as f:
        json.dump(rec, f, indent=2)
    return rec


def get_avatar(aid: str) -> dict | None:
    safe = os.path.basename(aid)
    meta = os.path.join(STORE, safe, "avatar.json")
    if not os.path.exists(meta):
        return None
    with open(meta) as f:
        return json.load(f)


def photo_path(aid: str) -> str | None:
    rec = get_avatar(aid)
    if not rec:
        return None
    p = os.path.join(STORE, os.path.basename(aid), rec["photo"])
    return p if os.path.exists(p) else None


def list_avatars() -> list[dict]:
    if not os.path.isdir(STORE):
        return []
    out = []
    for aid in sorted(os.listdir(STORE)):
        rec = get_avatar(aid)
        if rec:
            out.append(rec)
    return out
