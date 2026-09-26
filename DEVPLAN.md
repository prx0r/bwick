> **STATUS: CURRENT** — 2026-09-26. Full development plan: phases, tests,
> validation gates, promo/AR/ Etsy showcase. Read with `MESH_PIPELINE.md`
> (stage detail) and `BUILD_NOTES.md` (the 21-item backlog).

# DEVPLAN.md — build, test, validate, promote

## Phases & dependencies

```
P0 foundations ──► P1 mesh production ──► P2 surround (video/AR) ──► P3 physical
      │                    │                       │                      │
   normalise.py         Meshy key             USDZ/turntable         mounts/CAD
   compose()            post-mesh gates       AR page + QR           Makr3D sample
   catalog assets       pets/{id}/ store      impact math             print photos
                                                                       │
                              P4 commercial ◄──────────────────────────┘
                              Prodigi SKUs · Etsy listings · traffic engine
```

Nothing in P2–P4 is real without a P1 mesh. P0 items are buildable **today with
no key** — that's where the next agent starts.

### P0 — foundations (no key required)
| Task | Done when |
|---|---|
| `engine/normalise.py` | order dir → `image_urls[]`; rejects with reason |
| `boards/` + `tiles/` + `catalog.json` from `concepts.md` (36 IDs) | `json.load` succeeds, all 36 present, every `PRP-*` resolvable |
| `compose()` | emits prompt + shot list; refuses >3 identities, mutable identity, `ip_check != pass` |
| Unit tests green (below) | `pytest` passes on a machine with no API keys |

### P1 — mesh production
| Task | Done when |
|---|---|
| Meshy key + confirm two **Q** marks (free terms, image limits) | notes recorded in `MESH_PIPELINE.md` |
| Live multi-image call on a real pet | task `SUCCEEDED`, glb downloaded |
| Immediate store + checksum in `engine/pets/{id}/` | re-download test proves URLs expired but file intact |
| Post-mesh gates: GLB parses · 2mm walls · face count | `print-ready: true` only if all pass |
| USDZ conversion (headless Blender) | `ios-src` resolves on a phone |

### P2 — surround (video / AR / promo)
| Task | Done when |
|---|---|
| Turntable renderer (mesh → MP4) | 10s loop, no rig needed |
| `video.py` = teaser (15s muted, captions ≥96px) + full cut | both export from one render |
| AR page real URLs (`brick.py` `MESH-PENDING` gone) | grep returns 0 |
| UUID binding `/a/{uuid}` → pet → mesh → action | log shows resolution |
| QR emboss in base + **scan test at 30cm** | screenshot + log entry per design |
| Impact math: time-to-first-mesh, credits/pet, conversion notes | table in this file updated |

### P3 — physical
Mount CAD → prop geometry → Makr3D live quote on real STL → sample order →
hold + photograph (hero, before/after, lifestyle, scale, box) → print profile approved.

### P4 — commercial
Prodigi SKUs → live prices → listings per `listing-playbook.md` → traffic engine
(daily posting; reviews flywheel).

---

## Test suite (`engine/tests/` — run offline, no keys)

| File | Asserts |
|---|---|
| `test_normalise.py` | EXIF rotated correctly (fixture with rotation tag); <200px rejected; non-image rejected; role-sort puts front first; base64 round-trips; `favourite` excluded when QC fails |
| `test_intake.py` | fake clean order passes; messy order (missing pet name/facts) defaults and continues; zero-usable-photos rejected with reason |
| `test_avatar.py` | avatar created, persisted, listed, photo path resolves; re-upload idempotent |
| `test_render.py` | card PNG exists, 5:7, non-blank (stdev > threshold); template chosen by occasion |
| `test_compose.py` | **guards**: >3 identities → error; identity field cannot be rewritten by scene/props; `ip_check: pending|fail` → refuses listing pack |
| `test_meshy_stub.py` | with stubbed HTTP: multi-image payload shape correct (front first, `target_formats:["glb"]`); `SUCCEEDED` triggers immediate download; **expired-URL retry gives a clear error, not a silent empty file** |
| `test_postmesh.py` | GLB magic bytes; file present + checksum matches; `print-ready` false until all gates pass |
| `test_video.py` | MP4 has h264 + aac streams; duration ≈ audio duration; teaser ≤15s; captions burned (frame has non-uniform text region) |
| `test_ar.py` | page has no `MESH-PENDING`; `ios-src` present; binding UUID resolves to right pet; QR decodes back to the UUID |
| `test_pricing.py` | every price in `products`/`stack` is evidence-marked (✓/Q/EST); 30% net ≥ floor |

