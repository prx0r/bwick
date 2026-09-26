# AGENTS.md — bwick operations

> Personalized pet universe. ONE canonical repo: strategy + specs + engine
> all live here. Read VISION.md first, STACK.md second.

## What this repo is (and isn't)

- **Is**: `engine/` (the runnable pipeline), product strategy, supplier docs,
  build specs, listing packs, economics. Decisions are made here.
- **Is not**: a monorepo of unrelated projects. The former `funnylabs` repo is
  the source of `engine/` and is superseded — do not push engine changes there.

## Layout

- `engine/` — runnable pipeline (gallery, avatars, render_cards, talk.py,
  etsy_order.py, brick.py, MCP, studio server, Worker). Run from `engine/`.
- `docs/` + root `.md` — specs, pricing, listings. No engine code in `docs/`.
- `ideas.md` — inbox; graduates to `docs/products.md` or dies with a reason.

## How to work here

1. **Docs before code.** Spec the SKU/pipeline first; build only after the
   spec's acceptance criteria exist. A doc without acceptance criteria is a
   note — send it to `ideas.md`.
2. **Ideas graduate or die.** Promotion = entry in `docs/products.md` with
   price + fulfilment + demand evidence. Death = one-line reason in place.
   Never delete ideas silently.
3. **Prices are evidence-graded.** Suffix every figure: ✓ verified (live quote
   / published page), Q (needs quote endpoint / dashboard lookup), EST
   (modelled — confirm before listing). Unmarked numbers get challenged.
4. **IP check is a gate, not a guideline.** New theme/sku/copy → scan titles,
   tags, descriptions against `docs/trademark.md` BEFORE writing the listing
   pack. Fandom energy, zero trademarks. Memorial stays dropped.
5. **No secrets in this repo.** API keys live in service `.env` files (0600,
   gitignored) or the vault — never in docs, patches, or chat. Secret-scan any
   doc touching credentials before commit.
6. **Commit hygiene.** Small commits, one concern each; never commit `.env`,
   `data/`, DBs, or print files. Push to `origin/main` when green.

## Key files

| File | Why |
|------|-----|
| **canonical.md** | **THE product system — glossary, schema, 7 listings. Read first. Supersedes structure-spec + tarot-spec.** |
| VISION.md / STACK.md | thesis + locked SKUs/margins — decisions live here |
| BUILD_NOTES.md | built vs specced vs blocked — start here each session |
| ideas.md | inbox — graduate or kill, never silent-delete |
| docs/products.md | the line (P1–P8, prices, fulfilment) |
| docs/unit-economics.md + pricing.md | money (verified figures only) |
| docs/pipeline-spec.md + etsy-input.md | engine contract + Etsy limits/simulator |
| docs/limitations-ar.md | everything that constrains us + AR-on-everything |
| docs/listing-playbook.md + listing-001-ornament.md | conversion system + first real listing |
| docs/meshy-*.md + prodigi-*.md + makr3d.md + us-suppliers.md | supplier truth |
| docs/theme-packs.md + personas.md + trademark.md + universes.md | creative system + legal guardrails |
| docs/moat.md + targeting.md | positioning + buyers |
