# RD Report: idan-rubin/browserclaw-agent — Anti-Bot Browser Agent

**Repo:** `idan-rubin/browserclaw-agent`
**License:** MIT | **Language:** TypeScript/Node.js
**Stars:** ~150+ (estimated) | **Forked:** Yes (jvanleur2234-glitch/browserclaw-agent)
**Date:** 2026-04-23

## What It Is

AI-driven browser agent that reads page accessibility snapshots, reasons with an LLM, and executes actions iteratively (up to ~100 steps per run) with a memory scratchpad. Built on top of browserclaw library with anti-bot bypass capabilities.

## Key Features

- **Layered architecture** — LLM-agnostic (Claude, GPT, Gemini, local), swap browser layer
- **Built-in skills** — Anti-bot bypass (CDP-based), Cloudflare Turnstile solving, popup dismissal, loop detection, tab management
- **Domain learning** — each run generates domain-specific skill file stored remotely (MinIO); subsequent runs become more efficient
- **Anti-bot solutions** — OSS anti-bot bypass (no need for paid services)
- Works with browserclaw (the vehicle) vs browser-use's bundled Python stack

## Solomon OS Fit

**SKILL** — Anti-bot and Turnstile solving is a major gap in current ClawLess implementation. This could give Hermes browser automation the ability to handle protected sites. MIT license permits study.

## Recommendation

**SKILL** — Study anti-bot bypass patterns for ClawLess enhancement.