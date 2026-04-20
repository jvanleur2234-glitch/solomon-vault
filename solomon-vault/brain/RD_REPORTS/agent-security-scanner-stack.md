# agent-security-scanner-mcp + guard-scanner + agentverus-scanner — AI Agent Security Stack

**Already cloned:** `/home/workspace/agent-security-scanner-mcp`, `/home/workspace/guard-scanner`, `/home/workspace/agentverus-scanner`
**License:** MIT/Apache (verify each)
**Category:** security #agent-scanning #prompt-injection

## What They Do

### sinewaveai/agent-security-scanner-mcp
MCP server security scanner. Detects prompt injection, package hallucination (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix capabilities.

### koatora20/guard-scanner
TypeScript scanner for MCP/A2A agentic systems. 364 patterns across 35 threat categories, 27 runtime checks. Detects prompt injection, identity hijacking, SOUL.md tampering, A2A contagion.

### agentverus/agentverus-scanner
MIT-licensed trust/safety scanner for AI agent skills. Analyzes permission contracts, injection detection, dependency assessment, behavioral risk scoring.

## Key Patterns for Solomon Guardian
1. **AST + taint analysis** → scan Hermes skills for malicious code at install time
2. **SOUL.md tampering detection** → critical for protecting Russell Tuna's identity
3. **A2A contagion vectors** → cross-agent attack spread detection
4. **Trust reports** → structured security output for every skill/agent
5. **OWASP LLM Top 10 mapping** → standard compliance

## Verdict
**INTEGRATE** — Stack these scanners. Install guard-scanner as part of Hermes skill installation. Run agentverus-scanner on all incoming skills. agent-security-scanner-mcp for runtime protection.

## Links
- https://github.com/sinewaveai/agent-security-scanner-mcp
- https://github.com/koatora20/guard-scanner
- https://github.com/agentverus/agentverus-scanner