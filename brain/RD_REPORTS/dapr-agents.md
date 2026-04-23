# RD Report: dapr/dapr-agents

**Date:** 2026-04-22
**License:** MIT
**Stars:** ~655
**Language:** Python
**Relevance:** 🟡 High — Production-Grade Agent Orchestration

## What It Is
Build scalable, autonomous AI agents with built-in workflow orchestration, security, statefulness, and telemetry. Built on top of Dapr for distributed system primitives.

## Key Capabilities
- **Scales to thousands of agents** — efficient single-core execution with Dapr-managed distribution
- **Durable workflow engine** — guaranteed task completion despite interruptions
- **Kubernetes-native** — declarative deployment, auto-scaling
- **Data-source integration** — 50+ data sources (databases, documents, unstructured)
- **Multi-agent collaboration** — secure, observable inter-agent communication
- **OpenTelemetry** — built-in tracing, metrics, logging
- **v1.0.0 released** — March 19, 2026, production-ready

## Why It Matters
Dapr's proven distributed system primitives (state management, pub/sub, bindings) applied to AI agents. The durable workflow guarantee + Kubernetes-native deployment fills a gap in our current stack.

## Comparison
| Feature | Dapr Agents | Hermes |
|---------|-------------|--------|
| Workflow durability | Built-in Dapr | Custom |
| Scaling model | Kubernetes-native | Process-based |
| State management | Dapr state stores | SQLite |
| Agent discovery | Dapr service invocation | Manual |

## Solomon OS Fit
**STUDY** — Durable workflow + Dapr state management patterns could enhance Hermes reliability. The Kubernetes deployment model is relevant for Solomon OS enterprise scaling.

## Action
Already cloned. Study Dapr state management + durable workflow patterns.
