# RD Report: Dapr Agents — Kubernetes-Native Agent Orchestration

**Date:** 2026-04-22
**URL:** https://github.com/dapr/dapr-agents
**License:** Apache 2.0
**Fork:** https://github.com/jvanleur2234-glitch/dapr-agents

---

## What It Is
Python-based framework for scalable, autonomous AI agent systems. Built on Dapr for agent reasoning, action, and collaboration using LLMs. Emphasizes workflow orchestration, security, statefulness, telemetry, and Kubernetes-native deployment.

---

## Key Capabilities
- Durable execution workflow engine: tasks complete despite interruptions
- Scalable multi-agent workflows across clusters with state recovery
- Resilient task execution with automatic retries
- Kubernetes-native deployment
- Extensive data source integration (databases, unstructured data)
- Security and observability by default
- Vendor-neutral, open-source design

---

## Why It Matters
Dapr (Distributed Application Runtime) is battle-tested in production at thousands of companies. dapr-agents applies that same primitives to AI agents: sidecar model, durable state, service invocation, observability. This IS the production reference architecture for agent runtimes.

---

## Solomon OS Fit
- **SKILL** — Study Dapr's actor model and sidecar pattern for Hermes distributed deployment. Durable execution maps to persistent agent sessions. Kubernetes-native = potential JCPaid cloud deployment.

---

## Recommendation
**SKILL** — Reference architecture study only (Apache 2.0). Dapr sidecar pattern is directly relevant to Hermes distributed deployment.