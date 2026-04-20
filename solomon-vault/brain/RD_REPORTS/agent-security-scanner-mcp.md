# RD Report: sinewaveai/agent-security-scanner-mcp

**Date:** 2026-04-20
**Fork:** jvanleur2234-glitch/agent-security-scanner-mcp
**License:** MIT
**Category:** AI Security
**Relevance:** 🔴 Critical (Snyk competitor)

## What It Is

Security scanner MCP server for AI coding agents. Detects prompt injection, package hallucination (4.3M+ packages), 1700+ vulnerability rules with AST + taint analysis, auto-fix capabilities. 97.7% precision benchmark.

## Key Capabilities

- **Prompt injection firewall**: Blocks unsafe agent behavior
- **Package hallucination detection**: 4.3M+ package bloom filters
- **AST + Taint analysis**: Deep code understanding across 12 languages
- **1700+ security rules**: Cross-file data flow tracking
- **Auto-fix**: Automatic vulnerability remediation
- **MCP tools**: 11 MCP tools for AI agent integration
- **LLM semantic review**: Intent profiling for security analysis

## Comparison to Solomon OS Stack

- Security scanning → critical for Solomon's agent trust layer
- Prompt injection detection → core defense for Hermes
- AST analysis → could enhance Hermes's code understanding capabilities

## Recommendation

**FORGE** — Snyk competitor with superior precision (97.7%). This is a strategic security capability for Solomon OS. Fork for integration into Hermes security layer. Fork already exists.