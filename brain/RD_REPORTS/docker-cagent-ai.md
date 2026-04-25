# RD Report: Docker Agent (cagent) — Docker CLI AI Agent Plugin

**Fork:** https://github.com/jvanleur2234-glitch/docker-cagent-ai  
**Source:** https://github.com/docker/cagent  
**Date:** 2026-04-25  
**License:** Apache 2.0  
**Language:** Go  
**Stars:** Unknown (new discovery — Docker official)  

## What It Does
Docker CLI plugin (`docker agent`) for building, running, and sharing AI agents via declarative YAML. Multi-agent teams, any MCP server, model-agnostic (OpenAI/Anthropic/Gemini/Bedrock/Mistral/xAI/Docker Model Runner), RAG with BM25+embeddings+hybrid search+reranking, OCI registry packaging and distribution.

## Key Features
- **YAML-based agent definitions** — declarative, versionable, shareable agent configs
- **Multi-agent orchestration** with automatic task delegation and team composition
- **Model-agnostic** — 8+ providers supported, hot-swap LLMs without code changes
- **Built-in tools:** think/todo/memory reasoning tools, RAG pipeline (BM25 + embeddings + reranking)
- **MCP server integration** — connect any MCP server as tool source
- **OCI registry push/pull** — package agents and distribute via standard container registries
- **Docker-native deployment** — `docker agent` command, zero infrastructure to manage

## Solomon OS Fit
**INTEGRATE** — Docker-based agent packaging directly maps to JCPaid deployment story. RAG pipeline (BM25+embeddings+reranking) could replace/enhance Hermes knowledge retrieval. YAML config pattern maps to Hermes skill manifests. Apache 2.0 permits direct code use.

## Competitive Analysis
- **vs. Hermes:** YAML declarative + Docker packaging vs. Python skill manifests
- **vs. OpenClaw:** Docker-native deployment + OCI registry vs. gateway+token approach
- **vs. AgentFM:** Central registry + Docker vs. P2P compute mesh
- **vs. Microsoft Agent Framework:** Docker packaging story vs. Python/.NET SDK

## Recommendation
**INTEGRATE** — Study Docker-based agent packaging for JCPaid agent distribution. The RAG pipeline architecture is worth replicating for Hermes knowledge skills.

---

*Scout session: 2026-04-25 | Category: agent framework | Priority: worthwhile*