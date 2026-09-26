> **STATUS: CURRENT** — 2026-09-25.
>
> Two decisions: QR embossed into the figure base (deletes the insert problem) and serialized Act One/Act Two split shipping. Replaces packaging-insert-as-default for figure SKUs.
>
> Do not delete this file.

# Delivery experience — QR on the figure + serialized reveal (2026-09-25)

Two decisions that change how every physical product arrives. Cross-referenced
from `limitations-ar.md` (QR carriers) and `christmas-line.md` (lead times).

## 1. The QR goes on the figure itself (deletes the insert problem)

Emboss the QR code into the base/plinth — Bambu's in-slicer **text tool** does
this free. The figure is the ticket:

- **No paper insert** → nothing to pack, nothing to forget, nothing to print
  on the Prodigi side just to carry a code.
- **Permanent + unloseable** — the code is part of the object, travels with it
  forever, can't be separated from the AR moment it unlocks.
- **Cooler**: scanning your own desk figure is a better moment than scanning
  a packaging card.

Implementation:
- QR URL is the order's `/a/{uuid}` (same binding layer as everything else).
- **Embzzle AFTER the mesh is final** — QR must be exact-geometry, so it's a
  slicer/solid step on the mount/plinth, not a texture overlay (texture warp
  breaks scannability).
- Contrast + quiet-zone: light code on dark base (or reverse), 4-module quiet
  zone, test-scan at 30cm before approving the print profile.
- Fallback: printed QR on the gift box only (not the card, not the insert) for
  anyone who wants paper. `carrier` field on the order decides.

**What this changes elsewhere:** the `limitations-ar.md` per-product QR table
gains `figure base` as the default carrier for all figure/ornament/plinth SKUs.
Packaging insert remains the fallback for flat-only SKUs (cards, stickers) where
there's no 3D object to carry a code.

## 2. Two parcels as a feature — Act One / Act Two

Stop apologising for split shipping. Sequence it:

- **Act One — the card** (Prodigi, 2–3 days): ships first as the teaser.
  *Something's coming.*
- **Act Two — the figure** (Makr3D, arrives later): the main event.

**Market it as a two-part reveal**, staggered arrival dates stated upfront in
the listing and the order confirmation. Anticipation beats simultaneous arrival —
the unboxing-video economy runs on it; every reveal format proves it.

Rules:
- Both arrival dates published in the listing (never "arrives separately" as an
  apology — frame it: "Your preview lands first. The main event follows.").
- Act One must always beat Act Two by ≥2 days (Prodigi 2–3d vs Makr3D 1–2d
  dispatch + transit makes this natural, but verify per SKU).
- Bundles become **experiences across time**, not boxes. The customer's review
  covers the arc, not a parcel.
- One exception: buyers choosing "arrive together" (gift deadline) get both
  re-sequenced — offer the option, default to the serialized version.
