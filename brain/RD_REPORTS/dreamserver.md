# RD Report: DreamServer (Light-Heart-Labs)

**Date:** 2026-04-22
**URL:** https://github.com/Light-Heart-Labs/DreamServer
**Stars:** 453
**License:** MIT

## What It Is

DreamServer is an all-in-one local AI stack installer — ONE command gets you 13 pre-wired services running with zero configuration. It's positioned as "Local AI anywhere, for everyone."

### What's Inside the Box

| Service | Purpose |
|--------|---------|
| Open WebUI | Chat interface |
| llama-server | LLM inference engine |
| LiteLLM | API gateway (local/cloud/hybrid) |
| Whisper + Kokoro | Voice STT/TTS |
| **OpenClaw** | Autonomous AI agent framework |
| **n8n** | Workflow automation (400+ integrations) |
| Qdrant | Vector DB for RAG |
| SearXNG | Self-hosted private web search |
| Perplexica | Deep research engine |
| ComfyUI | Node-based image generation |
| Privacy Shield | PII scrubbing proxy |
| Dashboard | GPU metrics, service health |

### Auto-Detection

The installer auto-detects GPU and picks the right model:

| VRAM | Model |
|------|-------|
| < 8GB | Qwen3.5 2B |
| 8-11GB | Qwen3.5 9B |
| 12-20GB | Qwen3.5 14B |
| 20-40GB | Qwen3 30B MoE |
| 40GB+ | Qwen3 Coder Next 80B MoE |

### Bootstrap Mode

Downloads a tiny 1.5B model first → you chat immediately → full model downloads in background → hot-swap with zero downtime.

## How It Compares to Our Stack

| Feature | DreamServer | Solomon OS (ours) |
|---------|-------------|-------------------|
| Agents | OpenClaw | Hermes + Paperclip |
| Workflow automation | n8n | Solomon Bus |
| RAG | Qdrant | Can add |
| Voice | Whisper + Kokoro | We have this |
| Image gen | ComfyUI | We have MoneyPrinterTurbo |
| Web search | SearXNG + Perplexica | Sherlock + holehe |
| Privacy proxy | Privacy Shield | Can add |
| Dashboard | ✅ | ✅ Time Saver Dashboard |
| Windows | Docker/WSL2 | .exe (Tauri) ✅ |

## What We'd Use It For

**STRONG INTEGRATION FIT:**

1. **OpenClaw** — already on our research list. DreamServer has it pre-wired with agents + computer use + privacy shield. We could either:
   - Use their OpenClaw setup as-is (runs via Docker), OR
   - Pull OpenClaw out and wire it into Solomon OS

2. **n8n workflows** — 400+ integrations already built. Instead of building every integration from scratch, we point n8n at our agents and let it handle the app connectivity.

3. **Bootstrap model download** — this is genius. We could add a similar bootstrap mode to JackConnect so users start seeing value immediately while models download.

4. **Privacy Shield** — this is exactly what JackConnect needs for the "AI that never leaks your data" positioning.

## Verdict

**Recommendation: INTEGRATE (selectively)**

We're NOT replacing our stack with DreamServer. But we can cherry-pick:
- OpenClaw (from their stack or ours — same thing)
- n8n for workflow automation
- Bootstrap download pattern for JackConnect installer
- Privacy Shield for trust positioning

This is complementary, not competitive. JackConnect + DreamServer's best pieces = stronger offering.

**Priority:** 🟡 Worthwhile — selective integration, not full adoption
**Action:** Add OpenClaw integration to Paperclip+Hermes plan. Look at n8n for JackConnect workflows.

---
*Created 2026-04-22 | Source: https://github.com/Light-Heart-Labs/DreamServer*