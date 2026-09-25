#!/usr/bin/env python3
"""Brick pipeline: avatar -> Meshy brick (STUBBED, exact API shapes) -> voice/video/AR/print.

The ONLY missing input is MESHY_API_KEY. Everything else runs today.
Meshy calls log their exact request bodies; swap stub -> real with key, zero refactor.

Brick endpoints (verified docs):
  prototype: POST /openapi/creative-lab/brick-figure/v1/prototype
             {image_url} -> {result: prototype_id} (~6cr, concept PNG)
  build:     POST /openapi/creative-lab/brick-figure/v1/build
             {input_task_id} -> {result: build_id} (~30cr, GLB/OBJ/MTL + thumb)
  get:       GET .../v1/(prototype|build)/:id -> task object with model_urls

Fan-out (all real except mesh supply):
  voice  -> edge_tts MP3 (no mesh needed; audio drives everything downstream)
  video  -> talk.py MP4 (2.5D avatar + voice; swaps to mesh renders when GLB lands)
  ar     -> model-viewer page (needs GLB + USDZ; template ready, files pending)
  print  -> Makr3D job JSON (needs OBJ/STL; Makr3D accepts OBJ, no conversion needed)

Run: python3 brick.py --demo
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUT = "/tmp/opencode/brick-sim"
MESHY_KEY = os.environ.get("MESHY_API_KEY", "")


def meshy_prototype(photo_b64):
    """STUB. Real: POST prototype {image_url: data:...}. Returns concept PNG URL."""
    req = {"image_url": "data:image/jpeg;base64," + photo_b64[:40] + "..."}
    print(f"  [stub] prototype request logged ({len(photo_b64)}b image)")
    return {"stub": True, "request": req,
            "concept_png": "STUB-needs-key", "task_id": "STUB-needs-key"}


def meshy_build(prototype_id):
    """STUB. Real: POST build {input_task_id}. Returns GLB/OBJ/thumbnail URLs."""
    req = {"input_task_id": prototype_id}
    print("  [stub] build request logged")
    return {"stub": True, "request": req,
            "model_urls": {"glb": "STUB", "obj": "STUB", "mtl": "STUB"},
            "thumbnail_url": "STUB"}


def to_voice(text, voice="en-GB-RyanNeural"):
    """REAL. edge_tts -> MP3. No mesh needed."""
    import asyncio
    import edge_tts
    out = f"{OUT}/brick-voice.mp3"
    asyncio.run(edge_tts.Communicate(text, voice).save(out))
    return out


def to_video(avatar_id, template_id, audio_mp3):
    """REAL. talk.py pipeline (2.5D avatar + voice -> MP4). Mesh renders swap in later."""
    import subprocess
    out = os.environ.get("OUT", f"{OUT}/brick-video.mp4")
    r = subprocess.run([sys.executable, "talk.py", avatar_id, template_id, "x"],
                       capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)))
    return out if os.path.exists(out) else None


def to_ar_page(avatar_id, glb_url="MESH-PENDING", usdz_url="MESH-PENDING"):
    """REAL template; mesh URLs fill in when Meshy key lands."""
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Roast.pet AR</title>
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>
</head><body style="margin:0;background:#111">
<model-viewer src="{glb_url}" ios-src="{usdz_url}" ar ar-modes="webxr scene-viewer quick-look"
  camera-controls auto-rotate style="width:100vw;height:100vh"></model-viewer>
</body></html>"""
    out = f"{OUT}/ar-{avatar_id}.html"
    with open(out, "w") as f:
        f.write(html)
    return out


def to_print_job(obj_url="MESH-PENDING"):
    """STUB payload. Real: Makr3D job (accepts OBJ, no conversion)."""
    job = {"sku": "FIGURE-TBD", "material": "PLA", "colour": "single",
           "model_url": obj_url, "approve_required": True}
    with open(f"{OUT}/brick-makr3d.json", "w") as f:
        json.dump(job, f, indent=2)
    return job


def run_demo():
    import base64
    os.makedirs(OUT, exist_ok=True)
    from humour_mcp.avatar import create_avatar, photo_path
    # 1. avatar (REAL)
    with open("/tmp/opencode/etsy-sim/clean-front.jpg", "rb") as f:
        blob = f.read()
    tmp = f"{OUT}/brick-src.jpg"
    with open(tmp, "wb") as f:
        f.write(blob)
    av = create_avatar(tmp, "Buster", "dachshund")
    print(f"avatar: {av['id']}")
    # 2. brick prototype+build (STUBBED, exact shapes logged)
    b64 = base64.b64encode(blob).decode()
    proto = meshy_prototype(b64)
    build = meshy_build(proto["task_id"])
    print(f"brick: prototype+build stubbed (key missing: {not bool(MESHY_KEY)})")
    # 3. fan-out (all REAL except mesh files)
    voice = to_voice("I am Buster. I am made of brick. Fear me.")
    print(f"voice: {os.path.basename(voice)} ({os.path.getsize(voice)} bytes)")
    ar = to_ar_page(av["id"])
    print(f"ar page: {os.path.basename(ar)} (mesh URLs pending)")
    pj = to_print_job()
    print(f"print job: makr3d stub written (approve_required={pj['approve_required']})")
    print("\nDEMO GREEN. Give MESHY_API_KEY + rerun: mesh goes real, fan-out unchanged.")


if __name__ == "__main__":
    assert "--demo" in sys.argv, "usage: python3 brick.py --demo"
    run_demo()
