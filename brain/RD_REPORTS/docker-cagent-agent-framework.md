# Docker Agent (cagent) — YAML-Driven Multi-Agent Orchestration

**URL:** https://github.com/jvanleur2234-glitch/cagent
**Forked from:** https://github.com/docker/cagent
**License:** Apache 2.0
**Stars:** Unknown (new discovery)

## What It Does
Docker CLI plugin (`docker agent`) for building, running, and sharing AI agents via declarative YAML. Multi-agent teams, any MCP server, model-agnostic (OpenAI/Anthropic/Gemini/Bedrock/Mistral/xAI/Docker Model Runner), RAG with BM25+embeddings+hybrid search+reranking, OCI registry packaging.

## Why It Matters
- YAML-based agent definitions — declarative, versionable, shareable
- Multi-agent orchestration with automatic task delegation
- Built-in think/todo/memory tools + RAG pipeline
- OCI registry push/pull for agent distribution
- Docker-native deployment story

## Solomon OS Fit
- DIRECT INTEGRATION — YAML agent config pattern directly maps to Hermes skill manifests
- MCP integration aligns with Hermes MCP architecture
- RAG pipeline (BM25+embeddings+reranking) could replace/enhance Hermes knowledge检索
- Docker packaging for agent distribution = JCPaid deployment story
- Apache 2.0 permits direct code use

## Competitive Analysis
- **vs. Hermes:** YAML declarative + Docker packaging vs. Python skill manifests
- **vs. OpenClaw:** Docker-native deployment + OCI registry vs. gateway+token approach
- **vs. AgentFM:** Central registry + Docker vs. P2P compute mesh

## Recommendation
**INTEGRATE** — Study Docker-based agent packaging + RAG pipeline. YAML config pattern maps well to Hermes skill factory.

## Status
Already forked to jvanleur2234-glitch/cagent