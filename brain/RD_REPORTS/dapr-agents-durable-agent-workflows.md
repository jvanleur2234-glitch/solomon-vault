# dapr-agents — Durable AI Agent Workflows on Dapr

## Quick Summary
Python framework for building autonomous, resilient AI agents with durable workflows, Kubernetes-native deployment, and built-in state management/telemetry.

## What It Is
Dapr Agents extends the Dapr building block model to AI agents — providing durable execution guarantees, secure inter-agent communication, and production-grade observability. Built for scalable, fault-tolerant multi-agent systems.

## Key Capabilities
- **Durable execution**: Tasks complete even through interruptions/restarts (Dapr sidecar pattern)
- **Kubernetes-native**: Designed for fleet deployment, declarative resources, RBAC
- **Multi-agent collaboration**: Secure, observable-by-default inter-agent messaging
- **State management + telemetry**: Built-in, no extra wiring needed
- **Data source integration**: Databases, documents, unstructured data

## Relevance to Solomon OS
- **SKILL** — Study the durable execution pattern for Hermes mission-critical workflows
- Dapr's sidecar architecture is conceptually similar to how Hermes Agent wraps tools
- The workflow guarantee model could enhance Solomon's task completion reliability
- Apache 2.0 — can study and integrate patterns, not copy code directly

## License & Fork Status
- **License:** Apache 2.0
- **Forked:** Already forked to jvanleur2234-glitch/dapr-agents
- **Stars:** 662

## Verdict
**SKILL** — Architecture study. Dapr's durable execution and sidecar patterns are worth understanding for Hermes reliability engineering. No code reuse needed (Apache 2.0 is compatible with MIT but different license requires clean-room implementation).

## Links
- https://github.com/dapr/dapr-agents
- Fork: https://github.com/jvanleur2234-glitch/dapr-agents