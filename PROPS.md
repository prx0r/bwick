> **STATUS: CURRENT** — 2026-09-26. Defines mesh-vs-prop, the revised ceiling,
> the prop library, and custom-prop pricing. **Changes one locked rule**
> (max-2 → max-3 identity meshes) — authorized explicitly; family (4+) still cut.

# PROPS.md — what's a mesh, what's a prop, what costs extra

## The distinction that makes couple+dog work

A **mesh** carries *identity* — the customer's face or their pet's face is what
they paid for. Likeness is the product.
A **prop** carries *style* — a tree, a book, a pram, a baby. No customer photo
required, no likeness expectation, library-reusable.

**Baby = prop.** A swaddled bundle, a pram, a teddy — generic by design, so it
adds zero photo-herding and zero per-order cost. This is the right instinct and
it generalizes: *if the buyer doesn't care that it doesn't look like their
baby's actual face, it's a prop; if they do, it's a mesh.*

## Ceiling: revised to 3 identity meshes (was 2)

Reason the original lock existed: preview time, pricing complexity, composition,
photo-herding. **Couple + dog = 3 identities (2 people + 1 pet)** — all needed,
all identity-bearing, all from the same buyer's photo session in one upload.

| Category | Identity meshes |
|---|---|
| `solo` | 1 (human) |
| `pet` | 1 (animal) |
| `couple` | 2 (humans) |
| `couple` + pet variant | **3 (2 humans + animal) — NEW, authorized** |
| `solo_pet` | 2 (human + animal) |
| family (2+ adults, kids) | 4+ — **still cut** |

**This does NOT create a fifth product.** `couple + dog` is a **variant on the
existing couple listing** ("add your dog, +£X") — same listing, same scene, one
extra identity mesh and a price delta. Keeping it a variant rather than a
product line is what stops this from re-opening the family creep we just cut.

The line: **≤3 identities from one buyer session; anything beyond that is a
family, which stays out.** Props never count toward the ceiling.

## Standard prop library (from the concept library's `PRP-*`)

Grouped so `compose()` can auto-suggest:

- **Scene/structure**: arch, tower, library shelf, spell circle, throne steps,
  altar, fireplace, castle wall, forest, snow-globe base
- **Furniture/fixture**: potion table, book pile, candle set, cauldron, wand rack,
  drum, wreath, tree, stocking, gift pile, candy canes, picket fence
- **Character-adjacent**: owl, raven, broom, shield, banner, crown, cape stand,
  plinth (nameplate)
- **Baby/family props**: swaddled bundle, pram, teddy, high chair, photo frame
- **Live/pet props**: ball, bone, food bowl, lead, antlers, halo, hat

Source: the `PRP-*` library (28–32 entries specced in `productlist1.md`), plus
the new family set. All geometry must be verified before it becomes a bill of
materials — they are concept art until printed.

## Custom props — the premium tier

Standard props = **included** in the listed price (they're free: library
geometry, same for everyone, no per-order work).

**Custom prop = surcharge tier.** Buyer describes a specific object ("his
specific guitar," "the family's actual caravan," "the trophy they won"). Flow:
1. Buyer describes/uploads reference → we quote it (human time + print size).
2. Generate (Meshy or modelled) → preview → approve (same approve-gate).
3. Extra price on top of the figure. Surcharge tiers:
   - **Simple prop** (solid object, one colour, ≤60mm): **+£5**
   - **Detailed prop** (multi-part, textured, printed separately): **+£10–15**
   - **Hero prop** (large, structural, replaces the backdrop): **quote, £20+**
4. **Never** allow custom props to blow the preview-time promise — SLA stated
   in listing as "custom props: 7–10 working days" vs standard 5–8.

## Where this lands

- `canonical.md` §1 ceiling updated 2 → 3 + couple+pet variant authorized.
- `concepts.md`: the 36 stay as-is; add a `couple_pet` variant note per world's
  couple row (not a new product line).
- Pricing: figure price + prop surcharge (never bake custom props into base price).
