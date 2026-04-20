# RD Report: sinewaveai/agent-security-scanner-mcp

## Summary
Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

## Relevance to Solomon OS
- **Security layer**: Critical for hardening Hermes against prompt injection and package hallucination attacks
- **MCP integration**: Already MCP-native, fits Hermes architecture
- **Auto-fix**: Self-healing capability we want in Solomon OS defense layer

## Key Features
- Prompt injection firewall
- Package hallucination detection (4.3M+ indexed packages)
- 1000+ vulnerability rules
- AST + taint analysis
- Auto-fix capability
- Multiple scanner modes (full, lite, prooflayer)

## License
Not explicitly stated in summary — verify before forking

## Use for Solomon OS
INTEGRATE — Security hardening for Hermes agentic workflows

## Fork Status
Forked to: jvanleur2234-glitch/agent-security-scanner-sinewave
