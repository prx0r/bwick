# HANDOVER — FunnyLabs / Roast.pet

## Status

MVP is live. Consumer website deployed. MCP server working. 20 card templates.

## What Exists Today

### Live at studio.roast.pet
- Upload pet photo → see it in all 20 card templates
- Each card shows real joke content with distinct visual designs
- Click any card → modal with full preview + joke + price
- Download as PNG (html2canvas)
- Order button (sandbox — Prodigi stub)

### MCP Server (6 tools)
- `funny.list_templates` — returns 20 templates
- `funny.create_concepts` — generates joke candidates
- `funny.preview_card` — renders card SVG
- `funny.quote_card` — Prodigi price quote
- `funny.order_card` — places Prodigi order
- `funny.create_card` — high-level pipeline

### Card Rendering
- HTML/CSS cards (live website)
- Satori + resvg + Sharp pipeline (print-ready PNG, 1748x2480, A5 @ 300 DPI)
- Fonts: Inter TTF at /root/funnylabs/fonts/

### Receipt Chain
- Hash-chained append-only JSONL
- Every generate + render logged
- Verifiable with `funny.verify_chain`

## What Doesn't Work Yet

1. **Real pet photo compositing** — SVG/HTML shows paw emoji placeholder. Need Sharp to composite uploaded photos into card templates.
2. **Prodigi integration** — Sandbox stubs only. Need real API key and order flow.
3. **Etsy integration** — No listing/checkout flow yet.
4. **MCP-to-pi bridge** — Pi agent not installed on this box. Fallback dispatch works but no real LLM routing.
5. **FunnyLabs experiments** — No social R&D loop yet.
6. **Inside of card** — Only front is rendered. Inside text not implemented.

## Key Decisions Made

- **HTML/CSS cards** — not custom SVG engine. Simpler, faster, works everywhere.
- **Same engine for MCP + website** — both use humour_mcp/
- **Cloudflare Worker** — studio.roast.pet runs on Workers, not a VPS
- **No framework** — vanilla JS frontend, Python MCP server
- **Satori for print** — when we need actual print-ready PNGs

## How to Run

```bash
# MCP server
python3 humour_mcp/mcp_server.py funny.create_card '{"recipient_name":"James","occasion":"christmas"}'

# Local dev server
DASH_TOKEN=studio python3 card-studio/server.py
# http://localhost:8792/?token=studio

# Deploy website
cd worker && CLOUDFLARE_API_TOKEN=xxx npx wrangler deploy

# Render print card
node renderer/test-render.mjs
```

## File Map

| File | Purpose |
|------|---------|
| `humour_mcp/mcp_server.py` | MCP server entry point |
| `humour_mcp/jokes.py` | Joke pools per template |
| `humour_mcp/templates.py` | 20 template definitions |
| `humour_mcp/jev.py` | Post-generation ranking |
| `renderer/render-card.mjs` | Satori → PNG renderer |
| `renderer/prodigi.mjs` | Prodigi API client |
| `core/receipt.py` | Audit trail |
| `worker/src/index.ts` | Cloudflare Worker |
| `worker/static/index.html` | Consumer website |
| `card-studio/server.py` | Local dev server |

## Email Context

All design decisions came from emails to agents@intelligentothers.xyz:
- Lean Dev Plan — sprint priorities
- 10 Templates + Xmas Pack — template list
- Muse + Jev + MCP — tool surface
- Reuse Design Tech — don't build bespoke editor

## Agent Instructions

If you're picking this up:
1. Read AGENTS.md for project context
2. Read docs/THESIS.md for the full vision
3. Check studio.roast.pet to see current state
4. The MCP server is the reusable brain — both website and Muse use it
5. Don't build a Canva clone — keep templates constrained
6. humour_mcp/ is the core engine — everything else is a consumer
