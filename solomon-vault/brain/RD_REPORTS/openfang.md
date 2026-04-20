# OPENFANG — Research Report
**Date:** April 10, 2026  
**Repo:** https://github.com/RightNow-AI/openfang  
**Stars:** 16.7k  
**Language:** Rust  

## WHAT IT IS
OpenFang is an open-source AI agent orchestration framework written in Rust. Think of it as self-hosted AI agents with built-in channels (Telegram, Discord, CLI), scheduling, multimodal support, and security hardening. It's the backend that lets you run multi-agent systems with persistent context and per-channel configuration.

## KEY FEATURES
- **Channels:** Telegram, Discord, CLI — already wired up
- **Scheduling:** Cron-based scheduling that actually works (v0.5.10 fixed the bug where schedules weren't firing)
- **Context refreshing:** Agent `context.md` re-reads on every turn without restart — live market data updates, etc.
- **Multimodal:** User messages combine text + images into single user_with_blocks messages
- **Security:** Auth fail-closed by default; no api_key = 401 on non-loopback; loopback stays zero-config for local setups
- **Per-channel agent name prefix:** Responses wrapped with `[agent]` for multi-agent channels
- **CLI tools:** `openfang config get`, `openfang hand config <id>` — full configuration management

## HOW IT COMPARES TO SOLOMON OS
| Concern | Solomon OS (current) | OpenFang |
|---|---|---|
| Language | Python/mixed | Rust (faster, safer) |
| Channels | Russell Tuna (Telegram) + Zo | Built-in multi-channel |
| Scheduling | Hermes cron | Built-in, kernel cron (fixed in v0.5.10) |
| Context refresh | Needs restart | Live refresh via context.md |
| Multimodal | Via Zo API | Native |
| Security | Roll your own | Built-in fail-closed auth |

## WHAT STANDS OUT
1. **Rust** — memory safe, fast, production-grade. Could port Solomon Bus to Rust for reliability.
2. **Live context.md refresh** — this is smart. Our agents need to restart to pick up new context.
3. **Scheduling that actually works** — our Hermes cron was broken too. Could adopt OpenFang's scheduler pattern.
4. **16.7k stars** — high credibility, active community.

## RECOMMENDATION
**SKILL / INTEGRATE** — Not a full replacement, but:
- Study the Rust scheduler pattern for potential Solomon Bus upgrade
- Consider OpenFang as the channel layer (Telegram/Discord) if we ever migrate away from Russell Tuna's Python bot
- The live context.md idea is worth stealing for Hermes

## LINKS
- Repo: https://github.com/RightNow-AI/openfang
- Releases: https://github.com/RightNow-AI/openfang/releases/tag/v0.5.10