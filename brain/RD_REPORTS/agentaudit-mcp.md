# RD Report: AgentAudit MCP — Security Scanner for AI Agent Packages

**Date:** 2026-04-22  
**Category:** AI Security  
**Source:** web_research (github)  
**Fork Status:** FRESHLY FORKED → jvanleur2234-glitch/agentaudit-mcp

## What It Is
Security scanner for AI agent packages, available as CLI tool and MCP server. Scans MCP servers, AI skills, and packages for vulnerabilities, prompt injections, and supply chain attacks using regex static analysis and deep LLM audits.

## Key Capabilities
- **Quick scan:** Fast regex analysis
- **Deep audit:** 3-pass LLM audit for thorough vulnerability detection
- **Trust Registry:** Lookup prior audits of packages
- **MCP server:** Add to Claude Desktop, Cursor, Windsurf for direct auditing
- Detects: prompt injections, supply chain attacks, vulnerabilities
- Output: Reports with SAFE/Risk status indicators

## Comparison to What We Have
- Similar to: sinewave-agent-security-scanner-mcp, guard-scanner
- Unique: 3-pass LLM audit methodology, Trust Registry concept
- MCP integration for IDE workflows

## Relevance to Solomon OS / JCPaid
- **CRITICAL** — Security is core to JCPaid/Hermes
- Package auditing before skill installation
- Trust Registry for verifying third-party skills
- MCP server for Hermes's skill ecosystem

## Recommendation
**FORGE** — Add to Hermes security stack. Trust Registry concept aligns with skill verification.

## License
MIT

## Stats
- Language: JavaScript/TypeScript
- Status: Active (Feb-Mar 2026 updates)