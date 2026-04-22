# HyperAgent — AI-Enhanced Playwright Browser Automation

**URL:** https://github.com/jvanleur2234-glitch/HyperAgent
**Forked from:** https://github.com/hyperbrowserai/HyperAgent
**License:** MIT | **Language:** TypeScript

## What It Does
AI-powered browser automation built on Playwright. Natural-language commands drive headless browsers with AI fallback to regular Playwright actions. Cloud-ready via Hyperbrowser, MCP client integration, action caching for deterministic replay.

## Key Features
- `page.ai()`, `page.extract()`, `executeTask()` for natural-language automation
- `page.perform()` — granular single actions (accessibility tree, no screenshots, fast/cheap/reliable)
- CDP-first element execution with Playwright fallback
- Stealth mode (anti-bot detection), cloud-ready via Hyperbrowser
- MCP Client integration (e.g., Composio for Google Sheets)
- Action caching — record/replay workflows without LLM calls
- Vision mode, PDF generation, custom actions extension point
- TypeScript strict mode, Playwright-based browser providers

## Solomon OS Fit
**SKILL** — HyperAgent is the browser automation layer for Solomon Browser. Its `page.perform` + `page.ai` dual-mode pattern is ideal. MCP client integration aligns with Hermes skill system. Already forked to jvanleur2234-glitch.

## Recommendation
SKILL — Adopt HyperAgent as the core browser engine for Solomon Browser (Solomon OS component).