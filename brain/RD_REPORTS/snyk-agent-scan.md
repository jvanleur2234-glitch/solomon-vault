# RD Report: Snyk Agent Scan

## Summary
Python-based security scanner that inventories and analyzes AI agent components (MCP servers, harnesses/tools, agent skills) for prompt injections, malware, and sensitive data handling. Detects 15+ security risk types across MCP servers and skills.

## Relevance to Solomon OS
- **Score: 9/10** — Direct Snyk competitor for AI agent security — core to JCPaid trust layer
- OWASP LLM Top 10 aligned scanning
- Auto-discovers MCP configurations, agent tools, skills
- Scans popular agents: Windsurf, Cursor, Claude Desktop/Code, Gemini CLI, OpenClaw, Codex, etc.
- Apache-2.0, 2249 stars

## License & Fork Status
- Apache-2.0
- Already forked to jvanleur2234-glitch/snyk-agent-scan

## Key Capabilities
- Auto-discovers MCP configurations and agent skills on host
- Detects: Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows
- Malware payload detection for skills
- Hardcoded secrets / credential handling scanning
- SARIF output for GitHub Code Scanning integration

## What We'd Use It For
Hermes/Solomon security scanning pipeline — integrate into AgentArmor Studio skill for OWASP-aligned agent security audits on JCPaid deployments.

## Comparison to Existing
ClawLess/AgentArmor covers browser automation; Snyk Agent Scan covers the MCP/server attack surface — complementary.

## Recommendation
**FORGE** — Essential security layer for JCPaid. Fork already exists. Integrate with AgentArmor Studio.
