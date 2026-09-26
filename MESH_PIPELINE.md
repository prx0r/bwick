> **STATUS: CURRENT** — 2026-09-26. The next agent's build map. Every step
> states its inputs, its blocker, and its done-criterion. Facts marked ✓ are
> verified from live API docs this session; Q marks something you must confirm.

# MESH_PIPELINE.md — the production line

One pet photo in. Out the other side: a mesh, a video, an AR moment, a print job.
Five stages. Nothing runs without stage 2, and stage 2 needs `MESHY_API_KEY`.

```
INTAKE → NORMALISE → MESHY → POST-MESH → { VIDEO, AR, PRINT }
  ①        ②           ③         ④          ⑤a  ⑤b  ⑤c
```

---

## ① INTAKE — what images we request

Already specced in `etsysignal/roast/photo_role_policy.json` — **do not
reinvent it**. Four required roles:

| Role | Minimum | Why Meshy needs it |
|---|---|---|
| `front_face` | face + eyes visible, head/ears mostly uncropped | identity texture + thumbnail |
| `full_body` | torso/body proportions visible | geometry + silhouette |
| `side_view` | clear profile or strong ¾ profile | muzzle length, ear shape, depth |
| `favourite` | same pet; may be technically low quality | style reference **only** — excluded from Meshy if it fails QC |

Rules in force (from `photo_qc.py` + `INTAKE_SCHEMA.md`):
- Accept **3–8 photos** per order; verdict `PASS` needs **≥3 OK + one front**.
- File QC: ≥10KB, JPEG/PNG magic header. (Our engine's `etsy_order.py:ingest`
  also checks PIL-decodable, min dimension ≥200px, >3000 bytes — keep both.)
- Naming convention: `pet_01_front_face`, `pet_02_full_body`,
  `pet_03_side_threequarter` — order matters for Meshy (see ②).
- Buyer never writes this. `compose()` collects the photos; QC decides.

**Done when:** order has 3+ passing photos incl. front, and roles are labelled.

---

## ② NORMALISE — before anything touches Meshy

**No normalisation layer exists yet.** `photo_pipeline.py` only copies the
front photo into a FreakTown `portrait.png` — it does no rotation, no resize,
no format guard. Build `engine/normalise.py`:

1. **EXIF orient** (PIL `ImageOps.exif_transpose`) — phone photos are often
   rotated; Meshy will bake the rotation into geometry if we don't fix it.
