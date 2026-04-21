# RD Report: sinewave-agent-security-scanner-mcp

## What It Is
**ProofLayer** — enterprise-grade security scanner for AI coding agents. Detects prompt injection, package hallucination (4.3M+ packages), 1700+ vulnerability rules via AST/taint analysis, LLM-powered semantic code review, SBOM generation, SOC2/GDPR compliance evidence.

## License & Stars
MIT licensed, active repo — no star count in README but high npm download count (v4.x).

## Why It Matters for Solomon OS
- **DIRECT COMPETITOR** to ClawLess (browser automation) and Snyk competitors — this is a security scanner for agentic AI
- Prompt injection firewall blocks adversarial prompts before execution
- Package hallucination detection catches fake dependencies agents might install
- 1700+ security rules with AST + taint analysis = deep code understanding
- LLM-powered semantic code review understands what the project is *supposed* to do
- SOC2/GDPR compliance evidence collection for enterprise clients
- OpenClaw plugin available — matches Solomon's Hermes/OpenClaw stack
- MCP server for Claude Code, Cursor, Windsurf, Cline = universal agent support

## What We'd Use It For
Integrate into Hermes security layer as a pre-execution gate. Every skill/tool invocation gets scanned before running. The SOC2 compliance evidence feature is directly relevant to JCPaid enterprise client's SOC2 audit needs.

## Solomon OS Fit
**INTEGRATE** — core security primitive for the agentic AI stack. The OpenClaw plugin makes this a natural fit for Hermes.

## Risk / Caveats
- Heavy Python dependency for AST analysis
- LLM-powered review requires API key (Claude CLI supported for zero-key use)
- May need custom rules for Solomon's specific skill framework

## Action
Fork to jvanleur2234-glitch ✅ (done). Study AST/taint analysis rules, integrate into Hermes MCP security layer.