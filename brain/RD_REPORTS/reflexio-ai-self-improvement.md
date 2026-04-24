# RD Report: ReflexioAI/reflexio

**Fork:** https://github.com/jvanleur2234-glitch/reflexio
**Source:** https://github.com/ReflexioAI/reflexio
**Stars:** ~2.3K+ | **License:** Apache-2.0 | **Language:** Python
**Date:** 2026-04-24

## What It Is
Reflexio is an AI agent self-improvement harness that turns real user interactions into persistent behavioral improvements. It captures user corrections and successful execution paths to create reusable playbooks, enabling agents to learn from each interaction and transfer learned strategies across users without retraining.

**Benchmark claims:** 81% fewer planning steps, 72% less tokens on GDPVal knowledge-work tasks using a Hermes agent with MiniMax-M2.7.

## Key Capabilities
- User profile system for personalized learning
- Playbook extraction from successful agent trajectories
- Playbook aggregation across users
- Success evaluation for quality control
- Transfer learning: corrections propagate to all users without retraining
- Python client, SDK, and CLI integrations

## Relevance to Solomon OS
- **Self-improvement loop:** Reflexio's correction → playbook → aggregation pipeline is exactly what Hermes needs for persistent learning
- **Measured impact:** 81% fewer planning steps is massive — this could cut token costs dramatically
- **Apache 2.0:** Permits direct use in JCPaid commercial product

## Competitive Analysis
Direct competitor to our self-improving agent work (xmaks82, RangeKing). Reflexio's data-driven approach (user corrections → playbooks) vs. our prompt evolution approach — could combine both for maximum effect.

## Recommendation
**FORGE** — Integrate Reflexio's playbook extraction into Hermes self-improvement pipeline. Apache 2.0 allows commercial use. Measured 81% improvement is a strong signal.

## License Check
Apache-2.0 ✅

## Key Files
- `benchmark/gdpval/RESULTS.md` — Full benchmark methodology
- `reflexio/client.py` — Python SDK
- `reflexio/cli/` — CLI tool