# Telegram Session Summary — 2026-04-23 Morning

**Date:** April 23, 2026
**Key Theme:** JackConnect build-out + hardware auto-detection

## What We Decided

1. **PetPal app** — fully built at https://josephv.zo.space/petpal
   - Multi-pet support (dogs, cats, birds, fish, rabbits, horses, hamsters)
   - Natural language logging ("I walked buddy" → auto-logs walk)
   - Photo upload per pet
   - Care log, health, schedule, co-parent tabs
   - Lost dog alert button
   - Coming: Watch Once for family members

2. **TimeSaverAI** — Remio aApp Challenge entry built at https://josephv.zo.space/time-saver-ai
   - 5 time categories, streak tracking, weekly summary
   - Telegram bot for logging
   - Share to social

3. **Qwen3.6-27B integration** — added to JackConnect install
   - Claude Code-level coding agent
   - 27B params runs on laptop (beats models 15X larger)
   - Auto-detects hardware → picks best model tier

4. **Hardware auto-detection** — integrated llmfit/whichllm into install script
   - Detects RAM, GPU, VRAM automatically
   - Tier-based model selection (24GB VRAM → Qwen3.6-27B, etc.)
   - No manual model picking needed

5. **DeepSeek TileLang Tile Kernels** — open sourced April 23, 2026
   - Breaks CUDA dependency, supports NVIDIA + Huawei Ascend
   - TileRT: 500-600 tokens/sec on B200 GPU
   - Integrate into JackConnect v2.2 as kernel optimization layer
   - Decision: add to install script as v2.2 upgrade

6. **Replit for Startups** — needs Joseph's info (name, company, website, X handle, what building)

7. **Remio aApp Challenge** — registered, building TimeSaverAI

## Code Created/Modified
- `/jackconnect-dashboard` — live Zo Space route
- `/petpal` — full multi-pet care app (multi-pet, photo upload, natural language log)
- `/time-saver-ai` — Remio challenge app
- `install-jackconnect.sh` v2.1 — auto hardware detection + Qwen3.6-27B

## GitHub Pushes
- jack-connect repo: pushed (811d65a, then v2.2 TileLang update)
- solomon-vault: synced

## Unresolved
- Tauri desktop app build (needs WebView2/GTK libs on cloud server — can't compile Windows .exe here)
- Replit application (waiting on Joseph's info)
- PetPal "Watch Once for family" feature (next session)
- TileLang v2.2 integration (decision pending Joseph's approval)