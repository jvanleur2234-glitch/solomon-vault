# RD Report: Gollem — Go Agent Framework with Compile-Time Safety

**Date:** 2026-04-22
**URL:** https://github.com/fugue-labs/gollem
**License:** MIT
**Fork:** https://github.com/jvanleur2234-glitch/gollem

---

## What It Is
Production-grade Go agent framework emphasizing compile-time type safety, zero-allocation streaming, and single-binary deployment. Compile-time validation for output schemas, tool parameters, guardrails, and event subscriptions.

---

## Key Capabilities
- Compile-time validation across entire agent stack
- Zero-core dependencies, Go-based (type safety, fast binaries)
- Multi-provider: Anthropic Claude, OpenAI GPT/O, Google Gemini/Vertex, 5+ LLMs
- FuncTool[P] with JSON Schema from typed Go functions
- Guardrails: input/turn-level validation, per-tool result validators, auto-repair
- Observability: OpenTelemetry, structured traces, time-travel debugging
- Agent middleware: Logging, Timing, MaxTokens interceptors
- v0.3.1 (Mar 2026), MIT licensed

---

## Why It Matters
Every other agent framework is Python (runtime errors, type chaos). Gollem brings the rigor of Go's type system to agent development. Compile-time validation of tool parameters and output schemas eliminates entire classes of runtime bugs.

---

## Solomon OS Fit
- **SKILL** — Compile-time safety pattern is aspirational for Hermes (Python-based). Study for design guidance even if can't implement directly. MIT license.

---

## Comparison
| Aspect | Gollem | LangChain | AutoGen |
|--------|--------|-----------|---------|
| Language | Go | Python | Python |
| Type safety | Compile-time | Runtime | Runtime |
| Dependencies | Zero | Many | Many |
| License | MIT | MIT | MIT |

---

## Recommendation
**SKILL** — Study for design patterns. Type-safe tool schema generation is the right idea for Hermes 2.0.