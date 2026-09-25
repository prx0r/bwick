"""Card renderer — HTML output (Satori-ready structure)."""
from __future__ import annotations
from pathlib import Path
from typing import Any

def render_card_html(setup: str, punchline: str, visual: str,
                     roast_level: str, pet_image_url: str|None = None,
                     width: int = 1050, height: int = 1470) -> str:
    pet_img = (f'<img src="{pet_image_url}" class="pet-photo" />'
               if pet_image_url else '<div class="pet-placeholder">[YOUR PET HERE]</div>')
    color = "#ff4444" if roast_level == "savage" else "#ff8844" if roast_level == "roast" else "#44aaff"
    esc = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\n","<br>")
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"/><style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:{width}px;height:{height}px;background:#1a1a2e;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;font-family:system-ui,-apple-system,sans-serif;position:relative;overflow:hidden}}
.card::before{{content:"";position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle at 30% 70%,rgba(255,107,107,.15) 0%,transparent 50%),radial-gradient(circle at 70% 30%,rgba(78,205,196,.1) 0%,transparent 50%)}}
.content{{position:relative;z-index:1;text-align:center;max-width:90%}}
.headline{{font-size:36px;font-weight:900;line-height:1.2;margin-bottom:24px;letter-spacing:-.5px}}
.pet-photo{{width:280px;height:280px;border-radius:50%;object-fit:cover;border:4px solid rgba(255,255,255,.2);margin:20px auto;display:block}}
.pet-placeholder{{width:280px;height:280px;border-radius:50%;border:4px dashed rgba(255,255,255,.3);margin:20px auto;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.4);font-size:14px}}
.punchline{{font-size:22px;line-height:1.5;color:rgba(255,255,255,.9);margin-top:20px;white-space:pre-line}}
.brand{{position:absolute;bottom:20px;right:30px;font-size:12px;color:rgba(255,255,255,.3);letter-spacing:2px;text-transform:uppercase;z-index:1}}
.badge{{position:absolute;top:20px;left:30px;background:{color}33;color:{color};padding:6px 14px;border-radius:20px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:1px;z-index:1}}
</style></head><body>
<div class="card">
<div class="badge">{roast_level}</div>
<div class="content">
<div class="headline">{esc(setup)}</div>
{pet_img}
<div class="punchline">{esc(punchline)}</div>
</div>
<div class="brand">ROAST.PET</div>
</div></body></html>'''

def save_card(setup: str, punchline: str, visual: str, roast_level: str,
              pet_image_url: str|None = None, output_path: str|None = None) -> str:
    html = render_card_html(setup, punchline, visual, roast_level, pet_image_url)
    path = output_path or f"/tmp/roast_{hash(setup) & 0xFFFFFF:06x}.html"
    Path(path).write_text(html)
    return path
