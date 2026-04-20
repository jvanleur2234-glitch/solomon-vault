# RD Report: Hermes Agent by Nous Research

**Date:** 2026-04-19
**Type:** Open Source AI Agent Framework
**Recommendation:** FORGE — Integrate architecture + skills system into Solomon OS

---

## What It Is

Hermes Agent is an open-source AI agent built by Nous Research (the same team behind Hermes 3 8B/70B/405B language models). It's a general-purpose agent framework with a self-improving loop — it creates skills from experience, improves them during use, persists knowledge, searches past conversations, and builds user models across sessions.

**Key Stats:**
- 30-minute deploy on $5 VPS
- 16 messaging platform gateway (Telegram, Discord, Slack, WhatsApp, Signal, Email, etc.)
- Self-hosted, open source (MIT license)
- Just overtook OpenClaw in weekly GitHub stars
- Compatible with agentskills.io open standard

---

## Core Architecture

### Agent Loop
- Tool calling with 40+ built-in tools
- Skill system (procedural memory) — agents create skills after complex tasks
- Honcho dialectic user modeling
- FTS5 session search with LLM summarization
- Cross-session memory persistence

### Messaging Gateway
- Telegram, Discord, Slack, WhatsApp, Signal, Email from single gateway
- Voice memo transcription
- Cross-platform conversation continuity
- Runs headless on VPS, you talk to it from any platform

### Scheduling
- Built-in cron scheduler with delivery to any platform
- Daily reports, nightly backups, weekly audits in natural language

### Terminal Backends
- Local, Docker, SSH, Daytona, Singularity, Modal
- Daytona/Modal = serverless persistence (hibernates when idle, wakes on demand, near-zero cost between sessions)

---

## How It Compares to What We Have

| Feature | Hermes Agent | Solomon OS (ours) |
|---|---|---|
| Skills system | ✅ Yes — procedural memory, self-improving | ✅ Hermes has skills, we have Solomon Skills |
| User modeling | ✅ Honcho dialectic | ⚪ We have JackConnect personas |
| Messaging gateway | ✅ 16 platforms | ✅ Telegram connected, more available |
| Cron/scheduling | ✅ Built-in natural language | ✅ Zo Automations |
| Memory | ✅ FTS5 + LLM summarization | ⚪ Solomon Vault (RAG-style) |
| Local LLM | ✅ Ollama-compatible | ✅ Ollama on phone |
| Open source | ✅ Full MIT | ✅ Solomon OS is open |
| Self-improving | ✅ Yes — skill creation from experience | ✅ Personal OS roadmap addresses this |
| Skill marketplace | ❌ No | ⚪ Solomon Skills marketplace planned |

**Key differentiator Hermes has:** Built-in RL trajectory generation, Atropos RL environments, trajectory compression for training next-gen tool-calling models.

---

## What We'd Use It For

1. **Skills architecture reference** — Hermes Agent's skill creation and self-improvement loop is the most mature open-source implementation. We should model Solomon Skills on this pattern.

2. **Messaging gateway** — If we integrate Hermes's multi-platform gateway into Solomon OS, Solomon Air could reach users on every platform simultaneously.

3. **Trajectory compression** — Their RL training pipeline for improving tool-calling models could feed into our Personal OS self-improvement engine.

4. **Deploy anywhere** — Hermes's Daytona/Modal backend pattern (serverless hibernation) is exactly how Solomon OS should scale per-user instances.

5. **Agentskills.io compatible** — If we align Solomon Skills with this standard, we get interoperability with the broader open agent ecosystem.

---

## NOTABLE Features to Steal

- `/skills` browse, `/compress` context reduction, `/usage` cost tracking
- Skill self-improvement during use (skills get better the more you use them)
- Agent-curated memory with periodic nudges to persist knowledge
- Personality system (`/personality [name]`) — similar to our Russell personas
- `hermes claw migrate` — OpenClaw migration path shows how to do persona/memory portability

---

## Recommendation

**FORGE** — Clone the repo, study the skills system and self-improvement loop in detail, and integrate the best patterns into Solomon OS. The messaging gateway alone is worth integrating. The RL training pipeline is valuable for building our Personal OS self-improvement engine.

This is directly complementary — Hermes Agent is the kind of thing Solomon OS should seamlessly support and integrate with, not compete against.
