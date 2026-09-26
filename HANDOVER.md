# HANDOVER — start here

> **STATUS: CURRENT** — 2026-09-25. Written at end of a long spec/build session,
> before any listing shipped. Read this, then the files below in order.

## What this is

One canonical repo for a personalised pet-universe business: photo → avatar →
printable figure / card / video / AR. Brand **Figg**; three lines (**Roast /
Mystic / Holiday**); five products (dog, cat, solo, couple, family+pet).
Zero inventory: Meshy makes the mesh, Prodigi prints flat, Makr3D prints 3D,
Etsy sells, everything else is digital.

## Read order (do not skip)

1. **`thisisit.md`** — the special one-pager. Three collections, one display format.
2. **`canonical.md`** — THE product system: glossary, config schema, 7 launch listings. **Everything else defers to its vocabulary.**
3. `VISION.md` + `STACK.md` — thesis, locked SKUs, suppliers, margins.
4. `streamlined.md` — brand naming (authoritative: BWICK/BWITCH/BWICKMAS are dead as names).
5. `BUILD_NOTES.md` — what's built vs specced vs blocked.
6. `docs/` — specs. Every file carries a **STATUS** header (CURRENT / PARTIAL / STALE / SUPERSEDED); read the header before trusting a number.

## Doc status summary (48 files, all annotated in-place)

- **CURRENT (39)** — trust as written. Supplier facts verified live (Meshy API
  docs, Prodigi v4 quotes, Makr3D published GBP); Etsy demand figures cited.
- **PARTIAL (6)** — structure still good, numbers/labels superseded:
  `VISION.md`, `STACK.md` (PETSY-era name + pre-decision prices),
  `docs/catalogue.md`, `docs/pricing.md`, `docs/pricing-analysis.md` (collection
  labels), `docs/christmas-line.md` (pricing authority now lives in
  pricing-analysis), `docs/theme-packs.md` (pack labels), `docs/the-product.md`
  (net columns), `docs/moat.md`.
- **STALE (5)** — do not follow without canonical:
  `docs/products.md` (pre-7-listing + pre-rename),
  `docs/unit-economics.md` (**every retail figure superseded** — reuse its
  verified COSTS only),
  `docs/collections.md` (pre-scene-pack model),
  `docs/bwizards.md` / `docs/bwickmas.md` / `docs/bwitch.md` (names retired;
  content = scene-pack detail only).
- **SUPERSEDED (2)** — `docs/structure-spec.md`, `docs/tarot-spec.md` → merged
  into `canonical.md`. History, do not edit.

## What is built and green

`engine/` runs: gallery (20 card PNGs), avatar store (upload → situations),
photo-card compositing, `talk.py` MP4 (2.5D + voice), `etsy_order.py --demo`
GREEN (fake Etsy orders through the real pipeline), `brick.py --demo` GREEN
(Meshy + Makr3D calls stubbed with exact shapes), live Prodigi quoting via MCP.
Systemd timer: daily collection. R2 backup validated (8.4K objects / 18GB).

## What blocks shipping (in order)

1. **MESHY_API_KEY** — nothing 3D exists without it. Free 100 credits, no card.
2. Makr3D account + first test print (STL → quote → sample → photos).
3. Etsy shop + Prodigi/Makr3D dashboard connections (disclose production partners).
4. Disk near-full on this box (see aocsec/box-audit.md DROP list).
5. Decision: which line owns the Christmas SKUs overlapping Roast (see
   streamlined.md open question).

## Open decisions not made here

- Which SKU owner for the Roast/Holiday overlap (Santa self, mistletoe, stocking minis).
- Rename repo `prx0r/bwick` → `figg` (optional; nothing technical depends on it).
- 30%-net vs price-match-proven — both documented, `pricing-analysis.md` holds
  the live quotes; pick one and update `STACK.md` so there's a single authority.

## Rules that must not be eroded

Preview-before-print on every custom SKU · mild roast default for office SKUs ·
IP gate before any listing (`trademark.md` + `ip_check: pass` in config) ·
no franchise wording · 30%+ economics or documented exception · one owner per SKU ·
memorial parked, not this Q4 · evidence-graded prices (✓/Q/EST) · no secrets in git.
