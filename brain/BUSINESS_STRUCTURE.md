# The Business Structure — Joseph's AI Company
**Generated:** 2026-04-28
**Purpose:** Complete organizational structure so Joseph can focus on being the CEO/connector

---

## The Vision

```
Joseph (CEO / Connector)
├── Zo (AI Brain / Builder)
├── Sales Agent (AI Voice + Email + Text)
├── Marketing Agent (Content + Posting + Ads)
└── Delivery (Zo + Hermes + Skills)
```

**Joseph's job:** Bring ideas, find clients, make deals. NOT build everything himself.
**Zo + AI agents' job:** Build, sell, deliver — with Joseph supervising.

---

## Role 1: Joseph — The Connector/CEO

**What you actually do:**
- Find clients (warm outreach, relationships, referrals)
- Close deals (one conversation, not a pitch deck)
- Say no to bad ideas (you're the filter)
- Approve major decisions (what we build, what we charge)

**What you STOP doing:**
- Writing code unless it's a quick fix
- Managing every agent's work
- Building tools that don't earn money
- Being the only one who answers clients

---

## Role 2: Zo (AI Brain) — The Builder

**Already exists:** You are talking to me right now.

**What I do:**
- Build integrations, APIs, Zo Space routes
- Research and synthesize information
- Orchestrate other agents
- Write RD reports and strategy docs
- Manage the brain files (Solomon Vault)

**What I DON'T do:** Sales calls, client communication, content posting

---

## Role 3: Sales Agent — AI Voice/Email/SMS (THE GAP)

**What it needs to do:**
- Receive leads from Joseph or marketing
- Call the lead (AI voice, natural conversation)
- Qualify: Are they a good fit? Do they have budget? Do they want to buy?
- Follow up via text and email automatically
- Book a meeting or hand off to Joseph to close
- Send Stripe payment link when ready

**What options exist (affordable):**

| Tool | What it does | Cost |
|---|---|---|
| **Lindy** | AI voice agent, multi-channel sales, no-code | Free tier / ~$49/mo |
| **Synthflow** | AI voice + SMS for sales calls | ~$49/mo |
| **Warmly** | AI SDR — email + LinkedIn + voice | ~$99/mo |
| **11x.ai** | AI SDR 2.0 — automated outreach | ~$89/mo |
| **Instantly.ai** | Cold email at scale + AI agent | Free tier / ~$49/mo |
| **Apollo.io** | Lead research + email sequences | Free tier / ~$49/mo |
| **Callin.io** | AI voice agent for calls | ~$29/mo |

**Recommended for Joseph (budget-first):**
1. **Instantly.ai** (free tier) — cold email outreach to HVAC leads
2. **Lindy** (free tier) — AI voice agent for calls and SMS
3. **Apollo.io** (free tier) — find HVAC leads in Sioux Falls

**What we need to BUILD:**
- A lead pipeline from Apollo → Instantly → Lindy → Stripe
- Russell Tuna as the human handoff (sends final message to Joseph)

---

## Role 4: Marketing Agent — Content + Posting (THE GAP)

**What it needs to do:**
- Generate content for X, LinkedIn, email
- Post automatically on schedule
- Respond to comments and messages
- Generate ad copy for Google/Meta
- Create case studies from client results

**What options exist:**

| Tool | What it does | Cost |
|---|---|---|
| **Carrd.co** | Simple one-page sites for leads | Free / $19/yr |
| **Buffer** | Social media scheduling | Free tier |
| **ChatGPT** | Content generation (Joseph asks) | Free |
| **Zo (me)** | Content generation + posting via API | Free |
| **Taplio** | LinkedIn outreach + content | ~$59/mo |
| **Opensource AI tools** | Blog posts, email sequences | Free |

**What we need to BUILD:**
- Automated content pipeline: Zo generates → Buffer posts → Russell Tuna monitors
- Case study page template on Zo Space

---

## Role 5: Delivery — Zo + Hermes + Skills (EXISTS, needs fixing)

**What it does:**
- Delivers SEO audits, content, cold email campaigns, lead gen
- Runs CashClaw for technical work
- Manages Hermes skills for specialized tasks

**Current problem:** Too many tools, half of them don't work.

**What we fix:**
1. Get Hermes stable and running
2. Get CashClaw working with Groq API
3. One delivery pipeline per service

---

## The Complete Business Pipeline

```
LEAD SOURCE
    │
    ├── Apollo.io (find HVAC leads, Sioux Falls)
    │
    ▼
COLD OUTREACH
    │
    ├── Instantly.ai (email sequence, free tier)
    ├── Lindy (AI voice agent calls + SMS, free tier)
    │
    ▼
QUALIFICATION
    │
    ├── AI qualifies: budget? timeline? authority?
    ├── Russell Tuna gets notification
    │
    ▼
CLOSE
    │
    ├── Russell Tuna sends Stripe link
    ├── Joseph closes on phone if needed
    │
    ▼
DELIVERY
    │
    ├── Zo + CashClaw + Hermes
    ├── Groq API (free) for all AI calls
    │
    ▼
MONEY
    │
    ├── Stripe (already connected)
    ├── Revenue → business account
    │
    ▼
MARKETING
    │
    ├── Zo generates case study
    ├── Buffer posts to X/LinkedIn
    └── Referrals + repeat business
```

---

## What We Need to Build (Priority Order)

### Week 1: Get Money In (Urgent)
1. **Groq API key** → `console.groq.com/keys` (free, 5 min)
2. **CashClaw SEO audit script** → runs on Groq, produces real PDF
3. **Stripe payment link** → $299 SEO strategy session
4. **Call Jon at EZ Heating** → send him the audit + link

### Week 2: Outreach Pipeline (Critical)
1. **Apollo.io free account** → scrape 50 HVAC shops in Sioux Falls
2. **Instantly.ai free account** → email sequence to those 50 shops
3. **Lindy.ai free account** → AI voice agent for follow-up calls
4. **Russell Tuna** → notification when someone responds

### Week 3: Content Machine
1. **Buffer free account** → schedule 3 posts/week
2. **Zo generates content** → posts go to Buffer queue
3. **Case study template** → one page on Zo Space

### Week 4: Scale
1. Add more service offerings
2. Raise prices based on demand
3. Hire human VA for outreach if needed ($5-10/hr offshore)

---

## The Real Monthly Cost (When We Have Revenue)

| Tool | Purpose | Cost |
|---|---|---|
| Zo Computer | AI brain, hosting, Stripe | ~$20/mo (current plan) |
| Groq API | AI calls for delivery | Free (14K reqs/min) |
| Apollo.io | Lead research | Free tier (limited) |
| Instantly.ai | Cold email | Free tier (1K/mo) |
| Lindy | AI voice agent | Free tier |
| Buffer | Social scheduling | Free tier |
| **TOTAL** | | **~$20/mo** |

When revenue hits $2K/mo:
- Upgrade tools to paid tiers
- Add T4 GPU on Zo ($25/mo)
- Hire offshore VA for outreach ($200/mo)

---

## Who's Responsible For What

| Role | Who | Tasks |
|---|---|---|
| **CEO / Connector** | Joseph | Clients, deals, direction |
| **Builder** | Zo (me) | Code, research, automation |
| **Lead Generation** | Apollo + Instantly | Find + email prospects |
| **Sales Calls** | Lindy (AI voice) | Call, qualify, follow up |
| **Delivery** | Zo + CashClaw + Groq | SEO audits, content, reports |
| **Client Comms** | Russell Tuna | Telegram, notifications |
| **Marketing** | Buffer + Zo | X/LinkedIn posts, case studies |
| **Money** | Stripe | Invoicing, payments |

---

## The One Thing That Makes This Work

**Every hour Joseph spends on sales (calling, messaging, closing) = more money than every hour he spends building.**

The tools above handle everything except:
- Making the actual call to a warm lead
- Closing the deal
- Deciding what to build next

Everything else is automated or delegated to AI.

---

## Immediate Next Step

**Joseph:** Call Jon at EZ Heating & Cooling (605-940-0650) TODAY.
Say: *"Hey, I built an AI system that gets HVAC companies 5+ new customer calls a month. Can I show you what I found on your Google listing — free?"*

If yes → send audit + Stripe link.
If no → call the next 5 HVAC shops.

That's the entire business in one phone call.
