# Hermes Vault v0.1.0 — RD Report
**Date:** April 19, 2026
**Source:** https://x.com/tonysimons_/status/2045713413565718810
**Repo:** https://github.com/asimons81/hermes-vault/releases/tag/v0.1.0

## What It Is
Local-first credential vault, scanner, and broker for NousResearch Hermes agents. Catches plaintext secret leaks, kills credential sprawl, manages agent auth securely.

## Key Features
- Scans Hermes paths for leaks/duplicates
- Ephemeral TTL env vars
- SKILL.md generator
- SQLite + passphrase vault
- pip install — simple setup
- Hermes-native integration

## Comparison: Hermes Vault vs OneCLI

| | Hermes Vault | OneCLI |
|---|---|---|
| Approach | Local-first, Hermes-native | Rust proxy/gateway |
| Pros | Tight Hermes integration, leak prevention, simple pip install | Agents never see real keys, placeholders + transparent injection, host/path scoping |
| Cons | Secrets briefly in agent env, very new (v0.1), Python-based | Proxy setup required, Docker-focused |
| Best for | Tight Hermes integration | Max isolation in any setup |

## Relevance to Solomon OS
- Plug directly into Solomon Guardian's credential security layer
- Critical for scaling multi-agent auth across JackConnect, Russell Tuna, and Solomon Bus
- Related: Hermes Studio (github.com/JPeetz/Hermes-Studio) — community Hermes tool ecosystem emerging
- 11,900 views, 236 likes in 14 hours — fast-growing in Hermes ecosystem

## Recommendation
**SKILL** — Build Solomon OS credential module inspired by Hermes Vault patterns.
