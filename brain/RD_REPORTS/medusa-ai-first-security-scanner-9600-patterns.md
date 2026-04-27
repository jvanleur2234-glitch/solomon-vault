# RD Report: Medusa — AI-First Security Scanner with 9,600+ Patterns

## Summary
Medusa by Pantheon Security is an AI-first security scanner for AI/ML apps, agents, and LLM-based systems. Detects 9,600+ patterns with 200 CVE detections (Log4Shell, Spring4Shell, LangChain RCE). Git repo scanning, IDE integration (VS Code, Claude Code, Cursor, Gemini CLI), multi-format output (JSON, HTML, Markdown, SARIF). Parallel multi-core scanning with caching. MIT, v0.9.0.

## What It Does
- **9,600+ Detection Patterns**: Across 28+ file types
- **200 CVE Detections**: Log4Shell, Spring4Shell, LangChain RCE, repo poisoning
- **Git Repo Scanning**: `medusa scan --git` for AI supply-chain attack detection
- **AI Supply Chain**: Prompt/config/configuration risks
- **IDE Integration**: VS Code, Claude Code, Cursor, Gemini CLI
- **Output Formats**: JSON, HTML, Markdown, SARIF for CI/CD
- **Parallel Scanning**: 10-40x faster with multi-core
- **Smart Caching**: Fast rescans

## Tech Stack
- Language: Python
- License: MIT
- Latest: v0.9.0

## Strategic Fit for Solomon OS

**SKILL** — OWASP LLM Top 10 aligned. IDE integration means developers can scan during coding.

Key learnings:
1. **9,600 Patterns**: Comprehensive coverage for AI agent attack surface
2. **IDE Integration**: Security during development, not just deployment
3. **Git Repo Scanning**: Supply chain attack detection
4. **SARIF Output**: Standardized for GitHub Code Scanning integration

## Risk/Concerns
- Python-only
- Heavy scanning may be slow on large repos
- CVE database needs updates

## Verdict
STUDY — Pattern database informs AgentArmor Studio threat catalog. IDE integration study for Hermes dev tools. Git repo scanning for AI supply chain audit.

## Links
- Repo: https://github.com/Pantheon-Security/medusa
- Fork: Already forked