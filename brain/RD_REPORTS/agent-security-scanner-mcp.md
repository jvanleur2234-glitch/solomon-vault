# RD Report: Agent Security Scanner MCP (Sinewave)

## Summary
Security scanning suite for AI coding agents. Two versions: ProofLayer (lightweight, regex-based, 400+ rules, MIT) and Full Version (AST analysis, 1700+ rules, taint tracking, LLM semantic review). Covers prompt injection firewall, package hallucination detection, vulnerability scanning, auto-fix.

## Relevance to Solomon OS
- **Score: 8/10** — Comprehensive agent security scanning layer
- MIT License, 96 stars
- MCP server integration
- SOC2/GDPR compliance evidence collection
- Already forked to jvanleur2234-glitch/agent-security-scanner-mcp

## Key Capabilities
- Prompt injection firewall
- Package hallucination detection (4.3M+ packages)
- AST & taint analysis
- SBOM generation (CycloneDX)
- LLM-powered semantic code review
- Compliance evidence for SOC2 and GDPR

## What We'd Use It For
Hermes/Solomon security layer — integrate into AgentArmor Studio as a comprehensive scanning capability for JCPaid deployments.

## Comparison to Existing
Snyk Agent Scan covers MCP/skills inventory. Sinewave covers code-level vulnerabilities and compliance. Complementary tools.

## Recommendation
**INTEGRATE** — Pair with Snyk Agent Scan for full security coverage. Fork already exists.
