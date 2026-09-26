> **SUPERSEDED by `/canonical.md`.** Kept as history — do not edit, do not follow.
> The canonical glossary/schema/launch list lives in `canonical.md`.

# Tarot line — spec (2026-09-25)

## The reframe (important: conflicts with our locked strategy otherwise)

We locked "one collection, depth first, brick-only until the cult has members."
A third collection launched in Q4, before the first one exists, breaks that.

So spec it this way: **tarot is a frame system + archetype picker, not a third
collection.** The frame (border + title plate + numeral + keyword slots) is a
rendering format that can dress a wizard couple, a Christmas pet, or a solo
mystic. Build it once, every collection inherits it. "Btarot" is then a *skin*
of the frame, launched Jan/Feb on the review base — after Bwickmas cash and
Bwizards evergreen are proven. Order: Bwickmas (Q4) → Bwizards (Jan) →
Barcana via the frame (Feb). Not 20 themes. One frame, three skins, nine months.

## Why tarot is the strongest skin we have

- **It's a picker, not a brief.** Customer picks archetype from a dropdown —
  solves the choice-paralysis problem ("describe your fantasy" fails, "which
  arcana are they" converts). 22 cards = a menu the product already understands.
- **Emotional weight.** "The Star" means hope, "The Lovers" means connection.
  A pirate is a costume; an archetype is a meaning. Higher price tolerance than
  the funny line, without leaving the brand.
- **Female gifting audience**, which we currently underserve — mystical/witchy/
  zodiac buyers are established Etsy spenders.
- **Perfect frame geometry.** Fixed slots: image area, title banner, roman
  numeral, keyword line. Every product inherits the same layout (card front,
  backplate, sticker, poster). Design once per skin, not per SKU.

## Products (five, all reuse existing lines)

1. **"The Lovers" couple display** — archetypal couple, names + date on base,
   QR: step together → glow/stars → title appears. Variants: any pairing,
   couple+pet. Test **£49–59**. Anniversary/wedding/Valentine's. *Top priority.*
2. **Pet tarot** — pet given a *role*, not a costume: The Fool (goofy dog),
   Strength (big brave dog), The Moon (mysterious black cat), The Sun (golden
   retriever), The Empress (queen cat). The funny-meaningful intersection —
   likely our best pet SKU ever. Figure **£15–25**, card **£4–6**, ornament, sticker.
3. **"The Magician" single** — archetype with props (wand/crystals/raven).
   Birthday/self-gift/spiritual. **£25–35.** Semi-custom titles = zero bespoke design.
4. **"Your Card" archetype birthday** — recipient picks the arcana for them.
   Removes design paralysis; cleanest order flow we have.
5. **Trading-card add-on** — single archetype card, 2.5×3.5" 18pt stock.
   **$5.50 single / $0.70 @300** (MyTradingCards) or MPC API for automation,
   or check Prodigi's playing-card SKUs first. Cheap basket-stuffer; also the
   format for a future deck (22 archetypes + couples/pets as expansions).

## Technical build (reuses everything already spec'd)

- **Archetype config table**: `{arcana_id, name, keyword, palette[4], props[2–3],
  pose, meshy_fragment, gift_meaning}` — 22 rows, JSON. No pipeline changes.
- **Frame renderer**: slots = image area + title banner + numeral + keyword.
  One backplate PNG per skin; characters composite in as today.
- **Meshy prompt**: `<archetype fragment> + <pet/person fragment> + keep face
  markings exact` (the texture-prompts.md fidelity rule, unchanged).
- **Physical**: reuse the two bases (single + couple). Backplate = interchangeable
  printed panel, not a new 3D model — the desk display ships flat-packed with the
  figure slotting in. One print profile, one QA bar.
- **QR animation**: card-flip reveal → archetype effect (glow/stars/heart)
  → title + names. Same action-library intent structure (`reveal`, `glow`).
- **Trading card**: archetype card = frame renderer output at trading-card ratio;
  order via supplier chosen after Prodigi playing-card SKU quote.

## Legal (non-negotiable)

- **No Rider-Waite art.** Original 1909 Smith/Waite plates are US-public-domain
  (pre-1928), but copying them is a trademark/attribution mess on Etsy and is not
  our look anyway. Draw originals in our house style.
- **No Thoth** (Crowley/Harris — still copyrighted). No "Rider-Waite" wording.
- Archetype names (The Lovers, The Magician) = generic card terms, safe.
- Scan titles/tags/descriptions via trademark.md before any listing.

## Sequencing

Q4: Bwickmas ships, no tarot. Jan: Bwizards ships. Feb: frame system lands,
Barcana skins the first three SKUs (Lovers, pet tarot, Magician), trading-card
deck researched as a bundle if the singles sell.
