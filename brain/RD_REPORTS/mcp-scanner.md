# RD Report: Cisco MCP Scanner

**Repo:** `cisco-ai-defense/mcp-scanner` | **Stars:** ~200+ | **License:** Apache 2.0 | **Updated:** Apr 2026

## What It Is
Multi-engine MCP server security scanner combining YARA rules, LLM-as-judge, and Cisco AI Defense inspect API. Scans MCP servers and tools for security findings.

## Core Value for Solomon OS
- **3 scanning engines** — YARA rules, LLM-as-judge, Cisco AI Defense
- **Vulnerable package scanning** — pip-audit integration for CVE/PYSEC/GHSA
- **Behavioral code scanning** — static analysis of MCP server source code
- **VirusTotal binary scanning** — malware detection in bundled files
- **CLI + REST API modes** — flexible deployment
- **Offline/CI-friendly** — JSON scans without live connections
- **OAuth support** for remote MCP servers
- Apache 2.0 licensed ✓

## Security Relevance
Directly competes with guard-scanner, medusa, sinewave scanner. Enterprise-grade scanning with multiple engines. Useful for scanning Hermes MCP integrations before deployment.

## Integration Potential
- **MCP security scanning** for Hermes skill marketplace
- **CI/CD gate** — add to build pipeline for MCP server releases
- **YARA rules** could be integrated into AgentArmor guard-scanner

## Comparison vs guard-scanner/medusa
- **mcp-scanner:** Enterprise-grade, multi-engine (YARA+LLM+Cisco), broad CVE coverage
- **guard-scanner:** TypeScript, 364 patterns, 35 threat categories, OWASP ASI compliance
- **medusa:** 9,600+ patterns, 200 CVE detections, parallel scanning
- All are complementary — mcp-scanner adds enterprise scanning engine

## Verdict: **INTEGRATE / SKILL**
- Fork: YES (Apache 2.0, security tooling fits Hermes ecosystem)
- RD tracking: YES
- Hermes integration: MCP security scanning skill for Hermes marketplace