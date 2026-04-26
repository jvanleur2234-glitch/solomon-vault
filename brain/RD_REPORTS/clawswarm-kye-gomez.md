# ClawSwarm — Forked

**Date:** 2026-04-26  
**Forked from:** `The-Swarm-Corporation/ClawSwarm` → `jvanleur2234-glitch/ClawSwarm`  
**Stars:** 2 ⭐ (Apache 2.0)  
**Source:** https://github.com/jvanleur2234-glitch/ClawSwarm

---

## What It Is

ClawSwarm is a lightweight, multi-agent personal productivity OS built on the Swarms framework. It runs a hierarchical swarm of agents (director + specialist workers) that responds to users across Telegram, Discord, and WhatsApp through a unified gRPC gateway. Built by Kye Gomez (The Swarm Corporation / OpenMythos author).

## Architecture

```
Telegram / Discord / WhatsApp
         ↓
  gRPC Unified Gateway
         ↓
  Director Agent (ClawSwarm) — plans + delegates
         ↓
┌────────┼────────┬────────┐
 Resp   Search  Token   Developer
Worker  Worker  Worker     Worker
         ↓
  Telegram Summarizer → reply
```

- **Director:** orchestrates, no tools itself
- **Workers:** Response, Search (Exa), TokenLaunch (Solana), Developer (Claude Code)
- **Memory:** persistent markdown file + RAG for long conversations
- **Transport:** gRPC with optional TLS

## Relevance to Solomon OS

- Multi-channel messaging integration (Telegram, Discord, WhatsApp) — directly relevant to Solomon Bus
- Hierarchical multi-agent architecture — pattern for Solomon OS orchestration
- Swarms framework integration — Kye Gomez's ecosystem
- Could serve as inspiration for a lighter-weight inter-agent messaging layer

## Key Features

- Natively multi-agent (hierarchical swarm)
- One API surface for Telegram + Discord + WhatsApp
- Claude Code as a tool inside the Developer worker
- Persistent memory across channels and restarts
- Optional local model support (vLLM, HuggingFace Transformers)
- Docker + Railway deployment ready

## Skill/Integration Fit

| Solomon OS Component | Fit |
|----------------------|-----|
| Solomon Bus | Medium — gRPC gateway pattern is interesting for inter-agent messaging |
| Hermes Agent | Medium — multi-channel messaging overlap |
| Multi-agent orchestration | High — hierarchical swarm is a proven pattern |
| Claude Code integration | High — already using Claude as a tool |

## Recommendation

**SKILL** — Study the hierarchical swarm architecture and gRPC gateway pattern. The multi-channel messaging gateway could inspire Solomon Bus improvements. The Claude Code integration as a tool is worth examining for Hermes.

The star count (2) is low but this is a fresh fork from Kye Gomez and the Swarms ecosystem is important for Solomon OS research. Keep for architectural study.