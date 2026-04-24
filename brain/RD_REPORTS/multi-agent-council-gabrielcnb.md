# RD Report: Multi-Agent Council (gabrielcnb)

**Fork:** https://github.com/jvanleur2234-glitch/multi-agent-council
**Source:** https://github.com/gabrielcnb/multi-agent-council
**License:** MIT
**Language:** Python/TypeScript
**Stars:** ~300

## What It Is
Claude Code plugin that orchestrates multi-LLM debates via Perplexity Pro (single subscription → GPT/Gemini/Claude/Nemotron/Sonar). P2P debate (Round 1 parallel → Round 2+ reactions → Claude verdict). SQLite-backed persistent memory with FTS5. Real-time SSE dashboard.

## Key Features
- **Playwright trick:** Uses browser session on Perplexity Pro to access all models via single $20/mo subscription
- **Persistent memory:** SQLite + FTS5, recalls past debates when relevant topics reappear
- **Multi-room:** Each Claude Code window gets isolated room (project dir + PID)
- **Code review:** Parallel model review with automatic Round 2 reconciliation if severity assessments diverge
- **Tools:** llamar_conselho, ask_model, debate, code_review, vote, remember, recall_memory, get_report

## Solomon OS Fit
**SKILL** — Novel cost model (Perplexity Pro subscription = all models). Could inspire Hermes multi-model deliberation without per-token costs. MIT license.

## Comparison to Existing
- Cheaper than API-key-per-model approach (single Perplexity subscription)
- Better persistent memory than llmcouncil (FTS5 vs basic)
- More Claude Code-native than llmcouncil

## Action
Forked. Monitor Perplexity browser-auth model access pattern.

**Recommendation:** SKILL — study cost model for potential multi-model deliberation without per-token API costs