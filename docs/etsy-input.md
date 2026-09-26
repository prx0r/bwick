> **STATUS: CURRENT** — annotated 2026-09-26.
>
> Etsy hard limits + simulator spec; engine/etsy_order.py GREEN.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Etsy input — full limitations + simulator spec (2026-09-25)

## Hard storefront limits (what Etsy gives us, nothing more)

- **Personalization: 5 text boxes max** per listing (label + hint each, ~256 chars).
  No dropdowns, no radios, no file pickers, no conditional logic, no validation.
  Our mapping: box1 recipient, box2 pet name, box3 occasion, box4 roast level,
  box5 facts (free text, the comedy intake lives here as raw text).
- **Photos arrive unstructured.** No photo-upload fields exist. Buyers attach pet
  photos to order **messages/notes** (arbitrary count, any orientation/size/heic,
  often screenshots with UI chrome). Intake MUST accept mess: EXIF-rotate, strip
  metadata, reject unreadable with a polite message (never silently use a bad photo).
- **Listing surface**: 140-char title, 13 tags, 10 photos, one 15s muted autoplay
  video. No embeds, no configurators, no AR, no JS. Everything interactive lives
  behind QR/studio links.
- **Variations**: capped option sets (size/color) — use for card size + figure
  finish, not for open-ended customization (that's what the 5 boxes + messages do).
- **Digital vs physical**: separate listing types, separate delivery (instant
  download vs ship). A card+video bundle = physical listing with digital delivered
  via message/QR (Etsy has no mixed-fulfilment type).
- **Order data** (ShopReceipt via API/webhook): buyer, items, quantities, per-item
  personalization text, order notes, gift message flag. Photos are NOT in the
  receipt — they arrive separately via messages. Pipeline must join receipt +
  message attachments by order id (async, photos often land after the order).

## Simulator (build now, Meshy stubbed)

`engine/etsy_order.py`: generates faithful fake Etsy orders AND processes them
through the real pipeline (avatar → card → listing bundle), with Meshy calls
behind a stub interface. When the real key lands, only the stub swaps — nothing
else changes.

Fake order shape (mirrors ShopReceipt + message attachments):
```json
{
  "order_id": "ETSY-TEST-001",
  "buyer": "james.test@example.com",
  "items": [{"listing": "roast-card", "qty": 1,
             "personalization": {"recipient": "James", "pet": "Max",
               "occasion": "birthday", "roast": "savage", "facts": "AGI obsessive"}}],
  "notes": "please make him look extra guilty lol",
  "photos": ["<bytes: front>", "<bytes: side>"],
  "gift": false
}
```

Pipeline stages (each swappable, each logged):
1. `ingest(order)` → validate 5 boxes + notes; QC photos (sharpness/size/face
   present heuristics; reject politely with reasons, never silent).
2. `avatar(order)` → persistent avatar record (exists today: `humour_mcp/avatar.py`).
3. `mesh(order)` → **STUBBED**: returns local avatar PNG + records the exact call
   that Meshy multi-image will take (`image_urls[1..4]` base64, `target_formats:
   ["glb"]`, `multi_view_thumbnails: true`). Swap stub → real call, zero refactor.
4. `card(order)` → template select by occasion → render with avatar (exists:
   `render_cards.py` + `/photo-card/`) → front/inside PNGs.
5. `listing(order)` → title/tags/description/personalization JSON + shotlist +
   muted storyboards (exists: etsysignal `roastpet/listing.py` pattern).
6. `fulfil(order)` → **STUBBED**: writes Prodigi order payload JSON (real call needs
   live SKUs + key; already stored) and Makr3D STL job JSON. Review-before-send
   gate: nothing submits without approve flag.

Run: `python3 etsy_order.py --demo` (2 fake orders: clean photos + messy phone
screenshot) → asserts avatar created, card PNGs exist, listing bundle complete,
fulfil payloads valid JSON. Green = pipeline shippable the day the Meshy key lands.
