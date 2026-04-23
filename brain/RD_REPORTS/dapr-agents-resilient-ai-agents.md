# RD Report: Dapr Agents — Resilient Production AI Agents

**Repo:** https://github.com/dapr/dapr-agents
**Forked:** Already in workspace
**License:** Apache 2.0
**Stars:** Active (v1.0.0 Mar 2026)
**Language:** Python

## What It Is
Builds scalable, resilient AI agent systems on Dapr (battle-tested distributed primitives). Workflow orchestration, security, statefulness, telemetry built-in. Kubernetes-native with durable execution guaranteeing task completion.

## Key Features
- Durable workflow execution (auto-retry, state recovery)
- Scale thousands of agents on single core
- 50+ enterprise data source integrations
- Multi-agent collaboration, observable by default
- Vendor-neutral, Kubernetes-ready
- Agent reasoning + acting + Dapr state/workflows
- Built on Dapr actors (scale-to-zero, ~10ms latency)

## Solomon OS Fit
**Resilience pillar.** Dapr's actor model for agents could inspire Solomon OS agent persistence/scale-to-zero design. Its workflow resilience patterns (retry, recovery) are directly applicable to Solomon's autonomous agents.

## Comparison to What We Have
vs. **agentic-stack** (solomon-os-agentic-stack): Dapr Agents is more production-grade with actual distributed primitives. agentic-stack is more portable/.agent-focused. Dapr fills the "enterprise resilience" gap.

## Recommendation: INTEGRATE
Study Dapr's workflow resilience patterns. Consider how agent-memory persistence could use Dapr's actor model. Not a direct fork target but patterns are valuable.
