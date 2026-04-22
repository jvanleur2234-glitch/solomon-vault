# RD Report: Vercel agent-browser

**Repo:** `vercel-labs/agent-browser` | **Stars:** ~2.8K | **License:** Apache 2.0 | **Updated:** Apr 2026

## What It Is
Native Rust CLI for browser automation designed specifically for AI agents. Fast, lightweight, with accessibility tree and ref-based element targeting.

## Core Value for Solomon OS
- **Native Rust performance** — much faster than Node-based Playwright/Puppeteer approaches
- **AI agent-native** — built for AI agents to control browsers programmatically
- **Snapshot/ref system** — `@e1`, `@e2` element refs for reliable targeting
- **Supports CSS selectors, role/name-based selectors**
- **Screenshot, keyboard, multi-browser support**
- **Already installed locally** as `/usr/local/bin/agent-browser`
- Apache 2.0 licensed ✓

## Security Relevance
Browser automation is a core Hermes capability (OpenClaw/ClawLess competitor). This is a competitor worth watching — faster Rust implementation could influence Hermes browser tooling.

## Integration Potential
- **Already integrated** in this environment
- Could be exposed as Hermes MCP skill for browser automation
- Reference architecture for Hermes native browser automation

## Comparison vs OpenClaw/ClawLess
- **agent-browser:** Rust-native, CLI-first, accessibility tree, refs
- **OpenClaw:** TypeScript, Node ecosystem, broader AI agent integration
- Both are legitimate competitors in browser automation for AI agents

## Verdict: **MONITOR / REFERENCE**
- Fork: NO (Vercel-owned, Apache licensed — reference only)
- RD tracking: YES
- Hermes integration: Potential future MCP skill