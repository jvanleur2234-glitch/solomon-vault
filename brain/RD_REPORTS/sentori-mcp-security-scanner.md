# Sentori — MCP-Native Security Scanner

**Source:** https://github.com/TakumaLee/Sentori  
**License:** MIT / BSL-1.1  
**Stars:** ~N/A (new)  
**Date:** 2026-04-23

## What it does
Sentori is a TypeScript-based security scanner designed specifically for the MCP (Model Context Protocol) ecosystem and AI agent toolchains. It targets attack surfaces unique to autonomous agents and MCP servers.

Key features:
- 29 scanners across 7 categories
- Supply chain integrity (postinstall scripts, unsafe serialization, namespace squatting)
- Prompt injection detection (including visual prompt injection in images)
- MCP tool description / registry integrity checks
- Secret leak detection
- Deep scan with OCR for image-based threats
- JSON CI/CD output

## Solomon OS Fit
**INTEGRATE** — MCP security scanner for Hermes Agent. Could be added as a security skill to scan MCP server configurations and detect tool poisoning.

## Recommendation
INTEGRATE — Add as security skill for Hermes MCP integration. Directly addresses OWASP LLM Top 10 risks (prompt injection, tool poisoning, supply chain).
