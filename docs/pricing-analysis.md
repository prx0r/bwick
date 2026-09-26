> **STATUS: PARTIAL** — annotated 2026-09-26.
>
> LIVE-QUOTED cost table + Model A decision (ship absorbed, 30% net, start there + measure) are CURRENT. STALE: collection labels 'Bwizards/Bwickmas' — now Mystic/Holiday (streamlined.md). Heavy-SKU retails here superseded by 'price match proven'.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Pricing analysis — Bwizards + Bwickmas (live-quoted 2026-09-25)

Every number below is a **live quote** from the Prodigi v4 API (key verified,
GB address, Standard shipping). Method: `retail = (cost + £0.45) / 0.605`
where 0.605 = 1 − 0.30 target net − 0.095 Etsy fees (6.5% trans + ~3% payments
+ £0.45 fixed). Round to £.49/.99 on real listings.

## Verified costs (GBP, all-in)

| Product | SKU | item | ship | TOTAL |
|---|---|---|---|---|
| Fine-art greeting 7x5 | GLOBAL-GRE-MOH-7X5-BLA | 1.05 | 2.35 | **4.08** |
| Fine-art greeting 6x4 | GLOBAL-GRE-GLOS-6X4-BLA | 0.75 | 2.35 | **3.72** |
| Classic greeting A5 ×10 | CLASSIC-GRE-FEDR-A5-BLA-10 | 10.00 | 0.95 | **13.14** |
| Postcard gloss 6x4 | GLOBAL-POST-GLOS-6X4 | 0.40 | 2.35 | **3.30** |
| Postcard Mohawk 7x5 | GLOBAL-POST-MOH-7X5 | 0.90 | 2.35 | **3.90** |
| Kiss-cut sticker 3x4 | M-STI-3X4 | 0.80 | 2.45 | **3.90** |
| Kiss-cut sticker 14x14 | M-STI-14X14 | 6.50 | 5.60 | **14.52** (too rich — drop or resize) |
| Tattoo L | GLOBAL-TATT-L | 3.00 | 2.45 | **6.54** |
| Jigsaw 30pc | JIGSAW-PUZZLE-30 | 10.00 | 5.70 | **18.84** |
| Jigsaw 500pc | JIGSAW-PUZZLE-500 | 16.00 | 5.70 | **26.04** |
| Calendar A4 2027 | CALENDAR-A4-L-DATED | 10.00 | 3.74 | **16.49** |
| Fine-art print 10x10 | GLOBAL-FAP-10x10 | — | — | **11.40** |
| Aluminium ornament RC/SQ | XMAS-ALUM-RC/SQ | 6.00 | 6.45 | **14.94** |
| Porcelain bauble | XMAS-PORC-BAUB | 8.00 | 4.30 | **14.76** |
| Plastic bauble | XMAS-PLAS-BAUB | 5.00 | 6.45 | **13.74** |
| Glass ornament | XMAS-GLASS-SQ | 7.00 | 6.45 | **16.14** |
| Christmas sack | XMAS-SACK | 15.00 | 4.30 | **23.16** |

Print areas worth knowing: calendar = **14 areas** (cover, back cover, jan–dec —
exactly our 13-image plan); jigsaw = **jigsaw + lid** (both required, no `default`);
canvas needs `wrap` attribute.

## Pricing model — DECIDED: Model A, ship absorbed, start at 30% and measure

`retail = (item + ship + £0.45) / 0.605` — shipping is inside the cost, net is
exactly 30% of retail after fulfilment, ship and Etsy fees. Every SKU launches
here, heavy ones included. This is a starting position, not a permanent law:
list at 30%, read demand weekly, adjust. If ornament/jigsaw prices stall at the
Model A point (~£21 / ~£27, above typical bands), the fix is a cheaper SKU or
charged shipping — not guesswork beforehand.

Model B below is retained as the fallback lever, not the launch position.

## Bwizards prices

| SKU | cost | Model | retail | net |
|---|---|---|---|---|
| Fine-art greeting 7x5 | 3.40 | A (free ship) | **£6.36** → £6.49 | £1.91 |
| Fine-art greeting 6x4 | 3.10 | A | **£5.87** → £5.99 | £1.76 |
| Classic greeting A5 ×10 | 10.95 | A | **£18.84** → £18.99 | £5.65 |
| Postcard gloss 6x4 | 2.75 | A | **£5.29** → £5.49 | £1.59 |
| Kiss-cut sticker 3x4 | 3.25 | A | **£6.12** → £6.49 | £1.83 |
| Tattoo L | 5.45 | A | **£9.75** → £9.99 | £2.93 |
| Jigsaw 30pc | 15.70 | B | item **£17.27** + ship £6.25 | £5.18 |
| Jigsaw 500pc | 21.70 | B | item **£27.19** + ship £6.25 | £8.16 |
| Calendar A4 2027 | 13.74 | B | item **£17.27** + ship £4.25 | £5.18 |
| Fine-art print 10x10 | 11.40 | A | **£19.59** → £19.99 | £5.88 |

## Bwickmas prices

| SKU | cost | Model | retail | net |
|---|---|---|---|---|
| Aluminium ornament | 12.45 | B | item **£10.66** + ship £7.25 | £3.20 |
| Porcelain bauble | 12.30 | B | item **£13.97** + ship £4.75 | £4.19 |
| Plastic bauble | 11.45 | B | item **£9.01** + ship £7.25 | £2.70 |
| Glass ornament | 13.45 | B | item **£12.31** + ship £7.25 | £3.69 |
| Christmas sack | 19.30 | B | item **£25.54** + ship £4.75 | £7.66 |
| Xmas card (fine-art 7x5) | 3.40 | A | **£6.36** → £6.49 | £1.91 |
| Xmas sticker sheet 3x4 | 3.25 | A | **£6.12** → £6.49 | £1.83 |
| Xmas calendar A4 2027 | 13.74 | B | item **£17.27** + ship £4.25 | £5.18 |

## What's NOT in these numbers

- **Figures, keychains, magnets, desk/ornament figures** = Makr3D, not Prodigi.
  No account yet; their instant-quote page is open (upload STL → price, no login)
  but needs an STL from Meshy first. Blocked on MESHY_API_KEY.
- **Ship tiers:** I quoted Standard only. Budget/StandardPlus exist and are
  cheaper — **re-quote heavy SKUs on Budget before locking ornament/jigsaw prices.**
- **US/UK split:** all quotes are GB. US needs its own quote set (Prodigi US labs).
- Offsite-ads enrolment would eat into the 30% — excluded by design.

## How to re-quote (30 seconds each)

```bash
curl -s -X POST "https://api.prodigi.com/v4.0/quotes" \
  -H "X-API-Key: $PRODIGI_API_KEY" -H "Content-Type: application/json" \
  -d '{"shippingMethod":"Standard","destinationCountryCode":"GB","currencyCode":"GBP",
       "items":[{"sku":"SKU","copies":1,"attributes":{},
                 "assets":[{"printArea":"default"}]}]}'
```

Never list a SKU without a live quote. Prices above are today's; Prodigi churns
SKUs (two already returned NotAvailable today).
