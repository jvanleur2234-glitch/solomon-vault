# RD Report: inngest-self-learning-agent — Durable Self-Learning Agent

**Original:** `inngest/inngest-self-learning-agent` | **License:** MIT | **Stars:** ~500+ | **Lang:** TypeScript

## What It Is
Durable self-learning AI agent built with Inngest + pi-ai. Think/act/observe loop, scores responses (relevance, completeness, tool efficiency, tone), automated evaluation pipeline rewrites and promotes better prompts.

## Key Capabilities
- Self-improving prompts with versioning + A/B testing
- Post-response scoring + attribution to prompt versions
- Guardrails to prevent gaming scoring system
- Evaluation pipeline: rewrites underperforming prompts, promotes stronger ones
- Blocking mechanisms to avoid prompt optimization for the test itself
- Sub-agents + multi-channel (Slack, Telegram, etc.)
- Durable, async workflow with retries + singleton concurrency
- Local processing via Inngest-driven orchestration

## Relevance to Solomon OS
- **Self-Improvement:** Automated prompt evolution from feedback
- **Scoring:** Multi-dimensional quality scoring for agent outputs
- **A/B Testing:** Prompt version experimentation

## Threat Analysis
- MIT licensed, Inngest (credible vendor)
- TypeScript, active development
- Durable execution pattern = production-grade

## Integration Path
```
SKILL: self-learning-agent → Hermes self-improvement with scoring + evaluation
USE CASE: Agents that learn from every interaction and improve prompts automatically
```

**Recommendation:** FORGE — Self-learning pattern with scoring + evaluation. Inngest provides durable execution. Aligns with Evolver patterns. Add to self-evolution stack.