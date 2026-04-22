# RD Report: agent-security (empowered-humanity)

**Fork:** https://github.com/jvanleur2234-glitch/agent-security  
**Original:** https://github.com/empowered-humanity/agent-security  
**Date:** 2026-04-22  
**License:** MIT  
**Stars:** ~300  
**Relevance:** AI agent security, OWASP ASI coverage

## What It Does

Static analysis + runtime security library for AI agent architectures. Detects prompt injection, credential exposure, MCP server misconfigurations, and code injection attacks.

**Key Features:**
- 176+ detection patterns with taint analysis and context flow tracing
- OWASP ASI + MCP security coverage, CWE mappings
- SARIF output for GitHub Code Scanning
- Runtime guards: SSRF protection, path traversal prevention, execution allowlisting
- 220+ AI-agent-specific patterns, 44 MCP-related patterns
- Pre-commit hooks and GitHub Actions support

## Solomon OS Fit

**INTEGRATE** — Core security gate for Hermes. Directly complementary to existing agent-security-scanner stack. MIT license enables full commercial use. Add to Hermes skill pipeline as a pre-deployment check.

## Risk Assessment

- MIT licensed — clean for commercial use
- Static analysis only — no runtime risk
- Direct competitor to Snyk agent-scan — evaluate coverage overlap

## Recommendation

INTEGRATE — Add to Hermes security skill layer alongside Cybathreat agent-security-scanner and SineWave scanner for defense-in-depth.
