# hyperev/Hermes Agent v0.2.0 — MCP Client with Native HTTP Transport

**Date:** 2026-04-21  
**Category:** Skill Frameworks (Hermes Ecosystem)  
**License:** MIT  
**Stars:** ~8k (NousResearch/hermes-agent)  
**Source:** NousResearch/hermes-agent/releases/tag/v0.2.0

## What It Does
First-class MCP (Model Context Protocol) client with native support over stdio and HTTP transports, including reconnection, resource/prompt discovery, and sampling (server-initiated LLM requests).

## Key Features
- stdio + HTTP transports
- Reconnection handling
- Resource and Prompt discovery
- Sampling (server-initiated requests)
- MCP tools appear in Hermes Tools UI alongside built-in tools
- Multi-platform, plug-in friendly architecture

## For Solomon OS / Hermes
- Core MCP client implementation reference
- HTTP transport support = remote MCP server connections
- Sampling enables server → agent request initiation

## Recommendation
**INTEGRATE** — MCP client is core Hermes capability. HTTP transport support enables remote MCP integrations.