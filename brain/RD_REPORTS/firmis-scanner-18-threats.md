# RD Report: Firmislabs/firmis-scanner — 18+ Threat Categories

**Repo:** `Firmislabs/firmis-scanner`
**License:** Apache-2.0 | **Language:** TypeScript
**Forked:** Yes (jvanleur2234-glitch/firmis-scanner)
**Date:** 2026-04-23

## What It Is

AI-runtime security scanner for AI agents. Detects malicious/dangerous behavior across multiple platforms (Claude Skills, MCP servers, Codex plugins, Cursor) by auditing code surfaces (filesystem, network, shell) and instruction surfaces (SKILL/AGENTS guidance) for 18+ threat categories.

## Key Features

- **268 detection rules** covering credential harvesting, prompt injection, tool poisoning
- **Zero-config use** — run via npx or global npm install
- **Auto-detection** of common agent frameworks (LangChain, CrewAI, AutoGen, MetaGPT)
- Works across Claude Code, Claude Desktop MCP, Codex, Cursor
- Simple JSON configuration and tool commands
- Claims proactive intervention to prevent internal abuse and external manipulation

## Comparison to Sinewave

- **Sinewave ProofLayer** — lightweight, regex-based, 400+ rules, npm install
- **Firmis-scanner** — 268 rules, 18+ threat categories, auto-detects frameworks, Apache-2.0

## Solomon OS Fit

**INTEGRATE** — 18 threat categories and auto-framework detection adds coverage beyond current security tools. Apache-2.0 license.

## Recommendation

**INTEGRATE** — Add to security scanning stack alongside ProofLayer.