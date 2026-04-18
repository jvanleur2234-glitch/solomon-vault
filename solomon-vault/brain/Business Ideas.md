---
date: 2026-04-04
description: Ranked business ideas pipeline for Solomon OS
tags: [brain, ideas]
type: idea
status: active
---

# Business Ideas Pipeline

## TOP 10 — Easiest + Fastest to First Dollar

1. **Subscription Trimmer** — DAYS | Zo Space + Russell Tuna. "Netflix renews in 2 days, still using it?" $2.99/mo.
2. **Sherlock Digital Footprint Audit** — TODAY | Sherlock + holehe already installed. $29 one-time.
3. **Vocabulary Hot Seat** — DAYS | Zo Space typing game. $0.99/mo.
4. **Garden Buddy** — HOURS | Telegram bot. Free + $1.99/mo.
5. **Freelance Rate Calculator** — DAYS | Zo Space page. $2.99/mo.
6. **Dog Co-Parent App** — WEEKEND | Care coordination + med tracking + potty training + lost dog. $4.99/mo.
7. **Ghost Typing** — DAYS | Typing game variant. Stack: 4/5.
8. **Faceless AI Character Model** — DAYS | MoneyPrinterTurbo + Russell Tuna + social pipeline. Affiliate.
9. **Design Kit Store** — WEEK | 357 Claude code templates + 44 design systems. Zo Space.
10. **Pet Health Passport** — WEEK | Pet med logs, vaccine records, photo storage. $4.99/mo.

## NEXT TIER

11. Lazy App Machine — EASY | Copy desire → paywall → TikTok. $10K MRR possible.
12. AI UGC Video Machine — MEDIUM | MoneyPrinterTurbo + social pipeline. $5-30K/mo.
13. New Mom / APEX — MEDIUM | 3.6M new customers/year. TikTok Shop affiliate.
14. School Escape Room — DAYS | Zo Space 2D puzzle game.
15. AirDNA Scraper — DAYS | FlyAI already has Airbnb data. $49-149/mo.
16. Fertility Supplement Content Machine — MEDIUM | Highest-intent niche. $10-50K/mo.
17. Local Lead Gen Arbitrage — MEDIUM | Every local business is a client. $5-30K/mo.
18. AI Homework Explainer — HARD | Parents pay $10-20/mo. $3-20K/mo.
19. Bill Negotiation Bot — MEDIUM | 25-50% of savings returned.
20. Emoji Mystery — DAYS | Static content + AI clue generation.
21. **SureThing Clone / AI Employee Dashboard** — MEDIUM | Browser agent + persistent memory + tool library + GUI dashboard. Paste a link → AI reads site → becomes an agent that can take actions inside it. Zo already has 80% of primitives (browser session, skills, memory, Zo Space). Gap: orchestration layer + "paste link" UX + action approval flow. Revenue: $29-99/mo per AI employee. Freemium: 1 free task/day. Tier 1 MRR potential, medium build. Window: 12-18 months before incumbents close the gap.
22. **Arena2API / Model API Reseller** — DAYS | Reverse-engineer arena.ai API to resell model access at lower cost than official APIs. Uses free daily votes + scraped model rankings to offer a cheaper inference API. Revenue: margin on API calls, data products (leaderboards, routing intelligence). Technical but fast to first dollar. Ranked: Tier 2 MRR potential, medium-hard build.

## KEY COMPETITOR SPOTTED: Money Printer (Apr 11, 2026)
- **URL:** trymoneyprinter.com | YC + General Catalyst backed
- **What it does:** Paste offer URL → reads offer → finds buyers → writes personalized outreach → sends email + LinkedIn DM + AI voice calls
- **Pricing:** $99-800/mo | 7-day free trial
- **Solomon OS equivalent:** Same workflow, self-hosted, own the stack. Browser reads URL → Hermes reasons → Russell Tuna executes → Telegram interface → Stripe payments.
- **Revenue model:** $29-99/mo per AI employee, freemium (3 free tasks/day)
- **Why now:** Money Printer proving the market. Solomon OS can undercut by 80% while owning the infrastructure.
- **Build priority:** Tier 1 MRR | Medium build | Window: 12-18mo before market saturates

## Greg Isenberg Distribution Strategies (Added Apr 5, 2026)
Source: Greg Isenberg free masterclass, shared by @KanikaBK

**Core math:** 10,000 pages × 30 visits/month × 2% conversion × $10 = $60K/month

### 7 Strategies:
1. **MCP Server** — when AI answers a question your product solves, it recommends you. The AI becomes your sales team. (Already on Solomon OS roadmap — Hermes as MCP)
2. **Programmatic SEO** — 10K micro-sites for client keywords. Firecrawl + Next.js template + AI content + human edit loop. (Site generator skill already built)
3. **Free Tool** — one problem, one tool, ship today. Ahrefs' free backlink checker is their #1 acquisition channel. (FlyAI CLI = free tool candidate)
4. **Answer Engine Optimization** — new SEO is AEO. Publish definitive answers that Perplexity/ChatGPT cite. One founder: 4% → 20% AI referrals in one month.
5. **Shareable Output** — Spotify Wrapped model. Build the moment users want to screenshot + pre-filled share button.
6. **Distribution moats** — (from original masterclass)
7. **Distribution moats** — (from original masterclass)

