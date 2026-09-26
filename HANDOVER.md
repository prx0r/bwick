# HANDOVER — start here

> **STATUS: CURRENT** — 2026-09-26. Written at end of a long spec/build session,
> before any listing shipped. Read this, then the files below in order.

## What this is

One canonical repo for a personalised pet-universe business: photo → avatar →
printable figure / card / video / AR. Brand **Figg**; three lines (**Roast /
Mystic / Holiday**); four products (pet, couple, solo+pet familiar, solo).
**Hard rule: max three identity meshes per order — family sets are cut.**
Couple may add a pet (+£, third mesh); baby and identity-free bits ride as
props. See `PROPS.md`.
Zero inventory: Meshy makes the mesh, Prodigi prints flat, Makr3D prints 3D,
Etsy sells, everything else is digital.

## Read order (do not skip)

1. **`thisisit.md`** — the special one-pager. Three collections, one display format.
2. **`canonical.md`** — THE product system: glossary, config schema, 7 launch listings. **Everything else defers to its vocabulary.**
3. **`DEVPLAN.md`** — phases, offline test suite, validation gates G1–G6, promo/AR/Etsy showcase.
4. **`MESH_PIPELINE.md`** — THE build map for mesh production: photo intake, normalisation, Meshy call, post-mesh gates, video + AR + print. Ordered next-steps at the bottom.
5. **`concepts.md`** — our 36-concept library (3 worlds × 4 categories × 3). Composition rules live here.
6. `VISION.md` + `STACK.md` — thesis, locked SKUs, suppliers, margins.
7. `streamlined.md` — brand naming (authoritative: BWICK/BWITCH/BWICKMAS are dead as names).
8. `BUILD_NOTES.md` — what's built vs specced vs blocked.
9. `docs/` — specs. Every file carries a **STATUS** header (CURRENT / PARTIAL / STALE / SUPERSEDED); read the header before trusting a number.
10. `productlist1.md` — upstream concept-art retrieval rules (assets NOT in repo).

## Doc status summary (55 files, all annotated in-place)

- **CURRENT (36)** — trust as written. Supplier facts verified live (Meshy API
  docs, Prodigi v4 quotes, Makr3D published GBP); Etsy demand figures cited.
- **PARTIAL (11)** — structure still good, numbers/labels superseded:
  `VISION.md`, `STACK.md` (PETSY-era name + pre-decision prices),
  `docs/catalogue.md`, `docs/pricing.md`, `docs/pricing-analysis.md`,
  `docs/christmas-line.md` (pricing authority lives in pricing-analysis),
  `docs/theme-packs.md`, `docs/the-product.md`, `docs/moat.md`,
  `streamlined.md` (naming authoritative; product list pre-4-lock),
  `productlist1.md` (assets missing + family entries).
- **STALE (6)** — do not follow without canonical:
  `docs/products.md` (pre-7-listing + pre-rename),
  `docs/unit-economics.md` (**every retail figure superseded** — reuse its
  verified COSTS only),
  `docs/collections.md` (pre-scene-pack model),
  `docs/bwizards.md` / `docs/bwickmas.md` / `docs/bwitch.md` (names retired;
  content = scene-pack detail only).
- **SUPERSEDED (2)** — `docs/structure-spec.md`, `docs/tarot-spec.md` → merged
  into `canonical.md`. History, do not edit.

## What is built and green

**Docs (55 files):** full annotation pass complete — every file carries a
STATUS header; `MESH_PIPELINE.md` is the next agent's build map (photo intake →
normalise → Meshy → post-mesh → video/AR/print); `canonical.md` merged the three system docs; `concepts.md` holds
the 36-concept library; `delivery-experience.md` (QR-embossed-in-base + Act
One/Act Two split shipping); the 4-product lock is applied consistently across
all current files (verified by grep).

**Code (`engine/`):** gallery (20 card PNGs), avatar store (upload → situations),
photo-card compositing, `talk.py` MP4 (2.5D + voice), `etsy_order.py --demo`
GREEN (fake Etsy orders through the real pipeline), `brick.py --demo` GREEN
(Meshy + Makr3D calls stubbed with exact shapes), live Prodigi quoting via MCP.
Systemd timer: daily collection. R2 backup validated (8.4K objects / 18GB).

## What blocks shipping (in order)

1. **MESHY_API_KEY** — nothing 3D exists without it. Free 100 credits, no card.
2. **Concept library assets** — `boards/`, `tiles/`, `catalog.json` do not exist
   yet (`productlist1.md` build order, step 1–3). Blocks `compose()`.
3. Makr3D account + first test print (STL → quote → sample → photos).
4. Etsy shop + Prodigi/Makr3D dashboard connections (disclose production partners).
5. Disk near-full on this box (see aocsec/box-audit.md DROP list).
6. Decision: which line owns the Christmas SKUs overlapping Roast (see
   streamlined.md open question).

## Open decisions not made here

- Which SKU owner for the Roast/Holiday overlap (Santa self, mistletoe, stocking minis).
- Rename repo `prx0r/bwick` → `figg` (optional; nothing technical depends on it).
- 30%-net vs price-match-proven — both documented, `pricing-analysis.md` holds
  the live quotes; pick one and update `STACK.md` so there's a single authority.

## Done since this file was first written (do not re-do)

- Family sets cut → 4 products, max-two-meshes lock applied repo-wide.
- Brand retirement (Figg + Roast/Mystic/Holiday) recorded, `streamlined.md`
  demoted to PARTIAL (naming authoritative, product list stale).
- All 48 original docs annotated in place; zero deletions.
- Two delivery decisions: QR embossed in the figure base (deletes the insert
  problem); Act One/Act Two split shipping (serialized reveal).

## Rules that must not be eroded

Preview-before-print on every custom SKU · mild roast default for office SKUs ·
IP gate before any listing (`trademark.md` + `ip_check: pass` in config) ·
no franchise wording · 30%+ economics or documented exception · one owner per SKU ·
**max three identity meshes (couple+pet allowed; family cut), props never
count · memorial parked, not this Q4 ·
evidence-graded prices (✓/Q/EST) · no secrets in git.
