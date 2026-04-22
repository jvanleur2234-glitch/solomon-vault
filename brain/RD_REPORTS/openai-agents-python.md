# RD Report: openai/openai-agents-python

**Fork:** https://github.com/jvanleur2234-glitch/openai-agents-python
**Date:** 2026-04-22
**Category:** Agent Framework
**License:** Apache 2.0
**Stars:** ~26k (very active)

## What It Is
OpenAI's official Agents SDK — a lightweight, provider-agnostic framework for building multi-agent workflows in Python. Supports OpenAI APIs AND 100+ other LLMs out of the box.

## Key Features
- **Agents:** LLMs with instructions, tools, guardrails, handoffs
- **Sandbox Agents (v0.14+):** Run real work in configurable containers — filesystem access, long-horizon tasks, state persistence
- **Tools + Handoffs:** Agents can delegate to other agents or tools
- **Guardrails:** Input/output safety validation
- **Human-in-the-loop:** Built-in mechanisms for human oversight
- **Sessions + Tracing:** Full observability, conversation history, debugging
- **Realtime/Voice:** gpt-realtime-1.5 support for voice agents
- **Multi-LLM:** Provider-agnostic — works with 100+ LLMs beyond OpenAI

## Why It Matters
- Most popular open-source agent framework (26k stars, massive ecosystem)
- Sandbox Agents are a game-changer for long-running autonomous tasks
- Provider-agnostic = not locked into OpenAI
- Active development, production-ready

## Fit for Solomon OS
- **Competitor to Hermes** in agent orchestration
- **Could integrate** as alternative execution engine
- **Sandbox Agents** align with Solomon Browser's autonomous web navigation
- **MIT/Apache compatible** ✅

## Recommendation: SKILL
Study the Sandbox Agent architecture for Solomon Browser. Fork for experimentation. Not a direct Hermes replacement but excellent reference for multi-agent orchestration patterns.

## Sources
- https://github.com/openai/openai-agents-python