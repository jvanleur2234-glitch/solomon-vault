# RD Report: EvoAgentX — Self-Evolving Agent Framework

**Source:** https://github.com/EvoAgentX/EvoAgentX
**Type:** GitHub Open Source Framework
**Stars:** ~1,000+ (Aug 2025)
**Date:** April 15, 2026

---

## What It Is

EvoAgentX is an open-source Python framework for building, evaluating, and automatically evolving multi-agent workflows. You give it a goal in plain English ("build a stock analysis agent"), and it:

1. Auto-constructs a multi-agent workflow from a single prompt
2. Evaluates agent performance with built-in evaluators
3. Runs self-evolution algorithms (TextGrad, AFlow, MIPRO) to optimize prompts and workflow structure
4. Supports both ephemeral + persistent memory, human-in-the-loop checkpoints, and 20+ built-in tools (browser, code interpreter, database, search, etc.)

Backed by a published arXiv paper (July 2025) and a comprehensive survey on self-evolving agents (Aug 2025).

---

## What We'd Use It For

**Option A — Upgrade Hermes/Russell Tuna:**
EvoAgentX's self-evolution engine could be bolted onto Russell Tuna or Hermes to make them genuinely smarter over time — auto-optimizing prompts, workflow structure, and memory. This is the most aligned with Solomon OS's architecture.

**Option B — New Business: Self-Evolving Agent Studio:**
Package EvoAgentX as a service — businesses upload a goal, EvoAgentX builds + evolves + delivers a working agent. Monthly subscription SaaS.

**Option C — Research / Keep Watching:**
The survey paper (https://arxiv.org/abs/2508.07407) is a comprehensive map of the entire self-evolving agent landscape 2025-2026. High strategic value for understanding where the field is heading.

---

## Comparison to What We Have

| | Solomon OS (Russell Tuna) | EvoAgentX |
|---|---|---|
| **Focus** | Autonomous business ops | Multi-agent workflow evolution |
| **Self-evolution** | Manual skill filing | Automatic algorithm-driven |
| **Memory** | File-based + Hermes skills | Ephemeral + persistent + FAISS |
| **Ease of use** | Already running 24/7 | Python framework, needs hosting |
| **HITL** | Human approval on demand | Built-in interceptor framework |
| **Tool set** | Solomon Bus + 10+ services | 20+ built-in (browser, code, DB) |

**Bottom line:** Russell Tuna is a worker. EvoAgentX is a factory for building workers.

---

## Recommendation: SKILL

**Install EvoAgentX on the Zo and experiment.**
`pip install evoagentx` is one command. Run the quickstart. If it works cleanly with Ollama, it could become the evolution engine for Russell Tuna — making him genuinely self-improving.

Priority: Medium. Not urgent. But if Hermes/Russell Tuna can be made to auto-evolve, that's a genuine competitive moat.

**Also:** Read the survey paper (https://arxiv.org/abs/2508.07407) — it's the strategic map of the entire self-evolving agent space.

---

## Priority Rating

🟡 **WORTHWHILE** — 1K+ stars, clear technical fit with Hermes/Russell Tuna, open source, published research. Good candidate for an experiment weekend.