Run: `python3 -m pytest engine/tests -q`. **No test may require network or a key**
— mock everything external; the whole point is CI-green before Meshy exists.

## Validation gates (manual, in order — each blocks the next)

1. **G1 Photo gate**: 5 real buyers' photo sets pass `photo_role_policy`
   (front+body+side). If <4/5 pass, fix intake copy, not the pipeline.
2. **G2 Mesh gate**: one real pet through P1 → recognizability judged blind
   against the source photo ("is this your dog?"). Fail → adjust prompts
   (`texture-prompts.md`), not code.
3. **G3 Print gate**: Makr3D sample of one approved mesh. Fail → wall-thickness
   or orientation changes. **Never list before this.**
4. **G4 Scan gate**: 3 phones (iOS/Android), QR at 30cm, page loads, action plays.
   Screenshot each — these become listing assets.
5. **G5 Order gate**: one end-to-end fake order on Etsy sandbox → preview approve
   → real fulfil → delivered photo. First real money before any ad spend.
6. **G6 Review gate**: first 10 orders → review rate measured; below 10% →
   fix QR moment + follow-up messaging (the flywheel, per `xmas-stockfillers.md`).

---

## Promo video assets (what we produce)

All from the same renders; one shoot, several exports (see `listing-playbook.md` shot list).

| # | Asset | Where it goes | Spec |
|---|---|---|---|
| 1 | **15s listing teaser** | Etsy listing slot 1 | muted autoplay, captions ≥96px: photo(0-2) → mesh rotate(2-6) → print in hand(6-10) → AR scan(10-13) → price card(13-15) |
| 2 | **Vertical social cut** (9:16) | TikTok/Reels/Shorts | same content + TTS voice + music; burned captions |
| 3 | **Before/after reveal** | Etsy photo slot 2 + social | customer photo → 3D preview morph (the single highest-converting format per competitor audit) |
| 4 | **AR screen recording** | Etsy photo slot 10 + social | real phone, tap → spell/action plays; authentic OS chrome |
| 5 | **Process triptych** | photo slot 5 | upload → preview → printed in hand |
| 6 | **Seasonal promo cut** | paid/organic push, Q4 | same pet, Christmas scene + spell (snowfall) — one per collection per season |

Production: `video.py` (turntable + talk.mp4 path) → ffmpeg concat + caption burn →
two masters (muted-Etsy / sound-social). Frame assets come from mesh renders and
`engine/cards/*.png`.

## AR — what to show, and the Etsy constraint

**Etsy allows no embeds, no interactive, no AR on listings.** So AR is shown by
*recording it* and sold by *delivering it*:

- **On Etsy**: AR screen-recording in the photo/video slots (asset #4), copy
  line *"Scan the code on your figure — it comes alive"*. The promise is
  demonstrable without the feature being interactive on-platform.
- **After purchase**: QR/NFC embossed in the figure base (default carrier) →
  `/a/{uuid}` → `model-viewer` (GLB + USDZ + MP4 fallback). Pre-ship scan gate.
- **Demo pack (4 clips, each ≤10s)**: `lumos burst` (default, every SKU),
  `snowfall` (Christmas), `kiss` (couples), `levitation` (kids' gasp moment).
  Each is one screen-record on one phone — reuse across every listing in that
  collection.

## Etsy showcase — the 10 slots, filled

| Slot | Content | Source |
|---|---|---|
| 1 | Hero: finished figure, dark bg, gold accent | print photo (G3) |
| 2 | Before/after: customer photo → mesh | asset #3 |
| 3 | Lifestyle: real shelf, human hand for scale | print photo |
| 4 | Variant upsell (couple or +pet) | second mesh render |
| 5 | Process triptych | asset #5 |
| 6 | Base close-up + engraved name + QR | print photo (G3) |
| 7 | Gift box / packaging | print photo |
| 8 | Scale reference (coin/ruler) | print photo |
| 9 | Review screenshots | from G6 onward |
| 10 | AR moment | asset #4 |
| **video (slot 1 video)** | 15s muted teaser | asset #1 |

Title: keyword-first, 140 chars. Tags: 13. Personalization: 5 text boxes
(recipient, pet/breed, occasion/scene, style, message). Never say franchise
names. Publish lead-time SLA from `lead_time_sla` in config, three times.

## Definition of done (release)

P0–P4 tasks done · G1–G6 gates passed · tests green offline ·
`ip_check: pass` on every shipped template · first print sample held by a human ·
airtimer live on `engine/.env` secrets · `MESH_PIPELINE.md` Q-marks resolved.
