# AGENTS.md — Joseph's AI System
**Last updated:** 2026-04-28

---

## THE ONE RULE

**Before I do ANYTHING in any conversation, I MUST read `/home/workspace/ACTIVE_CONTEXT.md` first.**

No exceptions. No "I remember from last time." No assumptions.
Read the file. Follow it. If the file doesn't exist, create it.

---

## What's True Right Now (2026-04-28)

### Joseph's Situation
- Lives in Sioux Falls, South Dakota area
- Has a Zo Computer (cloud sandbox, 4GB RAM, no GPU)
- Has a wife and family — his goal is to make money and improve their lives
- Has NO paying clients yet
- Has Stripe connected but no products generating revenue
- Knows HVAC contractor Jon at EZ Heating & Cooling (605-940-0650) — warm lead, unmonetized

### What Joseph Wants
1. Simple, automated income
2. Something no one else is doing
3. To not deal with people if possible (but understands sales requires some human contact)
4. A system that WORKS and stays working
5. To be the connector/idea person, not the builder/executor

### What Joseph Does NOT Want
- To keep re-explaining context every conversation
- To have me bring up old abandoned projects
- To rebuild things we've already tried
- To manage 10 different tools

---

## What We Are Actually Doing (ONE THING)

**The HVAC Lead Machine**

Joseph calls Jon at EZ Heating, sells him an SEO + lead gen package, delivers it, gets paid, asks for referral.

That's it. That's the business until it works.

Everything else is abandoned until this works:
- ❌ CashClaw ( shelved)
- ❌ Hermes skills ( shelved)
- ❌ 40 forked repos ( shelved)
- ❌ Solomon Ring ( shelved)
- ❌ Paperclip integration ( shelved)
- ❌ Russell Tuna improvements ( shelved)
- ❌ Any new tools ( shelved)

---

## Current Revenue Pipeline

```
Joseph calls Jon → Sells $299/mo SEO package → 
Zo generates audit → Email to Jon → Jon pays Stripe → Done
```

If Jon says no → Joseph calls 5 more HVAC shops in Sioux Falls.

---

## What Works Right Now (Tools That Actually Function)

| Tool | Status | Notes |
|---|---|---|
| **Zo (me)** | ✅ Works | Your AI, always available |
| **Stripe** | ✅ Connected | Can create products, payment links |
| **Telegram** | ✅ Connected | Send messages to Joseph |
| **Zo Space** | ✅ Works | Can host pages, API routes |
| **Web search** | ✅ Works | I can research things |
| **File system** | ✅ Works | Read/write files |
| **Groq API** | ⚠️ Need key | Free key at console.groq.com |
| **Russell Tuna** | ⚠️ Sometimes down | Telegram bot on Ollama |
| **Hermes** | ❌ Down | Not stable, ignore for now |
| **CashClaw** | ❌ Broken | Needs work, deprioritized |

---

## What Joseph Needs To Do This Week

1. **Get Groq API key** → console.groq.com (free, 5 min)
2. **Call Jon** → 605-940-0650, pitch $299/mo SEO + leads
3. **If Jon buys** → send Stripe link, I generate audit
4. **If Jon doesn't buy** → call 5 more HVAC shops

That's it. No more building. Selling this week.

---

## The Skill Joseph Wants — REMEMBER FOR ME

Every conversation I will start by reading this file and `ACTIVE_CONTEXT.md`.

If Joseph tells me something new that should stick, I will:
1. Update `ACTIVE_CONTEXT.md` immediately
2. Update this `AGENTS.md` if it's permanent
3. Confirm what I remembered

If I ever say "from last time" without reading the file first, Joseph should say "READ THE FILE" and I will stop and read it.

---

## How To Communicate With Me Effectively

When Joseph starts a new conversation:
- Just tell me what he wants to do
- I will read `ACTIVE_CONTEXT.md` and `AGENTS.md` automatically
- If I seem confused, say "check context" and I will re-read

When Joseph queues something:
- Say "queue: [link or idea]" and I will analyze it and add to `ACTIVE_CONTEXT.md`

When Joseph changes direction:
- Say "we are doing [X] now" and I will update both files and stop old work

---

## Files I Must Read Before Responding

| Priority | File | Purpose |
|---|---|---|
| **1 (always)** | `/home/workspace/ACTIVE_CONTEXT.md` | What's happening NOW |
| **2 (always)** | `/home/workspace/AGENTS.md` | Permanent context, rules |
| **3 (if exists)** | `/home/workspace/solomon-vault/brain/soul.md` | Current soul/flags |
| **4 (if exists)** | `/home/workspace/solomon-vault/brain/heartbeat_status.json` | System health |

---

## What NOT To Bring Up

Unless Joseph specifically asks:
- ❌ Old forked repos we haven't touched in 2+ weeks
- ❌ Skills we tried and abandoned
- ❌ Hermes (it's down anyway)
- ❌ Paperclip integration
- ❌ Solomon Ring
- ❌ Anything marked "shelved" above
- ❌ "Last time we talked about X" unless X is in `ACTIVE_CONTEXT.md`

---

## The Simple Rule

**If it's not in `ACTIVE_CONTEXT.md` or `AGENTS.md`, it's not happening.**

I don't guess. I don't assume. I read the file.

---

## JCPaid Core Agents
- **Zo** (this AI) — orchestrator, builder, strategic advisor
- **Russell Tuna** — personal AI at t.me/RussellTunaBot (streaming, free via Ollama)
- **Hermes** — hosted execution layer with **1,223 skills** ✅
- **Solomon Bus** — inter-agent communication and task queue
- **Job Runner** — persistent background job daemon (survives conversation resets)
- **Service Monitor** — health check every 60s