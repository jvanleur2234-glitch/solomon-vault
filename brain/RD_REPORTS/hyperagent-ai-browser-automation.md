# RD Report: HyperAgent (hyperbrowserai/HyperAgent)

## What It Is
TypeScript-based AI-enhanced browser automation framework built on Playwright with natural-language driven automation, anti-bot stealth mode, action caching, and MCP client integration.

## License & Stars
- **License:** MIT (inferred — no explicit license visible)
- **Stars:** Not yet polled; project appears active

## Key Capabilities
- **page.ai() / page.extract() / executeTask()** — AI-assisted browser tasks via natural language
- **Standard Playwright fallback** when AI isn't needed — graceful degradation
- **Stealth mode** built-in anti-bot patches to avoid detection
- **Cloud-ready**: scales via Hyperbrowser to many sessions
- **MCP client integration** — connect to tools like Composio
- **Action caching**: record/replay workflows deterministically without repeated LLM calls
- **Two modes**: page.perform() for granular actions; page.ai for AI-guided actions

## Relevance to Solomon OS
- **Browser automation (ClawLess competitor)**: Strong alternative with AI-guided actions
- **Security**: Stealth mode + deterministic caching could be integrated into ClawLess
- **Skill frameworks**: MCP integration fits Hermes skill ecosystem

## Decision
**SKILL** — Clone to workspace, fork to `jvanleur2234-glitch/HyperAgent`, add to HERMES_CAPABILITIES.md. Direct competitor to ClawLess; study the action caching + stealth mechanisms.

## Notes
- Closest to ClawLess in the browser automation space with AI guidance
- Hyperbrowser cloud scaling is a different angle from our local-first approach
- Action caching is novel — deterministic replay without repeated API calls