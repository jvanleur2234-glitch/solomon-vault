# ACTIVE_CONTEXT.md — What's Happening Right Now
**Last updated:** 2026-04-29

---

## What We Are Doing

**JCPaid — AI Employee Agency**
Positioning: We find local businesses (real estate, HVAC, contractors), set them up with AI employees using Sauna.ai as the infrastructure, charge $500/mo flat, manage everything.

**THE PIVOT: Stop building. Start connecting.**
We are NOT building AI products from scratch. We are:
1. Finding great AI platforms (Sauna.ai, Naive.ai)
2. Connecting them to local businesses who need them
3. Pocketing the margin as the "AI agency layer"

**THE OFFER**
"Anything you hate doing — we automate it with AI. Flat $500/month. Cancel anytime."

---

## Page Built This Session

**JCPaid Landing Page** — https://josephv.zo.space/jcpaid
- Sells "AI Employee Agency" — flat $500/mo, cancel anytime
- Department selector: Sales ($500), Marketing ($500), HR ($400), IT ($400), Finance ($400), Support ($500)
- Bundle pricing: 2 = $900, 3 = $1,300, all 6 = $2,200
- Pain point capture form → contact form with business type, phone, email, biggest pain point
- 3-step process: Book → We build → AI works

---

## What's Working Right Now

- ✅ JCPaid landing page live at /jcpaid
- ✅ Channel partner model confirmed — use Sauna.ai as infrastructure
- ✅ Department packaging model — sell multiple AI employees per client

---

## What's NOT Working / Deprioritized

- ❌ Hermes — broken/down, don't rely on it
- ❌ CashClaw — shelved
- ❌ All 40 forked repos — ignore unless needed
- ❌ RD reports — stop researching, start building
- ❌ HVAC leads / Jon / EZ Heating — NOT the focus anymore

---

## JCPaid Revenue Model

| Clients | Revenue | Cost (Sauna ~$320/mo) | Profit |
|---------|---------|------------------------|--------|
| 1 | $500 | $320 | $180 |
| 5 | $2,500 | $1,600 | $900 |
| 10 | $5,000 | $3,200 | $1,800 |
| 25 | $12,500 | $8,000 | $4,500 |

---

## Priority Actions

1. **Sign up for Sauna.ai** with LAUNCH code (sauna.ai) — $80 free credits
2. **Test with Jack Vanleur** (JackConnect) — first real estate client. Set up AI employee for him.
3. **Share JCPaid landing page** — https://josephv.zo.space/jcpaid
4. **Document the setup process** — turn into template for future clients

---

## What NOT To Bring Up

- HVAC Lead Machine (replaced by JCPaid)
- CashClaw
- Hermes (down)
- 40 forked repos
- Old business ideas unless Joseph asks

---

## ONE RULE

**Read this file before doing ANYTHING else.**

If Joseph says "READ THE FILE" — stop and read this file first.

If it's not in here, it's not happening. No guessing, no assuming.

---

## REAL WORLD VALIDATION: David Roberts ($recap_david) — $2,000/mo with Paperclip AI
- 4 AI agents: CEO + Growth Engineer + Content Director + Sales Director
- 6,662 subscriber local newsletter, 47.5% open rate (2x industry average)
- Local newsletters: Naptown Scoop $320K/yr, Wichita Life 6 figures
- Offering FREE Paperclip company export to clone
- JCPaid play: same model for local service businesses (HVAC, real estate, etc.)
- Source: https://x.com/dotta/status/2049490085268111555

---

## Infrastructure Stack (CONFIRMED THIS SESSION)

| Tool | Purpose | Status |
|---|---|---|
| **Paperclip** | AI company orchestration (org chart, tasks, budgets) | Clone at paperclipai/paperclip |
| **hermes-paperclip-adapter** | Run Hermes as Paperclip employee | Clone at NousResearch/hermes-paperclip-adapter (1K stars, MIT) |
| **Hermes Workspace** | Native web UI for Hermes (profiles, knowledge browser, skills hub, MCP settings) | Released Apr 29/30, 2026 |
| **Hermes Agent** | AI employee with 30+ tools, persistent memory, 80+ skills | MIT license, NousResearch |
| **Sauna.ai** | Fallback / optional additional AI layer | $80/wk |

**Stack flow:**
```
JCPaid Client → Paperclip (company) → hermes-paperclip-adapter → Hermes (employee) → Hermes Workspace (web dashboard)
```

**Why this beats competition:**
- Hermes has 80+ skills, persistent memory, session persistence, 30+ native tools
- Paperclip handles org chart, cost tracking, task assignment
- Hermes Workspace gives clients a web dashboard (no CLI needed)
- hermes-paperclip-adapter bridges both — reports cost/time back to Paperclip
- Fully open source, MIT license — ZERO per-seat licensing costs
- 8 inference providers: Anthropic, OpenRouter, OpenAI, Nous, OpenAI Codex, ZAI, Kimi Coding, MiniMax

**Why this beats Sauna for our model:**
- Self-hosted = no per-user SaaS fees
- MIT license = we own the deployment
- Client sees a professional web dashboard
- We pocket 100% of the margin

**THE MONEY MODEL (CONFIRMED)**
- Each client: $299/mo
- Your cost: ~$0 (CPU already paid on Zo Computer)
- 20 clients = $5,980/mo
- MoClaw charges clients = you keep nothing
- YOUR Zo Computer hosts = you keep 100%

**Multi-client isolation needed:** Client API keys, data sandboxing, single dashboard.