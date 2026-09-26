> **STATUS: CURRENT** — annotated 2026-09-26.
>
> categories + v4 API essentials + week-one infra.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Prodigi catalogue — what we use (imported 2026-09-25)

Source: prodigi.com/products + Print API v4 docs. 500K+ SKUs, UK/EU/US labs.
Free account gives sandbox + live `X-API-Key`. Etsy integration is native
(dashboard → Sales channels → Connect, toggle products, auto-fulfil).

## Categories we care about

| Category | Products for us | Role |
|---|---|---|
| Cards & stationery | Fine Art + Classic greeting cards (Mail2Me/Mail4Me), postcards, custom notebooks | hero card + postcard variant |
| Stickers | kiss-cut, transparent | bundle sweetener, margin |
| Wall art | framed/canvas/metal/wood prints, photo tiles, posters | avatar prints |
| Books & magazines | hardcover/softcover/layflat photo books | "Year in Roasts" annual |
| Sport & games | **jigsaws** (multi print areas incl. lid!), skateboards | pet puzzle SKU |
| Technology | phone/tablet cases | avatar merch |
| Home & living | cushions, drinkware, kitchen | character-has-fans merch |
| Apparel | men/women/kids (weakest lane — deprioritize; Inkthreadable if ever) | later/none |

## API essentials (v4)

- Auth: `X-API-Key` header. Sandbox `api.sandbox.prodigi.com` (no fulfil, no charge);
  Live `api.prodigi.com` (produces + ships).
- Order = one POST: `shippingMethod` (Budget/Standard/StandardPlus/Express/Overnight),
  `recipient{}`, `items[]` each with `sku` + `copies` + `sizing`
  (`fillPrintArea`/`fitPrintArea`/`stretchToPrintArea`) + `assets[]` (`printArea`,
  `url`, `md5Hash`). `merchantReference` + `idempotencyKey` (GUID, anti-dupe).
- SKU discovery via product lookup endpoints (get exact SKU + attributes per product).
- Quotes endpoint for live pricing; callbacks (`callbackUrl`) for status;
  pause windows (review before fulfil); cancel/update-recipient/shipping/metadata
  while pre-fulfilment.
- **Branding per order** (free marketing): postcard/flyer inserts, packing slips
  (bw/color), exterior+interior stickers (round/rectangle) — our QR card rides
  in every parcel; pet-face stickers on the box.
- Assets must be publicly accessible URLs (our rendered PNGs served or R2-hosted).
- Mockup generator for the 10 listing photos; sample packs 50% off (order own
  card pre-launch, non-negotiable); global print network covers US buyers.

## What we need from Prodigi (accounts + SKUs)

1. Free account → sandbox key (build/test now) + live key (real orders).
2. Etsy store connected in dashboard (2 clicks, no code).
3. Exact SKUs to pin: Fine Art 5×7 card, postcard, kiss-cut sticker sheet,
   jigsaw (note multi-area: lid art!), framed print, layflat photo book.
4. Sample pack ordered before listing anything.
