# ClawAgents_py — Multi-Provider Lean Agent Framework

## Quick Summary
Production-ready Python framework for building agentic AI systems. ~2,500 LOC with built-in planning, memory, sandboxing, and gateway server. Supports OpenAI GPT-5, Gemini, Claude, Azure, Ollama, vLLM, Bedrock. MIT licensed.

## What It Is
- Lean Python framework drawing from OpenClaw + DeepAgents design principles
- Multi-provider support via pluggable architecture
- Built-in features: planning, memory, sandboxing, gateway server
- Version 6.0.0 (April 2026)
- MIT License

## Key Features
- **4-layer config**: create_claw_agent() params → shell env vars → CLAWAGENTS_ENV_FILE → .env
- **CLI**: `clawagents --init` generates project scaffold; `clawagents --task "..."` for one-off
- **Examples**: 01_openai.py through 08_compare_samples.py for each provider
- **Gateway server**: built-in HTTP interface for agent access
- Sandboxing + planning + memory out of the box

## Solomon OS Fit
- **SKILL** — Study the multi-provider architecture for Hermes skill routing
- Lean ~2500 LOC is a good reference for Hermes simplification
- The 4-layer config pattern is worth stealing for Hermes environment handling
- MIT license → can use code directly

## Stars / Activity
- Single contributor, MIT licensed, 0 open issues
- New (April 2026) — fresh codebase

## Links
- Repo: https://github.com/x1jiang/clawagents_py
- Forked: https://github.com/jvanleur2234-glitch/clawagents_py

## Recommendation
**SKILL** — study architecture for Hermes multi-provider support. Not a priority FORGE unless we need a lean agent framework standalone.