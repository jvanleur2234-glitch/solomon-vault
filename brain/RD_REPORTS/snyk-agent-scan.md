# RD Report: Snyk Agent Scan

**Repo:** `snyk/agent-scan`  
**URL:** https://github.com/snyk/agent-scan  
**License:** Apache License 2.0  
**Stars:** Unknown  
**Date:** 2026-04-26

## What It Is
Snyk's open-source security scanner for AI agents, MCP servers, and agent skills. Inventories installed agent components and scans for prompt injections, malware, sensitive data handling, and 15+ risk types.

## Key Capabilities
- Auto-discovers MCP configurations, agent tools, and skills
- Scans 15+ risk types across MCP servers and skills
- Supports multiple agents: Windsurf, Cursor, Claude, Claude Code, Gemini CLI, Amp, Amazon Q, OpenClaw, Kiro, Codex
- Cross-platform: macOS, Linux, Windows
- Issue taxonomy: E001, E004, E006, W007, W008, ToxicFlows, etc.
- SARIF output for CI/CD integration

## Relevance to Solomon OS
**HIGH** — Enterprise-grade security scanning for the entire agent ecosystem. Complements Hermes's own security tooling with Snyk's vulnerability database.

## Use Case for JCPaid/Hermes
- CI/CD security gate for Hermes skill submissions
- Periodic security audits of installed skills
- Supply chain risk detection for MCP servers

## Comparison to Existing
- Snyk brand trust and CVDB integration
- Broader agent support matrix than most competitors
- Apache 2.0 — fully open

## Verdict
**INTEGRATE** — Enterprise security tooling. Fork, document, add to HERMES_CAPABILITIES.

## Action Taken
Already cloned in workspace.