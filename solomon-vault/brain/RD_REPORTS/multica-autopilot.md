# RD REPORT: Multica Autopilot

**Date:** April 15, 2026
**Platform:** GitHub / X/Twitter
**URL:** https://github.com/multica-ai/multica
**Status ID:** 2044155895110848739
**Stars:** ~3.7k (growing fast)
**Sentiment:** 🔥 Hot — 41k views, 248 likes in <24h

---

## What It Is

Multica Autopilot is the open-source version of "Routines in Claude Code" — a way to run AI agent routines locally on a schedule or via API. It turns coding agents (Claude Code, Codex, OpenClaw, OpenCode) into team members with task boards, progress tracking, and reusable skills.

**Tagline:** "Your next 10 hires won't be human."
**License:** Open source (MIT?), self-hosted option available

## What We'd Use It For

- Running scheduled AI tasks on Solomon OS (Russell Tuna + Hermes)
- Giving Russell Tuna a proper task board instead of ad-hoc Telegram commands
- Building a proper multi-agent staffing queue system
- Competing with Claude Code's new Routines feature

## Comparison to What We Have

| | Multica | What We Have |
|---|---|---|
| Task/issue board | ✅ Full | ❌ Ad-hoc via Telegram |
| Agent runtime management | ✅ | ❌ Manual |
| Scheduled runs | ✅ | ⚠️ Via Zo agents only |
| Self-hosted | ✅ | ✅ (we self-host everything) |
| Works with Claude Code | ✅ | ❌ (we use Ollama/qwen3) |
| Skills compounding | ✅ | ❌ N/A |

Multica is basically what Solomon Bus is trying to be, but more polished and backed by a team. Our Solomon Bus watcher + task queue is a homemade version of this.

## Risks / Caveats

- Still MVP ("many improvements on the way" per founder)
- We already have Solomon Bus working — switching costs
- Self-hosting requires Docker/brew install on the server

## Verdict

**🟡 WORTHWHILE — evaluate as Solomon Bus upgrade**

This is a serious competitor to what we're already building. The right move: evaluate Multica as a potential replacement for Solomon Bus. It has the board, the skills compounding, the agent management — all things we've been building manually. If it runs on our self-hosted setup, it's a massive upgrade.

The founder (Jiayuan JY Zhang) has credibility — ex-TikTok US, CEO of devv_ai. Worth a deeper dive.

**Action:** Spin up Multica locally, test against Solomon Bus, report findings.

---
*Source: x.com/jiayuan_jy/status/2044155895110848739*
