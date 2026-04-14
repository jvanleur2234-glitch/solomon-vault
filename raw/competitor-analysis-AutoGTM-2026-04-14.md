# Competitive Analysis: AutoGTM vs. Solomon OS
**Date:** April 14, 2026  
**Prepared for:** Joseph V'  
**Status:** 🔴 Critical — Direct competitor to Russell Tuna AI SDR

---

## WHAT IS AUTOGTM?

AutoGTM is a product by **Explee** (Paris-based, ~$120k ARR, 7 employees). It launched April 13, 2026 — days ago.

**The pitch:** Paste your website URL. In 60 seconds, AI reads your site, researches the market, finds high-intent prospects, writes personalized cold emails with follow-up sequences, and books demos.

**Pricing:** $199/mo. 15× cheaper than Apollo/ZoomInfo.

---

## WHAT THEY HAVE vs. WHAT SOLOMON OS HAS

| Capability | AutoGTM | Solomon OS |
|---|---|---|
| Reads client website | ✅ | ✅ (via MarkItDown/Read) |
| Prospect database | 105M companies, 536M people | ❌ |
| Email sending | ✅ (2 pre-warmed mailboxes) | ❌ |
| Sequences + follow-ups | ✅ (1,000 auto-sequences) | ❌ |
| Personalization | ✅ (deep research agent) | ⚠️ (manual) |
| Email deliverability | 97% guarantee | ❌ |
| CRM integration | ✅ | ❌ |
| Calendar integration | ✅ | ❌ |
| Demo booking | ✅ | ❌ |
| 24/7 autonomous operation | ✅ | ⚠️ (Russell Tuna can, but no email pipeline) |
| Cost | $199/mo | Ollama free, but no email |

---

## TECH STACK (WHAT THEY'RE USING)

Based on open-source research and similar systems:

- **Lead data:** Apollo.io or similar for 105M+ company/people profiles
- **Email delivery:** Pre-warmed Google/Microsoft mailboxes with 97% deliverability
- **AI research:** Deep research agent to personalize each email
- **Sequences:** Automated multi-touch follow-up cadences
- **CRM + Calendar:** Native integrations (likely Zapier, API connections)
- **GTM skills:** Likely using GTM agent frameworks (similar to Claygent, cold-email-personalization skills)

**AutoGTM is NOT inventing new tech** — it's wiring together existing APIs and AI agents into a seamless pipeline.

---

## COMPETITIVE LANDSCAPE (BROADER)

Other players in this space:
- **Clay / Claygent** — Enrichment + AI personalization (~$200+/mo)
- **Apollo.io** — Lead data + sequences (~$60-100/mo)
- **Attrible (Aastra AI)** — Agentic GTM orchestration
- **Autonomous SDR Agent** (open-source) — GPT-4o + SendGrid, state-machine outreach
- **GTM Engine** — CRM noise elimination + automated workflows
- **Various GitHub GTM skill packs** — cold-email-personalization, ai-sdr, ai-cold-outreach

---

## THREAT ASSESSMENT

### What's the actual threat?
AutoGTM is selling exactly what Russell Tuna is supposed to become — **a hireable AI SDR**. They're already in market with a polished product. If a prospect searches "AI SDR" or "automated sales agent," they find AutoGTM (or Apollo, Clay, etc.) — not Russell Tuna.

### What are our advantages?
1. **Russell Tuna is free** via Ollama — no per-seat cost
2. **Telegram-native** — easy access, no setup friction
3. **Solomon Bus** — inter-agent orchestration infrastructure exists
4. **Total control** — self-hosted, no vendor lock-in

### What are our gaps?
1. **No prospect database** — 105M companies is not a small gap
2. **No email pipeline** — no warmed mailboxes, no sequences, no deliverability
3. **No CRM integration**
4. **No calendar booking**
5. **No polished UX** — it's a Telegram bot, not a product

---

## STRATEGIC OPTIONS

### Option A: Build the gap (Medium effort, High impact)
Add email outreach capability to Russell Tuna:
1. Connect a prospect database (Apollo.io API, or scrape LinkedIn via Apollo's data)
2. Add email sending via pre-warmed mailboxes (Google Workspace + SMTP)
3. Build sequence automation (follow-up cadences)
4. Add CRM tracking (Notion or Airtable as simple CRM)
5. Integrate calendar booking (Cal.com API)

**Estimated time:** 2-3 weeks of focused work  
**Result:** Russell Tuna becomes a real AutoGTM competitor

### Option B: Differentiate via niche (Low effort)
Don't compete on "AI SDR for everyone." Instead:
- Target faith-based organizations (churches, ministries — a niche AutoGTM won't bother with)
- Target a specific vertical Apollo ignores (e.g., Christian schools, nonprofit organizations)
- Use Solomon OS's religious AI angle as a differentiator

**Estimated time:** 1 week  
**Result:** First-mover in underserved niche

### Option C: Partner / Learn (Low effort)
Study what AutoGTM is doing and either:
- White-label their approach for a specific vertical
- Use their model as inspiration and document what to build for Russell Tuna v2

**Estimated time:** 1 week research  
**Result:** Clear roadmap, potential partnership conversation

### Option D: Reverse-engineer (High effort)
Build the exact AutoGTM stack:
- Clone their workflow using open-source GTM skill packs (Clay, cold-email-personalization, ai-sdr)
- Connect to Apollo + email delivery infrastructure
- Build as a Solomon Bus skill

**Estimated time:** 4-6 weeks  
**Result:** Full AutoGTM competitor

---

## RECOMMENDATION

**Do Option A (Build the gap) in parallel with Option B (Niche focus).**

The gap that matters most: **email pipeline + prospect database.**

The fastest path to a working Russell Tuna v2:
1. Get Apollo.io API key → access 220M+ contacts
2. Set up SMTP email delivery via Google Workspace
3. Build sequence manager in Solomon Bus
4. Connect to Russell Tuna as a new skill: `/find-clients` + `/send-outreach`

This turns Russell Tuna from a "chatbot that can theoretically find clients" into a "AI that actually sends emails and books demos."

---

## FILES TO UPDATE

After building the email pipeline, update:
- `/home/workspace/MegaPlan/HERMES_CAPABILITIES.md`
- `/home/workspace/MegaPlan/SOLOMON_OS.md`
- `/home/workspace/solomon-vault/brain/Business Ideas.md`