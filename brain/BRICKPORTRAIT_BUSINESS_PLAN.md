# BrickPortrait — AI-Powered Custom Lego Family Portrait Business

> Upload a photo. Get a real Lego set designed just for your family. Ships to your door.

---

## THE BIG IDEA

A family uploads a photo → AI designs a custom Lego mosaic/portrait → we source the bricks and ship them with instructions. Customers get a tangible, emotional piece of art they actually build themselves.

**Why this works:**
- Emotional product = high willingness to pay
- AI makes it scalable (no manual design work)
- Lego is a $28B global brand with 90%+ brand awareness
- Custom Lego is a proven niche (BrickLink designers sell MOCs for $20-500+)
- No inventory, no manufacturing — just AI + sourcing + shipping

---

## THE STACK

| Layer | Tool | Cost |
|-------|------|------|
| AI Design | LegoGPT (Carnegie Mellon, open source, free) | $0 |
| Design Generation | Custom prompt chain (Claude/GPT-4o) | ~$0.05/face |
| Brick Sourcing | BrickLink API + Pick a Brick (Lego's own store) | $0.05-0.12/piece |
| Ordering | Automated Python script against BrickLink API | $0 labor |
| Website | Zo Space page + Stripe checkout | $0 |
| Shipping | Third-party logistics (we hold no inventory) | $12-25/set |

---

## PRICING & MARGINS

### Tier 1: Standard BrickPortrait (8x10 inch, ~400-600 pieces)
- **Price:** $99
- **Parts cost:** ~$45-60 (sourced from BrickLink/Pick a Brick)
- **Shipping:** ~$15 domestic
- **AI design labor:** ~$0.05 (negligible)
- **Gross margin:** ~$24-39 (24-39%)

### Tier 2: Large BrickPortrait (16x20 inch, ~800-1200 pieces)
- **Price:** $179
- **Parts cost:** ~$80-120
- **Shipping:** ~$20
- **Gross margin:** ~$39-79 (22-44%)

### Tier 3: Premium Family Scene (complex, 1500+ pieces, multiple figures)
- **Price:** $299
- **Parts cost:** ~$130-180
- **Shipping:** ~$25
- **Gross margin:** ~$89-144 (30-48%)

**Note:** Parts costs drop significantly at scale (buying in bulk from single sellers reduces shipping overhead). At 50+ orders/month, parts cost could drop 20-30%.

---

## HOW IT WORKS (CUSTOMER FLOW)

1. **Upload photo** → customer goes to website, uploads a photo of their family (or pet, wedding, etc.)
2. **AI analysis** → we use GPT-4o Vision to identify the subjects, colors, composition
3. **Design prompt** → feed that into LegoGPT (or our own stable diffusion fine-tune) to generate the brick layout
4. **Brick list generated** → Python script converts the layout into a BrickLink-compatible parts list
5. **Auto-order** → script submits order to BrickLink seller with best pricing + inventory
6. **Quality check** → parts arrive at our fulfillment partner (or home address)
7. **Instruction booklet** → we generate step-by-step PDF instructions using the parts map
8. **Ship** → box goes to customer with parts + instructions + a small "build kit" gift
9. **Review loop** → request photo of the completed build for testimonials

---

## KEY TECHNICAL PIECES TO BUILD

### 1. Image-to-Lego Pipeline (The Core IP)
- **Input:** Photo upload
- **Process:** GPT-4o Vision → extract subjects, colors, scene → LegoGPT prompt → stable brick design
- **Output:** Parts list (CSV) + visual preview + step-by-step instructions
- **Tools:** LegoGPT (open source), GPT-4o Vision, Python PIL for color mapping
- **Time to build:** 2-3 weeks

### 2. BrickLink Auto-Sourcing Script
- **Function:** Take parts list → find cheapest sellers for each brick → auto-generate cart → checkout
- **BrickLink API:** REST-based, requires authentication
- **Challenge:** BrickLink doesn't have a public bulk buy API — may need to scrape or use their XML API
- **Alternative:** Use Pick a Brick (Lego's official service) — cleaner API, fixed pricing, ships from Lego directly
- **Time to build:** 1-2 weeks

### 3. Customer-Facing Website (Zo Space)
- Photo upload form
- Design preview (what the Lego version will look like)
- Stripe payment integration ($99, $179, $299 tiers)
- Email confirmation + build progress updates
- **Time to build:** 1 week

### 4. Fulfillment / Shipping
- **Option A (DIY):** Parts ship to Joseph's address → he repacks and ships
- **Option B (Third-party):** Use a 3PL like ShipBob or a fulfillment service
- **Option C (Dropship):** BrickLink sellers ship direct to customer (requires coordinating multiple sellers — complex)
- **Recommendation:** Option A at launch (keeps it simple, 10-20 orders/month manageable), migrate to 3PL at 30+/month

---

## COMPETITION CHECK

| Competitor | Price | Weakness |
|------------|-------|----------|
| Lego Mosaic Maker (official Lego service) | $60-200 | Limited customization, only works with select photos |
| BrickHazard (Etsy) | $80-300 | Manual design, slow turnaround |
| Print-a-Pixel | $40-150 | Canvas/poster, not real Lego |
| Custom BrickBros (Instagram) | $150-500 | Manual, expensive, one-person operation |

**Our advantage:** AI-powered speed + automated sourcing = lower price than competitors AND faster turnaround. We're the "AI-first" version of a manual craft business.

---

## FINANCIAL PROJECTIONS

### Launch Phase (Month 1-2): 5 orders/month
- Revenue: 5 × $99 = $495
- COGS: 5 × $65 = $325
- Time: ~3-4 hrs/order (Joseph's time — mostly me running automation)
- Net: ~$170/month (Joseph's time is the real bottleneck)

### Growth Phase (Month 3-6): 15 orders/month
- Revenue: 15 × $99 = $1,485
- COGS: 15 × $55 (bulk discount) = $825
- Time: ~1 hr/order (automation handles most of it)
- Net: ~$660/month

### Scale Phase (Month 7-12): 40 orders/month
- Revenue: 40 × $99 = $3,960/month (or upsell to $179 = $7,160)
- COGS: 40 × $48 (volume discount) = $1,920
- Fulfillment labor: ~$400/month (part-time help)
- Net: ~$1,640-$5,240/month

---

## WHAT I (Zo) CAN DO RIGHT NOW

✅ Design the website page (Zo Space)
✅ Build the AI image-to-brick prompt pipeline
✅ Write the BrickLink/Pick a Brick ordering script
✅ Set up Stripe payment links for each tier
✅ Generate the instruction PDFs
✅ Handle all customer communication via Gmail

## WHAT JOSEPH NEEDS TO DO

🤝 Approve designs that are borderline (AI occasionally generates weird Lego faces)
📦 Receive brick shipments and repack/ship (Phase 1)
📸 Take photos of builds for social proof

---

## FIRST STEPS TO LAUNCH

1. **This week:** I build the Zo Space landing page with photo upload form
2. **Week 2:** I build the AI design pipeline (LegoGPT + GPT-4o Vision)
3. **Week 3:** I build the BrickLink ordering script
4. **Week 4:** We do 3 test builds (Joseph's family photo, 2 friends)
5. **Week 5:** Soft launch — Stripe live, first real customers

---

## RISKS & MITIGATIONS

| Risk | Mitigation |
|------|------------|
| BrickLink parts out of stock | Use Pick a Brick (Lego direct) as backup |
| LegoGPT design quality poor | Human review step before ordering |
| Customer builds wrong thing | Clear instructions + video tutorial |
| Shipping damage | Bubble wrap + instruction card in box |
| No demand | Pre-sell 5 orders at discount to validate |

---

*Plan written by Zo Computer — Solomon OS, April 27, 2026*
*Business name: BrickPortrait | Domain: josephv.zo.space/brickportrait (pending)*