> **STATUS: CURRENT** — 2026-09-26. Our own concept library (36 concepts).
> Replaces the `productlist1.md` BWIZARD/BWITCH/BWICKMAS tables for planning
> purposes — those are upstream concept art, internal names only, and contain
> non-sellable family entries. Props still reference the `PRP-*` library.
>
> **Hard rules applied:** max 2 meshes per order · 4-product categories only ·
> customer photo identity immutable · no "printed scene exists" claim without an
> approved sample.

# concepts.md — our concept library (3 worlds × 4 categories × 3 variations)

## Structure

- **Worlds (3)**: `Wizard` (fantasy/adventure) · `Mystic` (esoteric/witchy) ·
  `Christmas` (holiday). Generic theme words — no franchise terms, ever.
- **Categories (4)** = the four products from `canonical.md` §4. Not five. Not three.
  1. `solo` — one human. 2. `couple` — two humans. 3. `solo_pet` — human + animal
  (2 meshes, the max). 4. `pet` — one animal.
- **Variations (3) per category per world** = **36 concepts total** (12 per world).

**2-mesh ceiling per order is absolute.** A king + queen + noble pet is *two
products*, not one order: `couple` (King & Queen) and `pet` (their guard dog)
share the regal scene pack and cross-link — never a 3-mesh SKU.

Props come from the existing `PRP-*` library (arch, books, wand, owl, crystal,
tree, wreath, gifts, stockings, candy canes…). Props are candidate geometry only —
verify before treating as a bill of materials.

---

## WIZARD world (fantasy / adventure)

### solo (3)
| ID | Concept | Scene |
|---|---|---|
| WZ-S1 | Apprentice Wizard | robes, wand, spellbook, library arch |
| WZ-S2 | Court Mage | heavy staff, tower steps, crystal altar |
| WZ-S3 | Dragon Tamer | leather kit, dragon-egg stand, ember light |

### couple (3)
| ID | Concept | Scene |
|---|---|---|
| WZ-C1 | **Wizard Pair** | two robed casters, shared spell circle, twin wands |
| WZ-C2 | **King & Queen** | crowns, velvet, throne steps (user pick) |
| WZ-C3 | Knight & Princess | armor + gown, castle arch |

### solo_pet (3)
| ID | Concept | Scene |
|---|---|---|
| WZ-S1P | Sorcerer & Familiar | cat on shoulder, potion wobble |
| WZ-S2P | Ranger & Hound | forest, bow, loyal dog at heel |
| WZ-S3P | Apprentice & Mischief Cat | spell knocked over, paw in the spill |

### pet (3)
| ID | Concept | Scene |
|---|---|---|
| WZ-P1 | **Royal Guard Dog** (noble pet) | crown-collar, shield, throne steps — **cross-links to WZ-C2** |
| WZ-P2 | Owl-post Companion | scroll in beak, moon, feather plume |
| WZ-P3 | Forest Hound | mossy log, ferns, lantern light |

---

## MYSTIC world (esoteric / witchy / gothic)

### solo (3)
| ID | Concept | Scene |
|---|---|---|
| M-S1 | **The Magician** | altar, tools, celestial symbols, name plaque |
| M-S2 | The Star | night-sky backdrop, water, hope motif |
| M-S3 | The Hermit | lantern, cliff, cloak |

### couple (3)
| ID | Concept | Scene |
|---|---|---|
| M-C1 | **The Lovers** | arched frame, stars/moon/floral, names + date |
| M-C2 | Witch & Warlock | cauldron, twin cauldrons, bubbling green light |
| M-C3 | Celestial Pair | one moon one sun, constellation base |

### solo_pet (3)
| ID | Concept | Scene |
|---|---|---|
| M-S1P | Priestess & Moon Cat | veiled figure, crescent, black cat |
| M-S2P | Alchemist & Raven | twin flasks, raven on shoulder |
| M-S3P | Hedge-witch & Hound | herb table, dog at feet, candlelight |

### pet (3)
| ID | Concept | Scene |
|---|---|---|
| M-P1 | Moon Cat | crescent backdrop, silver glow |
| M-P2 | Sun Dog | radiant gold, warm light — **The Sun archetype** |
| M-P3 | Oracle Cat | tarot fan spread, candles, third-eye scarf |

---

## CHRISTMAS world (holiday / Q4 urgency)

### solo (3)
| ID | Concept | Scene |
|---|---|---|
| X-S1 | Santa Self | red suit, sack, chimney base |
| X-S2 | Elf Self | pointy ears, tunic, toy-sack base |
| X-S3 | Nutcracker Self | military uniform, drum, parade base |

### couple (3)
| ID | Concept | Scene |
|---|---|---|
| X-C1 | **Our First Christmas** | matching jumpers, tree, names + year |
| X-C2 | Mr & Mrs Santa | twin suits, sack of minis, fireplace |
| X-C3 | Nutcracker & Ballerina | soldier + dancer, snow-globe base |

### solo_pet (3)
| ID | Concept | Scene |
|---|---|---|
| X-S1P | Santa & Reindeer-pup | handler + antler dog, sleigh fragment |
| X-S2P | Elf & Mischief Cat | cat mid-present-theft, tinsel trail |
| X-S3P | Mrs Claus & Cookie-hound | kitchen, tray, guilty eyes |

### pet (3)
| ID | Concept | Scene |
|---|---|---|
| X-P1 | **Reindeog** (antlers + red nose) | the scream SKU; snow base |
| X-P2 | Santa-pup | suit + beard ruff, gift box |
| X-P3 | Naughty-list Elf Cat | elf ears, tinsel, "officially naughty" plate |

---

## Composition rules (enforce in `compose()`)

```
compose(world, category, variation_id, photos[], names[]) ->
  { design_prompt, shot_list, ar_effect, base_variant }
```

1. `photos[]` → **immutable identity** (face, coat markings). Scene, costume,
   props and backdrop are overlays. Never regenerate identity.
2. `category` decides base: `solo`→single, `couple`→couple,
   `solo_pet`→single + pet plinth, `pet`→single.
   **`couple` accepts a pet variant → 3 identity meshes** (`PROPS.md`).
   **Never >3 identities.** Props (baby, pram, teddy, tree) never count.
3. Cross-links allowed (WZ-C2 ↔ WZ-P1) as *separate products in one scene pack*,
   promoted as a bundle — never one order.
4. Props: candidate only. Geometry verified before it becomes a bill of materials.
5. Output stays `state: concept_only` until a print sample is approved.

## Build order

1. Tiles/boards from the concept art (`productlist1.md` step 1).
2. Generate `catalog.json` from **this** table (36 IDs) + the `PRP-*` props.
3. Wire `compose()` → design prompt + shot list (the prompt stub is per-concept).
4. Approve one print per category before any listing ships.
