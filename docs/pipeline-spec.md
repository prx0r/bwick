# Pipeline spec — top products via etsysignal engine + Etsy limits (2026-09-25)

Engine: etsysignal `roastpet/` (intake → comedy → generate → cards → listing →
remotion/video) + funnylabs (gallery, avatars, talk.py MP4). Output builds prove
the shape (`output/buster-*/`: avatar, character, card/{front,back,inside,texts,
photo,prodigi_layout,qr}, final/{front,inside_right PNGs}, listing/{title,tags,
description,personalization,shotlist,storyboard,thumbs}).
Etsy limits (hard, from listing.py + playbook): 140-char titles, 13 tags,
10 photos, 15s muted video, 5 text-only personalization boxes (no guided UI,
no structured photo fields — buyer photos arrive via order messages, so the
studio ingests unstructured uploads), no embedded configurators/AR (AR lives
behind QR), digital vs physical listing types.

## P1 — Roast card (£4–6) [S]

- Pipeline: intake (3–5 photos, QC scored) → comedy (concepts + reroll) →
  generate (front/back/inside text) → render (front PNG + inside-right PNG) →
  listing (title/tags/description/personalization JSON + 8-image shotlist +
  2× muted 3–15s storyboards) → Prodigi order (prodigi_layout.json).
- Etsy packaging: title formula (keyword-first, 140), 13 tags from tags.txt,
  10 photos per playbook slots, 15s muted teaser (slot 1), personalization
  boxes = recipient/pet/occasion/roast-level/facts (mapped in personalization.json).
- Fulfilment: Prodigi Fine Art 5×7 + sticker insert, Etsy auto-sync.
- Constraint respected: everything interactive (reroll, guided intake, AR) stays
  on studio/QR; listing is static photos + muted video only.

## P2 — Stickers/tattoos/magnets/postcards (£2–15) [S]

- Pipeline: avatar art already rendered (card PNGs, thumbs) → repack to sticker
  sheets (kiss-cut paths), postcard backs, tattoo/magnet crops. No new generation.
- Etsy packaging: same title/tags formula, fewer photos needed (3–5 suffice),
  personalization often unnecessary (fixed designs) → faster list time.
- Fulfilment: Prodigi stickers/postcards. Purpose: review velocity, not margin.

## P3 — Mini figure (£25–40) [S]

- Pipeline: 3–4 photos → Meshy multi-image (30cr) → GLB + thumbs → Makr3D STL.
  Before/after + lifestyle + scale photos come free from mesh outputs.
- Etsy packaging: title leads "Custom … Figure From Photo"; photos: hero (dark/gold),
  before/after (highest-converting), lifestyle+hand scale, couple variant upsell,
  process triptych, base close-up, gift box, ruler shot, reviews, occasion.
  Personalization boxes: pet name (engraved base), species/breed, occasion, gift note.
- Fulfilment: Makr3D (no MOQ, 1–2d, white-label). Single/two-tone first
  (multi-colour purge = human quote). Position collectible, not toy (EN71 sits w/ us).

## P4 — Couples/family set (£45–70) [S]

- Pipeline: 2+ meshes (60cr+) → pair actions (`kiss`/`hug`) → AR moment + video.
- Etsy packaging: set listing (not two singles) with combined title/tags; photos
  show the pair interacting; video = kiss moment muted; personalization per member.
- Fulfilment: Makr3D paired figures + Prodigi couple card, one parcel.

## P6 — Jigsaw/calendar/prints/books [A]

- Pipeline: existing renders repurposed (portrait → puzzle image, 12 situations →
  12 calendar months, book = ordered situations). No new generation.
- Etsy packaging: calendar is Q4-only (2027 sells Oct–Dec); jigsaw needs piece-count
  variants; books need page-count mapping to Prodigi photobook SKUs.
- Fulfilment: all Prodigi, same order flow. Prices via quote endpoint (Q).

## P7 — Digital video/AR/download (£3–8) [S]

- Pipeline: talk.py MP4 (2.5D + voice) / USDZ AR / STL download, QR-bound per order.
- Etsy packaging: **digital listing type** (instant delivery, no shipping);
  preview video IS the product demo; personalization = pet name + message for
  custom video orders, none for stock clips.
- Fulfilment: served download/R2, QR payload per order. ~100% margin.

## Cross-cutting constraints (entire line)

- Photos arrive unstructured (order messages) → studio intake QC + avatar creation
  must accept messy inputs, never assume clean uploads.
- Preview-approve-print: nothing prints before buyer approves the preview
  (stated twice in policies; reroll loop = review insurance).
- AR never lives on Etsy (no embeds) — always QR-bound from physical or download page.
- One pet mesh feeds P1–P7; new products = new packaging of existing renders,
  not new generation. Variant generation (occasion/pet/breed) is the SEO strategy
  for the 500–1600-listing game — pipeline output, not manual listings.
