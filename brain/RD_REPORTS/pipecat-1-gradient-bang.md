# RD Report: Pipecat 1.0 + Gradient Bang

**Date:** April 15, 2026
**Type:** Framework / AI Infrastructure
**URL:** https://x.com/kwindla/status/2044268295692661069
**Source:** X/Twitter — kwindla (Pipecat founder)

---

## WHAT IS IT?

**Pipecat** — Most widely-used framework for voice agents, now at version 1.0 after two years of building. Not just voice agents anymore: it's a framework for **realtime, multi-modal, multi-model AI applications**.

**Subagents v0.1.0** — New library for sub-agent orchestration. Event bus that works locally and over network. Enables running lots of inference loops in parallel with partially shared context.

**Gradient Bang** — Side project / game built with Pipecat + Subagents. Described as "first massively multiplayer, completely LLM-driven game." Retro space trading game where you manage multiple LLMs. Factorio but you cajole your ship AI into tasking other AIs.

Tech stack: Pipecat + Supabase + Vercel. All open source.

---

## WHAT WE'D USE IT FOR

→ **Voice AI for Solomon OS** — Pipecat is the go-to framework for voice agents. Could power voice interfaces for Russell Tuna or Hermes.
→ **Multi-agent orchestration** — Subagents library directly solves the problem of running parallel AI workers with shared context. This is essentially what Solomon Bus tries to do.
→ **Realtime multiplayer AI interactions** — Gradient Bang proves it works at scale.

---

## HOW IT COMPARES TO WHAT WE HAVE

| Aspect | Pipecat | Our Current Stack |
|---|---|---|
| Voice AI | Built-in, production-grade | Parlor Voice AI (forked, basic) |
| Multi-agent orchestration | Subagents library, event-bus architecture | Solomon Bus (custom, simpler) |
| Realtime/multi-modal | Yes, designed for it | Limited |
| Community momentum | Very high (thousands of startups/enterprises) | Niche |
| Open source | Yes | Partial |

---

## VERDICT

🟡 **Worthwhile** — Pipecat's Subagents architecture is interesting but we're not currently building voice-first products. Our Solomon Bus handles basic multi-agent coordination. If we ever build voice into Russell Tuna or expand into voice AI services, Pipecat is the framework to use.

**Action:** Watch. If we do voice AI for clients, use Pipecat. Note the Subagents architecture for future Solomon Bus improvements.

**Flag:** The Gradient Bang game demo is impressive — proof that multi-agent LLM systems can sustain complex, real-time interactions. Worth keeping on radar as the AI-native application paradigm matures.

---

## PRIORITY ASSESSMENT

- 🔴 **Critical** — No. Not a current business priority.
- 🟡 **Worthwhile** — Yes, for future voice AI projects.
- 🟢 **Nice to have** — Current stack covers our needs.

**Recommendation:** SKIP for now. Revisit when/if Solomon OS expands into voice AI services.

---

*Report saved: /home/workspace/solomon-vault/brain/RD_REPORTS/pipecat-1-gradient-bang.md*