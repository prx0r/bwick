> **STATUS: CURRENT** — annotated 2026-09-26.
>
> constraint inventory + QR/NFC binding design.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Limitations + AR-on-everything (structural spec, 2026-09-25)

## 1. Limitation inventory (everything that can stop us, by layer)

**Etsy platform (hard, unchangeable):**
- 140-char titles, 13 tags, 10 photos, 15s muted autoplay video. No embeds,
  no configurators, no AR viewers, no interactive anything on listings.
- 5 text-only personalization boxes. No structured photo upload — buyer photos
  arrive unstructured via order messages. Intake must accept mess.
- Digital vs physical listing types (different delivery, reviews, policies).
- Production-partner disclosure required (list Prodigi/Makr3D/US labs in settings).
- No incentivized reviews; no IP-infringing titles (HP/Star Wars/Marvel text = ban).
- Star Seller = 95%+ on-time + 5-star avg (auto-fulfil protects this structurally).

**Prodigi (API + catalogue):**
- Assets must be publicly accessible URLs (our renders served or R2-hosted).
- Per-SKU required attributes (e.g. canvas needs `wrap`); SKUs must come from
  dashboard catalogue (no reliable API discovery — hand-pick SKUs once).
- Unit + ship pricing per SKU via quote endpoint (free, instant — quote everything
  before listing; never assume).
- Sandbox key ≠ live key (separate credentials; test sandbox, sell live).
- Pause windows / callbacks for review-before-fulfil; cancel/update only pre-fulfil.

**Makr3D (figures):**
- Quote per exact file (filament + time + colours); multi-colour purge = human
  quote (start single/two-tone). £1 minimum per dropship order.
- EN71 toy-safety sits with us (position collectible/keepsake, not toy).
- US orders need US lab (3D Vikings) or eat UK→US postage + days.

**Meshy (mesh supply):**
- 30cr multi-image per pet; signed URLs expire (download immediately).
- Webapp prototypes don't chain to API builds (both stages via API).
- Rig/anim humanoid-only (pets: mesh only). Free 100/mo; commercial needs paid.
- Brick = 6cr preview + 30cr build; approve-gate halves waste.

**Technical (ours):**
- Disk 100% full on build box (free DROP set first; never stage GBs locally).
- No GPU (no local TripoSR; cloud/GPU-box for heavy 3D if ever needed).
- Voice = edge_tts (works); video = talk.py 2.5D + ffmpeg (works); 3D talking
  pets have no cheap path (accepted — 2.5D covers it).

**Operational:**
- Q4 windows are hard (calendars Oct–Dec only; Xmas list-by-mid-Oct for indexing).
- Reroll loop + safety line ship with V1 (one wrong "savage" roast = 1-star spiral).
- Pre-ship QR scan check on every parcel (turns broken-QR reviews into a feature).

## 2. AR on every product (mechanism)

Principle: AR never lives on Etsy (no embeds possible). Every physical product
carries a **QR binding** → scans to that order's AR moment and/or video.
`qr_payload.txt` per order already exists in the pipeline — this formalizes it.

**QR generation + binding (per order, automated):**
1. Order completes (Etsy sync) → generate UUID payload
   `{order_id, pet_id, sku, action, ar_url, video_url}` → write `qr_payload.txt`
   into the order bundle (already a pipeline artifact).
2. Render QR PNG (stdlib `qrcode` or API) → composite into that SKU's print asset
   (card back, sticker sheet corner, packaging insert, hang tag) BEFORE submitting
   to Prodigi/Makr3D. QR is part of the artwork, not an afterthought.
3. QR resolves to `r petsy.site/a/{uuid}` → serves the pet's AR viewer
   (`<model-viewer>` GLB + USDZ Quick Look fallback) and/or the MP4. One URL per
   order, permanent, logged for pre-ship scan check.

**Per-product AR placement:**

| Product | QR carrier | AR moment |
|---|---|---|
| Card | printed on back/inside (part of design) | avatar performs the joke |
| Sticker sheet | corner QR on sheet backing | avatar wave + shop link (viral loop) |
| Figure/statue | **QR embossed in the base/plinth (default — see delivery-experience.md §1)**; fallback = hang tag | 360° spin + signature action (bow/wave) |
| Ornament | QR embossed in the base/plate; ribbon hang tag as fallback | wiggle + jingle sting |
| Jigsaw | box lid QR | completed-puzzle reveal video |
| Calendar | 12 QRs, one per month page | 12 monthly moments (seasonal pack engine) |
| Mug/cushion/phone | packaging insert (print can't carry QR well on curved/cushion) | avatar greeting |
| Couple set | shared base + gift box | kiss/hug moment |
| Digital video | description link + end card | full cut (already digital) |

**Viewer stack (all free, no app install for buyer):**
- `<model-viewer>` web page (GLB + USDZ, iOS Quick Look + Android Scene Viewer
  auto-fallback). Served per-order URL. Works from any phone camera scan.
- Fallback: MP4 inline if WebGL unavailable (same URL, content-negotiated).
- Pre-ship check: scan every QR before dispatch (стали process step; log pass/fail
  per order — reviews cite broken QRs on competitors, ours are verified).

**Why this compounds:** every physical SKU becomes a digital upsell demo (scan →
moment → "unlock more situations" link). The parcel is customer acquisition for
the digital line, and the digital line needs zero fulfilment. AR isn't a feature —
it's the loop that turns one-time buyers into repeat avatar customers.
