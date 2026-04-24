# RD Report: sinewaveai/agent-security-scanner-mcp

**Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner-mcp  
**License:** MIT | **Language:** TypeScript/Node.js  
**Date:** 2026-04-24

## What It Is
Security scanner MCP server for AI coding agents with prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, and auto-fix capabilities.

## Relevance to Solomon OS
- **Critical security layer** for AI agents
- Prompt injection detection (OWASP LLM Top 10 #1)
- Package hallucination prevention
- AST-based vulnerability scanning
- SOC 2 / GDPR compliance evidence

## Key Capabilities
- ProofLayer (lightweight): 400+ rules, regex-based, zero deps
- Full Version: 1700+ rules, AST/taint analysis, cross-file dataflow
- 4.3M+ package verification via bloom filters
- SBOM generation (CycloneDX)
- 30+ rules for prompt injection patterns
- Auto-fix capabilities

## Competitive Analysis
Direct competitor to Snyk agent-scan. More agent-native (MCP-first) approach. Token-efficient scanning.

## Recommendation
**INTEGRATE** — Install as Hermes MCP security skill. Prompt injection protection is essential for production agents.

## License Check
MIT ✅