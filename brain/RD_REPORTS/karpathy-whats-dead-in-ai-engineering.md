# RD Report: Andrej Karpathy — "What's Dead in AI Engineering"

**Date:** 2026-04-30
**Type:** Industry Insight / Positioning Validation
**Recommendation:** READ — validates JCPaid positioning, essential for sales narrative

---

## What It Is

Ronin (@DeRonin_) amplifying Andrej Karpathy's warning: "90% of what AI twitter tells you to learn will be dead in 6 months." Senior AI engineers share what's NOT worth focusing on, and what actually compounds.

**Engagement:** 309K views, 1,927 likes — viral in AI engineering circles.

---

## What's DEAD (What NOT to Build/Sell)

1. **AutoGen / AG2** — "moved to community maintenance, releases stalled. dead for production"
2. **CrewAI** — "demos well, breaks in production"
3. **Autonomous agent pitches** — AutoGPT / BabyAGI wave is dead in product form. Industry settled on **supervised, bounded, evaluated agents**
4. **Agent app stores / marketplaces** — "promised since 2023, zero enterprise traction"
5. **SWE-bench leaderboard chasing** — benchmarks can be gamed
6. **Microsoft Semantic Kernel** — unless locked into MS enterprise stack
7. **DSPy** — "philosophical merit, niche audience, not a general agent framework"
8. **Horizontal "build any agent" platforms** — Google Agentspace, AWS Bedrock Agents, Copilot Studio: "confusing, slow-shipping, math favors building yourself"
9. **Per-seat SaaS pricing** — "market moved to outcome-based. per-seat is already dead"
10. **Viral HN framework of the week** — wait 6 months

---

## What Actually COMPOUNDS

- **Context engineering**
- **Tool design**
- **Orchestrator-subagent pattern**
- **Eval discipline**
- **Harness > model** ← THE key insight
- **MCP as the protocol layer**

---

## "Harness > Model" — The Critical Insight

> "Swap a good harness onto a mid model, you ship. Swap a great model onto a bad harness, you get an agent that randomly forgets what it's doing. The field is still treating model choice as the interesting decision. It isn't. What's your harness stack looking like?"

**For JCPaid:** This is our entire value proposition. We're not selling a model — we're selling a **harness** (the system that makes the AI actually work reliably for your business). Hermes Agent is the model, but JCPaid is the harness.

---

## JCPaid Positioning Validation

| What's Dead | JCPaid Position |
|---|---|
| CrewAI (breaks in production) | ✅ JCPaid uses supervised, bounded, evaluated agents — exactly what the industry settled on |
| Per-seat pricing | ✅ JCPaid flat $299/mo — outcome-based positioning |
| Autonomous agents (BabyAGI wave) | ✅ JCPaid supervised by client — client stays in control |
| Agent app stores (no enterprise traction) | ✅ JCPaid is a service, not a store |
| "Build any agent" platforms (confusing) | ✅ JCPaid is simple: 1 price, 1 stack, done |
| Framework-chasing | ✅ JCPaid stack is stable: Hermes + The Agency + here.now + holaOS |

---

## Competitive Wake-Up

The AI engineering community is waking up to the fact that **the harness beats the model**. JCPaid's entire story is about the harness:

1. **The Agency** (147 agents) = orchestrator-subagent pattern ✅
2. **here.now** (10GB/client) = context engineering + memory ✅
3. **Solomon Bus** = eval discipline + job tracking ✅
4. **Supervised bounded agents** = exactly what we sell ✅
5. **MCP** = protocol layer ✅
6. **Flat $299/mo** = outcome-based, not per-seat ✅

**This post is ammunition for sales copy.** Every time a potential client says "but what about CrewAI?" or "can't I just use AutoGPT?" — link them to this thread.

---

## Action Items

- [ ] Save post as sales asset / competitor differentiation material
- [ ] Quote "harness > model" in JCPaid landing page
- [ ] Add to SHARED_KNOWLEDGE.md

**Links:**
- Main post: https://x.com/DeRonin_/status/2049613859623677978
- Original list: https://x.com/rohit4verse/status/2049548305408131349
