# RD Report: browserbase/stagehand

## Summary
AI-augmented browser automation framework that combines natural language commands with explicit code control for reliable, production-grade web automation. Hybrid approach: use AI for unfamiliar pages, code for known repeatable tasks.

## Key Details
- **License**: MIT
- **Language**: TypeScript
- **Stars**: ~9,000+
- **Repo**: https://github.com/browserbase/stagehand
- **Docs**: https://docs.stagehand.dev

## What It Does
- **Hybrid AI + code approach**: Choose when to use natural language vs explicit code for browser actions
- **Auto-caching + self-healing**: Remembers previous actions, runs without LLM inference, auto-repairs when sites change
- **Action preview**: Preview AI actions before running them
- **CDP-based low-level browser control**: Direct Chrome DevTools Protocol for reliable automation
- **Multi-step tasks**: `stagehand.agent()` orchestrates complex multi-step automation
- **Data extraction**: `stagehand.extract()` returns structured data from web pages
- **Python version available**: stagehand-python for Python-first workflows

## Relevance to Solomon OS / Hermes
- **ClawLess competitor**: Browser automation for AI agents — same category as browser-use, copilotbrowser, HyperAgent
- **Forked by**: jvanleur2234-glitch/stagehand
- **Differentiation**: Self-healing + caching + hybrid AI/code approach is more production-focused than pure AI-driven approaches

## Use Cases
- AI agents that need reliable, production-grade browser automation
- Web scraping that survives site structure changes
- Automated form filling and data extraction
- E-commerce automation, job applications, research tasks

## Competitive Position
- Stagehand vs browser-use: browser-use has 89K stars (much larger community), but stagehand's self-healing and caching is more production-grade
- Stagehand vs copilotbrowser: copilotbrowser focuses on "Follow Me" mode + cross-browser; stagehand focuses on reliability + self-healing
- Browserbase (the company) is well-funded and actively developing

## Verdict
**INTEGRATE** — Forked. Consider for browser automation capabilities in the ClawLess / EdgeClaw skill. Stagehand's self-healing approach is superior to most competitors for production workloads.