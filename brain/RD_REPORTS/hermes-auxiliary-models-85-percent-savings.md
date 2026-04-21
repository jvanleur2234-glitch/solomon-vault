# RD Report: Hermes Agent Auxiliary Models — 85% Token Cost Savings

**URL:** https://x.com/Teknium/status/2046374130157764636
**Date:** 2026-04-20
**Platform:** X/Twitter + YouTube (Onchain AI Garage)
**Stars:** N/A (tips post)
**License:** N/A (Hermes Agent feature)

## What It Is
Deep dive on Hermes Agent's 8 hidden auxiliary models that run silently during every chat. Most users don't know about them, but configuring them can cut background task costs by 85%+.

## The 8 Auxiliary Tasks
| Task | Trigger | Cost Impact | Recommended Model |
|------|---------|-------------|-------------------|
| **Compression** | Context hits threshold, fires 10-20x/day for heavy users | 🔴 HIGHEST | Kimi K2, Claude Haiku 4.5, Gemini Flash 2.5 |
| **Flush memories** | Session end (/new, /exit) | 🟡 HIGH | GPT-4o Mini, Gemini Flash |
| **Web extract** | Every web page fetched | 🟡 HIGH | Claude Haiku 4.5 (factual preservation) |
| **Vision** | Every image/screenshot | 🟡 MEDIUM | Gemini 2.5 Flash, GPT-4o |
| **Session search** | Past session summaries | 🟢 LOW | Any fast model |
| **Skills hub** | Query → skill matching | 🟢 LOW | Any fast model |
| **MCP dispatch** | MCP tool calls | 🟢 LOW | Any fast model |
| **Approval** | Risky command classification | 🟢 LOW | Any fast model |

## Key Findings
- Compression alone: Opus = 13¢ vs Kimi K2 = ~2¢ per run = **85% savings**
- Daily heavy use: Opus compression = $60/mo vs Kimi = $9/mo → **$50/mo saved**
- Local models (Ollama, LM Studio): **zero cost** for all auxiliary tasks
- Auto-detect chain: OpenRouter → NewPortal → Codex → Gemini Flash

## Config Location
`~/.hermes/config.yaml` → `auxiliary` section:
```yaml
auxiliary:
  compression:
    provider: openrouter
    model: moonshotai/kimi-k2
  vision:
    provider: openrouter
    model: google/gemini-2.5-flash
```

For local (zero cost):
```yaml
auxiliary:
  compression:
    base_url: http://localhost:11434
    model: qwen3:1.7b
    api_key: placeholder
    timeout: 120
```

## What We'd Use It For
Optimize our Hermes setup (94+ skills running). Current baseline is likely auto-detect → expensive models. Switch to Kimi K2 or local for compression = real monthly savings.

## Recommendation
🟡 FORGE — Configure our Hermes setup with auxiliaries. Set compression to Kimi K2 (OpenRouter) or local model. Update HERMES_CAPABILITIES.md with auxiliary model config. Potential $50+/month savings on our existing Hermes deployment.

**Source:** https://www.youtube.com/watch?v=NoF-YajElIM