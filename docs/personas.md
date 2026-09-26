> **STATUS: CURRENT** — annotated 2026-09-26.
>
> style picker mapping; fidelity rule enforced in texture prompts.
>
> Do not delete this file. Delete/merge only after the superseding file says so.

# Personas — style picker mapping table (2026-09-25)

The 5th question on every listing. Default "Match my photo" + 4 personas +
seasonal slot. Same face/markings always; personas replace clothes/props/pose
only. Worth ~£10 perceived value alone.

## Picker

"Match my photo" (default): outfit, colors, vibe lifted from the upload.
Safest, most accurate, fastest. The BrickPaws-customer expectation.

| Persona | Palette | Props | Pose default | texture_prompt core |
|---|---|---|---|---|
| Punk | ripped denim, safety-pin brights, black | mic / mini guitar | slouch, mic-drop | "punk rocker pet, ripped denim vest, mohawk energy, safety pins" |
| Soft | pastels, cream, cozy knit | blanket / cushion | cuddle loaf, sleepy eyes | "soft pastel pet, cozy knit textures, sleepy gentle expression" |
| Regal | velvet red/purple, gold | crown, cape, throne base | sit tall, chin up | "regal pet portrait, velvet cape, crown, royal pose" |
| Hero | primary red/blue, emblem chest | cape, city base | lunge, action stance | "superhero pet, cape, chest emblem, dynamic action pose" |
| Festive (seasonal) | Q4: Santa red/green + scarf | Santa hat, ornament base | sit + head tilt | "christmas pet, santa hat, festive scarf, ornament setting" |

Seasonal slot rotates quarterly (bunny spring, spooky autumn, Santa winter) —
same system, seasonal skin, no code changes.

## Wiring (already designed for this)

- `avatar.json` gains a `style` field (persona id or `match`).
- Meshy texturing takes a literal `texture_prompt` — the persona IS that prompt
  + palette + prop list. One mapping table (above), no new pipeline.
- Pose follows persona (punk slouches, regal sits tall, hero lunges) via the
  action library's intent defaults — persona sets them, actions play them.

## Outfit fidelity rule (stated in every listing)

"Match my photo" copies the outfit; personas replace clothes only — face,
markings, and identity never change. Kills the #1 likeness fear ("will it
still look like MY dog?"). State it twice: listing body + FAQ.
