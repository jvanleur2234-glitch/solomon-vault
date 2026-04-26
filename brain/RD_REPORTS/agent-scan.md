# snyk/agent-scan — AI Agent Security Scanner

**Fork status:** Not yet forked  
**Date:** April 26, 2026

## What it is
Snyk's official agent security scanner — discovers and scans AI agent components (MCP servers, skills) on your machine for 15+ security risks including prompt injection, malware, tool poisoning, and hardcoded secrets.

## Key capabilities
- Auto-discovers installed agent configurations (MCP servers, tools, skills) across macOS, Linux, Windows
- Scans for 15+ risk categories: prompt injection, tool poisoning/shadowing, toxic flows, malware payloads, untrusted content, hardcoded secrets
- Detects agents: Windsurf, Cursor, Claude, Gemini CLI, Amp, Amazon Q, etc.
- Outputs structured risk findings with codes defined in docs/issue-codes.md
- Apache 2.0 licensed, v0.4.17 (very recent)

## Relevance to Solomon OS
- **SKILL** — AgentArmor Studio competitor. Could be integrated as a scanner skill for Hermes
- **COMPETITOR** — Snyk is an established player; our AgentArmor needs to match this coverage

## Recommendation
STUDY — Understand the auto-discovery patterns and risk taxonomy. Consider fork + skill integration for Hermes Guard.

## Stars
~2.3k | Active (v0.4.17 released 2026-04-22)

## License
Apache 2.0