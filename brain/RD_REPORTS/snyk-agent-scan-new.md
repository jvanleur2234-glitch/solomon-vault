# RD Report: Snyk Agent Scan v0.4+

**Repo:** `snyk/agent-scan` → cloned to `snyk-agent-scan-new`  
**Fork:** https://github.com/jvanleur2234-glitch/snyk-agent-scan-new  
**License:** Apache-2.0  
**Stars:** 2,253  
**Date:** 2026-04-26

## What It Is
Snyk's enterprise-grade security scanner for AI agents, MCP servers, and agent skills. Auto-discovers installed components and scans for 15+ security risks including prompt injection, tool poisoning, and credential harvesting.

## Key Capabilities
- Auto-discovers MCP configs, agent tools, and skills across macOS/Linux/Windows
- Scans 15+ risk types: E001 (prompt injection), E002 (tool shadowing), ToxicFlows, W007 (credential handling), W008 (hardcoded secrets), E004/E006 for skills
- Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex
- CI/CD integration via SARIF output
- Technical report on agent skill ecosystem threats

## Relevance to Solomon OS
**HIGH** — Enterprise-grade security scanning with Snyk's vulnerability database. Apache-2.0 licensed. Fork is live at jvanleur2234-glitch/snyk-agent-scan-new.

## Use Case for Hermes
- CI/CD security gate for Hermes skill submissions
- Periodic security audits of installed skills
- Supply chain risk detection for MCP servers

## Verdict
**INTEGRATE** — Add to Hermes security skill ecosystem. Snyk brand trust + CVDB + Apache-2.0.