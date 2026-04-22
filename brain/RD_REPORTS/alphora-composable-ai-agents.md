# alphora — Production Python Agent Framework

**URL:** https://github.com/jvanleur2234-glitch/alphora
**Forked from:** https://github.com/opencmit/alphora
**License:** Apache-2.0 | **Stars:** ~500+ | **Language:** Python

## What It Does
Full-stack Python framework for production AI agents. Agent orchestration (ReAct, Plan-Execute, hierarchical), tool execution, memory management, secure code sandbox, skills ecosystem, streaming, deployment.

## Key Features
- Agent orchestration: ReAct, Plan-Execute, hierarchical derivation
- Built-in tool system with parallel execution, LLM load balancing (round-robin/random)
- Memory processor pipeline with tagging, undo/redo, observability hooks
- Secure code sandboxing (local/docker/remote)
- Skills ecosystem for extensibility
- Typed streaming (SSE) for results, charts, SQL outputs
- Rich prompt engine (Jinja2, parallel prompts, auto-continuation)
- One-line deployment via `publish_agent_api`, OpenAI-compatible interfaces

## Solomon OS Fit
**SKILL** — alphora's sandbox + skills architecture mirrors Hermes skill system. Plan-Execute pattern is good for complex task decomposition. Apache-2.0 permits code study. Python-based aligns with existing Solomon OS stack.

## Recommendation
SKILL — Study sandbox execution and skills ecosystem architecture for Hermes enhancement.