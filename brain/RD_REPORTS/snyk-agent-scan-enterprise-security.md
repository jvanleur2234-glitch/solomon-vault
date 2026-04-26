# RD Report: snyk/agent-scan — Enterprise AI Agent Security Scanner

**Date:** April 26, 2026  
**Repo:** snyk/agent-scan (Apache-2.0)  
**Stars:** ~1.2K | **Language:** Python/TypeScript  

## What It Is
Snyk's official security scanner for AI agents, MCP servers, and agent skills. Auto-discovers installed agent components and analyzes them for security risks.

## Key Capabilities
- **Auto-discovers** MCP configs, agent tools, and skills on your machine
- **Scans multiple agents:** Windsurf, Cursor, Claude, Gemini CLI, OpenClaw, Amp, Amazon Q, etc.
- **Detects 15+ security risks** in MCP servers and agent skills
  - Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows
  - Malware Payloads, Untrusted Content, Hardcoded Secrets
- **Cross-platform:** macOS, Linux, Windows
- **Quick start:** `uvx snyk-agent-scan@latest`

## Relevance to Solomon OS
- **Production security scanning** for all Hermes MCP servers and skills
- **CVE detection** patterns for agent dependency vulnerabilities
- **Multi-agent support** covers entire Hermes ecosystem

## Recommendation
**FORGE** — Deploy as pre-deployment security gate for Hermes skills. Enterprise-grade scanning with Snyk backing.

## Links
- https://github.com/snyk/agent-scan