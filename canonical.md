> **STATUS: CURRENT** — annotated 2026-09-26.
>
> THE product system. Anchor doc. Supersedes structure-spec + tarot-spec.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# CANONICAL — the product system (2026-09-25)

**This file supersedes `structure-spec.md`, `tarot-spec.md` and any earlier
standalone system docs.** Collections stay in `bwizards.md` / `bwickmas.md` /
`bwitch.md` as configuration skins. One glossary, one schema, one launch list.

## Moat

> Everyone else copies your photo. We cast you in a world.

## 1. One product system underneath all three collections

```
CHARACTER TYPE      OUTPUT BUNDLE                  REUSABLE FORMATS
solo            ┐   physical figure / display     desk display
couple          ├─  printed backdrop / frame      ornament
solo + pet      ┘   nameplate / title plaque      card + QR
                                          QR animation   premium couple display
```

Not 12 custom products. You are building:
**1 solo base · 1 couple base · 1 ornament mount · 1 backdrop system · 1 QR video system.**
Tarot / Wizard / Xmas are **scene packs** — that is the whole trick.

**HARD CONSTRAINT: max two meshes per order, ever.** One character + one pet, or
two people. This single rule kills preview-time risk, pricing complexity,
composition chaos and photo-herding. Family was cut for this reason — it returns
in a year as a collector play only if demand begs. Until then it does not exist.

## 2. Glossary (the only definitions — use these words everywhere)

| Term | Definition |
|---|---|
| **Character type** | solo, couple, solo+pet. **Never more than 2 meshes per order.** Drives base choice. |
| **Product format** | desk display, ornament, card+QR, premium couple display. |
| **Scene pack** | One collection's full visual kit: costume_pack + prop_pack + backdrop_pack + palette + copy_pack. Tarot / Wizard / Xmas. |
| **Costume pack** | The character's outfit, from the scene pack. |
| **Prop pack** | 2–3 meshes from the shared library (no new modelling per order). |
| **Backdrop** | Interchangeable printed panel — **not** a separately generated 3D model. |
| **Base / mount** | The 2 physical bases (single, couple) + mounts (spike, loop, plinth, magnet, ring). |
| **Frame** | Tarot card layout: image area + title banner + roman numeral + keyword line. One layout → card, backplate, sticker, poster. |
| **Archetype** | Tarot picker option. Curated set only (see §5), never all 22. |
| **Action** | `pog.action/v1` intent (kiss, reveal, glow, dance…). Style-agnostic. |
| **Video** | Action + packaging: script, voice, music, captions, formats, QR binding. |
| **Filter** | A scene pack applied to the same core. "Bwitch is a filter on bwizard" = same base, different skin. |

## 3. Config schema (the listing is a config, not a build ticket)

```json
{
  "collection_id": "tarot",
  "template_id": "lovers",
  "character_count": 2,
  "supports_pet": false,
  "costume_pack": "celestial-lovers",
  "prop_pack": "stars-flowers",
  "backdrop_pack": "tarot-arch",
  "base_style": "couple",
  "action_id": "lovers-glow",
  "copy_pack": "anniversary",
  "occasion_tags": ["anniversary", "wedding", "valentines"],

  "price_tier": "premium",
  "lead_time_sla": "5-8 working days",
  "ip_check": "pass"
}
```

- **`price_tier`** → premium / standard / impulse. Drives the pricing table.
- **`lead_time_sla`** → published verbatim in the listing (never guessed).
- **`ip_check`**: `pass | pending | fail`. **A template with `pending` or `fail`
  cannot ship.** Trademark clearance is process data, not a checklist someone
  remembers. Enforce in code: `if ip_check != "pass": refuse_to_list()`.
- Order flow: `funnylabs/etsy_order.py` becomes a config interpreter, not a
  per-product script.

## 4. Four products (the whole catalogue)

1. **Pet** — the engine and volume king. Dogs and cats, one line, same SKUs
   (figures, ornaments, cards, stickers). Validated by testing, not theory.
2. **Couple** — pair + shared scene + AR moment. Premium romance lane.
3. **Solo + pet familiar** — the signature combo. Highest emotion per order,
   and it's the only product your competitors structurally can't copy well.
4. **Solo** — single human, any scene pack. Entry point: birthdays, self-gifts.

**Family is cut** (not "later" — *out*). Max two meshes per order is a hard rule.

Everything else (keychains, stickers, cards, ornaments, toppers, tattoos) is a
**context** on one of these four — never a fifth product.

## 5. Collections = scene packs

