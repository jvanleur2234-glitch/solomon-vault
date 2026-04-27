# RD Report: Firmis-Scanner — AI Runtime Security Scanner

## Summary
Firmis-Scanner by Firmislabs is an AI runtime security scanner for detecting malicious/unsafe behavior in AI agents. 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Zero-config scanning via npx. Supports Claude Skills, MCP servers, Codex Plugins, Cursor. 268 detection rules, no API key required. Apache 2.0.

## What It Does
- **18+ Threat Categories**: Credential harvesting, prompt injection, tool poisoning, etc.
- **Platform Support**: Claude Skills, MCP servers, Codex Plugins, Cursor
- **268 Detection Rules**: Comprehensive threat coverage
- **Zero-Config**: npx or npm install, no API key required
- **Early Intervention**: Prevents dangerous agent behavior before deployment

## Tech Stack
- Language: TypeScript
- License: Apache 2.0
- Latest: Active, 2026-04

## Strategic Fit for Solomon OS

**SKILL** — Zero-config scanner for Hermes skills. No API key = easy onboarding.

Key learnings:
1. **268 Detection Rules**: Threat taxonomy for AgentArmor Studio
2. **Zero-Config**: npx simplicity for fast security assessment
3. **Multi-Platform**: Claude Skills, MCP, Codex, Cursor coverage
4. **No API Key**: Privacy-first scanning without external calls

## Risk/Concerns
- Newer project, community size unknown
- Apache 2.0 (not MIT) — still permissive
- TypeScript-only

## Verdict
STUDY — Zero-config model for Hermes security onboarding. Detection rules taxonomy for AgentArmor Studio Layer 3 (Static Analysis).

## Links
- Repo: https://github.com/Firmislabs/firmis-scanner
- Fork: Not yet forked