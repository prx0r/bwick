> **STATUS: PARTIAL** — annotated 2026-09-26.
>
> prompt fragments + palettes still valid. STALE: pack names (Academic/Pirate/Slayer/Christmas Workshop) predate Roast/Mystic/Holiday line rename — treat as internal labels.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Theme packs — prompt fragments, first three (2026-09-25)

Each pack = palette + props + pose + texture_prompt fragment + fidelity anchor.
Slots into Meshy prototype stage (or standard image-to-3D texture_prompt).
Face/markings never change — style the clothes, never the face.

## 1. Academy (wizard school, IP-safe)

- Palette: deep navy + antique gold + parchment cream.
- Props: pointed hat (no logo), wooden wand, leather satchel, owl perch (optional).
- Pose: standing at attention, chin up, wand raised (celebrate-adjacent).
- Fragment: `"dark academy uniform, navy wool robes with gold trim, pointed
  wizard hat, wooden wand, stone castle backdrop hint, oil-painting richness,
  keep face markings exact"`
- Avoid: lightning scars, round glasses + that exact combo, house names/crests,
  any series terminology in listing copy.

## 2. Pirate crew

- Palette: weathered cream + oxblood red + rope tan + sea green.
- Props: straw hat (PLURAL straw hats are generic — one hat, no scar, no vest
  combo), cutlass (blunt, toy-safe look), treasure chest base, rope coil.
- Pose: one foot on chest, hand on hat brim, grin (celebrate/wave actions).
- Fragment: `"pirate crew outfit, cream shirt, oxblood sash, straw hat, wooden
  cutlass prop, treasure chest base, adventure matte painting style, keep face
  markings exact"`
- Avoid: the specific straw-hat + scar + red-vest trio; "pirate king" phrasing;
  series names anywhere.

## 3. Slayer corps (demon-hunting uniform)

- Palette: near-black + checkered accent (NOT green-black — use rust/ochre or
  indigo/cream checks), silver.
- Props: uniform jacket with checkered hem panel, nichirin-style blade (generic
  single-edge sword, no flame patterns), wisteria sprig base.
- Pose: blade grounded point-down, free hand on hip (bow-adjacent formal stance).
- Fragment: `"demon-slayer corps uniform, black jacket with rust-checkered hem,
  single-edge sword grounded point-down, wisteria base sprig, ukiyo-e inspired
  shading, keep face markings exact"`
- Avoid: green-black checks specifically; flame/water/breath technique names;
  character names; corps symbols verbatim.

## 4. Christmas Workshop (Q4 money — seasonal spotlight)

- Palette: Santa red + snow white + pine green + gold trim.
- Props (modular — mix per order): Santa hat, elf tunic + pointy ears, **nutcracker
  soldier uniform** (tall hat, epaulettes, drum — December bestseller candidate),
  reindeer antlers, snow-dusted pine base.
- Pose: present-offering (gift held out), nutcracker at attention, antlers head-tilt.
- Fragment: `"christmas workshop style, red santa hat with white trim, festive
  scarf, snow-dusted base, warm holiday palette, pine sprig prop, keep face
  markings exact"`
- Nutcracker variant fragment: `"nutcracker soldier style, tall black hat, red
  coat with gold epaulettes, white trousers, toy-soldier stance, keep face
  markings exact"`
- Avoid: Coca-Cola Santa specifics, copyrighted carol lyrics in listings,
  trademarked character crossovers. Generic Christmas iconography is public domain.
- SKUs: ornament (hero), card set, calendar month, family set in matching hats.

## 5. Spooky Christmas (dual-holiday — Halloween through December)

- Palette: pumpkin orange + midnight black + bone white + moonlit purple.
- Props: pinstripe suit + bow tie (stitched gentleman), button eyes + yarn hair
  (patchwork doll), glowing nose ghost-dog companion, grinning gourd head,
  spiral hill base (every Oct–Dec figure stands on one).
- Pose: lopsided bow, arms slightly akimbo, head tilt (gloomy-cute, never scary).
- Fragment: `"spooky christmas style, pinstripe suit with bow tie, stitched
  seams, spiral hill base, pumpkin patch accents, moonlit palette, gloom-cute
  mood, keep face markings exact"`
- Copy bank (originals only): "Merry Christmas, you beautiful nightmare."
  "Christmas cheer level: legally dead." "What's this? Breakfast." (yours).
  Never soundtrack lyrics, never film quotes, never character names.
- Avoid: pinstripe + bat-bowtie + spiral-hill *exact combo* (trade dress);
  "Pumpkin King" phrasing (use "Gourd King"); green/red Christmas pairings that
  drift Grinch-ward; anything from the soundtrack.
- SKUs: stitched gentleman figure, patchwork doll figure, ghost-dog companion,
  spiral-hill display base, card line. October limited-run drop (scarcity +
  season + cult = highest-margin month). Christmas variant of same avatar =
  same customer twice (Oct + Dec).

## Wiring (all packs)

`avatar.json: style` → pack id → fragment appended to Meshy texture/texture_prompt
(or prototype-stage prompt) + prop attachment list + pose default into the action
player. New pack = one fragment + palette + 2–3 props. No pipeline changes, ever.
