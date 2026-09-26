> **STATUS: CURRENT** — annotated 2026-09-26.
>
> Index + read order only. Detail lives in the files below.
>
> Do not delete this file.

# Figg (repo codename: bwick)

Personalized pet universe: upload once, own the character, monetize across
cards, figures, video, AR. One pet mesh feeds every SKU. Zero inventory.
Brand **Figg** · lines **Roast / Mystic / Holiday** · four products
(pet, couple, solo+pet, solo — max three identity meshes; couple+pet variant
allowed, family cut. See `PROPS.md`).

ONE canonical repo: `engine/` (runnable pipeline) + `docs/` (specs) + root
strategy files. Former `funnylabs` repo is superseded.

## Read order

1. `HANDOVER.md` — start here: status, blockers, open decisions
2. `thisisit.md` — the special one-pager (three collections, one display format)
3. `canonical.md` — THE product system: glossary, schema, 7 launch listings
4. `VISION.md` → `STACK.md` — thesis, locked SKUs, suppliers, margins
5. `streamlined.md` — brand naming (authoritative)
6. `docs/` → `engine/` (build it), `ideas.md` (inbox)

## File map with status

**Root — CURRENT:** `HANDOVER.md` · `thisisit.md` · `canonical.md` ·
`DEVPLAN.md` (phases, tests, validation gates, promo/AR/Etsy showcase) · `MESH_PIPELINE.md` (build map: photo → normalise → Meshy → post-mesh → video/AR/print) ·
`concepts.md` (36-concept library) · `productlist1.md` · `streamlined.md` ·
`AGENTS.md` · `BUILD_NOTES.md` · `ideas.md`

**Root — PARTIAL:** `VISION.md` (pre-rename labels) · `STACK.md` (PETSY-era
header, pre-decision prices)

**docs/ — CURRENT (majority):** supplier truth (`meshy-*`, `prodigi-*`,
`makr3d`, `us-suppliers`) · engine contracts (`pipeline-spec`, `etsy-input`,
`limitations-ar`, `action-library`, `delivery-experience`) · creative/IP
(`trademark`, `texture-prompts`, `base-system`, `personas`, `targeting`,
`universes`, `moat`) · demand evidence (`tiers-validated`, `xmas-stockfillers`,
`wizard-extensions`) · launch (`secret-santa-spec`, `listing-playbook`,
`listing-001-ornament`, `sell-structure`, `simple-products`)

**docs/ — PARTIAL:** `catalogue`, `pricing`, `pricing-analysis`,
`christmas-line`, `theme-packs`, `the-product` (structure good, numbers/labels superseded)

**docs/ — STALE:** `products`, `unit-economics` (**all retails superseded —
reuse costs only**), `collections`, `bwizards`, `bwickmas`, `bwitch` (names
retired; scene-pack detail only)

**docs/ — SUPERSEDED:** `structure-spec`, `tarot-spec` → merged into `canonical.md`

Every file carries its own `> STATUS:` header explaining what is stale and why.
