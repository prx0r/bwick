# THE product — one figurine, NFC alive, cheap print attach (2026-09-25)

Doctrine: ONE product (small plastic figurine of your photo). Topper, ornament,
desk, keychain, magnet = contexts (base + mount + packaging + story), not
products. One pipeline, one QA bar, one print profile. Price by context
(£15 magnet → £35 ornament → £80 topper set), never by cost.

## The figurine (constant)

- Single approved mesh profile (multi-image Meshy → GLB → STL, ~80–100mm).
- Single-colour PLA first (two-tone max until multi-colour purge quotes firm).
- One Makr3D print profile, one QA check. Per-unit fulfilment £1.29–2.50 ex-VAT.

## NFC (the alive layer)

- Tag: NTAG213 (144 bytes — plenty for a short URL), bulk ~£0.08–0.15/tag.
  URL shape kept tiny: `r.pet/a/{order-uuid}` (~20 chars, fits with room).
- Placement: adhesive tag **under the base post-print** (not mid-print embed —
  Makr3D runs the printers, we can't insert pauses; post-print adhesion works
  with any fulfilment partner, zero process change).
- UX: tap phone → stock OS opens URL (iPhone background NFC iOS 14+, Android
  always — no app, no camera aiming, no QR framing). Lands on the order's AR
  viewer + video. Fallback: printed QR alongside (card back, hang tag, insert)
  for NFC-off phones. Belt + suspenders, never a dead product.
- Per-order binding: UUID payload `{order, pet, sku-context, ar_url, video_url}`
  (same `qr_payload.txt` system, transport now NFC-first).

## Context kit (merchandising, not products)

| Context | Add to figurine | Packaging | Price | Story |
|---|---|---|---|---|
| Magnet | magnet disc under base | backing card | £15 | cheapest custom gift |
| Ornament | ribbon hook + gift box | Xmas box | £35 | stocking hero |
| Desk piece | plinth + name engraving | shelf box | £25 | everyday hero |
| Keychain | ring + split ring | tag card | £8–12 | entry/review engine |
| Cake topper | spike + gift box | wedding box | £60–80 set | deadline premium |
| Couple/family | 2+ figurines + shared base | set box | £45–70 | AR kiss moment |

Same £3 figurine throughout. Context = mount + box + story + price.

## Cheap printed attach (every parcel)

Stickers, roast card, postcard via Prodigi (pennies) + QR insert (NFC fallback +
shop link). Every physical order carries its own review engine (QR → AR moment →
prompt) and its own acquisition (stickers travel, cards get kept).

## Unit math (figurine + attach, example £30 order)

Mesh £0.15 (amortized) + Makr3D ~£2 + NFC £0.12 + print attach £1.50 + ship £3.50
+ Etsy ~£4.50 ≈ £11.77 COGS+fees → **~£18 net (~60%)**, zero inventory, 1–2d dispatch.
