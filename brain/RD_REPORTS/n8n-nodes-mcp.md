# RD Report: nerding-io/n8n-nodes-mcp — MCP Server Integration for n8n

**Date:** 2026-04-22  
**Category:** Skill Framework / Agent Integration  
**License:** MIT  
**Stars:** ~3K  
**Fork:** jvanleur2234-glitch/n8n-nodes-mcp  
**URL:** https://github.com/nerding-io/n8n-nodes-mcp  

## What It Does
Enables Model Context Protocol (MCP) server connections from n8n workflows. AI agents in n8n can access external tools and data via MCP standardized protocol.

## Key Features
- Connect to MCP servers, access resources, execute tools, manage prompts
- Two transport modes: HTTP Streamable (recommended) and SSE (legacy)
- STDIO transport for command-line based MCP servers
- 20+ contributors, active maintenance (v0.1.37 as of Jan 2026)

## Solomon OS Fit
**INTEGRATE** — MCP is the backbone of Hermes skill system. This n8n node lets non-programmers build workflows that call Hermes MCP tools. Direct integration path: JackConnect workflow builder → n8n → Hermes MCP tools via this node.

## Status
**INTEGRATE**