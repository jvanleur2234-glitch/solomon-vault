# RD Report: maxun — Open-Source AI Browser Agent / Web Scraping Platform

**Date:** 2026-04-23  
**For:** Solomon OS / JCPaid Research  
**Status:** FORGE (AGPL-3.0 — non-commercial use only)

## What It Is
maxun is an open-source, no-code platform that turns websites into structured APIs for scraping, crawling, search, and AI data extraction. Key for AI browser agents: real-time rrweb-based recorder, LLM-powered natural-language extraction, and SDK/CLI for automation.

## Key Capabilities
- **Recorder Mode:** Records user actions into reusable robots (rrweb-based live streaming, not snapshots)
- **AI Mode Extract:** Natural-language extraction without needing a URL (auto-search via DuckDuckGo + LLM)
- **AI-Native Workflow SDK:** LLM integrations with popular AI frameworks
- **Separate browser service:** Remote CDP/WebSocket browser, decoupled from backend
- **Maxun CLI:** Official command-line interface for robot management
- **N8N node support:** Integration with n8n workflows
- **Auto search logic:** DuckDuckGo + LLM for URL auto-detection

## Why It Matters for Solomon OS
maxun's browser automation layer competes with HyperAgent, browserable, and browserclaw. The real-time rrweb recorder is technically interesting. AGPL-3.0 means we can't use code commercially, but the architecture is worth studying for our own implementation. JCPaid's data pipeline could use maxun-style scraping skills.

## License
**AGPL-3.0** ⚠️ — Cannot use code commercially. Architecture reference only.

## Status
**STUDY** — Study architecture only (AGPL-3.0 incompatibility with JCPaid commercial use)

## RD Report
`file 'solomon-vault/brain/RD_REPORTS/maxun-ai-browser-agent.md'`