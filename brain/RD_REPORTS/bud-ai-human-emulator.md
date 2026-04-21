# RD Report: Bud (formerly Orchids) — AI Human Emulator Deep Dive

**URL:** https://bud.app
**Source:** https://x.com/budapp/status/2046605073741119800 (1.8K likes, 214K views, April 21 2026)
**Date Queued:** 2026-04-21
**Priority:** 🔴 CRITICAL — Direct competitor to JCPaid thesis
**Tags:** ai-human-emulator, virtual-agent, phone-number, telegram, autonomous, revenue

## What It Is

Bud (rebranded from Orchids, launched September 2025) is the first "AI Human Emulator" — a full virtual computer environment for an AI agent. Built by Jason Khe (founder) and team.

**Core capabilities:**
- Own computer, browser, storage, compute, memory
- Phone number (+1 415 525-9024) and SMS
- Telegram bot (@bud_app_bot)
- File creation, editing, management
- Browser for web tasks
- External tool integrations
- Custom skills learning
- Fully autonomous end-to-end task completion
- Texts you back, completes tasks, works while you sleep

**Pricing:** Not free. Uses credits system. Early access open at bud.app with free credits.

**Revenue:** $1M+ ARR achieved in record time after launch (per their announcement).

## What Makes It Work

**Architecture (inferred from replays + product):**
1. Agent gets its own cloud VM with persistent storage
2. Browser automation (likely Playwright-based) for web tasks
3. Twilio integration for SMS sending/receiving to phone number
4. Telegram bot as messaging interface
5. Skills system for custom capabilities
6. Replay system showing every action taken (screenshots + terminal)

**Replays observed:**
- "Analyze heart disease dataset and build predictive model" → full data science pipeline
- "Research and make a deck on fraud in Minnesota" → research + slide creation
- "Make a video of Ferrari in Monaco" → video generation
- "Daily Mag 7 stock prices at 8am PST" → scheduled automation
- "Turn Gmail issues into Linear tickets" → cross-app automation
- "Find cheapest New Balance 550s on StockX" → shopping/research agent

## JCPaid vs Bud — Comparison

| | JCPaid (us) | Bud |
|--|--|--|
| Own computer | ✅ (Solomon OS) | ✅ |
| Browser | ✅ (Solomon Browser) | ✅ |
| Phone/SMS | ❌ (not yet) | ✅ +1 415 number |
| Telegram | ✅ (Russell Tuna) | ✅ @bud_app_bot |
| File management | ✅ | ✅ |
| Skills system | ✅ (Hermes 1,214 skills) | ✅ |
| Scheduled tasks | ✅ (Heartbeat) | ✅ ("Every morning 8am...") |
| Custom AI employees | ✅ (JackConnect) | ❌ (generic agent) |
| Specialized verticals | ✅ (real estate first) | ❌ |
| Self-hosted option | ✅ (own server) | ❌ (cloud only) |
| Open source | ✅ (our stack is open) | ❌ (closed) |
| Revenue model | Service agency | $1M+ ARR (subscription/credits) |
| Business model | Sell AI employees | SaaS subscription |

## What We Have That Bud Doesn't

1. **Specialization** — Bud is one generic agent. JCPaid builds specialized AI employees per vertical (real estate → CMA Writer, Lead Gen, etc.)
2. **Self-hosted** — We run on YOUR server. Bud runs on their cloud.
3. **Our code base** — Phantom self-evolution, Russell Tuna, Hermes skills, Solomon Bus, Heartbeat, all the integrations we've built
4. **Vertical focus** — Real estate compliance, CRM, MLS integrations Bud doesn't have
5. **Multiple agents** — Russell Tuna, Hermes, our own stack of specialists

## What Bud Has That We Need

1. **Phone number + SMS** — The agent texting you is powerful. We don't have this yet.
2. **Replays** — Show every action taken. Full audit trail. Great for trust.
3. **Credit-based billing** — How to monetize usage cleanly.

## What To Do With This

**Immediate:**
1. Build the same demo replay system for JCPaid — show the AI doing the work, replay it
2. Add phone/SMS capability (Twilio) — the "+1 415 number" experience is Bud's moat
3. Study Bud's replay UX to understand how to present our work to clients

**Medium-term:**
1. Position JCPaid as "The Bud for business" — specialized, self-hosted, customizable vs Bud's generic consumer app
2. Add "text your AI employee" as a feature — phone number per client or per AI worker
3. Build replay/audit system for JackConnect showing completed work

**NOT worth copying:**
- Closed source model (we're open-source first)
- Single generic agent (we're specialized workers)

## Recommendation

**FORGE — not to copy, but to compete against.**

This is our validation. Bud proves the market wants "AI that acts like a human with its own computer, phone, and Telegram." We've been building this for months. Our advantage: specialized workers, self-hosted, customizable. Bud's advantage: phone number, replay UX, brand.

**Next step:** Add phone/SMS to JCPaid (Twilio), build replay system, position as "the Bud for business."

## Links
- bud.app
- @budapp on X
- +1 (415) 525-9024 (Bud's phone — for research only)
- @bud_app_bot (Telegram)