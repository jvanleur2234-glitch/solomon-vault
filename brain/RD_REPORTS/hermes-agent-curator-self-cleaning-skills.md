# RD Report: Hermes Agent Curator — Self-Cleaning Skill Infrastructure

**Date:** 2026-04-30
**Type:** Feature Analysis
**Recommendation:** FORGE — JCPaid long-term memory hygiene pattern. Adopt Curator mindset for client AI employees.

---

## What It Is

Hermes Agent Curator — background "skill janitor" that auto-cleans, consolidates, and archives near-duplicate agent-created skills. Ships with Hermes v0.12.0 "The Curator Release" (today).

**Core behavior:**
- Tracks which skills you actually use
- Auto-archives skills collecting dust after 90 days
- Runs LLM review to suggest merges + cleanup
- Never touches bundled, hub-installed, or pinned skills
- Skills go: active → stale (30d) → archived (90d) — NOT deleted, always recoverable
- Pin keepers: `hermes curator pin my-skill`
- Check status: `hermes curator status`

**Key quote:** *"Your agent creates skills from experience. Curator makes sure that doesn't become a liability."*

---

## Why It Matters for JCPaid

JCPaid AI employees will self-improve by creating skills from client interactions. Without Curator, the skill library becomes a liability — bloat, duplicates, drift. With Curator, it compounds cleanly.

**For JCPaid clients:** Their AI employee gets better over time without drowning in its own output. This is a trust-builder — clients see their AI learning and staying organized.

**Architecture insight (from @novasarc01):** Hermes does act → notice → write → reuse all in one loop. No separate skill-extraction model, no embedding clustering pass, no dedicated replay loop. The same runtime that acts ALSO writes down reusable procedures.

This is agent-mediated procedural distillation. We want this for JCPaid.

---

## What to Do

1. **Clone + study** Curator implementation in Hermes source
2. **Adopt pattern** for here.now / JCPaid skill management
3. **Document** as JCPaid onboarding step: "Your AI employee starts lean, learns fast, Curator keeps it clean"

---

## Status
- Already have Hermes v0.12.0 capabilities in HERMES_CAPABILITIES.md
- Curator = core feature of that release
- Integrate into JCPaid agent lifecycle documentation

**Links:** https://github.com/NousResearch/hermes-agent