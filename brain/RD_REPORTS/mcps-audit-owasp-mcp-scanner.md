# mcps-audit — OWASP MCP Server Scanner (April 24, 2026)

## Summary
Free OWASP CLI tool for scanning MCP server code and AI agent code against the OWASP Agentic AI Top 10 and MCP Top 10. Generates professional PDF reports with MITRE ATT&CK mappings.

## What It Does
- `npx mcps-audit ./my-agent` — scan any AI agent or MCP server
- Maps findings to OWASP Agentic AI Top 10 (AS-001 to AS-012)
- Includes: dangerous code execution, hardcoded credentials, excessive permissions, prompt injection from file input, known CVEs (SQL/XSS/command), sandbox escapes, missing lockfiles, auto-approve bypass, unsafe output, no logging, risky HTTP exfiltration, unauthenticated endpoints
- Severity: LOW to CRITICAL per rule
- Outputs PDF with remediation guidance

## Why It Matters Now
- MCP servers are the primary integration layer for Hermes — security here is critical
- mcps-audit is from OWASP itself — the authoritative voice on agentic AI security
- Static pattern-based scanning is fast and automatable in CI/CD pipelines

## Solomon OS Fit: **FORGE**
- Pre-installation security gate for all Hermes MCP servers
- Integrate into hermes-skill-factory and hermes-agent installer
- SOC 2 compliance evidence for OWASP mappings

## License: MIT (inferred from OWASP org)
## Source: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/issues/805