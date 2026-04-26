# clawagents_py — Production-Ready Python Agent Framework (MIT)

## Quick Summary
Lightweight (~2,500 LOC), production-ready Python agent framework with multi-provider support (OpenAI, Gemini, Claude), built-in planning/memory/sandboxing, and gateway server.

## What It Is
A lean, full-stack agent framework for building autonomous, tool-using LLM agents. Supports GPT-5, Gemini, Claude out of the box with a pluggable provider architecture. Designed for reduced complexity compared to similar projects.

## Key Capabilities
- **Lightweight**: ~2,500 LOC, single primary contributor
- **Multi-provider**: OpenAI, Gemini, Claude, Azure OpenAI, Ollama, vLLM, Bedrock
- **Built-in**: Planning, memory, sandboxing, gateway server
- **Environment config**: .env → CLAWAGENTS_ENV_FILE → shell vars → create_claw_agent() params (4-priority override system)
- **Quick start**: `clawagents --init` generates .env, run_agent.py, AGENTS.md
- **CLI one-liner**: `clawagents --task "your task"` for quick execution

## Relevance to Solomon OS
- **SKILL** — Study the 4-priority environment config pattern for Hermes
- The planning/memory/sandboxing combo is core to what Hermes does
- MIT licensed, 2500 LOC is clean and readable
- Multi-provider support parallels Hermes's provider routing

## License & Fork Status
- **License:** MIT
- **Stars:** ~50 (estimated, not in top repos)
- **Cloned:** Already at /home/workspace/clawagents_py

## Verdict
**SKILL** — Clean reference implementation. The environment config priority system is worth studying. The planning/memory/sandboxing pattern is complementary to Hermes but not novel enough to fork.

## Links
- https://github.com/x1jiang/clawagents_py