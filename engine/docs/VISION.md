# Vision — FunnyLabs / Roast.pet

## The One-Liner

> FunnyLabs learns what humans actually find funny; the Humour Module
> packages that learning for agents; Roast.pet proves it by turning
> personal context and a pet into genuinely funny personalised gifts
> through Muse and existing commerce/fulfilment rails.

---

## Phase 1: Cards That Ship (NOW)

**Status:** MVP live at studio.roast.pet

What exists:
- 20 card templates (10 core + 10 Christmas)
- MCP server with 6 tools
- Consumer website with upload → browse → buy flow
- Prodigi integration stubs
- Receipt chain audit trail

What's next:
- Wire real Prodigi API for order fulfilment
- Add real pet photo compositing (Sharp)
- Add Etsy listings for discovery/checkout
- First paid order

**Success metric:** Someone discovers a card → uploads pet → pays → card ships → they share it.

---

## Phase 2: Muse Integration

**Goal:** Muse users can generate funny cards without leaving chat.

Flow:
1. User: "Make James a Christmas card about AI. Use my dog Max."
2. Muse calls `funny.create_concepts` → 3 joke options
3. User picks one
4. Muse calls `funny.preview_card` → card preview
5. User approves
6. Muse calls `funny.order_card` → Prodigi ships

The MCP is the reusable brain. Muse, ChatGPT, and the website are all consumers.

---

## Phase 3: Jev Routing

**Goal:** Cheap, fast, typed decisions after joke generation.

Jev doesn't write jokes. Jev decides:
- Which template fits this context?
- Which of 5 candidates is most relevant?
- Is this topical reference likely to land?
- Mild / roast / savage?
- Card / shirt / digital?
- Does the joke depend too much on context?
- Does it feel generic?
- Should we use current news or evergreen?

When confidence is high → route automatically.
When confidence is low → show multiple options.

---

## Phase 4: The Social Loop

**Goal:** Learn what actually makes people laugh.

```
Social joke test
→ winner identified
→ convert into card template
→ sell static version
→ sell personalised version
→ measure purchases
→ feed result back into FunnyLabs
```

And the reverse:
```
Personalised card format sells well
→ turn it into recurring social bit
→ test characters/topics
→ generate more variants
```

Social content is not a side hobby. It is the cheapest high-volume test bench for humour structures.

---

## Phase 5: FunnyLabs Research

**Goal:** Build the learning system.

Controlled experiments:
- **Same joke, different character** — does a depressed dog funnier than a corporate CEO?
- **Same character, different joke structure** — which structures work for which persona?
- **Same material, different delivery** — voice, pacing, visual staging
- **Same template, different personalization depth** — generic / name / one fact / rich context
- **Same structure, topical vs evergreen** — decay curves, share rates

Metrics:
- purchase (strongest signal)
- share
- replay
- comment quoting the joke
- completion
- follow
- like
- impression (weakest)

Do not collapse to one "funny score" initially. Different behaviours may represent different kinds of humour.

---

## Phase 6: Synthetic Comedians (Pogtown)

**Goal:** Persistent characters with stable identities.

Each comedian has:
- stable identity, visual form, voice
- worldview, comedy style, recurring topics
- boundaries, immutable version history

```
comedian_id: depressed_dog
version: 4
style: dry, low-energy, self-deprecating, observational
devices: deadpan, understatement, callbacks
topics: owners, food, AGI, work
```

Update versions based on real performance.
Do not silently mutate a character.
Keep v1, v2, v3... so you can measure improvement.

---

## Phase 7: Commerce Expansion

**Goal:** Same engine, multiple surfaces.

```
Engine (jokes + templates + render + commerce)
├── MCP Server → Muse/ChatGPT
├── studio.roast.pet → consumer website
├── Etsy → discovery/checkout
├── Moonpig → connector
├── Printify → connector
├── Social → avatars, stand-up, shorts
└── FunnyLabs → research loop
```

Each new surface is an adapter over the same core.

Product expansion:
- Cards (now)
- T-shirts
- Mugs
- Posters
- Digital cards
- Social videos
- AI stand-up clips

---

## Phase 8: The Moat

The moat is NOT a custom editor.

The moat is:
- **Persistent Pog identity** — characters that accumulate personality
- **Humour context** — what this user actually laughs at
- **Performance history** — which templates/structures win
- **Product templates** — constrained, not freeform
- **Agent-accessible commerce flow** — MCP-first
- **Physical + digital reveal loop** — QR on card opens video/AR
- **Learning loop** — every purchase improves ranking

The editor and fulfilment engines are replaceable infrastructure.

---

## The North Star

> Make agents actually funny.

Not "make funny AI cards."
Not "build an AI print-on-demand company."
Not "create a generic Etsy automation tool."

Become the place that is actually funny.

Roast.pet is the first commercial surface.
Muse is the interface.
Prodigi is the factory.
The renderer is disposable infrastructure.
FunnyLabs eventually supplies the learning loop.

The first job is simply:

**MAKE TEN CARDS THAT ARE GENUINELY FUNNY AND GET THEM LIVE.**

Then let the system grow outward from proof.
