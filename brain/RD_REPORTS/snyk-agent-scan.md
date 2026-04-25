# RD Report: snyk/agent-scan

**Fork:** https://github.com/jvanleur2234-glitch/snyk-agent-scan  
**Upstream:** https://github.com/snyk/agent-scan  
**Stars:** 2,246 | **License:** Apache-2.0 | **Date:** 2026-04-25

---

## What It Is

Snyk Agent Scan discovers and scans AI agent components (MCP servers, skills, harnesses) on a machine for security threats. Detects 15+ risk types including prompt injection, tool poisoning, tool shadowing, toxic flows, and malware payloads hidden in natural language.

## Key Capabilities

- **Auto-discovery** of MCP configs, agent tools, and skills across macOS/Linux/Windows
- **Scans 13+ agent platforms**: Windsurf, Cursor, VS Code, Claude Desktop, Claude Code, Gemini CLI, OpenClaw, Kiro, Antigravity, Codex, Amazon Q, Amp
- **Risk categories**: Prompt Injection (E001/E004), Tool Poisoning, Tool Shadowing (E002), Toxic Flows, Malware Payloads (E006), Untrusted Content (W011), Credential Handling (W007), Hardcoded Secrets (W008)
- **Skills report** (v0.4+): Technical report on emerging agent skill ecosystem threats
- **CI/CD integration** via SARIF output, GitHub Actions support
- **Multi-platform**: Python-based, uv-installable (`uvx snyk-agent-scan@latest`)

## Solomon OS Fit

- **INTEGRATE** — Security gate for Hermes. Apache 2.0 license permits direct code use.
- Direct competitor to ProofLayer/Sinewave scanner stack. Snyk brand gives enterprise credibility.
- Auto-discovery of OpenClaw (Hermes) agent components is directly relevant.
- Deploy as pre-deployment CI/CD gate for JCPaid agent skills.

## Comparison to Existing Stack

| Feature | snyk/agent-scan | ProofLayer | Sinewave MCP |
|---------|----------------|------------|--------------|
| Stars | 2,246 | 96 (MIT) | 96 (MIT) |
| License | Apache 2.0 | MIT | MIT |
| Auto-discovery | 13+ agents | CLI-based | MCP-based |
| Skills scanning | Yes (v0.4+) | Yes | Yes |
| SARIF output | Yes | Yes | Yes |

## Status

**FORKED** — Clone at `/home/workspace/snyk-agent-scan`, fork at https://github.com/jvanleur2234-glitch/snyk-agent-scan
