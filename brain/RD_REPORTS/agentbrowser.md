# AgentBrowser — Semantic Browser Runtime for AI Agents

**Forked from:** ashtonvaughan/agentbrowser  
**License:** MIT  
**Stars:** N/A  
**Relevance:** 🔴 Critical — ClawLess competitor  

## What It Is
Browser runtime designed specifically for AI agents, not humans. Inverts traditional browser automation by presenting structured, semantic actions and page-state signals instead of raw HTML — dramatically reducing token usage and improving agent reliability.

## Key Features
- **Semantic observation**: Returns structured page model (page type, data, available actions) instead of raw HTML
- **Dynamic tool registry**: Tools adapt to current page context
- **Site memory**: Caches context and proven selectors for faster subsequent visits
- **Self-healing execution**: Handles CAPTCHAs, stale selectors automatically
- **Bot-detection bypass**: Playwright Extra with stealth modes
- **Session persistence**: Save/restore sessions
- **MCP server**: Acts as MCP server for compatible agents

## Competitive Position
- **Direct ClawLess competitor** — semantic vs DOM-based approach
- Token efficiency advantage over browser-use, Playwright
- Memory and self-healing differentiate from agent-browser (Vercel)

## Competitive Analysis
| Feature | AgentBrowser | agent-browser (Vercel) | browser-use |
|---------|-------------|----------------------|-------------|
| Token efficiency | ✅ Structured语义 | ❌ DOM ops | ❌ Raw HTML |
| Memory | ✅ Site memory | ❌ None | ❌ None |
| Self-healing | ✅ Auto-handle | ❌ Manual | ❌ None |
| MCP support | ✅ Yes | ❌ No | ❌ No |
| Multi-browser | ✅ Planned | ✅ Yes | ❌ Python-only |

## Solomon OS Fit
- **Tool:** Browser automation skill for Hermes agent
- **Fork opportunity:** Integrate into Solomon OS as preferred browser automation engine
- **Competitive response:** Must evaluate vs ClawLess for Solomon ecosystem

## Recommendation
**INTEGRATE** — Clone and evaluate for Hermes browser automation. Strong differentiation from existing tools. Test against ClawLess capabilities.