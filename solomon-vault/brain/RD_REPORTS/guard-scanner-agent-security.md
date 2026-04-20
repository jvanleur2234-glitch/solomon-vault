# RD Report: guard-scanner

**Repo**: `koatora20/guard-scanner`  
**Fork**: `jvanleur2234-glitch/guard-scanner-new`  
**Date**: 2026-04-19  
**License**: MIT  
**Stars**: ~2 (novel concept, early)  
**Relevance**: SECURITY / SKILL FRAMEWORKS  

## What It Is
Security scanner for AI agent ecosystems (MCP servers, skills/SKILL.md, autonomous workflows). Detects prompt injection, identity hijacking (SOUL.md overwrites), memory poisoning, and A2A contagion. **364 detection patterns across 35 threat categories + 27 runtime checks.**

## Key Features
- Scans SKILL.md, handler.js, MCP server configs for malicious patterns
- **364 patterns**: invisible Unicode injections (U+200B zero-width chars), SOUL.md identity theft, memory-poisoned conversations, cross-agent contagion
- OWASP-ASI compliance mapping
- Runs as CLI, watch mode, MCP server (for Cursor/Windsurf/Claude Code/OpenClaw)
- Machine-readable finding schema (severity, rule_id, remediation_hint)
- MIT licensed, 362 tests passing

## What We'd Use It For
**Scan every skill/MCP server before it enters Hermes.** This is the guardrails layer for the skill ecosystem — catches poisoned skills, hidden prompt injections, and identity hijacks in SKILL.md files.

## Comparison to What We Have
- **vs firmis-scanner / agentverus-scanner**: guard-scanner focuses specifically on agentic-era attacks (A2A contagion, SOUL.md overwrites) vs general MCP scanning
- **vs medusa**: medusa is SAST-focused (CVE/LangChain RCE); guard-scanner is skill/MCP-specific with deeper agentic threat models
- **Novel angle**: SOUL.md immutability enforcement — checks that agent identity files can't be overwritten

## Recommendation: **SKILL** (Integrate into Hermes skill vetting pipeline)
- Install: `npx @guava-parity/guard-scanner ./skills/ --strict --soul-lock`
- Add to Hermes as pre-flight check before skill installation
- MIT license → fork to jvanleur2234-glitch ✅

## Links
- Fork: https://github.com/jvanleur2234-glitch/guard-scanner-new
- NPM: `@guava-parity/guard-scanner`
- Research: Zenodo 3-paper series (Sanctuary Protocol)