2. **Validate**: decodable, ≥200px min side, JPEG/PNG only.
3. **Role-sort**: front → body → side (Meshy: *"first image is the primary
   (front) view, order of the rest doesn't matter"* ✓). `favourite` is excluded
   unless it passed QC.
4. **Size guard** (Meshy rejects out-of-range): resize so longest edge ≤2048
   (Q: confirm exact Meshy limit — the brick docs say "too small / exceeds
   max file size or max pixel count"), re-encode JPEG quality 90.
   Total base64 must stay inside the request body limit (Q).
5. **Emit** the `image_urls[]` array: `data:image/jpeg;base64,...` ×1–4.

**Rejected** → the existing `NEEDS_REPLACEMENT` path + a polite message to the
buyer ("one more photo of their face, ideally face-on in daylight"). Never
silently proceed on a bad photo.

**Done when:** `normalise.py` takes an order dir → returns `image_urls[]` +
a rejection reason when it can't.

---

## ③ MESHY — the call

**Endpoint choice matters:**
- `POST /openapi/v1/multi-image-to-3d` — **use this** (same 30cr as single;
  1–4 photos, better identity). Params: `ai_model: latest`, `should_texture: true`,
  `texture_resolution: 2k`, `target_formats: ["glb"]`,
  `multi_view_thumbnails: true` (free 4-angle renders = listing art), `alpha_thumbnail: true`.
  ✓ verified this session.
- Single `image-to-3d` — fallback when only one photo survived QC.
- Brick `prototype`+`build` (6cr + 30cr) — **only for the brick theme**, and
  only via API (webapp prototypes don't chain to API build ✓).
- Do **NOT** spend on `rigging` (5cr) for animals — humanoid-only ✓ (422 on
  non-humanoid). Humans only, when we do the human line.

**Credit budget:** 30cr/mesh establish (+6/30 if brick). Free tier = ~100/mo
≈ 3 meshes (Q: confirm free-tier terms at signup).

**Done when:** task returns `SUCCEEDED` with `model_urls.glb`.

---

## ④ POST-MESH — the part everyone forgets

**Download immediately.** `model_urls` are signed, expiring URLs — the docs say
"expires_at" on every task. Store as `engine/pets/{pet_id}/mesh.glb` +
`textures` + `thumbnail_urls` the moment the task succeeds. This is the
permanent asset; everything else in this file consumes it.

Checks before it ships (each is a gate, not a suggestion):
1. **GLB parses** (magic `glTF`, we did this on the dachshund test ✓).
2. **Wall thickness** — texture prompts carry `"walls and features ≥2mm"`;
   a mesh that fails slicer review gets re-textured at 2k/4k, not shipped.
3. **Face count** — human rigging path requires <300k faces (rigging docs ✓);
   pets don't rig, but keep the count sane for print slicing.
4. **USDZ** — for iOS AR. Brick build does **not** emit USDZ; convert
   headless in Blender (`--background --python` GLB→USDZ). One script, both
   lines benefit. (Q: confirm Blender on the target box, or use a converter lib.)
5. **STL/OBJ for print** — brick build already gives OBJ+MTL; Makr3D accepts
   STL/3MF/STEP/OBJ/ZIP ✓ so OBJ goes straight through. Single-colour first,
   two-tone max (purge quotes unresolved).

**Done when:** `pets/{id}/` holds mesh.glb + textures + USDZ + print file, all
checksummed, and a `print-ready: true` flag only after checks pass.

---

## ⑤a VIDEO — turning a mesh into something watchable

Two render modes, both consume the stored mesh:
- **Turntable (proof of object)** — Blender headless renders N frames of the
  mesh rotating → MP4. Cheap, no rig needed, works for any mesh.
- **Talk/action (the product)** — our existing 2.5D path first: `talk.py`
  drives avatar + voice via audio envelope (jaw/bob/blink), MP4 export verified.
  When the mesh is rigged (human line), swap the composite for mesh frames —
  same audio envelope, same ffmpeg mux, same output contract.

Listings need: **15s muted teaser** (captions ≥96px, autoplay silent —
`listing-playbook.md`) + full cut via QR. One render, two exports.

**Done when:** `video.py <pet_id> <template> <text>` → MP4 on disk, captioned
teaser variant present.

---

## ⑤b AR — the moment that closes the sale

- **Page**: `model-viewer` HTML, GLB + `ios-src` USDZ, auto-rotate + AR modes.
  Template already exists in `brick.py` with `MESH-PENDING` slots — fill them.
- **Binding**: per-order UUID (`/a/{uuid}`) → pet_id → that mesh + action.
  **QR embossed into the figure base** is the default carrier
  (`delivery-experience.md` §1); packaging QR is the fallback for flat SKUs.
- **Effects**: action library intents (lumos burst, snowfall, levitation,
  owl post — `ACTION_LIBRARY.md`). `pog.action/v1` semantics unchanged.
- **Gate:** pre-ship scan check — every QR tested at 30cm before dispatch.

**Done when:** scan on a phone opens the page, the mesh loads, the action
plays, and the log records the scan. Screenshot it — that's the listing photo
that justifies the premium.

---

## What the next agent should do first (ordered)

1. Write `engine/normalise.py` (stage ②) — pure PIL, no key needed, testable
   today against `etsysignal/roast/roastpet_checkpoint1_demo` sample uploads.
2. Confirm Meshy free-tier terms + image size limits → fill the two **Q** marks.
3. Get `MESHY_API_KEY` from the human → run stage ③ on Max → stage ④ gates.
4. Blender headless: USDZ converter script + turntable renderer (stage ④/⑤a).
5. Fill the `MESH-PENDING` slots in `brick.py`'s AR page with the real URLs.
6. Wire `Perform` in the studio gallery → `talk.py` (todo already in BUILD_NOTES).
7. One approved print sample (Makr3D) before any listing ships.

## Blockers (only a human clears these)

`MESHY_API_KEY` · Makr3D account · Etsy + Prodigi dashboards · disk space ·
the Roast-vs-Holiday Christmas SKU ownership call (streamlined.md open question).
