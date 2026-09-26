> **STATUS: CURRENT** — annotated 2026-09-26.
>
> file set + mount library + go/no-go checklist. Canonical.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Sell structure — what must exist to sell (2026-09-25)

Everything below is a file, a dimension, or a checklist item. Nothing ships
without all three per SKU. Fandom energy throughout, zero trademarks anywhere.

## 1. File set per product (in repo, versioned)

```
products/<sku>/
  figure.glb          # master mesh (from Meshy, identity-approved)
  figure-print.stl    # print file (remeshed, watertight, oriented, supported)
  mount-<type>.stl    # spike | loop-cap | plinth | magnet-disc | ring-cap
  assembly.md         # which mount + glue/hardware + orientation notes
  print-profile.md    # material, layer, infill, colours, est. time + filament
  quote.json          # Makr3D instant-quote output (cost locked before listing)
  listing/            # title.txt, tags.txt, description.md, 10 photos, video.mp4
```

No SKU lists without a printed, photographed, quoted physical sample in hand.
Sample pack rule extends to figures: hold the product before selling it.

## 2. Mount library (CAD parameters, one-time build)

| Mount | Structure | Key dims | Hardware |
|---|---|---|---|
| Spike pick | 2 pegs (standard cake pattern) under base | pegs Ø6mm × 40mm long, 25mm spacing | none (printed) |
| Ribbon loop | slotted cap + through-hole | slot 3×12mm, cap Ø20mm | ribbon + split ring (bought) |
| Plinth | solid base, embossed name face | 60×40×12mm, text ≥3mm tall | none |
| Magnet | flat back + disc recess | recess Ø20×3mm (standard neodymium) | N52 disc (bought, glued) |
| Keychain | loop cap + ring hole | hole Ø4mm | split ring (bought) |

Socket standard: 3mm peg × 8mm deep on every figure; all mounts carry the mate.
Tolerance-test one print before batching SKUs.

## 3. Fandom themes (Gen Z current, IP-safe framing)

Rule: aesthetic + vibe, never names/logos/quotes. "Inspired by" energy, original text.

| Theme | Look | Applies to | Avoid (IP) |
|---|---|---|---|
| Dark academia / Wednesday-ish | black dress, braids, deadpan pose, gothic arch base | figures, cards, stickers | character name, show title, Netflix marks |
| Anime hero | oversized eyes style, dynamic base, energy effects | figures, stickers, tees later | series/character names, studio names |
| Block builder | stud texture, square proportions | brick line, ornaments | LEGO word/logo, set numbers |
| Pop star eras | sequin jacket, mic, stage base, era colorways | figures, cards, videos | artist names, lyrics, album titles |
| K-pop idol | mic, stage light base, photocard-style print | figures, prints, photocards | group/song names, agency marks |
| Cozy gamer | headset, controller prop, RGB base glow | desk minis, stickers | game titles, character names |
| Cottagecore / goblincore | mushrooms, moss, toadstool base | figures, prints, stickers | none (public-domain aesthetic, safest lane) |
| Y2K | chrome, flip-phone prop, butterfly clips | stickers, cards, phone cases | brand names |

Each theme = palette + 2–3 props + base style + joke-tone shift. Same avatar,
new skin. No theme ships without an IP check (title/tags/description scanned
for trademarked terms before listing).

## 4. Per-SKU sell checklist (all boxes or no list)

- [ ] Mesh approved (recognizability signed off, front/side/back checked)
- [ ] Mount merged + test printed (fit, stability, weight checked)
- [ ] Print profile locked (Makr3D quote saved as quote.json)
- [ ] Physical sample held + photographed (hero, before/after, lifestyle, scale)
- [ ] Listing pack complete (title/tags/description/personalization/10 photos/video)
- [ ] IP scan clean (no trademarked terms anywhere)
- [ ] Price set from live quote + fee math (never from estimates)
- [ ] QR/NFC binding tested (scan → AR/video resolves)
- [ ] Packaging defined (box + insert + ribbon/ring/tag hardware on hand)
- [ ] Cut-off dates published (seasonal only)
