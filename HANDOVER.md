# HANDOVER — start here (2026-09-27)

> **STATUS: CURRENT** — rewritten at the end of the simplification session.
> First thing to read. Detail lives in the files below; every file carries its
> own STATUS header. Do not delete this file.

## What this is, in one breath

**Figg (repo codename bwick):** personalised brick-figure business — *upload
your pics, get your brick self, $9.99*. One plain figure, mounts for context
(desk/tree/cake/magnet), **handhelds as the killer wedge** (your figure holds
your thing), couple as the premium wedge, world packs as skins, zero
inventory, Meshy in → Makr3D/3D Vikings out → Etsy.

## Simplifications locked this session (do not relitigate)

1. **Pets = V2 experiment track.** No identity-pet SKUs until a standard brick
   pet exists (preview-gated, free-tier play allowed) or BrickLink parts are
   adopted. V1 familiar = library prop. Pet Arcana + Naughty List Pet → phase 2.
2. **Photo backing out.** Flat photo prints = digital-only SKU if ever
   (two-parcel mess otherwise). See `docs/fulfilment.md`.
3. **AR parked** (USDZ/UUID work is spec'd, cheap to resume).
4. **Cake toppers = a mount, not a product** (spike mount on the same figure).
5. **Family still cut** — ≤3 identity meshes holds; props unlimited.
6. **Packaging = plain kraft box (S/M) + logo sticker + thank-you/QR card.**
   One artwork file, both providers, no MOQ, no deadlines.

## Read order

1. **this file** → `canonical.md` (THE product system; §4 amended today)
2. `docs/creative-system.md` (clean images · listing video · Xmas poster) —
   what actually converts
3. `docs/theme-packs.md` (demand + **IP playbook**: aesthetic words green,
   franchise red, safe vocabulary per pack, custom-request gate)
4. `docs/fulfilment.md` (box, providers, provider split, sample rule)
5. `docs/targeting.md` (personas + today's competitive scan + $9.99 evidence)
6. `PROPS.md` (mesh vs prop + **handheld library**)
7. `MESH_PIPELINE.md` → `DEVPLAN.md` (build map, phases, gates)
8. `docs/` rest · `engine/` (code) · `concepts.md`36 concepts

## What is built and green (unchanged)

Gallery20 card PNGs · avatar store · photo-card compositing · `talk.py` 2.5D
talking MP4 · `etsy_order.py --demo` GREEN · `brick.py --demo` GREEN
(Meshy/Makr3D stubbed) · live Prodigi quoting via MCP · R2 backup (8.4K/18GB).

## Blockers, in order

1. **P0 code (no key needed):** `engine/normalise.py` → `boards/tiles/
   catalog.json` (36 concepts) → `compose()` + guards + pytest. Start here.
2. **MESHY_API_KEY** (free100cr/mo) → first real mesh. (Free alternative
   exists: Kaggle-local meshgen — see easy/docs/ANIMATION_FORMAT.md.)
3. Concept library assets (`productlist1.md` build order).
4. Makr3D sample order + 3D Vikings sample order (**both before any listing**);
   claim Makr3D founding-seller discount (60–90d clock started ~Sep25).
5. Etsy shop + production-partner disclosure.
6. Brick grammar bible (style law for people+props) — not yet written.
7. Disk: see aocsec/box-audit.md DROP list.

## Open decisions (not made here)

- Figg/Roast/Mystic/Holiday naming final — **BWICK/BWITCH/BWICKMAS are taken
  brands; internal labels only** (`streamlined.md`).
- Price authority: `pricing-analysis.md` (30%-floor vs price-match) → update
  `STACK.md` when chosen.
- Printed boxes revisit for2027 (Vikings MOQ100,10-day lead).

## Done this session (do not re-do)

canonical §4 rewritten (two cores + mounts + handheld wedge + pets V2) · §5
held-prop rule amended · glossary `Handheld` added · §6 Pet Arcana→phase2 ·
PROPS handheld library · targeting competitive scan + word bans ·
`docs/theme-packs.md` superseded with demand+IP playbook · `docs/fulfilment.md`
+ `docs/creative-system.md` created · sibling repo `easy/docs/ANIMATION_FORMAT.md`
(the motion contract easy/sleepdraw/bwick share).

## Word bans (listing-time)

LEGO · minifigure · every franchise name and fandom term · "inspired by X".
Say **brick figure · block figure · building-block figure**.
