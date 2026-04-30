# RD REPORT: Paperclip Newsletter Blueprint
**Date:** 2026-04-30
**Source:** https://x.com/dotta/status/2049490085268111555 (via recap_david)
**Type:** Real-world validation + workflow analysis
**Recommendation:** FORGE — Clone this model for JCPaid client vertical

---

## WHAT IT IS

David Roberts (@recap_david) built a zero-person AI newsletter business (Spokane Pulse) generating **$2,000+/month** using Paperclip AI as the orchestration layer. He's offering a free Paperclip company export to clone.

---

## THE PROOF

| Metric | Value |
|---|---|
| Monthly Revenue | $2,000+ |
| Subscribers | 6,662 |
| Open Rate | 47.5% (2x industry avg) |
| Click-through Rate | ~11% |
| Hours/week David spends | < 4 hours |

**Comparable local newsletters:**
- Naptown Scoop: $320K/year
- Wichita Life: 6 figures
- Model works in EVERY city

---

## THE PAPERCLIP ORG CHART

```
CEO (Cloud Code / Claude Code)
  ├── Content Director (writes newsletter, curates events)
  ├── Sales Director (handles ad inquiries, creates ad creative)
  └── Growth Engineer (web scraping, data pipelines, integrations)
```

---

## THE WORKFLOW (Paperclip Routines)

**Content Director's Weekly Routine:**
- Every Wednesday 4pm → scrapes local news/events → writes Thursday newsletter
- Uses custom skill ("Spokane Pulse Thursday") with editorial rules, voice/tone guidelines
- Output: Markdown document → copy-paste into Beehiiv

**Sales Director's Routine:**
- Monitors "Advertise With Us" form submissions
- Emails lead, negotiates, presents ad packages
- Uses Nano Banana API to generate ad images (headline + image + body + CTA)

**Growth Engineer's Routine:**
- Scrapes local news, Reddit, city event pages → builds JSON database
- Builds integrations (Beehiiv, Instagram, ad platforms)
- Handles any technical connective tissue

---

## TOOLS STACK

| Tool | Purpose |
|---|---|
| **Paperclip AI** | Agent orchestration, org chart, routines, skills |
| **Claude Code** (via Cloud Code) | LLM powering the CEO agent |
| **Beehiiv** | Newsletter hosting, subscriber management, website |
| **Nano Banana** | AI ad image generation (API for creative) |
| **Reddit** | Local event/content scraping |
| **Instagram** | Social posts for weekend event roundups |
| **Local news sites** | Content sourcing |

---

## HOW TO CLONE IT FOR JCPAID

The model is directly transferable to local service businesses:

**Instead of newsletter → client service business**
- HVAC shop: Growth Engineer scrapes local listings/reviews, Content Director sends weekly update emails, Sales Director handles quote requests
- Real estate: Growth Engineer scrapes MLS listings, Content Director writes weekly market update, Sales Director follows up on leads
- Restaurant: Growth Engineer scrapes reviews/events, Content Director manages social media, Sales Director handles reservation inquiries

**Key insight:** David uses the CEO agent as the client interface. The CEO receives goals from David and fans out to team. This is exactly how JCPaid would work — Joseph (or client) gives CEO goals, CEO delegates to AI employees.

---

## PAPERCLIP FEATURES DEMONSTRATED

1. **Org Chart** — visual hierarchy of AI agents
2. **Skills** — custom prompt packages per agent (e.g., "Spokane Pulse Thursday" skill)
3. **Routines** — cron jobs scheduled for recurring tasks
4. **Inbox** — issue tracking with agent comments and outputs
5. **Documents** — agents produce documents (Markdown newsletters) as output
6. **Parallel execution** — multiple agents working simultaneously
7. **Approval workflow** — CEO creates approval items for human review
8. **Company export/import** — JSON file containing full company setup to clone

---

## WHAT THIS VALIDATES FOR JCP AID

✅ **The model works** — $2K/mo proof with zero human employees
✅ **Paperclip is production-ready** — used in real business, not demo
✅ **MIT license** — we can clone and white-label the company structure
✅ **Skills system** — exactly what we need for vertical-specific AI employees
✅ **Routines (cron)** — automated recurring work without manual triggering
✅ **Parallel agents** — each agent has specific role, no context bloat
✅ **Human-in-loop** — approval items, feedback loop, skill refinement over time

---

## ACTION FOR JCP AID

1. Download David's free Paperclip export (from his Skool community)
2. Import into Paperclip to see full agent setup
3. Clone the company structure for JCPaid's first client vertical (HVAC or real estate)
4. Swap "newsletter" skills for industry-specific skills (e.g., HVAC maintenance, real estate listings)
5. Use as the demo/template when pitching JCPaid to local businesses

---

## COMPETITIVE Advantage vs Naive/Zenflow

This is EXACTLY what Naive AI does ($310/mo) but:
- We use Paperclip (MIT, self-hosted) + Hermes (MIT) instead of paying $310/mo
- We add our management layer and sell to local businesses who don't know Paperclip exists
- We pocket the margin: $500/client - $0 infrastructure = $500 pure profit

**The moat:** Not the AI tool — the client relationship + industry-specific skills + management.