# Telegram Session Summary — April 25, 2026

**Date:** 2026-04-25  
**Session:** R&D Queue (Ghost OS + PriceGhost)  
**Trigger:** Telegram DM

## Repos Analyzed

### Ghost OS (ghostwright/ghost-os)
- **1.4k stars, MIT license**
- macOS-native computer-use for AI agents
- Uses macOS accessibility tree instead of screenshots — structured data about every UI element
- Falls back to local vision model (ShowUI-2B) only when AX tree falls short (web apps)
- **Self-learning recipes**: manually perform task once → synthesizes parameterized recipe → small model runs forever
- 29 tools via MCP: ghost_context, ghost_state, ghost_find, ghost_click, ghost_type, ghost_run, ghost_learn_start/stop, etc.
- Works with Claude Code, Cursor, VS Code, any MCP client
- macOS-only → not applicable to our Linux/Debian environment directly
- **Recommendation:** SKILL — study accessibility-first architecture for future desktop agent work

### PriceGhost (clucraft/PriceGhost)
- **530 stars, MIT license**
- Self-hosted price tracking with multi-strategy extraction
- 4 extraction methods in parallel: JSON-LD, site-specific scrapers, CSS selectors, AI fallback
- **Price Voting Modal** — unique feature where methods vote and user picks when they disagree (prevents tracking "save $X" instead of actual price)
- AI verification: Claude Haiku/GPT-4o-mini/Ollama (fractions of a cent per check)
- Notifications: Telegram, Discord, Pushover, ntfy.sh, Gotify
- PostgreSQL + React + Docker
- **Recommendation:** FORGE — clone to /home/workspace/priceghost/, use extraction engine for custom home component pricing + build arbitrage layer for savings business

## Decisions Made
- PriceGhost queued as FORGE task (priceghost-001) — custom home configurator + arbitrage engine
- Ghost OS noted as SKILL — study for future desktop agent capabilities

## Tasks Added
- `priceghost-001` — PriceGhost self-hosted price tracking for Custom Home + Arbitrage (type: forge, priority: high)

## Follow-up Needed
- Clone PriceGhost to /home/workspace/priceghost/
- Write RD_REPORT for PriceGhost at brain/RD_REPORTS/priceghost.md
- Map Ghost OS accessibility tree patterns for potential future desktop agent features