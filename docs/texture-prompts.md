# Texture prompting — reference guide (2026-09-25)

Sources: Meshy prompting docs (4-part formula, 800-char limit, 3–6 details),
AI texturing guide, OpenAI image-prompt constraints research. Adapted for our
two modes. Meshy accepts text XOR image for texture guidance per call.

## The rule that matters most

**Leave `texture_prompt` EMPTY for identity work.** The pet photos ARE the
texture reference — an empty prompt lets the images drive fidelity with zero
drift risk. Only write a prompt when imposing a STYLE (personas) or fixing a
specific defect. Every word you add is a chance to deviate from the dog.

## Mode 1 — Fidelity (default, pets, print products)

Goal: texture matches the input photos exactly (coat markings, colors).
- Prefer `texture_image_urls[]` (close-up face + coat shots) over text.
- If text needed (single-image calls): describe to PRESERVE, not invent:
  `"match input photo exactly: short brown dachshund fur, tan markings above
  eyes and on paws, black nose, natural coat variation, no style change"`
- Settings: Remove Lighting ON (accurate PBR), 2K default (4K hero products).
- Never add style words here ("Pixar," "cartoon," "stylized" all degrade identity).

## Mode 2 — Persona/style (punk, regal, festive, chibi line)

Goal: impose a style while keeping identity. Meshy formula:
`[Subject] + [Material] + [Art Style] + [Constraints]`, most important first,
3–6 details, 5–20 words. Copy-paste starters:

- Punk: `"dachshund in punk rocker style, ripped denim vest texture, safety-pin
  metallic accents, bold cartoon shading, keep face markings exact"`
- Regal: `"dachshund royal portrait style, velvet cape deep red, gold crown
  metallic, oil-painting richness, keep face markings exact"`
- Chibi: `"chibi pet figure, oversized head, smooth vinyl toy plastic, pastel
  palette, flat-shaded, keep coat colors exact"`
- Christmas: `"dachshund in festive style, red knit santa hat wool texture,
  snow-dusted fur tips, warm holiday palette, keep face markings exact"`
- Print-safe suffix (add when the mesh goes to Makr3D):
  `", solid, watertight, no thin overhangs"`

Note every persona prompt ends with a fidelity anchor ("keep face markings
exact"). Style the clothes, never the face. This is the outfit-fidelity rule
from personas.md, enforced in the prompt itself.

## Universal rules (all modes)

- One subject only. No scenes ("knight in forest" → mess). No multiple objects.
- No contradictions ("realistic cartoon," "simple extreme detail").
- Negative prompts for print work: `"no background elements, without floating
  particles, no text or labels"`.
- Longer ≠ better. Key info first (highest weight). 800 chars is a ceiling,
  not a target.
- Iterate on cheap calls: test persona prompts on retexture (10cr) before
  committing to full generations, not on 30cr meshes.
