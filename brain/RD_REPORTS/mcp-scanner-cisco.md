# RD Report: mcp-scanner by Cisco AI Defense

## Summary
MCP Scanner by Cisco AI Defense — multi-engine security scanner for MCP servers using YARA rules, LLM-as-judge, and Cisco AI Defense. Apache 2.0.

## What It Does
- Scans MCP servers, tools, prompts, resources for security findings
- Three scanning engines: YARA rules, LLM judgment, Cisco AI Defense inspection
- Vulnerable dependency scanning via pip-audit (CVE/PySEC/GHSA)
- VirusTotal integration for binary/file hashing
- Static analysis for production readiness (timeouts, retries, error handling)
- CLI and REST API server modes
- Offline/CI-friendly JSON output

## Relevance to Solomon OS
- **Security layer for Hermes MCP ecosystem** — directly applicable to JCPaid's MCP server security needs
- Scans MCP tools, prompts, resources, server instructions
- CI/CD integration for agent deployment gatekeeping
- 15+ distinct risk categories across MCP servers and agent skills

## License
Apache 2.0

## Stars / Activity
~Cisco-backed, active development (v4.6.0 Apr 2026)

## Recommendation
**INTEGRATE** — fits directly into Hermes MCP security posture. Fork to jvanleur2234-glitch for internal use.

## Links
https://github.com/cisco-ai-defense/mcp-scanner