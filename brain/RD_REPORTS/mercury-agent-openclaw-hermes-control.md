# RD Report: Mercury Agent — OpenClaw + Hermes + Control (Soul-Driven, Permission-Hardened, Token-Aware)

**URL:** https://github.com/cosmicstack-labs/mercury-agent
**Date:** 2026-04-20
**Platform:** GitHub
**Stars:** 131 (v0.2.0 released TODAY, viral launch)
**License:** MIT

## What It Is
"Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram."

The tagline of the announcement: "OpenClaw had the Idea. Hermes had the Energy. Mercury brings what both were missing: Control."

**21 built-in tools:**
- Filesystem: read_file, write_file, create_file, edit_file, list_dir, delete_file, send_file
- Shell: run_command, approve_command
- Git: git_status, git_diff, git_log, git_add, git_commit, git_push
- Web: fetch_url
- Skills: install_skill, list_skills, use_skill
- Scheduler: schedule_task, list_scheduled_tasks, cancel_scheduled_task
- System: budget_status

**Key features:**
1. **Permission-hardened** — Shell blocklist (`sudo`, `rm -rf /`, etc. never execute). Folder-level read/write scoping. Pending approval flow. Skill elevation with granular `allowed-tools`. "Mercury asks first."
2. **Token-aware** — Daily budget enforcement. Auto-concise when over 70%. `/budget` command to check, reset, override.
3. **Soul-driven** — Personality defined by markdown files you own (`soul.md`, `persona.md`, `taste.md`, `heartbeat.md`). No corporate wrapper.
4. **Multi-channel** — CLI with real-time streaming. Telegram with HTML formatting, file uploads, typing indicators.
5. **Always on** — Run as background daemon. Auto-restarts on crash. Starts on boot. Cron scheduling, heartbeat monitoring, proactive notifications.
6. **Extensible** — Install community skills with single command. Schedule skills as recurring tasks. Based on Agent Skills spec.
7. **Provider fallback** — DeepSeek → OpenAI → Anthropic automatic failover.
8. **Flat-file persistence** — No database. YAML + JSON in `~/.mercury/`.

**Architecture:** TypeScript + Node.js 20+, Vercel AI SDK v4, grammY for Telegram, ESM, tsup build.

## Why It Matters
This is EXACTLY what Solomon OS is trying to build, but Mercury has it production-ready. The announcement says it combines OpenClaw (execution/runtime) + Hermes (self-improvement loop) with "what both were missing: Control."

## What We'd Use It For
1. **Reference architecture for Solomon OS** — clone and study the permission system, budget enforcement, soul files pattern, daemon mode
2. **Fork as JCPaid agent core** — if Mercury is robust enough, fork it as the base for JCPaid's AI agent layer instead of building from scratch
3. **JackConnect integration** — Mercury's permission-hardened tools + approval flow is exactly what JackConnect real estate clients need
4. **Solomon OS patterns to adopt** — Soul files (soul.md, persona.md, taste.md, heartbeat.md) map directly to Solomon OS brain files

## Compares to What We Have
| Feature | Solomon OS | Mercury Agent |
|---------|-----------|---------------|
| Permission system | Manual/AgentArmor | Built-in, hardened |
| Budget/token control | Not explicit | Daily budget, auto-concise at 70% |
| Soul/personality | brain/*.md (ad-hoc) | soul.md, persona.md, taste.md, heartbeat.md |
| Multi-channel | Telegram connected | CLI + Telegram, streaming |
| Always-on | tmux + heartbeat | Daemon mode, auto-restart, auto-start |
| Skills | Hermes 94+ skills | Installable via Agent Skills spec |
| Provider fallback | Not explicit | DeepSeek → OpenAI → Anthropic |
| Self-improvement | SEPL loop (Autogenesis) | Not mentioned (inherited from Hermes) |

## Recommendation
🔴 FORGE — CRITICAL. Clone to /home/workspace/mercury-agent/. Study the architecture thoroughly. This could become the core of JCPaid's agent layer. The permission system + budget enforcement + soul files pattern are exactly what Solomon OS needs.

Key actions:
1. `npx @cosmicstack/mercury-agent` — try it out
2. Clone to workspace: `git clone https://github.com/cosmicstack-labs/mercury-agent`
3. Read ARCHITECTURE.md and DECISIONS.md carefully
4. Map Mercury patterns → Solomon OS brain files
5. Consider forking Mercury as JCPaid agent core (with proper attribution)

Also watch: Mercury is v0.2.0 released TODAY — active development, could become the standard.