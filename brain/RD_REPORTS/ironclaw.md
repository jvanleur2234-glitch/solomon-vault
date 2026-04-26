# RD_REPORT: nearai/ironclaw

**Date:** 2026-04-25
**Repo:** https://github.com/nearai/ironclaw
**License:** MIT OR Apache-2.0
**Stars:** ~2.5K (estimate)
**Language:** Rust (1.92+)
**Clone path:** `/home/workspace/Skills/ironclaw/`

## What It Is

IronClaw is a **Rust-based personal AI assistant** built with security-first principles. Think of it as a self-hosted alternative to commercial AI assistants, with defense-in-depth built into every layer.

**Core architecture:**
- Agent loop → Scheduler (parallel jobs) → Worker (LLM reasoning + tools)
- Orchestrator manages Docker containers for job isolation
- WASM sandbox for untrusted tools (capability-based permissions, no full container overhead)
- Routines Engine for cron/webhook/event-driven background tasks
- PostgreSQL + pgvector for persistence (hybrid search)

## Security Model

IronClaw's differentiator is its layered security:

```
WASM ──► Allowlist ──► Leak Scan ──► Credential ──► Execute ──► Leak Scan ──► WASM
         Validator     (request)     Injector       Request     (response)
```

- **WASM sandbox** vs Docker: lightweight, capability-based isolation
- **Credential injection** at host boundary — secrets never exposed to tool code
- **Endpoint allowlisting** — HTTP only to approved hosts
- **Prompt injection defense** — pattern detection, sanitization, policy enforcement (Block/Warn/Review/Sanitize)
- **AES-256-GCM** secrets encryption
- **Full audit log** of tool executions

## Channels

REPL, HTTP webhooks, WASM channels (Telegram, Slack), Web Gateway (SSE + WebSocket).

## LLM Providers

Built-in: Anthropic, OpenAI, GitHub Copilot, Google Gemini, MiniMax, Mistral, Ollama.
OpenAI-compatible: OpenRouter (300+ models), Together AI, Fireworks AI, vLLM, LiteLLM.

## What We'd Use It For

1. **Hermes security layer** — IronClaw's WASM sandbox + leak scanning + credential injection is exactly what a 24/7 AI agent needs. We could adopt the WASM tool sandbox model for Hermes skills.
2. **Self-hosting stack** — IronClaw is a complete replacement for a commercial AI assistant, running on our own infrastructure.
3. **Docker isolation for client work** — IronClaw's orchestrator/Docker sandbox pattern is the right model for isolating client project work in Hermes.
4. **Prompt injection defense** — The policy enforcement layer (Block/Warn/Review/Sanitize) could be adapted into Hermes rules.

## Comparison to What We Have

IronClaw overlaps with our current Hermes agent concept. Key differences:
- Hermes is Zo-native, IronClaw is standalone Rust binary
- IronClaw has the WASM sandbox model we discussed but never implemented
- IronClaw's Docker orchestrator is production-grade vs our concept stage
- Hermes has deep Zo workspace integration IronClaw lacks

## Recommendation

**🟡 WORTHWHILE** — The WASM sandbox + credential injection + Docker isolation pattern is the most production-grade open-source implementation I've seen for personal AI agents. 

**Next steps:**
1. Extract the WASM sandbox + leak scanner logic as a reference implementation
2. Consider integrating the Docker orchestrator pattern into Hermes for client project isolation
3. The security model (allowlist + leak scan + credential injection) should directly inform Hermes v2's tool execution layer
4. Not a full replacement for Hermes — closer to a reference architecture

## Files

- Repo: `/home/workspace/Skills/ironclaw/`
- Full README: `/home/workspace/Skills/ironclaw/README.md`