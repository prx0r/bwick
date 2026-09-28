# DEVPLAN — build, test, validate, promote (rewritten 2026-09-27)

> **STATUS: CURRENT** — post-simplification plan. Read `HANDOVER.md` first,
> `MESH_PIPELINE.md` for mesh-stage detail, `docs/creative-system.md` and
> `docs/fulfilment.md` for today's new workstreams. Test suite + gates carried
> forward unchanged (they're good). Do not delete this file.

## Session decisions that shape this plan (S-cards)

- **S1** Product = plain "brick self" $9.99 + couple premium; mounts = listing
  contexts; **handhelds = the wedge** (library props, checkout picker).
- **S2** Pets V2 (experiment allowed, no pet SKUs yet); familiar = prop.
- **S3** Photo backing out · photo print digital-only · AR parked ·
  cake topper = spike mount · family cut (≤3 identity meshes).
- **S4** Packaging = plain box S/M + logo sticker + thank-you/QR card; name
  prints on plinth via variant data; both providers need one sample order each
  before any listing.
- **S5** Theme packs: Xmas first (list mid-Oct), then Wizard + Witch/Gothic
  evergreen, Anime-Style Originals (IP-safe), Life-Events occasion layer;
  custom requests pass `ip_check` only.
- **S6** Words we never print: LEGO, minifigure, any franchise/fandom term,
  "inspired by X".

## Phases & dependencies

```
P0 foundations ──► P0.5 brand & creative ──► P1 mesh ──► P2 surround ──► P3 physical ──► P4 commercial
 no key needed      docs, templates,          Meshy key    turntable +      samples +       listings +
                    shot lists                 (or Kaggle)  listing video    packaging       traffic
```

### P0 — foundations (no key required) ← START HERE
| Task | Done when |
|---|---|
| ✅ `engine/normalise.py` (EXIF, role-sort front-first, size guard, `image_urls[]`) — **DONE this session**,9 tests green (`engine/tests/test_normalise.py`) | order dir → payload; rejects with reason |
| `boards/` + `tiles/` + `catalog.json` from `concepts.md` (36 IDs) | `json.load` OK, all36 present, `PRP-*` resolvable (incl. **new handheld PRP ids**) |
| `compose()` | prompt + shot list; refuses >3 identities, mutable identity, `ip_check != pass` |
| Unit tests green offline | `pytest engine/tests -q` passes with no keys |

### P0.5 — brand & creative (docs, no key) — mostly DONE this session
| Task | Status |
|---|---|
| canonical §4/§5/glossary/§6 amendments | ✅ done |
| handheld library (`PROPS.md`) | ✅ done |
| positioning + competitive scan (`targeting.md`) | ✅ done |
| theme packs + IP playbook (`theme-packs.md`) | ✅ done |
| fulfilment + packaging (`fulfilment.md`) | ✅ done |
| shot list + listing video + Xmas poster spec (`creative-system.md`) | ✅ done (assets not) |
| **brick grammar bible** (studs, minifig scale, ABS gloss, palette) | ⬜ todo |
| Xmas launch one-pager (dates, SKUs, cut-offs) | ⬜ todo |
| poster/shot **assets** (renders once mesh exists) | ⬜ blocked on P1 |

### P1 — mesh production
| Task | Done when |
|---|---|
| Meshy key + confirm two **Q** marks (free terms, image limits) | notes in MESH_PIPELINE |
| Live multi-image call on a real photo (or Kaggle-local fallback) | task SUCCEEDED, glb stored immediately |
| Post-mesh gates + store (`pets/` → rename `figures/`) | checksums, `print-ready` only after gates |
| **Standard brick pet iteration** (V2 track, preview-gate, free tier) | brick dog+cat base meshes OR BrickLink fallback chosen |

### P2 — surround (video, no AR)
| Task | Done when |
|---|---|
| Turntable renderer (mesh → MP4, headless) |10s loop |
| Listing video slot A shipped on first listing | muted, no audio dependency |
| `video.py` teaser + talk.mp4 wiring (spells as video) |6s spell teasers export |
| Before/after composite (photo → brick) template | one image, reused |
| ~~AR page / UUID / USDZ~~ | **PARKED (S3)** — spec remains in old DEVPLAN history |

### P3 — physical
Mount parts (spike/loop/magnet/ring/plinth) → handheld prop geometry →
**Makr3D sample + 3D Vikings sample** (both, before listing) → plain-box
pack-in artwork (sticker + QR card) mailed to providers → order a customer-
ready S box → photograph the unboxing (creative-system slots1,4,5).

### P4 — commercial
Prodigi photo-print SKU only if demand → Etsy listings per
`listing-playbook` + **creative-system image5 + video** → Xmas: poster +
Snowfall teaser live **mid-Oct**, cut-offs published → traffic engine →
first-10 review flywheel (G6).

## Test suite (carried forward — run: `python3 -m pytest engine/tests -q`)

`test_normalise` (EXIF/role-sort/base64/rejects) · `test_intake` ·
`test_avatar` · `test_render` (card PNG5:7 non-blank) · `test_compose`
(>3 identities, identity immutability, ip_check refusal) · `test_meshy_stub`
(payload shape, front-first, expired-URL clear error) · `test_postmesh`
(magic bytes, checksum, print-ready gating) · `test_video` (h264+aac,
duration match, teaser ≤15s) · `test_ar` *(kept, dormant while AR parked)* ·
`test_pricing` (evidence marks,30% floor). **No test may need network or a key.**

## Validation gates (manual, sequential — each blocks the next)

1. **G1 Photo gate**:5 real photo sets pass `photo_role_policy`.
2. **G2 Mesh gate**: real subject through P1 → blind recognisability.
3. **G3 Print gate**: Makr3D sample approved. **Never list before this.**
4. **G4 Scan gate**: QR at30cm,3 phones → screenshots become assets.
5. **G5 Order gate**: sandbox order → preview → fulfil → delivered photo.
6. **G6 Review gate**: first10 orders, review rate ≥10% or fix the QR moment.

## Promo assets (from `docs/creative-system.md`, AR entries dropped)

15s listing teaser · vertical social cut · before/after reveal · process
triptych · **Xmas poster + Snowfall teaser** · seasonal re-skins per pack.
Production: turntable renderer + talk.mp4 → ffmpeg concat + captions → two
masters (muted-Etsy / sound-social).
