# dapr-agents — Dapr-Powered Resilient AI Agent Framework

**URL:** https://github.com/dapr/dapr-agents
**Forked:** Already in workspace (/home/workspace/dapr-agents)
**License:** Apache 2.0

## What It Does
Python framework for building production-grade resilient AI agents on Dapr. Durable workflow execution, automatic retries, Kubernetes-native deployment, multi-agent systems with built-in observability, 50+ data source integrations.

## Key Features
- Durable execution workflow engine (guarantees task completion)
- Scale-to-zero architecture (actors pattern, thousands of agents on single core)
- Multi-agent communications with Dapr pub/sub
- Built-in connectivity to 50+ enterprise data sources
- Structured outputs, multi-agent orchestration
- Kubernetes-native deployment
- Python-first, Apache 2.0 licensed

## Why It Matters
Dapr's battle-tested infrastructure combined with AI agent patterns provides production-grade resilience. The actor-based scale-to-zero design is particularly elegant — agents run on-demand, retain state, and are reclaimed when unused. This is production architecture that Hermes should study.

## Solomon OS Fit
**INTEGRATE / SKILL** — Dapr workflow patterns (automatic retry, stateful durability) are directly applicable to Solomon Bus task execution. Kubernetes deployment story maps to enterprise client needs. Workflow engine patterns inform Hermes fault tolerance design. Already cloned for study.

## License
Apache 2.0 (unlike HyperSpace AGI's NOASSERTION, this IS usable)

## RD Report
/home/workspace/dapr-agents/