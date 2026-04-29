# Self-Memory System (SMS) — Conway & Rubin 2005
## Zo Computer Global Memory Architecture

> "Human memory is not a database. It is a constructive, hierarchical system filtered by active goals."

---

## THE THREE LAYERS

### 1. Lifetime Periods (LTP)
Major chapters of existence. Stable, rare updates.
- "Joseph's AI Business era" (2025–ongoing)
- "Build phase" (early Zo setup)
- "Family/managing relationships"
- "Real estate client work"

### 2. General Events (GE)
Recurring patterns and knowledge. Medium stability.
- "How to run CashClaw audits"
- "HYRVE job search workflow"
- "Stripe payment troubleshooting"
- "Russell Tuna bot maintenance"

### 3. Episodic Details (ED)
Specific moments. High plasticity, decay over time.
- "April 27 session: Built Deal Bundle, Russell upgrade, Huginn"
- "April 28 session: Fixed NVIDIA NIM errors, Polymarket API live"
- "April 28: Hermes Workspace cloned, Self-Memory System architected"

---

## WORKING SELF

The active goal filter. Before every response or action, the Working Self determines:

1. What is Joseph's current objective?
2. Which LTP does this belong to?
3. Which GEs are relevant?
4. What EDs inform this specific moment?

**Rule: Retrieve by GOAL relevance, not semantic similarity.**

---

## INTEGRATION POINTS

### Zo (this AI)
- AGENTS.md — Lifetime periods
- SOUL.md — Working Self (goals, personality)
- Per-conversation memory → Episodic buffer

### Solomon OS
- brain/soul.md — Working Self
- brain/NORTH_STAR.md — Lifetime periods
- brain/LESSONS.md — General events
- raw/telegram_SUMMARY_YYYY-MM-DD — Episodic details

### Hermes
- HERMES_CAPABILITIES.md — General events (learned skills)
- Per-skill memory → Episodic buffer

### Memary (installed)
- Memory stream → Episodic buffer
- Entity knowledge store → General events
- Graph store → Lifetime periods

### Hermes Workspace (NEW — cloned Apr 28)
- brain/RESEARCH_HERMES_WORKSPACE.md — Full integration plan
- solomon-hermes-workspace/ — Frontend UI (Node.js)
- solomon-hermes-agent/ — Backend with WebAPI (Python)

---

## RETRIEVAL HIERARCHY

```
Query → Working Self (active goal)
         ↓
    Filter LTP by relevance
         ↓
    Filter GE by current LTP + goal
         ↓
    Filter ED by current GE + goal
         ↓
    Construct response from filtered set
```

Not "most similar embedding" → "most goal-relevant to current context"

---

## IMPLEMENTATION STATUS

| Layer | Status | Notes |
|-------|--------|-------|
| Lifetime Periods | ✅ In brain files | NORTH_STAR, soul.md |
| General Events | ✅ In brain files | LESSONS.md, DECISIONS.md |
| Episodic Details | ✅ In raw summaries | telegram_SUMMARY files |
| Working Self (Solomon) | ✅ In brain/soul.md | Goals, identity |
| Working Self (Zo) | ✅ In SOUL.md | Active |
| Memary integration | ✅ Installed | Needs hierarchical wiring |
| Hermes Workspace frontend | ✅ Cloned | Node.js :3000 |
| Hermes Agent WebAPI | ✅ Cloned | Python :8642 |
| Hierarchical retrieval | 🔧 In progress | scripts/sms_retrieve.py |

---

*Built: April 28, 2026 — following Conway & Rubin (2005) Self-Memory System*