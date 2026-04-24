# RD Report: n8n-nodes-mcp

**Fork Status:** Already forked  
**License:** MIT  
**Stars:** ~100 (n8n community node for MCP client)  
**Relevance:** HIGH — MCP integration, n8n workflow automation

## What It Is
TypeScript-based n8n community node enabling AI agents to interact with MCP servers within n8n workflows. Supports HTTP Streamable Transport (recommended) and legacy SSE.

## Key Capabilities
- Connect to MCP servers, access resources, execute tools, use prompts
- HTTP Streamable Transport (recommended) and STDIO
- Three credential options: STDIO, HTTP Streamable, combined
- Security assessed via MseeP badge

## Relevance to Hermes/Solomon
- MCP client integration directly aligns with Hermes's MCP capabilities
- n8n integration enables Hermes to participate in enterprise automation workflows
- Could enable Solomon OS to act as MCP server for n8n orchestrations

## Integration Recommendation
**INTEGRATE** — MCP client implementation patterns could inform Hermes MCP tool development. n8n integration enables broader workflow ecosystem participation.

## Notes
- MIT licensed
- v0.1.37 (Jan 2026)
- 20+ contributors, 29 releases
- Active maintenance