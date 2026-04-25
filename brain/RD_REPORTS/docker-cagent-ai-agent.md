# Docker Agent (cagent) — Declarative Multi-Agent Runtime (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/docker-cagent-ai` (Apache 2.0)
**Source:** https://github.com/docker/cagent

## What It Does
Docker Engineering's agent framework. Declarative YAML config for multi-agent orchestration with:
- MCP server support (any MCP tool/host)
- Multi-provider: OpenAI, Anthropic, Gemini, AWS Bedrock, Mistral, xAI, Docker Model Runner
- RAG with BM25 + embeddings + hybrid search + reranking
- OCI registry push/pull for agent sharing

## Why It Matters for Solomon OS
- Declarative YAML model maps to Hermes skill definition format
- RAG pipeline (BM25 + embeddings) could replace or enhance Hermes knowledge layer
- OCI registry model for agent portability aligns with Solomon Brain export/import
- Docker-native = could run inside Solomon OS container stack

## Fit: SKILL
Apache 2.0. Study RAG pipeline and OCI packaging model. Docker dependency limits direct integration but YAML orchestration patterns are transferable.

## Action Items
- [ ] Study BM25 + embedding hybrid search implementation
- [ ] Extract RAG pipeline for Hermes knowledge layer
- [ ] Map OCI agent packaging to Solomon Brain bundle format
