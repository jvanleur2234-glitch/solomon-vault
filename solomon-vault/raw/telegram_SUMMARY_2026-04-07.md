# Telegram Session Summary — 2026-04-07

## Date
2026-04-07

## Key Decisions Made
- Agreed to work on arena2api project — a CLI tool to reverse-engineer LM Arena (arena.ai) API
- Context loaded from `/home/workspace/arena2api/`

## Code Created / Modified
- Existing project at `/home/workspace/arena2api/` with:
  - `injector.js` — Chrome extension content script that extracts models from `__next_f`
  - `server.py` — OpenAI-compatible proxy using `POST /api/stream/create-evaluation` on canary.lmarena.ai
  - `arena_bridge.py` — Playwright-based headless session manager
  - `auth_tokens_parsed.json` — Contains valid ES256K JWT access token (expires ~1 hour ago based on timestamps)
  - `all_cookies.json` — Contains `arena-auth-prod-v1` (base64 custom format) and `cf_clearance`
  - `models.json` — 209KB extracted model list

## Problems Solved
- Decoded the `arena-auth-prod-v1` cookie format: `base64-{jwt}` (custom format, not standard JWT)
- Decoded the actual ES256K JWT access token from `auth_tokens_parsed.json`
- Identified full API flow: cookie auth → refresh endpoint → ES256K JWT → stream/create-evaluation

## Unresolved Issues
1. arena.ai direct SSL errors — need canary domain or origin IP discovery
2. `__APOLLOCLIENTSTATE__` format not yet investigated
3. Need to test whether current tokens/cookies are still valid
4. Need to confirm full POST payload schema for chat completions
5. CLI with Click not yet built

## Follow-up Needed
- Run live browser capture against arena.ai to confirm API endpoints and payload formats
- Check if cookies are still valid or need re-authentication
- Investigate `__APOLLOCLIENTSTATE__` hydration data
