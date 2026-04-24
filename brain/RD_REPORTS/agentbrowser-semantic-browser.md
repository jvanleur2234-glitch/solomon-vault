# RD Report: AshtonVaughan/agentbrowser

**Fork:** Already forked
**Source:** https://github.com/ashtonvaughan/agentbrowser
**Stars:** ~500+ | **License:** MIT | **Language:** TypeScript
**Date:** 2026-04-24

## What It Is
AI agent-specific browser runtime. Inverts traditional browser automation by exposing semantic, structured actions and page-state information rather than raw DOM. Semantic observation reduces tokens ~95%.

## Key Capabilities
- **Semantic observation:** Structured page model (page type, data, available actions)
- **Dynamic tool registry:** Actions adapt to current page context
- **Site memory:** Persistent caching + LLM-augmented analysis
- **Self-healing:** CAPTCHA detection, stale selector recovery, state verification
- **Bot-detection bypass:** Playwright Extra stealth mode
- **Session persistence:** Save/restore/branch browser state
- **MCP server:** Ships as MCP server for easy agent integration

## Architecture
- Semantic layer: exposes meaningful actions instead of raw DOM
- Tool registry: per-page action sets
- Memory: persistent site knowledge
- Recovery: automatic handling of common failures

## Relevance to Solomon OS
- **Browser automation:** ClawLess competitor with MIT
- **95% token reduction:** Huge win for web research tasks
- **Self-healing:** Reduces maintenance burden
- **MCP server:** Native Hermes integration point

## Recommendation
**SKILL** — Study semantic observation pattern. 95% token reduction for browser tasks is significant. Self-healing reduces operational burden. MCP server enables native Hermes integration.

## License Check
MIT ✅