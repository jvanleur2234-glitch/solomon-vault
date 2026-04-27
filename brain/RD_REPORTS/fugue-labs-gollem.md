# RD Report: gollem — Type-Safe Go Agent Framework

**Date:** April 26, 2026  
**Repo:** fugue-labs/gollem  
**Stars:** ~900 (est.) | **License:** MIT | **Lang:** Go  

## What It Is
Production-grade Go agent framework with compile-time type safety. Generic `Agent[T]`, multi-provider (Anthropic, OpenAI, Vertex, Gemini), structured output via "final_result" tool pattern, zero-allocation streaming (`iter.Seq2`), guardrails, cost tracking, middleware chain, OTel tracing, team swarms, graph workflow engine, MCP client, and Temporal durable execution.

## Why It Matters for Solomon OS
- **Compile-time guarantees** — eliminates entire categories of Python runtime bugs (pydantic.ValidationError, NoneType errors)
- **Multi-agent team orchestration** — concurrent teammates with task claiming, personality generation, lifecycle management
- **Code mode (monty)** — N tool calls in 1 model round-trip via WASM Python sandbox
- **Graph workflow engine** — typed state machines with conditional branching
- **Cost + usage quotas** — per-model pricing, hard token limits, auto-termination

## Solomon OS Fit
**FORGE** — Fork and adapt as core agent runtime for Solomon OS backend. Go's single-binary deployment maps to Hermes CLI tool pattern. Type safety aligns with AgentArmor Studio's security focus. Multi-agent team swarms match Solomon Bus orchestration needs.

## Key Differentiators vs. Existing
| Feature | gollem | python-agent (Hermes) |
|---|---|---|
| Type safety | Compile-time | Runtime |
| Tool calls | N in 1 round-trip (monty) | Sequential |
| Deployment | Single binary | Python interpreter |
| Cost tracking | Built-in per-model | Via hooks |

## Action Items
- [ ] Fork to jvanleur2234-glitch
- [ ] Study monty code mode for Hermes skill optimization
- [ ] Evaluate for Solomon Bus agent core replacement

## RDD Score
**9.2/10** — Highest production-readiness of any agent framework found this session. Type-safe + single-binary + rich orchestration = ideal for Solomon OS backend.