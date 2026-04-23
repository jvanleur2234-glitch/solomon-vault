# RD Report: microsoft/agent-framework

**Date:** 2026-04-22
**License:** MIT
**Stars:** ~9,700
**Language:** Python + .NET/C#
**Relevance:** 🔴 Critical — Enterprise Agent Orchestration Standard

## What It Is
Microsoft's official multi-language (Python + .NET) agent framework for building, orchestrating, and deploying AI agents and multi-agent workflows. Graph-based orchestration with streaming, checkpointing, human-in-the-loop, and time-travel capabilities.

## Key Capabilities
- **Graph-based workflows** — connect agents + deterministic functions with data flows
- **Cross-language parity** — consistent Python + .NET APIs
- **DevUI** — interactive UI for development, testing, debugging
- **AF Labs** — experimental features (benchmarking, RL, research)
- **Streaming + checkpointing** — durable execution with state persistence
- **Human-in-the-loop + time-travel** — pause, inspect, resume agent workflows
- **OpenTelemetry** — built-in observability and distributed tracing
- **Middleware framework** — pluggable request/response pipelines
- **Multi-provider support** — Anthropic, OpenAI, Azure AI, etc.

## Why It Matters
~9.7K stars makes it one of the most popular agent frameworks. Microsoft's backing = enterprise-grade. The graph-based workflow model + human-in-the-loop + time-travel is directly relevant to Hermes's orchestration needs.

## Comparison
| Feature | Microsoft AF | Hermes |
|---------|-------------|--------|
| Language | Python + .NET | Python |
| Workflow model | Graph-based | Skill-based |
| Time-travel | ✅ Yes | ❌ No |
| Human-in-the-loop | ✅ Yes | Partial |
| Enterprise backing | Microsoft | Community |

## Solomon OS Fit
**STUDY** — Graph-based workflow engine + time-travel debugging are advanced features we should consider for Hermes 2.0. The checkpointing model could inspire Hermes session persistence.

## Action
Already cloned. Study graph orchestration patterns for Hermes workflow engine upgrade.
