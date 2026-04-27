# j-d0g/self-improving-agent — Self-Improving Financial Analysis Agent

**Forked:** NO — MIT license | **Stars:** ~1.2K | **Lang:** Python

## What It Does

A self-improving financial analysis agent that learns from execution traces to continuously enhance its knowledge base. Two architectures: V1 (per-query improvement cycle) and V2/ACE (batch-based learning with solver → reflector → curator pipeline).

## For Solomon OS

**Use case:** Hermes memory/self-improvement patterns. The cross-session learning loop (Learner logs traces → Improver analyzes → updates knowledge base → next Learner starts smarter) is directly applicable to Hermes skill evolution.

**Integration:** Study `agent/knowledge/` directory for knowledge propagation patterns. The V2 ACE pipeline (Solver → Reflector → Curator) is a clean template for any skill that needs batch-based self-improvement.

## Key Components

- **Learner (Haiku):** Provides answers, keeps session logs
- **Improver (Sonnet):** Reviews logs, identifies errors/patterns, updates knowledge base
- **Knowledge artifacts:** `knowledge/schema.md`, `knowledge/examples.md`, helper functions
- **Benchmarking:** Built-in eval framework comparing learning-on vs baseline

## Comparison

| Repo | Focus | License |
|------|-------|---------|
| j-d0g/self-improving-agent | Financial Q&A + knowledge evolution | MIT |
| xmaks82/self-improving-agent | General 16-agent prompt evolution | MIT |
| pratiksangle01/self-improving-ai-agent | Minimal 3-agent generator→critic→improver | MIT |
| ouroboros | Self-modifying code agent | MIT |

## Verdict

**SKILL** — Financial domain, but the ACE pipeline pattern is transferable to any skill self-improvement. Clone and study `agent/prompts/` and `agent/tracing.py` for Hermes skill evolution patterns.

## Links

https://github.com/j-d0g/self-improving-agent