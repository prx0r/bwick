# Meshy Brick Figure — complete reference (verified from API docs + product page)

## Pipeline (two API stages, must both be API — webapp prototypes do NOT chain)

1. **Prototype** `POST /openapi/creative-lab/brick-figure/v1/prototype`
   - Input: `image_url` (jpg/png/webp, URL or base64), optional `name`,
     `remove_background` (transparent RGBA concept for compositing).
   - Output: task id → poll/stream → `image_urls[]` (brick-style concept PNG).
   - Cost: **6 credits**. Failed = refunded.
2. **Build** `POST /openapi/creative-lab/brick-figure/v1/build`
   - Input: `input_task_id` (the succeeded prototype id, same API key).
   - Output: `model_urls` (glb + obj + mtl), `thumbnail_url` (preview PNG),
     `texture_urls[0].base_color`.
   - Cost: **30 credits**. Total per figure: **36 credits**.

## Product specs (from product page)

- Poseable pre-export: head, arms, legs (set the pose in browser/API, baked in).
- Minifigure scale (fits existing brick sets/cities/dioramas).
- Full color, textured. Export GLB/STL/OBJ/3MF (3MF = multi-color print).
- Print-at-home today (own printer or local service); Meshy shipped option "coming soon"
  (keychains already ship to 9 countries — precedent).
- Free tier to start; commercial rights require paid plan (free = personal/eval only).

## Pet notes

- Brick style flatters pets (blocky proportions hide mesh imperfections that
  realistic style would expose). Recommended default theme for pet figures.
- Face likeness carries in brick style (big head, printed face) — better identity
  retention than realistic at small print sizes.
- Single photo works; 3–4 angles better (use multi-image-to-3D instead when identity
  is critical, then style via texture prompt — same 30cr class).

## Cost map

| Step | Credits | $16 plan ($0.0053/cr) | $8 plan ($0.008/cr) |
|---|---|---|---|
| Prototype (preview/approve gate) | 6 | $0.03 | $0.05 |
| Build (GLB/OBJ/MTL) | 30 | $0.16 | $0.24 |
| **Total per brick figure** | **36** | **~$0.19** | **~$0.29** |

Rejected designs cost 6 (prototype only); build only on approve. ~83 figures/mo
on $16, ~27 on $8, ~2 free/mo.
