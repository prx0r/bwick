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

## What's specced, not built — the full remaining work (priority order)

Detail for 1–6 lives in `MESH_PIPELINE.md`; props in `PROPS.md`.

### A. Production line (mesh) — nothing ships until A1–A4

1. `engine/normalise.py` — EXIF orient, validate, role-sort (front first),
   size guard, emit `image_urls[]` base64. Reuse `photo_role_policy.json` +
   `photo_qc.py`; don't reinvent. **Testable today against the etsysignal sample
   uploads — no key needed. This is the right first build.**
2. Two **Q** marks to confirm at Meshy signup: free-tier credit terms; exact
   image size/dimension limits.
3. `MESHY_API_KEY` → real pet mesh (multi-image, 30cr, `target_formats:["glb"]`,
   `multi_view_thumbnails:true`).
4. Post-mesh gates + store: download URLs **immediately** (they expire) into
   `engine/pets/{id}/` — glb + textures + thumbnails, checksummed,
   `print-ready` flag only after gates pass (GLB parses / 2mm walls / face count).

### B. Surround (built once the mesh exists)

5. USDZ converter (headless Blender, GLB→USDZ) — iOS AR needs it; brick output
   has no USDZ.
6. Turntable renderer (headless, mesh → N frames → MP4) + `video.py` wiring so
   studio "Perform" calls `talk.py` (teaser + full cut from one render).
7. AR page: fill the `MESH-PENDING` slots in `brick.py` with real GLB/USDZ URLs;
   per-order UUID binding (`/a/{uuid}` → pet → mesh → action).
8. QR embossed in figure base (Bambu in-slicer text tool, `delivery-experience.md` §1);
   test-scan at 30cm before approving the print profile.
9. Blender headless script: turntable + USDZ + (later) mesh-frame renders.

### C. Concept library (enables `compose()`)

10. `boards/` + `tiles/` from the concept art → generate `catalog.json` from
    `concepts.md` (36 IDs) + `PRP-*` props.
11. `compose()` → design prompt + shot list; enforce immutable identity + ≤3
    identity meshes + `ip_check: pass` before any listing packs.
12. Verify prop geometry before treating any `PRP-*` as a bill of materials.

### D. Physical product

13. Mount library CAD (socket dims; spike/loop/plinth/magnet/ring) — spec'd, not modeled.
14. Prop library geometry (standard props) + **custom-prop quote flow**
    (simple £5 / detailed £10–15 / hero £20+, own SLA — `PROPS.md`).
15. Makr3D account → first live quote on a real STL → sample order → hold +
    photograph (lifestyle/scale/box shots for listing-001).
16. Couple+pet variant: base accepts a third identity mesh (+£ pricing delta).

### E. Commercial

17. Prodigi SKUs from dashboard (6 still needed) → live prices for Tier-S.
18. Etsy shop + Prodigi/Makr3D dashboard connections (disclose production partners).
19. Listings: `listing-001-ornament` drafted; needs mesh renders + print photos.
20. Traffic engine: daily posting of video/AR clips (the reviews flywheel —
    currently unspecced anywhere; see `xmas-stockfillers.md` mechanics).
21. Open decision: which line owns the Christmas SKUs overlapping Roast
    (`streamlined.md` open question).

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