### The frame, mechanic, and picker (shared rules)
- 3D props must be **worn or beside, never held** (pets don't grip).
- Max 3 elements per character (clutter kills it).
- Archetype/costume choice via **picker**, never "describe your fantasy" —
  buyers choose from tight templates.
- Custom comedy off by default (see §7).

### TAROT (Bwitch) — premium, symbolic, adult gifting
Pitch: *"Turn yourself, your partner, or your pet into a tarot archetype."*
Best at: birthdays, anniversaries, self-gifts, spiritual/witchy buyers.
**Launch archetypes: 5, not 22** — The Lovers, The Magician, The High Priestess,
The Empress, The Star. Flattering + giftable; the rest can follow on signal.
- `The Lovers` couple display: 2 figures + arch backdrop + names/date base +
  stars/moon/floral. QR: step together → glow → heart/constellation → title.
- `The Magician` solo: altar/tools/celestial props + name plaque. QR: wand
  raises → light → symbols glow.
- `Pet Arcana`: pet as archetype (cat=The Moon, golden=The Sun, brave dog=Strength,
  pampered cat=The Empress). Role, not costume.
- Rules: elegant, symbolic, never tacky. 5 archetypes max at launch.

### WIZARD (Bwizards) — broadest evergreen mass-market
Pitch: *"Turn yourself into an original magical character."* **No franchise wording.**
- `Wizard Couple`: 2 figures + shared base + backdrop + plaque. QR: both cast,
  sparks meet, heart/starburst.
- `You + Familiar`: **person + their real pet.** Emotional, uses true pet
  likeness, distinct from everyone else. QR: pet causes magical chaos.
- Props: books, wand, potion, familiar (owl/raven/cat), crystal, moon.
  Charming, not generic cosplay.

### XMAS (Bwickmas) — Q4 conversion machine, not the deepest world
- `Our First Christmas` couple: jumpers + tree + names/year, ornament option.
  QR: lights up → gifts exchange → snow.
- `Naughty List Pet Ornament`: elf pet / tangled in lights / stealing presents.
  Easiest to thumbnail, funniest, sells harder than a serious keepsake.
  QR: pet steals gift → bauble falls → "Officially on the naughty list".
- Stocking filler mini: ornament / small display / card+QR. Not everything premium.
- Rules: clarity > originality; names+year matter; ornament format very strong;
  lead-time > complexity; **list early — Q4 search starts early.**
- `Family Christmas Display` = **phase 2** after simpler products validate.

## 6. Launch: 7 listings (count is exact — don't add to it)

| # | Collection | Listing |
|---|---|---|
| 1 | tarot | The Lovers |
| 2 | tarot | The Magician |
| 3 | tarot | Pet Arcana |
| 4 | wizard | Wizard Couple |
| 5 | wizard | You + Your Familiar |
| 6 | xmas | Our First Christmas |
| 7 | xmas | Naughty List Pet Ornament |

**Cut from launch (phase 2):** Solo Wizard, Magical Pet Familiar, Family Xmas
display, full-deck energy, Christmas memorial (**locked: not this Q4** —
parked, not "maybe later," or it creeps back in October).

Blunt ranking: Lovers > You+Familiar > Our First Christmas > Naughty List >
Wizard Couple > The Magician. (Pet Arcana kept for positioning reasons — see §7.)

## 7. Shared order inputs + hard rules

**Buyer supplies:** 1–4 photos · names · optional date · collection · template ·
optional message · optional pet add-on · then collection-specific choice
(tarot archetype / wizard role / xmas scene). **Never make buyers invent from
scratch.**

**Positioning distance (brand-safety rule):** Pet Arcana (meaningful) and Naughty
List (funny) share the same buyer but carry **opposite emotions**. Keep both, but
separate shop sections and **never cross-recommend** — showing a grieving buyer a
prank SKU is a brand injury.

**IP:** every template ships `ip_check` in config; `pending`/`fail` cannot list.
Tarot: archetype names generic-safe; **no Rider-Waite art, no Thoth, no
"Rider-Waite" wording.** Wizard: **no franchise wording anywhere.**

**Price:** 30% net floor (ship absorbed), evidence-graded (✓/Q/EST). Xmas
memorial parked explicitly.

## 8. What the coding agent builds

A **config interpreter**, not separate product systems: one schema (§3), one
listing template per collection, one base set, one backdrop system, one QR
video system. `etsy_order.py` reads the config and executes. Every new listing
is a config object — interpretation arguments become impossible because the
glossary above is the only vocabulary in the repo.

## Archival

`structure-spec.md` and `tarot-spec.md` are superseded by this file — keep as
history, do not edit. `bwizards.md` / `bwickmas.md` / `bwitch.md` remain valid
as scene-pack detail (breed→archetype maps, palettes) but defer to this glossary.
