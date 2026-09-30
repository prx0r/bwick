# BUILD NOTES — 2026-09-29 Update

> **STATUS: CURRENT** — Session build state.
> 
> Do not delete this file.

## What's Built (runs today)

### PogPet Etsy Store
- **Shop:** PogPet (ID: 67863887)
- **6 draft listings** created via Etsy API
- **Shipping profile** configured (Free Shipping US)
- **Processing profile** set (made_to_order)
- **Status:** DRAFT — needs photos, videos, then publish

### Card Template System
- **10 PogPet templates** (5 Christmas, 3 birthday, 2 general)
- **Card generation API** — photo + template → 1500x2100 PNG
- **Card Studio** — existing bwick roast templates (20) still work
- **Prodigi integration** — sandbox mode ready, needs API key

### Video Prompts
- **Brick Figure** — Human → brick → costume cycling (15s)
- **Pet Bauble** — Puppy → chibi figurine → on tree (15s)
- **Couple Brick** — Two people → brick couple (15s)
- **Tested on:** H3 Max Turbo, Flux 3 Draft, Wan 3

## What's Specced But Not Built

### Production Line (needs Meshy API key)
1. Meshy Creative Lab → generate chibi figures
2. Blender → add hook loops to ornaments
3. Makr3D/3D Vikings → print and ship

### Agent Interface (agents.pog.pet)
1. Conversational card/figure generator
2. Template selection via chat
3. Photo upload → mesh → preview → order

### Platform (pog.town)
1. User profiles with stored meshes
2. Community gallery
3. Creator tools

## Blockers

1. **Prodigi API key** — needed for card/sticker/wrapping paper fulfilment
2. **Meshy API key** — needed for 3D figure generation
3. **Makr3D account** — needed for sample order
4. **Etsy token refresh** — access tokens expire hourly

## Next Build Steps

1. Get Prodigi API key → test card order
2. Get Meshy API key → generate first figure
3. Order sample from Makr3D
4. Create Prodigi mockups for listings
5. Add photos to Etsy listings → publish
