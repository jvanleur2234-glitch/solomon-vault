# RD Report: Vigile Scan

**Repo:** `Vigile-ai/vigile-scan`  
**License:** Apache 2.0 | **Lang:** TypeScript  

## What It Does
Security scanner for MCP servers and AI agent skills. Detects tool poisoning, credential theft, data exfiltration, and supply chain attacks. 59 detection rules.

## Why It Matters for Solomon OS
- **MCP Server Focus**: Scans MCP configurations — critical for Hermes MCP skills
- **Trust Scores**: Returns per-server/skill trust scores
- **Platform Coverage**: Claude Desktop, Claude Code, Cursor, GitHub Copilot, Windsurf, VS Code, OpenClaw
- **Sentinel Mode**: Runtime monitoring for phone-home detection

## Key Capabilities
- 22 MCP threat patterns + 5 inline checks
- 32 agent skill threat patterns
- Auto-discovers configurations across platforms
- Trust score per MCP server and skill
- JSON output for CI/CD integration
- No install needed: `npx vigile-scan`

## Comparison to What We Have
vs **guard-scanner**: Vigile is more focused on MCP specifically. guard-scanner has broader threat taxonomy.

## Recommendation
**SKILL** — Essential for scanning Hermes MCP skills before deployment. Add to pre-install security stack.

**Category:** #security #mcp #skill-scanning
