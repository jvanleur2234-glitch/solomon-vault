# agent-express — Express.js-Style Middleware Framework for AI Agents

**Forked:** jvanleur2234-glitch/agent-express  
**License:** MIT  
**Stars:** N/A (new discovery)  
**Language:** TypeScript

## What It Is

Minimalist middleware framework for building AI agents in TypeScript. Applies the Express.js middleware pattern `(ctx, next)` to AI agents. Three concepts: `Agent`, `Session`, `Middleware`. If you've built an Express app, you already know the mental model.

## Key Features

- **Express.js pattern:** `use()`, `(ctx, next)` interface replaces 15-20 concepts in alternatives
- Built-in safety: budget guards, input/output validation, timeouts, iteration limits, HITL approval
- Observability: structured logs, OpenTelemetry metrics/traces, token tracking, tool usage recording
- Multi-provider: 12+ model/providers (Anthropic, OpenAI, Google, Mistral, Groq, etc.)
- Complexity-based model routing across providers
- Context window compaction with multiple strategies
- MCP integration: connects to MCP servers as tool sources
- HTTP adapter with SSE streaming
- CLI tooling: dev (hot reload) + test (CI-friendly output)
- Zod-based schema validation for model outputs

## Architecture

```typescript
const agent = new Agent({
  model: "anthropic/claude-sonnet-4-6",
  instructions: "You are a helpful assistant.",
})

// Middleware pipeline with 5 onion hooks:
// agent → session → turn → model → tool
```

## Solomon OS Fit

- **Pattern match:** Lightweight alternative to heavy frameworks
- **Use for:** Hermes skills that need middleware composition pattern
- **Why fork:** Express-style mental model for agent middleware is clean and familiar to web devs
- **Competitive:** vs agent-express (this) vs full frameworks (Dapr agents, Gollem)

## RD Status

✅ Forked  
**Recommendation:** SKILL — middleware pattern for Hermes skill composition