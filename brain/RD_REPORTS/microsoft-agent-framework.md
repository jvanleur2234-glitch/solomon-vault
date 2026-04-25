# Microsoft Agent Framework — Graph-Based Multi-Agent Orchestration (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/microsoft-agent-framework` (MIT)
**Source:** https://github.com/microsoft/agent-framework

## What It Does
Microsoft's multi-language (Python + .NET) agent framework with:
- Graph-based workflows: connect agents + deterministic functions with data flows
- DevUI: interactive development/testing/debugging UI
- AF Labs: RL + benchmarking experimental packages
- Cross-language parity (Python + .NET)
- Human-in-the-loop, streaming, checkpointing, time-travel debugging
- Latest: Python 1.1.0 (Apr 2026), .NET RC1

## Why It Matters for Solomon OS
- Graph-based orchestration is the RIGHT mental model for Hermes skill workflows
- Time-travel debugging directly solves "why did the agent do that?" for enterprise clients
- Cross-language parity means Python skills work alongside .NET tooling
- Active: 9.7k+ stars, Microsoft-backed = long-term maintenance

## Fit: INTEGRATE
MIT licensed. Graph workflow model should map directly to Hermes skill orchestration. Time-travel debugging is a premium enterprise feature worth stealing.

## Action Items
- [ ] Study graph-based workflow implementation
- [ ] Evaluate time-travel debugging for Hermes self-correction logs
- [ ] Consider as orchestration layer vs native Hermes implementation
