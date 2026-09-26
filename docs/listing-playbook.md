> **STATUS: CURRENT** — annotated 2026-09-26.
>
> shop signals + title + 10 photos + 15s video + AR film recipe. Memorial removed.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Listing + shop playbook (2026-09-25)

Conversion system for Etsy. Shop wins clicks before reviews exist; listings
convert with the same 10-photo + 15s-video formula every time; AR videos are
filmed with the pipeline itself (no crew).

## Shop level: one brand, three signals

- **Identity**: roast-stage grammar (dark, gold, podium) in name + banner + icon.
  Every thumbnail instantly recognizable in search results.
- **Sections mirror buying occasions, not org chart**: Birthday Roasts / Wedding
  & Couples / Christmas. Buyers shop occasions.
- **About**: origin story with real emotion (dead-dog shape: real feeling, real
  shelf, real name) + process triptych (photo → preview → doorstep).
- **Policies that pre-kill 1-stars**: processing times in days (not ranges),
  Christmas order-by dates in season, "preview approval before anything prints"
  stated twice.

## Listing level: the formula

**Title** (140 chars, keyword-first):
`Custom Brick Pet Figure From Photo | Personalized Dog Gift | 3D Printed Keepsake | Birthday Gift For Dog Mom`
Front-load the searchable noun; occasion stack at the back.

**10 photos** (same slots every listing):
1. Hero: finished figure, dark background, gold accent
2. Before/after: customer photo → brick figure (highest-converting format)
3. Lifestyle: real shelf/desk, human hand for scale
4. Couple/family variant (in-image upsell)
5. Process triptych: photo → 3D preview → printed figure
6. Base close-up with engraved name
7. Gift box / unboxing
8. Size comparison (ruler or coin)
9. Review screenshots (once they exist)
10. Occasion shot (tree / wedding cake with topper)

**Video** (slot 1, Etsy boosts video listings; autoplay muted — must land silent):
15s max, burned-in subtitles never under 96px. Shot list: photo on screen
(0–2s) → morphs into rotating 3D preview (2–6s) → printed figure on desk, hand
picks it up (6–10s) → AR moment on phone screen + "IT COMES ALIVE" (10–13s) →
price + "preview in minutes" card (13–15s).

## AR videos: filmed with the pipeline (no crew)

1. Screen-record a real phone (not emulator): open AR viewer (`<model-viewer>`),
   screen-record, perform the moment (tap → wave/bow/kiss). Real phone UI in
   frame reads as real product.
2. Three shots per product: (a) reveal (tap, it moves), (b) couple kiss
   (noses meet), (c) celebration (figure dances, confetti sting). Each is a standalone
   10–15s social clip AND a listing-video candidate.
3. Assemble with ffmpeg (on box): concat, burn subtitles, export vertical
   1080×1920 (TikTok/Reels/Shorts) + square (Etsy). Situation PNGs = thumbnails
   + end cards.
4. Audio split: social = TTS + music; Etsy = same cut muted, bigger subtitles.
   One shoot, two masters.

## Trust stack (beats BrickPaws)

- Free preview renders in minutes — say the number, show a timer graphic
  (their 1–3 days is the headline).
- UK printed, 1–2 day dispatch, no customs — stated three times (title tail,
  photo 7, FAQ). US orders via 3D Vikings, same promise.
- Pre-ship scan check — "we scan every QR before it leaves" (turns broken-QR
  reviews into a feature).
- Review engine: QR insert in every parcel → AR moment → review prompt.
  Reviews are the ranking algorithm; engineer them like inventory.
