# Structure spec — theme × actions × videos

The product configurator model. Every shippable = theme + action(s) + video
package, bound to physical goods via QR/AR. None of the three knows about the
others' internals; the SKU is the join.

## 1. THEME (visual identity — "brick etc.")

What the character *looks like*. One theme skins every action and video.

| Theme | Mesh source | Style prompt | First use |
|---|---|---|---|
| `brick` | Meshy brick endpoint (6+30cr) | minifig proportions, stud details | hero figure line |
| `chibi` | Meshy image-to-3D + chibi texture prompt | big-head, impulse price | mini line |
| `real` | Meshy multi-image (identity-first) | photoreal PBR | memorial, wedding premium |
| `toon` | 2D PIL render (already built) | flat roast.pet house style | cards, stickers |
| `wizard` / `galaxy` / seasonal | theme overlay on any base (hat, robe, backdrop, palette) | fandom energy, no trademarks | Xmas, Halloween, Valentine's |

Theme record: `{id, mesh_pipeline, style_prompt, palette, card_layout,
joke_tone, occasions[]}`. New theme inherits all actions + video packaging.

## 2. ACTIONS (what happens — AR + physical)

Named, parameterized, style-agnostic intents. Applied to physical goods by
scan-to-play (QR on card/packaging → AR or video of the action).

| Action | Roles | Duration | Audio slot | Physical binding |
|---|---|---|---|---|
| `kiss` | pair | 4s | smooch sfx / song clip | Valentine's/anniversary card + couple figures |
| `hug` | pair/group | 4s | warm sting | family set, memorial |
| `wave` | solo | 3s | greeting line | all figures (default alive state) |
| `dance` | solo/pair/group | 8s | music bed | party, stag/hen, Xmas |
| `take-turns` | pair | 15–30s | roast script A/B | roast battle video + card |
| `bow` | solo | 3s | applause | performer/thank-you |
| `celebrate` | any | 5s | cheer sfx | birthday, graduation, new job |
| `sleep` | solo | loop | lullaby / silence + candle glow | memorial line |
| `present` | solo | 5s | gift sting | Xmas, birthday (holds out gift) |
| `walk-in` | solo | 4s | footstep + sting | video intros, AR reveals |

Binding rules per body type:
- **Rigid** (brick/chibi/statue): whole-body position/rotation/scale keyframes.
  No rig needed. Works on pets, objects, everything.
- **Rigged** (humanoid GLB): same action drives named bones if present
  (`Head`, `ArmL/R`), else falls back to rigid. One definition, two fidelities.
- **2.5D** (cards/video): collapses to bob/squash/zoom + audio. Already shipped.

Action record: `{id, roles, duration_s, audio_slot, camera_note, bindings:
{rigid, rigged, flat}, occasions[], ar_trigger}`. New action works on every
style ever made, including customers' existing avatars.

## 3. VIDEOS (actions rendered + packaged)

A video = one or more actions + audio-visual packaging. Actions define WHAT
happens; videos add everything that makes it a watchable, sellable artifact:

- **Script/voiceover** (joke text → TTS voice, per-avatar voice casting)
- **Music bed + SFX** (per-action audio slots filled + mastered mix)
- **Captions/subtitles** (accessibility + silent-feed viewing; Etsy buyers
  watch muted — captions are conversion, not garnish)
- **Multi-scene edit** (action sequences: `walk-in` → `take-turns` → `bow`;
  the roast *show* vs a single roast *moment*)
- **Format variants**: vertical 9:16 (listing video, Shorts/Reels/TikTok),
  square 1:1 (feed), landscape 16:9 (YouTube) — one render graph, three outputs
- **Thumbnail/cover frame** (highest-contrast moment, auto-picked + captioned;
  doubles as an extra listing photo)
- **Duration variants**: 6s teaser (listing autoplay, muted, captioned) vs full
  cut (product, QR-linked). Same project, two exports.
- **QR payload binding** (`qr_payload.txt` per order → this exact video file)

Video record: `{id, actions[], script, voice_cast, music, captions: bool,
scenes[], formats[], durations{}, thumbnail, qr_binding}`.

Why videos are more than actions: an action is a playable intent (live in AR,
interactive, no fixed duration); a video is a fixed, shareable, sellable edit
with audio design, captions, and platform formats. Same source, different jobs:
AR = "holy shit it's alive on my table" (conversion moment), MP4 = "watch/share
this" (acquisition asset + product itself).

## SKU join (examples)

- Valentine's couple card: theme `real` + action `kiss` + video (6s teaser for
  listing + full cut via QR) + Prodigi card + sticker insert.
- Xmas family set: theme `wizard` + actions `present` + `celebrate` + video
  (carol sting, 3 formats) + Prodigi cards + Makr3D figures.
- Memorial: theme `real` + action `sleep` + video (tribute cut, captions) +
  framed print + keychain figure.
- Stag roast battle: theme `toon` + action `take-turns` ×3 rounds + video
  (full edit + teaser clips for the group chat) + cards for the table.
