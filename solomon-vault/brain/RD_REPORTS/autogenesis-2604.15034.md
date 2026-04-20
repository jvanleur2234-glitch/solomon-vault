# RD_REPORT: Autogenesis (arXiv:2604.15034)

**Date:** 2026-04-18
**Source:** https://arxiv.org/pdf/2604.15034
**Stars:** N/A (research paper, not a repo)
**License:** N/A (academic paper)
**Recommendation:** FORGE — Architectural blueprint for Solomon OS 2.0

---

## What It Is

**Autogenesis** is a two-layer self-evolution protocol for AI agent systems. It introduces:
- **AGP (Autogenesis Protocol)** — decouples "what evolves" from "how evolution occurs"
- **AGS (Autogenesis System)** — concrete multi-agent implementation with an agent bus

The core insight: existing agent protocols (MCP, A2A) only solve **connectivity** — they don't solve **state mutation, lifecycle management, or version tracking**. Autogenesis填补 this gap.

---

## Architecture

### Layer 1: RSPL (Resource Substrate Protocol Layer)

Models 5 entity types as first-class, versioned, protocol-registered resources:

| Entity | Description |
|--------|-------------|
| Prompt | Instruction templates |
| Agent | Decision policies |
| Tool | Native scripts, MCP tools, agent skills |
| Environment | Task/world dynamics |
| Memory | Persistent state |

Key properties:
- Resources are **passive** — cannot self-modify
- All mutations go through controlled **RSPL interfaces**
- Explicit **lifecycle** (init, build, run, update, restore)
- **Version lineage** with rollback support
- **Context manager** per entity type handles lifecycle + versioning
- **Server interface** exposes a unified API to external callers

### Layer 2: SEPL (Self-Evolution Protocol Layer)

A closed-loop control system with 5 operators:

```
1. Reflect (ρ)   → Analyze failure traces → generate failure hypotheses
2. Select (σ)    → Translate hypotheses → candidate modifications
3. Improve (ι)   → Apply mutations → candidate state
4. Evaluate (ε)  → Test against objectives + safety invariants
5. Commit (κ)    → Conditional acceptance; rollback on failure
```

The loop runs until convergence or budget exhaustion. Each iteration is traceable, reversible, and auditable.

---

## Why It Matters for Solomon OS

Solomon Bus already has the bones of this:
- ✅ Agent bus architecture (message-based dispatch)
- ✅ Sub-agents that receive tasks via bus messages
- ✅ Skills registered as resources (Hermes)
- ✅ Memory as a separate layer (Solomon Vault)

What's **missing** from our architecture:
- ❌ No version lineage on prompts or skills (can't roll back a bad change)
- ❌ No formal evaluation step (no test-before-commit)
- ❌ No explicit failure hypothesis generation (we know something broke, not WHY)
- ❌ No safety gates (no "this change would break X" checks)

SEPL turns Russell Tuna from a **reactive chatbot** into a **self-improving worker**. That's the AI White-Collar Staffing Agency at scale.

---

## What to Build

Add SEPL to Solomon Bus:

```
When a task fails:
  1. Reflect → log WHY it failed (semantic gradient from failure traces)
  2. Select → pick the best fix from 3 candidates
  3. Improve → write the fix to the skill/prompt/memory
  4. Evaluate → run against test cases + safety invariants
  5. Commit → if it passes, deploy; if not, rollback
```

**Implementation priorities:**
1. Add version lineage to Hermes skills (RSPL layer)
2. Add failure hypothesis logging to Solomon Bus (Reflect step)
3. Build evaluation harness (test cases per skill)
4. Add commit/rollback logic (SEPL Commit gate)

---

## Verdict

🔴 **FORGE** — This is not "inspiring" or "interesting." This is the **architectural blueprint** for Solomon OS 2.0. The protocol-level framing (decoupling what evolves from how evolution occurs) is exactly the right mental model.

The SEPL loop is what takes Russell Tuna from "Zo fixes it when Joseph wakes up" to "Russell Tuna notices the pattern, generates a fix, validates it, and deploys it — all while Joseph sleeps."

**Joseph confirmed: build SEPL into Solomon Bus.**