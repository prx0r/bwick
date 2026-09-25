# ACTION_LIBRARY.md — pog.action/v1 + 10 starter actions

Actions are style-agnostic intents. Same definition drives rigid brick bodies,
rigged humanoids, rigged quadrupeds, and 2.5D cards/video. New style inherits
all actions; new action works on all styles including customers' existing avatars.

## pog.action/v1 schema

```json
{
  "id": "kiss",
  "roles": ["a", "b"],
  "duration_s": 4,
  "audio_slot": "smooch sfx | song clip",
  "camera": "medium close-up, slow push-in",
  "tracks": {
    "rigid": [{"t": 0.0, "pos": "apart", "rot": 0}, {"t": 3.0, "pos": "touch", "rot": -12}],
    "humanoid": {"bones": ["Head", "ArmL", "ArmR"], "fallback": "rigid"},
    "quadruped": {"note": "whole-body lean + head tilt; no limb IK"},
    "flat": {"bob": 6, "squash": 0.0, "zoom": 1.1}
  },
  "occasions": ["valentines", "anniversary", "wedding"],
  "ar_trigger": "scan card → play on table",
  "pet_notes": "nuzzle variant: noses touch, tails wag (manual tail bone — auto-rig skips tails)"
}
```

Bind rules: rigid (everything incl. pets/objects — position/rotation/scale keys,
no rig needed); humanoid (named bones when present, else rigid fallback);
quadruped (Meshy webapp rig ~30s manual click per pet; body + legs, NO tail/facial —
tail wag and jaw talk are manual bones or 2.5D overlay); flat/2.5D (collapses to
bob/squash/zoom + audio for cards and video; already shipped in talk.py).

## 10 starter actions

| # | Action | Roles | Dur | Audio | Camera | Pet notes (honest) |
|---|---|---|---|---|---|---|
| 1 | `kiss` | pair | 4s | smooch/song | slow push-in | nuzzle: noses touch, tails wag (manual) |
| 2 | `hug` → `nuzzle` | pair/group | 4s | warm sting | medium | pets nuzzle, don't hug — heads press, bodies lean |
| 3 | `wave` → `wiggle` | solo | 3s | greeting line | static | whole-body wiggle + tail (manual); reads as waving |
| 4 | `dance` | any | 8s | music bed | wide, slight orbit | bounce + spin; quadruped presets exist in library |
| 5 | `take-turns` | pair | 15–30s | roast script A/B | shot/reverse-shot | 2.5D heads + alternating audio (shipped pattern) |
| 6 | `bow` | solo | 3s | applause | low angle | front-leg bow / head dip; reads fine rigid |
| 7 | `celebrate` | any | 5s | cheer sfx | pull-back | jump + spin; group sync for crews |
| 8 | `sleep` | solo | loop | lullaby + candle glow | overhead slow drift | curled pose; calm/rest line (parked, not launched) |
| 9 | `present` | solo | 5s | gift sting | side reveal | holds/gives gift (mouth/paw prop point); Xmas/birthday |
| 10 | `walk-in` | solo | 4s | footstep + sting | track-in | enters frame; video intros + AR reveals |

Meshy animation library (600+ presets, free endpoint to list, 3cr each to apply)
covers walk/run/dance/fighting/daily for rigged bodies — map our actions to
their `action_id`s where they exist instead of hand-keying (kiss/hug/nuzzle are
custom; walk/dance/celebrate likely have presets).

## Seasonal mapping (quarterly $5-pack engine)

- Q1 Valentine's/anniversary: `kiss` + `hug` (couples wedge).
- Q2 Father's Day/graduation: `celebrate` + `bow` + `present`.
- Q3 Halloween: custom spooky set (pet villain + howl audio).
- Q4 Christmas: `present` + `celebrate` + family `hug` + Santa-hat theme skins.
Same avatars, new action pack each quarter. Build the machine once, reskin quarterly.

## Credit map (pets, verified)

Mesh 30cr (multi-image, download all) + webapp quadruped rig ~30s manual
(same 5cr class as API rig; confirm in-app) + anims 3cr each from the 600+
library. Talking stays 2.5D + edge_tts (no Meshy facial path for animals;
tails also manual). Rig once per pet, reuse across all actions forever.
