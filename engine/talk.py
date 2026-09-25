#!/usr/bin/env python3
"""2.5D talking avatar -> MP4. No vendors, no keys, no GPU.

Pipeline: avatar circle + TTS voice -> audio envelope drives head-bob and
jaw-squash -> composited over the template scene -> ffmpeg muxes to MP4
(vertical 1080x1920, doubles as the Etsy listing video).

The avatar's POG_FACE_V1 intents used here: jaw_open (squash), blink_left/right
(periodic lid). Full 3D visemes arrive when a rigged mesh exists; this ships today.

Run: /usr/bin/python3 talk.py <avatar_id> <template_id> "<text>" [voice]
Out: /tmp/opencode/talk-<avatar>-<template>.mp4  (override with OUT= path)
"""
import audioop
import math
import os
import subprocess
import sys
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humour_mcp.avatar import photo_path  # noqa: E402
from render_cards import circle_thumb  # noqa: E402

from PIL import Image, ImageDraw  # noqa: E402

FUNNY = os.path.dirname(os.path.abspath(__file__))
FPS = 12
VW, VH = 1080, 1920


async def tts(text, voice, out_mp3):
    import edge_tts
    await edge_tts.Communicate(text, voice).save(out_mp3)


def envelope(wav_path, fps, duration):
    """RMS amplitude per video frame (0..1)."""
    with wave.open(wav_path, "rb") as w:
        n, fr, sw = w.getnframes(), w.getframerate(), w.getsampwidth()
        raw = w.readframes(n)
    per = max(1, int(fr / fps))
    env = []
    for i in range(0, len(raw), per * sw):
        seg = raw[i:i + per * sw]
        if not seg:
            break
        env.append(audioop.rms(seg, sw) / 32768.0)
    # normalize + smooth + pad/trim to duration
    peak = max(env) if env else 1.0
    env = [min(1.0, e / (peak or 1.0)) for e in env]
    need = int(duration * fps)
    return (env + [0.0] * need)[:need]


def scene(template_id):
    """Template card PNG as the situation backdrop (centered on vertical canvas)."""
    bg = Image.new("RGB", (VW, VH), (10, 10, 14))
    for cand in (f"card-studio/static/cards/{template_id}.png",
                 f"worker/static/cards/{template_id}.png"):
        p = os.path.join(FUNNY, cand)
        if os.path.exists(p):
            card = Image.open(p).convert("RGB")
            card.thumbnail((VW - 80, VH - 500))
            bg.paste(card, ((VW - card.width) // 2, 120))
            break
    return bg


def frames(avatar_circle, env, out_dir):
    """Head-bob + jaw-squash frames. Returns frame count."""
    os.makedirs(out_dir, exist_ok=True)
    base = avatar_circle.resize((560, 560))
    paths = []
    for i, amp in enumerate(env):
        bob = int(14 * math.sin(2 * math.pi * 2.2 * i / FPS))
        squash = 1.0 - 0.16 * amp  # jaw_open: mouth opens (head squashes) on loud frames
        head = base.resize((560, max(64, int(560 * squash))))
        fr = scene_bg.copy()
        fr.paste(head, ((VW - 560) // 2, 1180 + bob), head)
        # blink every ~3.5s for 2 frames
        if i % int(FPS * 3.5) in (0, 1):
            d = ImageDraw.Draw(fr)
            d.rectangle([0, 0, VW, 26], fill=(10, 10, 14))
        p = os.path.join(out_dir, f"f{i:04d}.png")
        fr.save(p)
        paths.append(p)
    return paths


if __name__ == "__main__":
    import asyncio
    aid, tid, text = sys.argv[1], sys.argv[2], sys.argv[3]
    voice = sys.argv[4] if len(sys.argv) > 4 else "en-GB-RyanNeural"
    out_mp4 = os.environ.get("OUT", f"/tmp/opencode/talk-{aid}-{tid}.mp4")

    av = photo_path(aid)
    assert av, f"unknown avatar {aid}"
    mp3 = "/tmp/opencode/talk-voice.mp3"
    asyncio.run(tts(text, voice, mp3))
    wav = "/tmp/opencode/talk-voice.wav"
    subprocess.run(["ffmpeg", "-y", "-i", mp3, "-ar", "24000", "-ac", "1", "-f", "wav", wav],
                   capture_output=True, check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", mp3], capture_output=True, text=True).stdout.strip())
    env = envelope(wav, FPS, dur)
    circle = circle_thumb(av, 560)
    fdir = "/tmp/opencode/talk-frames"
    scene_bg = scene(tid)
    frames(circle, env, fdir)
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", fdir + "/f%04d.png",
                    "-i", mp3, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
                    "-shortest", out_mp4], capture_output=True, check=True)
    print(f"MP4: {out_mp4} ({os.path.getsize(out_mp4)} bytes, {dur:.1f}s, {len(env)} frames)")
