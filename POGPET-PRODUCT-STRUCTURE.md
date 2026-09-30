# PogPet Product Structure

> **Status:** Blueprint for pog.pet website
> 
> Mirrors Etsy store + adds preview/customization features

## Core Concept

```
User uploads photo
    ↓
Meshy generates mesh (3D)
    ↓
Mesh stored in user profile
    ↓
User sees mesh as:
├── Brick Figure (3D printed)
├── Pet Ornament (3D printed)
├── Couple Figure (if 2 photos)
├── Keychain (3D printed)
├── Wrapping Paper (2D render)
├── Sticker Pack (2D render)
├── Greeting Card (2D render)
└── Video (animated mesh)
```

## Product Tiers

### Tier 1: Core Products (3D printed)
| Product | Price | Meshy Template | Production |
|---------|-------|---------------|------------|
| Brick Figure | $19.99 | brick-figure | Makr3D/Vikings |
| Couple Figure | $34.99 | brick-figure (x2) | Makr3D/Vikings |
| Pet Ornament | $14.99 | brick-figure + loop | Makr3D/Vikings |
| Keychain | $12.99 | keychain | Makr3D/Vikings |

### Tier 2: Matching Add-Ons (2D print via Prodigi)
| Product | Price | Source | Add-On To |
|---------|-------|--------|-----------|
| Wrapping Paper | $8.99 | Prodigi | Any core product |
| Sticker Pack | $4.99 | Prodigi | Any core product |
| Greeting Card | $3.99 | Prodigi | Any core product |
| Christmas Card | $5.99 | Prodigi | Any core product |

### Tier 3: Bundles
| Bundle | Products | Price | Savings |
|--------|----------|-------|---------|
| Starter | Figure + Keychain | $27.99 | Save $5 |
| Christmas | Ornament + Card + Stickers | $22.99 | Save $6 |
| Ultimate | Figure + Keychain + Ornament + Stickers | $36.99 | Save $10 |

## User Flow (pog.pet)

### Upload Flow
```
1. User lands on pog.pet
2. "Upload your pet" CTA
3. Google sign-in (required)
4. Drag & drop photo (max 10MB, JPEG/PNG)
5. Photo uploads to R2
6. Meshy API generates mesh
7. Mesh stored in user profile
8. User redirected to preview page
```

### Preview Flow
```
1. User sees 3D viewer with their mesh
2. Below viewer: product cards
   ├── "Brick Figure — $19.99" → shows mesh as figure
   ├── "Pet Ornament — $14.99" → shows mesh as ornament
   ├── "Keychain — $12.99" → shows mesh as keychain
   ├── "Wrapping Paper — $8.99" → shows pattern preview
   ├── "Sticker Pack — $4.99" → shows sticker sheet preview
   └── "Greeting Card — $3.99" → shows card preview
3. User selects products
4. Add to cart → Stripe checkout
```

### Data Model
```sql
User
  id, email, name, image, createdAt

Photo
  id, userId, r2Url, createdAt

Mesh
  id, userId, photoId, meshyTaskId, glbUrl, thumbnailUrl, createdAt

Product
  id, name, price, description, category, meshRequired

Order
  id, userId, stripeSessionId, status, items JSON, createdAt

CartItem
  id, userId, productId, meshId, quantity, createdAt
```

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `POST /api/upload` | POST | Upload photo → R2 → Meshy → store mesh |
| `GET /api/mesh/:id` | GET | Get mesh details + thumbnails |
| `GET /api/products` | GET | List all products |
| `POST /api/cart/add` | POST | Add product + mesh to cart |
| `POST /api/checkout` | POST | Create Stripe session |
| `POST /api/webhook` | POST | Stripe webhook → fulfill order |

## Fulfillment Routing

```python
def fulfill_order(order):
    for item in order.items:
        if item.product.category == "3d_printed":
            # Route to Makr3D (UK) or 3D Vikings (US)
            send_to_makr3d(item.mesh.stl_url, item.shipping_address)
        elif item.product.category == "flat_print":
            # Route to Prodigi
            send_to_prodigi(item.design_url, item.sku, item.shipping_address)
```

## Preview Rendering (per product)

| Product | How Preview Works |
|---------|------------------|
| Brick Figure | Load GLB in three.js viewer |
| Pet Ornament | Load GLB with loop, show on tree |
| Keychain | Load GLB with chain, show on keys |
| Wrapping Paper | Render mesh → tile into pattern → show on roll |
| Sticker Pack | Render mesh → 8 expressions → show on sheet |
| Greeting Card | Render mesh → place on card front → show card |

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Next.js + three.js (3D viewer) |
| Backend | Next.js API routes |
| Auth | NextAuth.js (Google OAuth) |
| 3D Storage | Cloudflare R2 |
| 3D Generation | Meshy API |
| Payments | Stripe |
| Fulfillment | Makr3D + Prodigi APIs |
| Database | SQLite (Prisma) or Supabase |
