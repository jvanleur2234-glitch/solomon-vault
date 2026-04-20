# RD Report: Supermemory AI

**Date:** 2026-04-20
**Source:** [GitHub supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)
**Task:** supermemory-001

## What It Is

State-of-the-art memory engine for AI agents — persistent memory, user profiles, hybrid RAG search, connectors to Google Drive/Gmail/Notion/GitHub. **22K stars, MIT license.**

Key differentiator: **Memory ≠ RAG.** Traditional RAG is stateless document chunks. Supermemory tracks facts over time, resolves contradictions, auto-forgets expired info.

## Benchmarks

- LongMemEval: **81.6% — #1** (long-term memory)
- LoCoMo: **#1** (fact recall across conversations)
- ConvoMem: **#1** (personalization and preferences)

## Key Features

| Feature | What It Does |
|---------|-------------|
| `memory` tool | Save/forget facts — AI calls automatically |
| `recall` tool | Search memories by query, returns relevant + profile |
| `context` tool | Inject full user profile at conversation start |
| User profiles | Static (long-term facts) + Dynamic (recent context) — one call ~50ms |
| Connectors | Google Drive, Gmail, Notion, OneDrive, GitHub — real-time webhooks |
| File processing | PDFs, images (OCR), videos (transcription), code (AST-aware) |

## Framework Integrations

Vercel AI SDK, LangChain, LangGraph, OpenAI Agents SDK, Mastra, Agno, Claude Memory Tool, n8n.

## For Solomon OS

**Direct overlap with Icarus (cross-agent memory).** Supermemory gives us:
- Proven memory extraction engine (replaces our manual memory tracking)
- User profile system (complements Jack's client profiles)
- Benchmarked performance (#1 on 3 major benchmarks)
- Connectors to Google Drive/Gmail (Jack's existing stack)

**Plugin already exists for Hermes** — `npx skills add supermemoryai/memorybench` for benchmarking.

## Recommendation

**INTEGRATE (HIGH PRIORITY)**

1. Add Supermemory as Icarus's memory backend — proven, benchmarked, connectors already work
2. JackConnect clients get memory across sessions (Remembers client preferences, deal history, conversation context)
3. Benchmark against our current memory approach using MemoryBench
4. Fork the Hermes plugin — adapt for Solomon OS

## Link Fit

★★★★★ — #memory #icarus #hermes #jackconnect #benchmark

---
*Last updated: 2026-04-20*