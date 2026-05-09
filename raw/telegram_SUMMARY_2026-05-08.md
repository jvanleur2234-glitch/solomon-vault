# Telegram Session Summary — 2026-05-08

## Date & Context
- **Session:** Fri May 08, 2026
- **Channel:** Telegram DM

## Key Decisions Made
1. **Huly platform cloned** — 25,576 stars, self-hosted replacement for Jira+Slack+Notion+Linear
2. **OSagnent stack finalised:**
   - Observation Layer: UI-TARS-desktop (screen recording) + camofox-browser + holaOS + TinyFish (web intelligence)
   - Kill Switch API: Running on port 5015 via user service
   - Base platform: Huly (self-hosted OS for company work)
   - Memory: here.now (10GB) + MemOS + cognee
   - Training: DeepSwarm (parallel batch) + Hermes v0.13.0
3. **Hermes v0.13.0 "The Tenacity Release"** installed and working
4. **SGLang credits:** Validated as useful for testing only (not infrastructure)

## Code Created/Modified
- `/tmp/kill-switch-api.ts` — Fixed version with proper Hono imports
- `~/.hermes/plugins/osagnent-observe/` — OSagnent Hermes plugin (pre_tool_call + post_tool_call hooks)
- `~/.hermes/plugins/kill-switch/` — Kill Switch Hermes plugin (block expensive tools over budget)
- `~/.hermes/config.yaml` — Updated with OSagnent + Kill Switch config

## Repos Cloned This Session
- `holaOS/` — Self-hosted desktop OS
- `UI-TARS-desktop/` — ByteDance visual agent (observation layer)
- `camofox-browser/` — Anti-detection browser for web scraping
- `tinyfish-cookbook/` — Web intelligence agents
- `Huly/platform/` — 25.5K stars, replaces Jira+Slack+Notion+Linear

## Problems Solved
- Kill Switch API kept dying — fixed by running as user service instead of space route
- Sandbox kept dropping — recovered each time, kept working through it
- Hermes v0.13.0 install failed — fixed by manually stashing changes and pip install -e .

## Unresolved
- OSagnent enterprise spec still needs full product requirements doc
- Huly needs docker deployment testing
- SGLang credits not yet claimed

## Files Synced
- OSAGNENT.md (workspace + zo-excellence-package + solomon-vault)
- OSAGNENT_ENTERPRISE_COMPLETE_SPEC.md
- All Hermes plugins
- Session summary

*Session complete. All brain files synced to GitHub.*
