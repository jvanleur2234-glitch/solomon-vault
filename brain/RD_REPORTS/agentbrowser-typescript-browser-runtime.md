# agentbrowser — Semantic Browser Runtime for AI Agents

## What It Is
TypeScript browser runtime exposing semantic, structured actions to AI agents (not raw DOM). Reduces token costs via structured page models with type/data/available actions.

## Key Signals
- **License:** MIT
- **Lang:** TypeScript
- **Fork:** https://github.com/jvanleur2234-glitch/agentbrowser

## Core Features
- Semantic observation: structured page model per navigation (dramatically reduces tokens)
- Dynamic tool registry adapts to current page
- Site memory: persistent caching across visits
- Self-healing: CAPTCHA detection, stale selector recovery
- Bot-detection avoidance built-in
- Session persistence: save/restore/branch browser state
- MCP server support

## Solomon OS Fit
- **FORGE** — MIT license. Semantic page model IS what Solomon Browser needs for efficient agent-native DOM access.
- Memory + self-healing patterns directly applicable

## Recommendation
FORGE — Direct implementation value. Structured page model + memory for Solomon Browser.