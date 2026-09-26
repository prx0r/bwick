> **STATUS: PARTIAL** — annotated 2026-09-26.
>
> **Assets missing:** `catalog.json`, `tiles/` and `boards/` are **not in this
> repo** (verified: no such files/dirs). This file is the spec for a concept
> library that must still be built or imported — do not treat it as live
> retrieval until those files exist. Everything below is design, not running code.
>
> **Conflicts with the 4-product lock** (`canonical.md` §4): entries with
> `kind: family` (BWZ-19..22 and equivalents) are **non-sellable** — families
> are cut, max two meshes per order. Keep them as visual reference only.
>
> **Names are internal only:** BWIZARD/BWITCH/BWICKMAS are retired as brands
> (`streamlined.md`) — never in listings, shop names or titles.
>
> Do not delete this file.

# productlist1.md — concept library: retrieval rules + catalog structure

## Retrieval (for model / coding agent)

Use `catalog.json` for retrieval. Its IDs are stable references to the generated
concept-art boards, **not certified parts or sales-ready products**.

1. Filter by `collection` and `kind` (e.g. BWITCH + cat).
2. Read `visual_description`.
3. Open the corresponding `tile_image` and, if needed, `source_image` for style
   and relative composition.
4. Follow `component_refs` to retrieve additional PROPS entries.

**Never infer true connector compatibility, manufacturing price or exact LEGO
compatibility from appearance.**

### Suggested agent operation

```
compose(collection, characters, template_id, optional_component_ids, names)
  -> (concept design prompt, proposed shot list)
```

Rules the system must enforce:
- **Customer photo identity is immutable.** Style/scene/props are overlays,
  never replacements for face/markings.
- Treat components as *candidate props*: **verify physical geometry before
  treating them as a bill of materials.**
- **Never claim a printed scene exists until an actual print sample is approved.**

### Worked example

`template_id=BWT-09` (Witch & Black Cat) uses the personalised person and pet
in a gothic scene; suggests `PRP-03` (arch) and `PRP-13` (candles).

Christmas variant: keep the same person/pet identity, use `BXM-04` visual mood,
swap in `PRP-26` (wreath) and `PRP-27` (tree) **on a verified shared base**.

That is the whole scene-pack mechanic in one example: identity held constant,
mood + props swapped.

## Fields (every concept record)

`id` · `collection` · `title` · `kind` · `visual_description` · `component_refs`
(cross-links to prop concepts) · `tile_image` · `source_image` ·
`source_tile_bbox_px` · `source_tile_bbox_normalized` · `state` · `prompt_stub`

`boards` lists the original posters the tiles were cropped from.

## Library summary

**128 annotated concepts**: 32 BWIZARD, 32 BWITCH, 32 BWICKMAS, 32 reusable
props/structures.

Read `catalog.json` as the canonical source. Each concept has an ID, category,
description, crop, parent board image, crop coordinates, and links to
compatible-looking prop concepts. **These are not measured assemblies.**
`state: concept_only` everywhere — visual concepts pending physical verification.

## BWIZARD (32)

| ID | Concept | Category | Components |
|---|---|---|---|
| BWZ-01 | Apprentice Wizard | solo | PRP-03, PRP-16, PRP-17, PRP-21, PRP-13 |
| BWZ-02 | Wizard Tower | structure | PRP-03, PRP-04 |
| BWZ-03 | Enchanted Library | structure | PRP-04, PRP-16, PRP-13 |
| BWZ-04 | Forest Portal | structure | PRP-10, PRP-12 |
| BWZ-05 | Dragon Egg Stand | structure | PRP-03, PRP-12, PRP-22 |
| BWZ-06 | Spell Circle | structure | PRP-03, PRP-12, PRP-18 |
| BWZ-07 | Potion Table | structure | PRP-15, PRP-16, PRP-13 |
| BWZ-08 | Broom Parking | prop_display | PRP-19, PRP-07 |
| BWZ-09 | Loyal Companion | dog | PRP-07 |
| BWZ-10 | Forest Hound | dog | PRP-10, PRP-07 |
| BWZ-11 | Royal Guard Dog | dog | PRP-24, PRP-23 |
| BWZ-12 | Curious Cat | cat | PRP-16, PRP-13 |
| BWZ-13 | Moonlight Cat | cat | PRP-11, PRP-12 |
| BWZ-14 | Library Cat | cat | PRP-16 |
| BWZ-15 | Couple of Wizards | couple | PRP-03, PRP-17 |
| BWZ-16 | Knight & Princess | couple | PRP-03, PRP-23 |
| BWZ-17 | Adventurer Couple | couple | PRP-10, PRP-07 |
| BWZ-18 | Elf Couple | couple | PRP-10 |
| BWZ-19 | Wizard Family | family | PRP-03, PRP-21 |  ← non-sellable (4-product lock) |
| BWZ-20 | Adventurer Family | family | PRP-10, PRP-16 | ← non-sellable |
| BWZ-21 | Royal Family | family | PRP-23, PRP-24 | ← non-sellable |
| BWZ-22 | Elf Family | family | PRP-10 | ← non-sellable |
| BWZ-23 | Magical Classroom | group | PRP-16, PRP-17 |
| BWZ-24 | Tavern Scene | group | PRP-16, PRP-13 |
| BWZ-25 | Owl Post | prop_display | PRP-21, PRP-07 |
| BWZ-26 | Magical Dragon | creature | PRP-22, PRP-12 |
| BWZ-27 | Wand Collection | prop_display | PRP-17, PRP-18 |
| BWZ-28 | Spell Books | prop_display | PRP-16, PRP-13 |
| BWZ-29 | Crystal Altar | structure | PRP-12, PRP-03 |
| BWZ-30 | Shields & Banners | prop_display | PRP-23 |
| BWZ-31 | Mushroom Grove | structure | PRP-10 |
| BWZ-32 | Cape Stand | prop_display | PRP-24 |

`kind: group` entries (BWZ-23/24) exceed the 2-mesh character rule — treat as
backdrop scenes, not sellable character products.

## catalog.json excerpt (record shape)

```json
{
  "id": "PRP-28",
  "collection": "PROPS",
  "title": "Christmas Stockings",
  "kind": "structure",
  "visual_description": "Green and red fabric-inspired stockings with white cuffs.",
  "component_refs": [],
  "source_image": "boards/bw_ick_magical_modular_catalog.png",
  "source_tile_bbox_px": [0, 1006, 187, 1218],
  "source_tile_bbox_normalized": [0.0, 0.71755, 0.16491, 0.86876],
  "tile_image": "tiles/PRP-28.png",
  "state": "concept_only",
  "prompt_stub": "Personalized small brick-style collectible display. Green and red fabric-inspired stockings with white cuffs. Original design, studio product photography, realistic scale, customizable faces and names."
}
```

Other PROPS records referenced: **PRP-29 Fireplace** (grey stone hearth, holly
mantle), **PRP-30 Wrapped Gifts** (festive parcels, bows), **PRP-31 Candy Canes**,
**PRP-32 Snowy Fence** (picket fence + lanterns) — all `state: concept_only`,
all cropped from `boards/bw_ick_magical_modular_catalog.png`.

## Build order (what's missing)

1. Create `boards/` (source posters) + `tiles/` (cropped concept art).
2. Generate `catalog.json` from the tables above (IDs + crops + prompts).
3. Wire `compose()` in `engine/` to read it and emit design prompts + shot lists.
4. Gate: any record reaching `state != concept_only` requires an approved print
   sample. No exceptions — that is what stops concept art becoming a fake promise.
