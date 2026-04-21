# RD Report: phero — Go Multi-Agent Framework

**Date:** 2026-04-21  
**Repo:** henomis/phero  
**URL:** https://github.com/henomis/phero  
**License:** Apache-2.0  
**Stars:** ~low (new)  
**Relevance:** Agent orchestration, multi-agent workflows, A2A protocol, skill system  

## What It Is
A Go 1.25+ framework for building multi-agent AI systems with agent-to-agent communication via A2A protocol, MCP support, and a skills ecosystem defined by SKILL.md files.

## Key Capabilities
- **Multi-agent orchestration** with role specialization and runtime handoffs
- **A2A protocol** — agents exposed as HTTP servers or consumed as local tools
- **LLM middleware** for cross-cutting behaviors
- **Skills system** (SKILL.md-based), memory management, MCP support
- **RAG/vector stores** (Qdrant, pgvector, Weaviate)
- **Tool guardrails** with blocklists/allowlists and timeouts
- **OpenAI-compatible** endpoints + Anthropic

## Relevance to Solomon OS / Hermes
- Go-based = zero dependencies, single-binary deploy (Solomon OS philosophy)
- A2A protocol aligns with Hermes' delegate_tool inter-agent communication
- Skills ecosystem matches Hermes SKILL.md pattern
- MIT/Apache compatible for commercial use

## Verdict
**SKILL** — Fork for Hermes Go agent capabilities. The A2A protocol and skills system are directly applicable to Solomon OS inter-agent communication.