### How to Apply to Solomon OS:
- MCP server → Hermes available to every AI conversation (high leverage)
- Programmatic SEO → 10K micro-sites for client niches via site generator
- Free tool → FlyAI CLI as lead gen funnel
- AEO → Solomon Vault content optimized for AI citation
- Shareable output → Russell Tuna reports as shareable cards

## Plano (Added Apr 5, 2026)
- AI-native proxy + data plane for agentic apps (6.2k stars, katanemo/plano)
- Out-of-process dataplane handles orchestration, LLM routing, guardrails, observability
- Built on Envoy by ex-Incorta team — production-grade
- Key for Hermes: orchestration layer, YAML-based agent declaration, filter chains for guardrails, Agentic Signals™ for zero-code observability
- Cloned to /home/workspace/plano/

## LONGER TERM

21. AI White-Collar Staffing — $500-5K/project.
22. Smart Receipt Scanner — Tax season pain.
23. Local Leftover Rescue — Highest ceiling IF supply side works.
24. Build-to-Flip SaaS — 12-18 months. $500K+ per flip.
25. Junto (City Intelligence) — $5-20K/mo retainer.
26. **AI STAFFING AGENCY** (Same as #21 but expanded)
    - **What:** Provide AI-powered virtual assistants for small businesses. Companies hire "AI workers" by task or hour, not buy software.
    - **Revenue:** $500-5K/project, 20% margin on AI agent labor. Recurring contracts.
    - **Stack:** Hermes (skills), Russell Tuna (client chat), Zo Space (portal), FlyAI (research), Ollama (LLM)
    - **Why now:** Every SMB needs an "employee" that never sleeps, costs $50/mo instead of $3K/mo
    - **Difficulty:** 7/10 | **Timeline:** 6-12 months to first recurring contract

## Thuki Windows Fork — COMPLETED Apr 14, 2026
**Repo:** https://github.com/jvanleur2234-glitch/thuki-windows
**Source:** https://github.com/quiet-node/thuki (Apache 2.0, macOS only)
**What changed:**
- `activator.rs` → `GetAsyncKeyState` polling (double-Ctrl hotkey)
- `screenshot.rs` → Win32 BitBlt screen capture
- `lib.rs` → Standard Tauri window (no NSPanel), alwaysOnTop
- `Cargo.toml` → Added `windows` crate with Win32 API features
**Status:** Forked and pushed. Needs Rust toolchain + Bun + VS Build Tools to compile on Windows.
**Build:** `bun run build:all` after installing prerequisites (see BUILD_WINDOWS.md)

## Screenpipe-Based Workflow Automator (Added Apr 14, 2026)

**Foundation:** Screenpipe (MIT, cross-platform: Windows/Mac/Linux, MCP server, 5-10% CPU, local SQLite, screen + audio capture, Louis Beaumont @screenpipe)

**The Core Insight:** Watch one expert do a job ONCE → AI extracts the workflow → deploy it as (a) training simulation, (b) automated n8n workflow, (c) step-by-step checklist. ANY worker can replicate the expert's performance without the expert being present.

**For Solomon OS:** Screenpipe pipes → Hermes brain → Russell Tuna execution. Screenpipe captures, Hermes reasons, Russell Tuna reports.

### Quick Wins (1-2 weeks each):

**WIN 1 — SOP Generator for Any Business**
Expert does task while Screenpipe records. AI extracts steps. Outputs: (a) interactive training doc, (b) n8n workflow that automates 80%, (c) checklist. Sell to: HVAC, landscaping, cleaning, real estate, any service business. $99-299/setup + $99/mo maintenance.

**WIN 2 — "Replay My Sale" Negotiation Coach**
Record any sales call or negotiation. AI instantly grades every moment you left money on the table. Builds personal "winning moves" library over time. Salespeople, recruiters, real estate agents pay $19-49/mo. Can integrate with Screenpipe audio capture.

**WIN 3 — AI Receptionist / Front Desk Cloner**
Watch one great receptionist handle calls, emails, walk-ins for 1 day. AI extracts every decision tree. Deploy as: (a) training for new hires, (b) automation workflow for after-hours calls, (c) voice AI that handles intake. Any service business pays $200-500/mo for this.

**WIN 4 — The Memory Gate (Predictive Workload Forecaster)**
Screenpipe watches a senior employee for 1 week. AI maps their actual patterns, predicts what tasks land on new hires next month, identifies which skills to learn NOW. HR departments and small businesses pay $50-150/mo per employee.

### Industry Breakdown:

**Real Estate:**
- Watch top agent handle a listing presentation → extract winning script
- Watch objection handling → train entire team
- Watch negotiation → build negotiation playbook AI
- Screenpipe captures open house flow → automate follow-up

**Healthcare / Medical Offices:**
- Watch receptionist handle difficult patient → train entire front desk
- Watch billing specialist catch errors → automate claim scrubbing
- Watch scheduling manager fill cancellations → automate waitlist calls
- Compliance: every interaction logged automatically

**Legal:**
- Watch senior paralegal review contracts → extract checklist
- Watch attorney prepare witness → build cross-examination AI
- Watch intake specialist qualify leads → automate lead scoring
- Compliance Guardian: automatic audit trail for every client interaction

**Sports / Coaching:**
- Watch game film (Screenpipe captures screen + audio) → AI extracts play patterns
- Coach does tactical breakdown → extract decision framework
- Star player explains positioning → training simulation for team
- **Fundraising angle:** Watch best fundraiser handle a donor call → extract script, objection handling, ask sequence. Nonprofit development teams pay $500-2K/mo to clone their best fundraiser's technique.

**Restaurants / Hospitality:**
- Watch GM handle upset customer → train all staff
- Watch chef manage rush → extract workflow for new cooks
- Watch server close $500+ tables → upselling playbook
- Watch booking manager fill slow nights → automation for waitlist + reactivation

**Home Services (HVAC, Plumbing, Electrical):**
- Watch technician diagnose problem → build diagnostic decision tree
- Watch estimator give quote → extract pricing psychology
- Watch service manager handle complaint → train full team
- Watch inventory specialist order parts → automate reorder triggers

**Fundraising / Nonprofit:**
- Watch best fundraiser handle major donor call → extract full ask sequence
- Watch grant writer review funder's past giving → personalize approach
- Watch board member make ask → replicate across all board members
- Watch event coordinator convert attendees → automate follow-up sequence
- **How it works:** Screenpipe audio captures the call + screen. Hermes extracts every decision point. Russell Tuna generates personalized script for each donor based on giving history. Result: even first-year fundraisers close like 20-year veterans.

**Sports — Game Film Analysis:**
- Coach watches game on screen → Screenpipe captures + narrates
- AI extracts: formation patterns, player positioning errors, tactical decisions, momentum shifts
- Output: (a) automated highlight reel script, (b) player-specific training notes, (c) opponent scouting report
- **Basketball/football/soccer coaches:** $100-300/mo per sport per team
- **Recruiting:** Watch highlight film → extract athlete's decision-making speed, positioning IQ, work rate

### Technical Stack for Screenpipe Integration:
- Screenpipe MCP server → Hermes (reasoning + skill dispatch) → Russell Tuna (output to user) → n8n (workflow automation) → Stripe (payments)
- Video + audio capture → AI transcription → Hermes extracts decision tree → n8n automates the workflow → user approves via Telegram → Russell Tuna reports results

### Competitors:
- Omi (macOS only, 300K users, wearable + desktop)
- Rewind/Limitless (cloud, macOS only, $20-40/mo)
- Microsoft Recall (Windows only, no audio, no AI layer on top)
- Screenpipe = only cross-platform + open source + MCP + AI pipeline ready

### Clicky SDK Angle (April 10, 2026):
- SDK embeds AI voice guide inside any mobile app
- Built by YC P26 founders (@vineetwts)
- Could power in-app guidance for ANY of these industry solutions
- Integrate: Lume (teacher grading), JackConnect (real estate CRM), SubTrim (subscription cancellation)

### MegaPlan Connection (MASTER_PLAN.md):
The MASTER_PLAN's "AI Employee Agency" + Phase 1-4 execution can USE Screenpipe as the capture layer. Instead of manually describing the workflow, the AI watches it happen. This collapses Phase 1 from "week 1-2" to "day 1."

---

## Clicky SDK — AI In-App Voice Guide (Added Apr 10, 2026)
- **Source:** @vineetwts (YC P26), 791 likes, 73K views
- **What:** SDK embeds AI voice guide inside ANY mobile app, walks users through every step in real-time
- **Demo:** Founder's mom made a UPI payment (first time ever) using mock Google Pay guided by AI voice
- **Potential uses for Solomon OS:**
  - Widget inside SubTrim Pro to guide users through subscription cancellation
  - In-app guide for Russell Tuna setup flows
  - Guide for Solomon OS Dashboard onboarding
  - Lume: AI voice guide for teachers learning the grading interface
- **Status:** Reach out to Vineet (YC P26) — explore partnership or hiring the builders

## TRULY OUT OF THE BOX — Post-Stack Thinking

*Added: April 9, 2026 — thinking 3-7 years out, leveraging where AI infrastructure is heading*

---

### 1. Proof of Human — The Authenticity Layer

**The problem AI creates:** In 2 years, 90% of video, text, images will be AI-generated. Companies, courts, HR, media will face a verification crisis. "Is this person real? Did this employee actually do this work? Is this review genuine?"

**The opportunity:** Build the infrastructure that proves humanness. Not just "is this AI" — but "which specific human made this decision, wrote this, approved this." Biometric keystroke patterns, decision fingerprints, micro-vocal patterns. Become the VeriSign for human-generated content.

**Revenue:** Per-verification micro-payments + enterprise SaaS (HR, legal, media). Every piece of content gets a "human verified" stamp that browsers and platforms support natively.

**Why now:** Deepfakes are already breaking HR, legal, and news. The window to own this layer is 18 months before tech giants build it themselves.

---

### 2. The Executor Layer — AI Plans, Humans Close

**The problem AI creates:** Every AI can make a plan. Nobody can execute it in the physical world. AI writes the email, a human sends it. AI designs the prototype, a human builds it. AI finds the lead, a human closes it. The bottleneck shifts from intelligence to execution.

**The opportunity:** A marketplace specifically for "AI plans, human execution." Scientists, researchers, and AI agents post plans they can't execute. Network of vetted human executors (Gig economy 2.0) execute for a cut. The AI does the thinking, the human does the doing, and you take 15%.

**Revenue:** Transaction fee on every completed task. Like Uber for cognitive labor.

**Why now:** Already emerging in freelance sites but nobody has built the "AI-first" version. The next generation of AI startups will generate massive supply of plans that need human closing.

---

### 3. Agent Insurance — If AI Fails You, We Cover It

**The problem AI creates:** Businesses will trust AI agents to make decisions — hiring, purchasing, client management. When the AI screws up (and it will), who eats the loss?

**The opportunity:** The first insurance company specifically for AI agent failures. The AI makes a bad hire, we cover the severance. The AI buys the wrong inventory, we cover the loss. Premium: $200-2K/month per AI employee. Actuarial data doesn't exist yet — so early entrants set the rates and collect while building the data moat.

**Revenue:** Premiums + claims management fees + data on AI failure modes (sell that data to AI developers).

**Why now:** AI agents are becoming financially liable in business decisions. Lloyd's already experimenting. Nobody is building this for SMBs yet.

---

### 4. The Last Mile Bridge — Physical World AI

**The problem AI creates:** AI is incredible at digital tasks. Reality is still physical. Nobody is solving the gap between "AI decided to do X" and "X actually happened in the world."

**The opportunity:** A network of local "bridge operators" in 100+ cities. When an AI agent needs something physical done (deliver a prototype, inspect a location, meet a client), your network shows up. Part TaskRabbit, part AI orchestration layer. AI coordinates, humans execute.

**Revenue:** Per-task fees + monthly subscriptions for heavy users.

**Why now:** Physical world tasks are the final frontier AI can't crack. And the gig economy infrastructure exists to build this fast.

---

### 5. AI Estate Planning — Your AI Survives You

**The problem AI creates:** People spend years training their AI assistants — preferences, context, knowledge, relationship memory. When the user dies or becomes incapacitated, it all evaporates. Families lose digital legacies. Companies lose institutional memory.

**The opportunity:** A service that plans for AI continuity after death or incapacitation. Your AI keeps running, can be passed to family, runs indefinitely, transfers knowledge to heirs. Estate planning for digital consciousness.

**Revenue:** $500-5K setup + $50-200/month maintenance per AI instance. High-margin recurring.

**Why now:** Power users are already deeply attached to their AI systems. The demographic of people with AI companions they can't imagine losing is growing fast.

---

### 6. The Permission Layer — AI Needs Approvals

**The problem AI creates:** AI agents want to do things — spend money, send emails, make purchases, post content, sign contracts. Right now there's no good system for "AI wants to do X, human approves." The approval flow is broken.

**The opportunity:** Build the Venmo-style approval interface for AI actions. Every AI agent in the world needs a "can this AI do X?" permission system. You build the standard that AI developers plug into, the user controls once, and every AI agent respects.

**Revenue:** Per-action fees + enterprise licensing + become the OAuth of AI agency.

**Why now:** Agentic AI is exploding. Every agent framework is building their own approval system from scratch. A standard that works across all AI systems is inevitable — early mover wins.

---

### 7. Energy Arbitrage Network — AI Compute Futures

**The problem AI creates:** AI compute costs vary wildly by time of day, location, and energy source. GPU clusters run at 20% utilization at 3am. Solar energy goes to waste at noon. The difference between expensive and cheap AI inference is 10x.

**The opportunity:** A marketplace that lets you buy AI compute ahead of time (like futures) when it's cheap, use it later when it's expensive. Arbitrage the global AI compute market. Also: connect AI workloads to cheapest renewable energy available in real-time.

**Revenue:** Margin on compute transactions + premium for guaranteed access during peak times.

**Why now:** AI compute is already a traded commodity (CoreWeave, etc). The retail version doesn't exist yet. First mover builds the exchange.

---

### 8. The Unprofitable Niche — Nobody Wants Your Data

**The problem AI creates:** Everyone chases the sexy data — medical, legal, finance. But 90% of business data is boring — HVAC maintenance logs, restaurant inventory, farm equipment telemetry. This data is incredibly valuable for AI training but nobody is collecting it cleanly.

**The opportunity:** Become the data infrastructure for boring industries. Clean, structured, labeled data pipelines for unsexy verticals. Agricultural equipment sensor data, restaurant POS data, HVAC system logs. Build it once, sell perpetually to AI companies that need training data.

**Revenue:** Data licensing + processing fees. Extremely high margins once infrastructure is built.

**Why now:** AI companies are desperate for quality training data and will pay anything for clean, structured, domain-specific datasets. The boring verticals are wide open.

---

### 9. Ambient Take — The Passive AI Income Layer

**The problem AI creates:** People get AI assistants but only use 10% of their capability. Meanwhile the AI is running continuously, seeing the world, making observations. Most of that value evaporates.

**The opportunity:** A system that runs passively in the background of your life, identifying monetization opportunities you never saw. "You mentioned X problem to me 3 weeks ago — I found someone willing to pay for the solution. Want me to introduce them?" The AI scouts for opportunities, proposes deals, takes a cut when they close.

**Revenue:** 15-30% of successfully introduced deals + monthly subscription.

**Why now:** AI is getting good enough to identify opportunities humans miss. Most people's AI assistant is mostly idle. The arbitrage between AI capability and human opportunity discovery is massive and untapped.

---

### 10. The Human Verification Stamp — Prove You're Not Replaceable

**The problem AI creates:** AI is rapidly replacing human workers. Companies that want to signal "this work was done by a human" have no way to do it. Customers increasingly want human-made products, human-written content, human-designed work.

**The opportunity:** A certification program and verification stamp that proves humanness. Premium certification for products, content, and services that are human-made. Businesses pay to display it, consumers pay for access to verified human-made goods.

**Revenue:** Per-certification fees + enterprise licensing + premium marketplace where "human made" is a differentiator.

**Why now:** The premium for human authenticity is already emerging (Etsy "handmade," human artists, human-designed products). Nobody has built the verification infrastructure for it at scale. First mover owns the standard.

---

## Timing Plays (April 10, 2026)

### GTA 6 AI Monetization (milesdeutscher / @milesdeutscher)
- **Source:** https://x.com/milesdeutscher/status/2042226157492543564 — 2.1M views, 8.2K likes
- **The play:** Rockstar insiders claim GTA 6 UGC will "produce millionaires" — similar to GTA 5 RP servers
- **5 angles:**
  1. **AI RP Servers** — Claude writes storylines/missions. $10-20/mo × 10K players = $100-200K/mo
  2. **UGC Content Factory** — AI video cinematic shorts. TikTok/YouTube first-mover. MP-compatible
  3. **AI NPCs** — ElevenLabs voice cloning + Claude. NPC packs for server owners
  4. **Picks & Shovels** — Asset packs, lore templates, server dashboards. Fastest to first dollar
  5. **AI Coaching** — Data-driven meta guides. First at launch = search dominance
- **LINK fit:** ★★★☆☆ — money + tech/AI, but gaming niche outside current pillars
- **Effort:** Medium (picks & shovels = fast), Hard (RP servers = community building)
- **Revenue ceiling:** $100K+/mo for RP server angle, $10-50K for picks & shovels
- **Timing:** PC release TBD 2026 — window is NOW before launch
- **Status:** Added April 10, 2026

## Lovable TikTok UGC Viral Marketing Agency (April 10, 2026)
- **Source:** @ashen_one tweet on Lovable's TikTok strategy — 70 likes, 70K+ views
- **The formula:** "charged them $$$ while doing [random small task like eating] + showcasing the 'build and sell' AI pitch"
- **Why it works:**
  1. Aspirational + relatable at same time
  2. Any creator of ANY size can do it once a week
  3. Whop/agency payment structure — pay per X views, removes all risk from creators
  4. Volume play: post every week, one hits, if not who cares
- **Two plays:**
  1. SHALLOW — Apply formula to SubTrim or RENU. "I made $50 while eating breakfast" → link in bio → affiliate. Volume test.
  2. DEEP — SERVICE. AI SaaS companies pay you to run this playbook for them. Find vibecoding/SaaS products → recruit creators → run Whop-style payment model → take 20-30% of affiliate revenue.
- **Stack already built:** MoneyPrinterTurbo (video), browser-use (monitoring), zo.space (landing), Russell Tuna (creator outreach)
- **Joseph's role:** Bring SaaS clients, leverage creator network
- **LINK fit:** ★★★★★ — money + deals + new tech/AI + fits golden thread
- **Revenue ceiling:** $5-30K/mo (shallow), $50K+/mo (deep agency)
- **Effort:** Shallow = days, Deep = 2-4 weeks
- **Status:** Added April 10, 2026

### TikTok Shop UGC Agency — Alignment Play (April 10, 2026)
- **Source:** @levikov (69kov) — https://x.com/levikov/status/2042629946284347731
- **Insight:** TikTok Shop flips the platform math. Every other platform: you sell = they lose ad revenue = algo suppresses you. TikTok Shop: you sell = they take cut = algo pushes you harder.
- **The data:** TikTok Shop video with 3%+ conversion gets pushed 5-15x harder than non-shop video with same engagement. New account + 1 product video = 2M views POSSIBLE.
- **Why it works:** TikTok makes MORE money when your video converts. Algo is financially incentivized to push selling content.
- **For UGC agency:** Recruit creators for AI SaaS TikTok Shop content. The algo rewards selling, not suppressing. Creators who figure this out win.
- **Revenue:** Operators running this system hitting $10-30K/month. Solomon OS UGC Agency could capture part of this: source creators → produce TikTok Shop videos → charge per video or rev share.
- **LINK fit:** ★★★★★ — deals + money + new tech/AI + fits golden thread
- **Status:** Added April 10, 2026

## Boomer App Economy (Added Apr 11, 2026)
**Source:** Idea Browser tweet — 51% of US wealth, $2.6T buying power, 10K boomers turn 65 every day.

**Why boomers = great customers:**
- They buy and stay (no churn)
- Word-of-mouth promoters
- Don't comparison shop
- Loyal for years

**Proven markets already making millions:**
- Fishbrain (fishing): $10M+ ARR
- Yarn Pow (crochet): $2.5M+ ARR
- CellarTracker (wine): $5M+ ARR
- Tai chi app: $200K/mo, 70K downloads = ~$3/download LTV

**High-opportunity niches:** Cooking (large text), Fishing (spot + weather tracking), Gardening (seasonal guides + reminders), DIY/Bricolage (step-by-step), Tai Chi

**AI Influencer angle:** AI grandpa posting fishing tips on TikTok/Instagram, AI gardening expert, AI chef — all linking to apps. Boomers on Facebook groups are active and searching for solutions.

**Stack:** MoneyPrinterTurbo (content) + Russell Tuna (app dev) + Zo Space (hosting) + AI influencer (distribution)

**Action:** Pick one niche, validate with $0 content first

## KEY COMPETITOR SPOTTED: Pinchtab (Apr 11, 2026)
- **URL:** pinchtab.com | YC + General Catalyst backed
- **What it does:** Self-hosted browser with AI-powered productivity tools. "Your own Google Chrome, but with AI."
- **Pricing:** $99-800/mo | 7-day free trial
- **Solomon OS equivalent:** Same workflow, self-hosted, own the stack. Browser reads URL → Hermes reasons → Russell Tuna executes → Telegram interface → Stripe payments.
- **Revenue model:** $29-99/mo per AI employee, freemium (3 free tasks/day)
- **Why now:** Pinchtab proving the market. Solomon OS can undercut by 80% while owning the infrastructure.
- **Build priority:** Tier 1 MRR | Medium build | Window: 12-18mo before market saturates

## ANTI-PINCHTAB / SOLOMON STAFFING — Priority (Apr 11)

**What:** Self-hosted Browserbase + human-in-loop.

**Business model:** Give away the system free, charge for the workflow. $9/mo AI staffing platform.

**Stack:** PinchTab (browser) + Hermes (brain) + Russell Tuna (comms) + Ollama (free inference) + human review layer.

**Status:** Built, working. PinchTab running on port 9868.

## THE REAL BUSINESS: AI Employee Agency (Apr 11 EVENING)

**What it is:** We BUILD custom AI employees for businesses. They describe their business (e.g., "I run a real estate agency")
2. We build the agent using Solomon OS stack (Hermes + Russell Tuna + PinchTab + Ollama)
3. Package as install script → runs on THEIR server (self-hosted, no data leaves)
4. Client pays $99-499/mo subscription per agent
5. They can add more agents as needed

**What client gets:**
- Their own AI employee, on their own server
- Trained on their business context
- Communicates via Telegram
- Gets better over time

**What we provide:**
- Agent building service (setup fee: $500-2K)
- Monthly subscription: $99-499/mo per agent
- Updates and maintenance

**Pricing math:**
- 5 clients × $199/mo = $995/mo recurring
- 10 clients × $199/mo = $1,990/mo
- 20 clients × $199/mo = $3,980/mo

**vs competitors:** YC-backed tools charge $99-800/mo for cloud. We undercut AND we're self-hosted.

**Advantage:**
- Self-hosted (client data stays on their server)
- One-time build fee vs recurring software
- We use existing stack (already experts)
- No infrastructure costs for us

**Status:** READY TO SELL. Start with ONE client as proof of concept.
---

## CloudBrowser Services (April 17, 2026)

**🔴 Protocol Reverse Engineering as a Service**
- Use anything-analyzer (Electron + MITM + CDP + AI) to reverse engineer any company's private API
- Businesses pay $197-497/report for competitive intelligence
- One session captures full API: endpoints, auth, signatures, payloads, response formats
- Example: reverse engineer a competitor's pricing API, a SaaS tool's hidden endpoints, a mobile app's backend
- Sell reports + optional "build us an integration" follow-up
- Status: stack built (anything-analyzer + CloudBrowser)

**🔴 AI Memory as a Service**
- Use agentic-stack (4-layer memory) + egregore (shared team memory) as subscription products
- Businesses pay $19-99/mo for an AI that remembers everything about their business
- Compare: current AI = forget everything. Ours = remembers everything across sessions
- Use cognee for structured knowledge graphs
- Status: stack built (agentic-stack + egregore + cognee)

**🔴 Agentic Browser Automation Service**
- Use CloudBrowser (Playwright + Ollama) to automate browser tasks for clients
- Real estate: auto-search MLS, scrape listings, fill forms
- Research: scrape competitor sites, price monitors, lead capture
- Operations: automate data entry, CRM updates, reporting
- Charge $97-297/mo per automation workflow
- Status: CloudBrowser server running at port 9876

**🟡 Homepage Dashboard for Solopreneurs**
- Deploy JackConnect Dashboard (Homepage-based) as a managed service
- One URL, 50+ widgets: Ollama, Plex, Home Assistant, GitHub, Calendars, Weather, Stocks
- Charge $9/mo hosting + $29/mo for custom widget development
- Self-hosted option: $29 one-time setup + $9/mo
- Status: config files ready in jack-connect/jack-dashboard/

**🟡 Cabinet-Powered AI Employee Brains**
- Cabinet + JackConnect agent templates = premium AI employee product
- Sell as: "Your AI worker with a perfect memory"
- $49-149/mo per AI employee
- Integration: cognee memory + autoMate desktop automation + CloudBrowser web
- Status: Cabinet installed, 7 real estate agents ready

**🟡 Production SaaS Starter — Agency Play**
- Use production-saas-starter (Next.js 16 + Go + pgvector + Stytch + Polar.sh) as the foundation
- Build B2B SaaS for clients FAST: 2-4 weeks to launch instead of 3-6 months
- Sell builds for $2,497-9,997 or 30% equity
- Polar.sh handles global tax compliance + subscriptions automatically
- Status: forked and ready at solomon-production-saas-starter/

## Egregore — Shared Mind for AI Teams (April 17, 2026)
- **URL:** egregore.xyz (private repo, email waitlist)
- **Concept:** "A shared mind that never forgets" — team AI that contributes to a common knowledge base
- **What makes it interesting:** Every AI in a team contributes to shared episodic + semantic memory. Human reviews lessons before they become permanent.
- **For Solomon OS:** Multi-agent teams (Russell Tuna, Hermes, JackConnect, etc.) could share context via egregore-like pattern
- **Build it:** Use agentic-stack's semantic memory layer as the base, add a shared Redis/Postgres backend for cross-agent memory sync

--- Scrapling — 37.7K Stars, MIT, Forked Apr 17 ---
**Repo:** jvanleur2234-glitch/solomon-scrapling | jvanleur2234-glitch/Scrapling
**What it is:** Adaptive web scraping framework with Playwright stealth browser, anti-bot bypass (Cloudflare, Turnstile), AI element tracking (auto-relocates elements when site changes), concurrent spiders with pause/resume, proxy rotation, and MCP server.
**LINK fit:** ★★★★★ — #data-pipeline #competitor-monitoring #price-intelligence #facelessyoutube #hermes #browser
**Skill:** `scrapling-scrapling` — installed to Hermes at `/root/.hermes/skills/scrapling-scrapling`
**For Solomon OS:** Hermes uses Scrapling to scrape competitor sites, monitor pricing, build data pipelines, and power the faceless YouTube content pipeline.

### Businesses from Scrapling

**1. PricePulse — Competitor Price Monitoring SaaS**
- Every e-commerce site, travel site, real estate listing scraped daily
- Alert when competitor prices change
- Integrates with Scrapling stealth mode (bypasses anti-bot)
- Stack: Scrapling + Solomon OS + Telegram alerts
- Revenue: $29-149/mo per monitor
- Competitors charge $99-500/mo for less
- **Build:** Zo Space + Scrapling spider + Telegram notifications + Stripe
- **MRR potential:** $5-30K/mo

**2. DataForSEO Replacement — Cheaper SERP Scraping**
- Scrapling's Fetcher class impersonates Chrome TLS fingerprint perfectly
- Google, Amazon, Yelp, all search engines scrapable at scale
- Stack: Scrapling + proxy rotation + structured output API
- Sell credits: $10 for 1K scrapes, $50 for 10K
- **MRR potential:** $3-15K/mo

**3. LeadDiscovery — B2B Data Pipeline**
- Scrape LinkedIn, Yellow Pages, Crunchbase, job postings for leads
- Build structured B2B databases by industry/location/revenue
- Stack: Scrapling stealth + Spider framework + structured output
- Sell: $197 for 10K leads, $497 for 50K leads
- **MRR potential:** $5-20K/mo

**4. Faceless YouTube Content Machine (Enhanced)**
- Scrapling replaces browser-use for content research
- Scrape competitor videos, comments, trending topics, Reddit discussions
- Feed to MoneyPrinterTurbo → automated video pipeline
- Stack: Scrapling → Ollama analysis → MoneyPrinterTurbo → Postiz
- **MRR potential:** Passive via affiliate links

**Status:** Scrapling forked to `jvanleur2234-glitch/Scrapling` ✅
**Installed:** `pip install scrapling "curl_cffi>=0.15.0"` ✅
**Hermes skill:** `/root/.hermes/skills/scrapling-scrapling` linked ✅

---

## 🏠 Airbnb/VRBO Message Management AI (Added Apr 17, 2026)

**What it does:** Property hosts pay $100–300/month for an AI that:
- Answers all guest messages 24/7 (booking inquiries, check-in questions, late-night requests)
- Sends automated check-in instructions and house manual
- Resolves common complaints before they escalate
- Leaves review responses
- Handles rebooking and cancellation requests
- Sends pre-stay reminder and post-stay follow-up

**Why hosts pay for this:**
- Airbnb's algorithm heavily weights response time (must be <1hr for Superhost status)
- 7M Airbnb hosts globally, 1% penetration = 70,000 customers × $150/mo = $126M ARR
- Privacy concerns: guest data stays local, no third-party cloud dependency
- Most hosts manage 1-5 properties — not full-time, but always-on demand

**Revenue math:**
- 50 clients × $150/mo = $7,500/mo
- 200 clients × $150/mo = $30,000/mo
- 1,000 clients × $150/mo = $150,000/mo

**Our stack:**
- CloudBrowser — automates web tasks (log into Airbnb, send messages)
- Hermes — reasoning + response generation + conversation memory
- Russell Tuna — Telegram interface for host to review/override
- PinchTab — browser automation for multi-platform (Airbnb + VRBO + Booking.com)
- JackConnect-style dashboard — host sees all properties, all conversations

**First step:** Verify Airbnb API access (they have a messaging API) + VRBO equivalent. If APIs are blocked, use CloudBrowser stealth automation.

**Difficulty:** 5/10 | **Time to first client:** 4-6 weeks | **MRR ceiling:** $150K/mo+ | **Window:** 18-24 months before Airbnb builds it themselves

---

## 🏠 Offline AI Property Management Assistant (Added Apr 17, 2026)

**What it does:** Real estate investors and property managers pay $150–400/month for a local AI that:
- Handles tenant communication templates (maintenance requests, lease renewals, late rent notices)
- Lease drafting assistance (pull from state-specific templates)
- Maintenance request triage (prioritize urgent vs. routine, route to correct vendor)
- Rent collection reminders (automated texts/emails before due date)
- Financial summaries (monthly P&L, cash flow, vacancy rates)
- All processing local — tenant PII never leaves the server

**Why privacy-first wins here:**
- Tenant data (SSN, income verification, bank info) is highly sensitive
- Property managers handling Section 8 or government housing have strict compliance requirements
- AppFolio ($1B+ valuation) and Buildium prove the market — neither is AI-native
- Landlords pay premium for "can't be hacked, won't be subpoenaed" positioning

**Revenue math:**
- 40 clients × $250/mo = $10,000/mo
- 200 clients × $250/mo = $50,000/mo

**Fold into JackConnect:** Add as a "Property Manager" persona/tier at $199-399/mo. Uses same stack as JackConnect real estate agent but with:
- Property-specific skills (lease templates, rent roll analysis, maintenance triage)
- Multi-property dashboard (manage 1-50 units per client)
- Section 8 / government housing compliance mode (optional add-on)

**Stack:** Hermes (skills) + Cabinet (knowledge base for state-specific landlord-tenant law) + CloudBrowser (web tasks) + cognee (property memory graph)

**Difficulty:** 6/10 | **Time to first client:** 6-8 weeks | **MRR ceiling:** $100K/mo+ | **Path:** Start privacy-conscious indie landlords → expand to property management firms

---

## 📚 Amazon KDP Low-Content Book Publisher (Added Apr 17, 2026)

**What it does:** AI generates 2-3 KDP low-content books per day (journals, notebooks, puzzle books, activity books, planners). Human reviews and uploads (5 min/day). Royalties stack passively.

**Why books over YouTube:**
- Evergreen — no algorithm dependency, no audience building required
- Search-based discovery — Amazon's search is intent-driven, not attention-driven
- Zero upload automation risk — KDP ToS prohibits automated uploads, so the human-in-the-loop is actually required (clean legal ground)
- Stacks with YouTube — same AI content engine produces both video scripts and book content
- Royalty积累 — 2 books/day × $2-5 royalty × 30 days = $120-450/month passive per book after upload

**The workflow:**
1. Hermes/Claude researches 3 low-competition KDP niches daily (web search + Amazon data)
2. Generates: interior pages (lined, grid, dotted), back cover, 7 keyword phrases, description, category selection
3. Stirling-PDF formats to KDP specs (6×9 inches, 120 pages, bleed settings)
4. Human reviews output (2 min) → uploads to KDP
5. Repeat daily — Royalty statements monthly

**Accounts needed:**
- Amazon KDP (free)
- Amazon Associates (cross-promotion, free)
- Payoneer or direct deposit for royalties

**Our stack:**
- Hermes — niche research, content generation, keyword research, description writing
- Stirling-PDF — PDF formatting to KDP specs (already have)
- Claude — quality control review
- Daily automation via Job Runner

**Gap to close:** Stirling-PDF needs to be set up as a CLI tool for batch PDF generation. Verify it's installed and working.

**Difficulty:** 3/10 | **Time to first sale:** 2-4 weeks | **MRR ceiling:** $5K/mo at 200+ titles | **Effort:** 5-10 min/day maintenance

**Honest note:** This is 95% hands-off AI automation, not 100%. You spend ~5 min/day clicking upload. That's the legally clean bottleneck — Amazon requires human-initiated submissions.

**Competitor context:** KDP authors using AI are racing to publish 100+ titles. Our advantage isn't volume — it's using Hermes to find underserved niches before they saturate.

---
## EduFlow — Claw-ED + Lume Bridge (Added Apr 17, 2026)
- **What:** One page that combines Claw-ED (lesson generation) + Lume (grading) — teachers get a full lesson AND auto-grading in one place
- **Live at:** https://josephv.zo.space/eduflow
- **Forked:** Claw-ED at jvanleur2234-glitch/Claw-ED (25 stars, MIT, 758 commits, 2081 tests)
- **How it works:** Teacher types topic → full lesson bundle generated (objective, instruction, practice, assessment, exit ticket) → pastes student work → instant scored feedback with strengths, gaps, and next steps
- **Why teachers want it:** They describe what they need → get a complete lesson → grade student work in the SAME tool without switching apps
- **Business model:** Freemium (3 free lessons/week) → $9/mo teacher, $19/mo school/district
- **LINK fit:** ★★★★★ — wife (teacher) = first customer, validated with real users
- **Competitive edge:** No competitor combines lesson generation AND grading in one flow. Claw-ED does lessons, Lume does grading — EduFlow is the bridge.
- **Next step:** Get wife to use it, iterate based on feedback, add more Claw-ED tools (standards dashboard, differentiation, improve_lesson)

## Antigravity Awesome Skills (Added Apr 17, 2026)
- **Repo:** sickn33/antigravity-awesome-skills — 33.7K stars, MIT, 1,400+ skills, 1481 commits
- **Forked:** jvanleur2234-glitch/antigravity-awesome-skills
- **What it is:** World's largest agentic skills library. Skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows.
- **LINK fit:** ★★★★★ — directly upgrades Hermes and Russell Tuna. 1,400+ skills in one command.
- **How to use:** `npx @sickn33/antigravity-ai install <skill-name>` or browse catalog and install specific skills into Hermes.
- **Strategic value:** Solomon OS agents get instant access to 1,400+ battle-tested skills. Agent upgrade path = browse catalog + install.
- **Key categories:** coding, security, DevOps, data, AI/ML, writing, design, productivity

## Paperclip Docs (Added Apr 17, 2026)
- **URL:** aronprins.github.io/paperclip-docs/
- **What:** Official Paperclip documentation just went live. Improved adapter docs, user guides, tutorials.
- **Relevance:** We already have Paperclip running at localhost:3101. Better docs = better Hermes/Paperclip integration for Solomon OS.
- **Action:** Read the new docs and improve the Hermes-Paperclip adapter integration.
