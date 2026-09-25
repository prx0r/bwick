# FunnyLabs / Roast.pet

> "Make agents actually funny."

## What Is This

A humour module that powers:

1. **MCP Server** — 6 tools Muse/ChatGPT can call to generate funny pet cards
2. **Consumer Website** — studio.roast.pet where users upload pets, browse templates, buy cards
3. **FunnyLabs** — research/learning loop for what makes comedy work

## Architecture

```
Same Engine (jokes + templates + render + Prodigi)
├── MCP Server (6 tools) → Muse/ChatGPT
├── studio.roast.pet → consumer website (Cloudflare Worker)
└── FunnyLabs → experiments + social R&D
```

## What's Where

```
funnylabs/
├── humour_mcp/              # Core engine
│   ├── mcp_server.py        # MCP server — 6 tools
│   ├── jokes.py             # Joke pools per template
│   ├── templates.py         # 20 template definitions
│   ├── jev.py               # Post-generation ranking
│   └── render.py            # Satori + resvg card renderer
├── core/                    # Receipt chain (from content-sensor)
│   ├── receipt.py           # Hash-chained audit log
│   ├── proof.py             # Immutable source evidence
│   ├── gates.py             # Freshness + no-duplicate + claim-resolved
│   ├── processor.py         # Bounded computation
│   └── artifact.py          # Output with proof chain
├── renderer/                # Print-ready card rendering
│   ├── render-card.mjs      # Satori → SVG → resvg → PNG (1748x2480, A5)
│   └── prodigi.mjs          # Prodigi REST v4 API integration
├── fonts/                   # Inter TTF (Regular, Bold, Black)
├── worker/                  # Cloudflare Worker for studio.roast.pet
│   ├── src/index.ts         # Worker: API routes + SVG card renderer
│   ├── src/templates.ts     # Template definitions (TS)
│   ├── src/jokes.ts         # Joke pools (TS)
│   └── static/index.html    # Consumer website
├── pi-extension/            # MCP-to-pi bridge
├── card-studio/             # Local dev server (Python)
├── brand/                   # Audio brand kit
└── docs/                    # Thesis + dev plans
```

## Quick Start

### MCP Server (for Muse/ChatGPT)
```bash
python3 humour_mcp/mcp_server.py funny.create_card '{"recipient_name":"James","occasion":"christmas","facts":["AGI obsessive"],"roast_level":"savage","pet_name":"Max","pet_species":"dog"}'
```

### Consumer Website (live)
https://studio.roast.pet

### Local Dev Server
```bash
DASH_TOKEN=studio python3 card-studio/server.py
# http://localhost:8792/?token=studio
```

### Card Renderer (print-ready PNG)
```bash
node renderer/test-render.mjs
```

## MCP Tools

| Tool | Description |
|------|-------------|
| `funny.list_templates` | List 20 card templates |
| `funny.create_concepts` | Generate 3-5 joke candidates |
| `funny.preview_card` | Render card HTML/SVG |
| `funny.quote_card` | Prodigi price quote |
| `funny.order_card` | Place Prodigi order |
| `funny.create_card` | High-level: generate → rank → render → quote |

## Templates (20)

**Core (10):** thought_bubble, pet_standup, breaking_news, performance_review, pet_therapist, search_history, complaint_dept, split_panel, incident_report, wildcard

**Christmas (10):** xmas_santa_automated, xmas_santa_vs_robots, xmas_elf_redundancy, xmas_pet_security, xmas_performance_review, xmas_human_vs_pet, xmas_cat_vs_tree, xmas_santa_search_history, xmas_ai_card, xmas_pet_complaint

## Deployed

- **studio.roast.pet** — Cloudflare Worker on roast.pet domain
- **MCP server** — stdio mode for Muse/ChatGPT integration

## Vault Keys

- `OPENCODE_API_KEY` — pi agent (opencode-go/mimo-v2.5)
- `CLOUDFLARE_WORKERS_TOKEN` — Cloudflare Workers deploys
- `CLOUDFLARE_API_TOKEN` — DNS + zones
- No Prodigi/Etsy keys yet — use sandbox/stubs

## Next Steps

1. Wire Prodigi API for real order fulfilment
2. Add Etsy integration for discovery/checkout
3. Add real pet photo compositing (Sharp)
4. FunnyLabs experiments (social R&D)
5. Muse MCP integration
