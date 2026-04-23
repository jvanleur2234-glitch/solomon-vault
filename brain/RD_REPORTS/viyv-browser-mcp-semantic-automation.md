# RD Report: viyv-browser — Chrome Extension + MCP Server for AI Browser Automation

**Date:** 2026-04-23  
**Classification:** SKILL  
**License:** MIT  
**Stars:** ~500+  
**Fork:** https://github.com/jvanleur2234-glitch/viyv-browser

---

## What it is

Chrome extension + MCP server that enables AI agents to operate in the user's real browser with authenticated sessions. Adds a semantic automation layer on top of standard browser tools for reliable, repeatable, scalable browser tasks.

## Key Capabilities

- **Authenticated Real Browser:** Operates in user's actual Chrome with session cookies — no headless browsers, no credential sharing
- **Semantic Automation:** Define data targets once, replay reliably — vs. screenshot-based AI that varies each time
- **Batch Execution:** Jobs run multiple scenarios in sequence with error handling
- **Scheduled Execution:** Run Jobs on a schedule via Cowork integration
- **Execution History & Diff:** Auto-detects changes between runs
- **Google Sheets Integration:** Read/write via session cookies (no OAuth)
- **Dashboard:** Chart.js visualizations, CSV/JSON export
- **MCP Server:** Connects to Claude Desktop/Cowork as MCP client
- **Low Token Cost:** Indexed DOM text instead of screenshots

## What we'd use it for

- Solomon Browser POC enhancement — real authenticated browser automation
- Competitive analysis, price monitoring, recurring data collection
- E2E testing for Solomon OS web interfaces
- Google Sheets integration for business intelligence

## Comparison to what we have

- More mature than our Clicky walkthrough player — production-grade with batch/schedule
- Real browser with auth vs. headless Playwright — critical advantage for authenticated scraping
- MCP-native integration aligns with Hermes's MCP skills ecosystem
- Semantic targeting (define targets once, replay) is superior to screenshot-based approaches

## Recommendation: SKILL

MIT licensed, production-grade, MCP-native. Forked. Aligns with Solomon Browser strategy. Would integrate as MCP skill for Hermes.