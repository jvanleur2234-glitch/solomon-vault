# RD Report: snyk/agent-scan

**Date:** April 26, 2026  
**Forked:** Already in workspace  
**License:** MIT  
**Latest:** v0.4.17 (2026-04-22)  

## What It Is
Python-based security scanner for AI agent components (MCP servers, agent skills) on your machine. Detects prompt injections, malware payloads, and 15+ risk types.

## Key Capabilities
- **Auto-discovers** installed agent configurations: Windsurf, Cursor, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Codex
- **Scans MCP servers + skills** for: Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows, Malware Payloads, Untrusted Content, Hardcoded Secrets
- **Cross-platform:** macOS, Linux, Windows
- **Risk-coded results** per agent/OS with clear indicators

## How to Run
```bash
uvx snyk-agent-scan@latest
```

## Solomon OS Fit
**INTEGRATE** — Direct competitor to our AgentArmor Studio security layer. Snyk's agent scan is production-grade with 20+ contributors. Their risk taxonomy (15+ risk types) validates our categorization. Key insight: automatic agent discovery across multiple platforms.

## Threat/Competitor
Snyk has brand recognition and existing customer relationships in security. If they expand agent-scan into a full AgentArmor competitor, they could own the security layer for enterprise AI agents. We need to match their discovery capabilities while adding our unique value (Solomon OS integration, JCPaid billing).

## Action
Study. Reverse-engineer their agent discovery pattern for AgentArmor Studio. Add their risk types to our taxonomy.