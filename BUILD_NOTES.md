> **STATUS: CURRENT** — annotated 2026-09-26.
>
> build state current; overlaps list updated after canonical merge.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# BUILD NOTES (2026-09-25)

## What's built (runs today)

- gallery (20 card PNGs served), avatar store (upload → persistent
  avatar → situations), photo-card compositing, Etsy order simulator
  (`etsy_order.py --demo` GREEN), brick pipeline stubs (`brick.py --demo` GREEN),
  talk.py MP4 (2.5D + voice), R2 backup (8.4K objects / 18GB, validated).
- Live Prodigi quoting through MCP (`funny.quote_card` returns real £).
- Live timers: powstock daily collection; powops health monitoring.

## What's specced, not built (in priority order)

1. Meshy key → real pet mesh (multi-image, 30cr) → rig/AR/print fan-out.
2. Card-studio Perform button → talk.py wiring in gallery.
3. QR/NFC per-order binding + model-viewer AR page (template exists in brick.py).
4. Prodigi SKUs (6 needed from dashboard) → live prices for full S tier.
5. Makr3D account + first test print (STL → quote → sample → photos).
6. Etsy listings (listing-001 ornament drafted; needs mesh renders + print photos).
7. Mount library CAD (socket dims, spike/loop/plinth/magnet/ring — spec'd, not modeled).

## Blockers (need human)

- **MESHY_API_KEY** — the critical path. No mesh = no figure, no print, no
  listing, no video frame. Everything else can build; nothing ships without this.
- Makr3D account + first test print (STL → live quote → sample → photos).
- Etsy shop connection (Prodigi + Makr3D dashboards).
- Disk near-full on build box (freed 3.9G; more in DROP list).

## Keys

- Prodigi: `engine/.env` (local, mode 600, **gitignored — never committed**).
  Live key, verified working (quotes return real £). Sandbox key is separate.
- Others: not yet obtained. Put them in `engine/.env` alongside Prodigi.

## Known overlaps (intentional, don't "fix" by merging)

- **Resolved:** `canonical.md` merged the three system docs (structure-spec,
  tarot-spec, scene-pack) into one glossary + schema + 7-launch list. Those two
  are now banner-marked superseded — history only, do not edit or follow.
- products.md vs STACK.md (strategy vs locked SKUs); tiers-validated vs
  prodigi-tiers (demand evidence vs catalogue ranks); xmas-stockfillers vs
  secret-santa-spec (seasonal SKUs vs shelf spec); meshy-brick vs meshy-pet
  (brick line vs pet line); moat vs VISION (positioning vs thesis).
  Read STACK.md for decisions; others for evidence. Merging loses history.

## Conventions

- Docs and code both live here: specs in `docs/`, runnable pipeline in `engine/`.
  One canonical repo. Former `funnylabs` repo is superseded (engine moved in).
- Prices: verified figures only, marked ✓/Q/EST. Never invent SKU pricing.
- IP: fandom energy, zero trademarks in titles/tags/descriptions. Check
  trademark.md before any new theme.
- Memorial stays dropped. Cheap + fun + nimble + seasonal.
