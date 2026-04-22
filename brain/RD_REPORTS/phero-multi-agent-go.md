# Phero — Go Multi-Agent Framework (A2A Protocol)

**URL:** https://github.com/jvanleur2234-glitch/phero
**Forked from:** https://github.com/henomis/phero
**License:** Apache-2.0 | **Language:** Go (1.25+)

## What It Does
Modern Go framework for multi-agent AI systems. Agent orchestration with role specialization, coordination, runtime handoffs. A2A protocol support, OpenAI-compatible + Anthropic, MCP integration.

## Key Features
- Multi-agent workflows with role specialization + runtime handoffs (`Result.HandoffAgent`)
- A2A protocol: expose agents as HTTP servers, call remote agents as local tools
- LLM abstraction: OpenAI-compatible + Anthropic, multimodal (text/images/audio)
- Speech tools: transcriber + speech synthesizer
- LLM middleware: reusable cross-cutting behaviors
- Function tools from Go functions with automatic JSON Schema generation
- RAG: built-in vector storage + semantic search (Qdrant, pgvector, Weaviate)
- Skills system with `SKILL.md` files
- MCP support as agent tools
- Tool guardrails: Bash blocklist/allowlist, timeout, safe-mode

## Solomon OS Fit
**SKILL** — Phero's A2A protocol + runtime handoff patterns are directly relevant to Solomon Bus inter-agent communication. Go-based aligns with Bonsai/Thoth/RustDesk Rust stack. Apache-2.0 allows code study.

## Recommendation
SKILL — Study A2A protocol and runtime handoff patterns for Solomon Bus enhancement.