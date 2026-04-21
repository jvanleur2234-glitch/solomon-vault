# RD Report: Gravesh/sAWc

**Date:** 2026-04-21  
**Slug:** gravesh-sawc  
**Category:** Security Scanner  
**License:** MIT  
**Language:** TypeScript  

## What It Is
Security scanner for AI agent skills — detects malicious behavior in Claude Skills, MCP Servers, Codex Plugins, Cursor Extensions, CrewAI, AutoGPT plugins, and more.

## Key Features
- 242 detection rules across 21 threat categories
- Runtime security scanner analyzing codebases before installation
- Auto-detects agent frameworks (LangChain, CrewAI, AutoGen, MCP Servers, n8n)
- Outputs: JSON, HTML, SARIF formats for CI/CD integration
- BOM generation in CycloneDX format
- CI/CD fail gates support

## Relevance to Solomon OS
- **Direct match:** Already have fork at `/home/workspace/sawc`
- **Security:** Critical for Hermes skill vetting before deployment
- **Integration:** CI/CD scanner for all Hermes skills

## Verdict
**INTEGRATE** — Already forked. Integrate into Hermes skill installation pipeline.

## Priority
🔴 Critical