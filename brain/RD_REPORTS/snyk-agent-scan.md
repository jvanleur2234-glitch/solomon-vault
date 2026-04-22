# RD Report: Snyk Agent Scan — Agent Security Inventory & Scanner

**Date:** 2026-04-22
**URL:** https://github.com/snyk/agent-scan
**License:** Apache 2.0
**Fork:** https://github.com/jvanleur2234-glitch/agent-scan

---

## What It Is
Snyk's open-source security scanner for AI agents, MCP servers, and agent skills. Auto-discovers installed agent components on the machine, inventories them, and scans for prompt injections, malware payloads, hardcoded secrets, and sensitive data handling risks. Supports 15+ distinct security risk categories.

---

## Key Capabilities
- Auto-discovers MCP configurations, agent tools, agent skills
- Scans agents: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex, etc.
- 15+ distinct security risks detected:
  - MCP: Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows
  - Skills: Prompt Injection, Malware Payloads, Untrusted Content, Credential Handling, Hardcoded Secrets
- Technical report on emerging threats of the agent skill ecosystem
- Python-based, `uvx snyk-agent-scan@latest` one-liner run
- Apache 2.0 licensed

---

## Why It Matters
Every AI agent deployment needs a security inventory. Before you can secure agents, you need to know what's installed. This tool does that automatically across the entire agent ecosystem on a machine. OWASP Agentic Top 10 validates this is a critical need for 2026.

---

## Solomon OS Fit
- **INTEGRATE** — Core security primitive for JCPaid. Pre-deployment audit for every Hermes/OpenClaw installation. Maps to JCPaid enterprise client compliance needs (SOC2, pen testing). Already forked.

---

## Recommendation
**INTEGRATE** — Add as mandatory pre-flight check to Solomon OS deployment. Run on every new client onboarding.