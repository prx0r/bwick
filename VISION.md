# PETSY — finalized vision (2026-09-25)

Personalized pet universe: upload once, own the character, monetize across
cards, figures, video, AR. One pet mesh feeds every SKU. Zero inventory.

## Thesis

Every pet owner buys identity, not objects. A card with *their* dog roasting
*their* husband outsells any generic funny card; a brick figure of *their* cat
outsells any shelf toy. Personalization is the product — print, video, and 3D
are just manifestations. Meshy proved demand ($39–41 pet figures, memorial
reviews); Etsy proves distribution (8.1k couple figurines, 3.5k $272 wedding
toppers); nobody combines them with comedy + video + AR.

## Architecture (settled)

```
pet photos (3-4, front + sides)
  → Meshy multi-image-to-3D (~30cr) → canonical GLB + textures + thumbnails
  → PET_IDENTITY = geometry + textures (+ skeleton where possible)
  → offline forever: situations, renders, prints, cards, video, AR
```

- **Meshy = mesh supplier only.** Download everything on success (signed URLs
  expire). Never pay twice for the same animal.
- **Talking = 2.5D** (audio-envelope jaw + bob + blink + neural voice → MP4).
  Meshy rigging is humanoid-only; quadruped rigging is a separate project.
- **Actions = data** (`kiss`, `hug`, `wave`, `dance`, `take-turns`, `bow`,
  `celebrate`, `sleep`, `present`, `walk-in`). Style-agnostic: rigid bodies get
  transforms, rigged meshes get bone drives, 2.5D gets squash. New style
  inherits all actions; new action works on all styles.
- **Human line** (same pipeline + rig 5cr + anim 3cr = 38cr total): fully rigged
  talking humans for weddings, couples, Xmas sets. Premium tier.

## Product ladder (in order)

1. **Card + QR video** (Prodigi Fine Art 5×7, auto-fulfil via Etsy integration).
   Hero. 20 templates live, 10 Christmas for Q4.
2. **Sticker pack + postcard variant** (Prodigi, same order flow). Margin +
   review velocity + bundle sweetener (pet-face stickers in every order).
3. **Mini figurine** (Meshy STL → Makr3D Huddersfield: no MOQ, 1–2 day dispatch,
   white-label; Etsy/Shopify integrated). Premium upsell ~£25–40.
4. **Framed avatar print / photo book** (Prodigi wall-art; "Year in Roasts"
   annual compilation = retention hook).
5. **Digital**: talking videos, AR kiss/moments (USDZ free with mesh), downloads,
   extra situations. ~100% margin.
6. **Later**: apparel (weak lane, use Inkthreadable if ever), brick sets,
   desk-buddy subscription, memorial packages.

## Unit economics (per pet, verified credits)

- Mesh establish: ~30cr (~$0.16–0.30). Human full loop: ~38cr.
- Free tier covers ~3 pets/mo at $0. Brick figure: 6cr preview + 30cr build.
- Retail anchors: cards £4–6, figures £25–40, wedding premium £200+,
  digital ~100% margin. Mesh cost never the constraint; acquisition is.

## Roles (who does what)

- **Meshy**: mesh + textures + thumbnails (+ brick builds for physical line).
- **Prodigi**: all flat print (cards, stickers, postcards, wall art, books) +
  Etsy auto-fulfil. Free account; X-API-Key for orders.
- **Makr3D**: UK 3D print fulfilment (no MOQ, 1–2 day). STL in, parcel out.
- **Etsy**: acquisition + checkout. Listings manual first, API later.
- **Studio (this repo's build target)**: upload → avatar → situations →
  preview/approve → order. Prototype-cheap, build-on-approve throughout.

## IP rule

Fandom energy, no trademarks. "Wizard academy," never "Harry Potter" in a
listing. Parody/personal-use gray; commercial HP/Star Wars/Marvel text is
infringement. Same for brick-as-brand.

## Q4 plan

Cards + Xmas figure set live by mid-Oct (Etsy indexing lead time). Christmas
templates (10) already rendered. Family/Xmas sets = highest basket. Valentine's
AR-kiss cards next; funeral/memorial line on standby (proven demand, premium).

## Repo map (to build)

- `studio/` — upload → avatar → gallery → approve → order (from funnylabs)
- `pipeline/` — mesh jobs, talk renderer, action player, SKU exporters
- `products/` — per-SKU specs (card, sticker, figure, video, AR, book)
- `docs/` — listings copy, Prodigi/Makr3D runbooks, unit economics
