# Meshy docs — pet-relevant subset (imported 2026-09-25)

Full API: docs.meshy.ai. Auth: `Authorization: Bearer KEY`. All calls async
(create → poll/stream → download). Signed URLs expire — download immediately.
Failed tasks refund to 0. Base64 data URIs accepted everywhere (no public URL needed).

## PETS: mesh + products (rigging excluded — see below)

**Multi-image-to-3D** `POST /openapi/v1/multi-image-to-3d` (~30cr textured):
`image_urls[1..4]` (jpg/png, base64 ok; first = front view), `ai_model: latest`
(Meshy 7.1), `should_texture: true`, `texture_resolution: 2k`,
`target_formats: ["glb"]` (skip unused, faster),
`multi_view_thumbnails: true` (front/right/back/left 512px PNGs — free listing
art), `pose_mode` (a/t-pose or empty). Returns `model_urls` (glb/fbx/obj/usdz/stl),
`thumbnail_urls`, `texture_urls` (base+metallic/normal/roughness). Same 30cr for
1–4 photos — always send multi. Etsy upload must collect 3–4 angles.

**Brick Figure** (physical line): prototype (photo → concept PNG, **6cr**) then
build (concept → GLB/OBJ/MTL + thumbnail, **30cr**). Total 36/pet. Prototype is
the approve-gate (show 6cr preview, build 30cr only on approve). Webapp prototype
tasks do NOT chain to API build — both stages via API. Also exists: Figure,
Vinyl Figure, Keychain, Magnet, Lamp (same two-stage pattern; keychain relief
is ideal for pets — no rigging involved).

## HUMANS ONLY: rigging + animation (do not spend on pets)

**Rigging** `POST /openapi/v1/rigging` (5cr): humanoid/bipedal ONLY —
"auto-rigging is not suitable for Non-humanoid assets"; 422 if pose estimation
fails. Input: textured GLB <300K faces, face toward +Z. Returns rigged FBX+GLB
**plus basic walk/run animations included**. Use for the human premium line.

**Animation** `POST /openapi/v1/animations` (3cr per action, up to 10/call):
needs `rig_task_id`. Preset library (`GET /animations/library`, FREE, with GIF
previews per action): WalkAndRun, BodyMovements, DailyActions, Fighting,
Dancing. `motion_task_id` (Text-to-Motion clips) **rejects quadruped rigs**.
Outputs animation GLB/FBX + USDZ. Human line only.

## Credit map per pet (verified)

| Step | Credits | Pets? | Humans? |
|---|---|---|---|
| multi-image mesh + texture + thumbs | 30 | yes | yes |
| brick prototype (preview) | 6 | yes | yes |
| brick build (GLB/OBJ/MTL) | 30 | yes | yes |
| rigging (+walk/run included) | 5 | NO — 422 on non-humanoid | yes |
| animation (per action) | 3 | NO (needs rig) | yes |

Cheapest pet establish: **30cr** (multi-image, download all, offline forever).
Cheapest human establish: **38cr** (30 + 5 + 3). Free tier (~100/mo): ~3 pets
or ~2 humans at $0. Talking for pets stays 2.5D + edge_tts (no Meshy path).
