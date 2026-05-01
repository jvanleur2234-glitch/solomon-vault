# RD Report: AI Engineering Trends — What's Dead vs What Compounds

**Date:** 2026-04-30
**Type:** Industry Insight / Competitive Positioning
**Recommendation:** INTEGRATE — validates JCPaid architecture + immediate positioning material

---

## What It Is

Ronin (@DeRonin_, CEO of CloseAI) posted Andrej Karpathy's quote: *"90% of what AI twitter tells you to learn will be dead in 6 months"* — then listed 10 things senior AI engineers stopped wasting time on, and what actually compounds.

**10 Things That Are DEAD:**
1. AutoGen/AG2 — moved to community maintenance, releases stalled
2. CrewAI — demos well, breaks in production
3. Autonomous agent pitches (AutoGPT/BabyAGI wave) — dead in product form
4. Agent app stores/marketplaces — promised since 2023, zero enterprise traction
5. SWE-bench leaderboard chasing — can be gamed without solving the task
6. Microsoft Semantic Kernel — not where the ecosystem is heading
7. DSPy — philosophical merit, niche audience
8. Horizontal "build any agent" platforms (Agentspace, Bedrock Agents, Copilot Studio) — confusing, slow-shipping
9. Per-seat SaaS pricing for agent products — market moved to outcome-based
10. The framework that went viral on HN this week — wait 6 months

**What Actually Compounds:**
- Context engineering
- Tool design
- Orchestrator-subagent pattern ← **this is JCPaid's core architecture**
- Eval discipline
- **The harness mindset: harness > model, always** ← **key insight**
- MCP as the protocol layer ← **Hermes uses MCP natively**

---

## For JCPaid — Direct Validation

**1. "Harness > model, always"**
The field is still treating model choice as the interesting decision. It isn't. JCPaid's differentiation is the harness (orchestrator-subagent dispatch, eval discipline, 147-agent fleet, here.now memory layer) — not which LLM underneath.

**2. Orchestrator-subagent pattern**
This is literally what The Agency framework implements. The industry settled on supervised, bounded, evaluated agents — which is JCPaid's model.

**3. Outcome-based pricing**
Per-seat is dead. JCPaid already charges $299/mo flat — aligns with where the market is going.

**4. MCP as protocol layer**
Hermes Agent uses MCP natively. JCPaid's stack aligns here.

---

## Hermes Agent Datasets (Thread)

**Post 2049793654269845933:** Teknium (Nous Research cofounder) sharing a new Hermes Agent dataset for training open models. Made by @mr_r0b0t using:
- Hermes reasoning traces (GLM5.1-K2.5)
- Claude Sonnet 4.6-120000x traces
- MiMo-V2.5-Pro/Hermes reasoning traces
- NVIDIA NeMo Curator for quality filtering
- 28,000 rows, 10 categories

**What this means:** Fine-tuning ecosystem for Hermes-specialized models is actively developing. This is infrastructure-level — relevant if we ever need to specialize a model for client workflows.

**For JCPaid:** Low priority now. Watch for Hermes fine-tune datasets as ecosystem matures.

---

## Key Quote to Remember

> "Swap a good harness onto a mid model, you ship. Swap a great model onto a bad harness, you get an agent that randomly forgets what it's doing."

This is JCPaid's competitive thesis in one sentence.

---

**Recommendation:** INTEGRATE — immediate positioning material. Use "harness > model" as JCPaid tagline differentiator. Update HERMES_CAPABILITIES.md with this validation.
