# Medusa — AI-First Security Scanner

**Fork:** https://github.com/jvanleur2234-glitch/medusa  
**Source:** https://github.com/Pantheon-Security/medusa  
**License:** MIT  
**Stars:** ~800+  
**Date:** 2026-04-23

## What it does
Medusa is an AI-first security scanner designed to detect AI/ML, agent, and LLM-related risks. It ships with 9,600+ detection patterns and 200 CVE detections (including Log4Shell, Spring4Shell, LangChain RCE, and MCP-related risks).

Key features:
- No-setup usage (pip install and scan)
- Multi-core parallel processing for fast scans
- Built-in repo-poisoning detection across 28+ file types
- Scans entire GitHub repos via --git feature to identify AI supply-chain attacks, prompt-injection risks, MCP tool poisoning
- Outputs: JSON, HTML, Markdown, and SARIF reports
- Optional linter integrations and IDE support (VS Code, Claude Code, Cursor, Gemini CLI)
- Cross-platform (Windows/macOS/Linux)
- Smart caching for faster rescans

## Solomon OS Fit
**INTEGRATE** — Core security primitive for Hermes. MIT licensed. The MCP-related CVE detections and prompt injection scanning directly address current OWASP agentic AI threats. Could be pre-execution gate.

## Key Components
- 9,600+ detection patterns
- 200 CVE detections (including MCP)
- Multi-core parallel processing
- SARIF output for CI/CD
- IDE integrations
- Git repo scanning

## Recommendation
INTEGRATE — Add as pre-execution security scanner to Hermes workflow. MIT license enables direct use.