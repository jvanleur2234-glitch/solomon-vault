# RD Report: firmis-scanner

**Fork Status:** Already forked  
**License:** Apache-2.0  
**Stars:** ~80 (TypeScript AI agent security scanner)  
**Relevance:** HIGH — AI agent security, credential harvesting detection, MCP patterns

## What It Is
TypeScript-based AI agent runtime security scanner detecting malicious behavior across platforms (Claude Skills, MCP servers, Codex plugins, Cursor). Audits code and instruction surfaces.

## Key Capabilities
- Detects: credential harvesting, prompt injection, tool poisoning
- 268 security rules across threat categories
- Zero-config scanning: npx firmis-cli scan
- Supports: Claude Code, Claude Desktop, Cursor, LangChain, CrewAI, AutoGen, MetaGPT, AutoGPT, LangFlow, n8n
- Auto-detects framework from project files

## Relevance to Hermes/Solomon
- Directly applicable to Solomon OS security requirements
- MCP pattern detection aligns with Hermes's MCP client implementation
- Could be integrated as a pre-deployment security check for Hermes skills

## Integration Recommendation
**INTEGRATE** — Add to AgentArmor Studio security layer. Firmis-scanner's credential harvesting and prompt injection detection patterns should inform Solomon OS security tooling.

## Notes
- Apache-2.0 licensed
- CLI-based, no API key required
- Framework auto-detection for diverse agent platforms