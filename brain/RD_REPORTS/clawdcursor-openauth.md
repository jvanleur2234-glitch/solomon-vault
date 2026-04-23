# RD Report: Clawd Cursor + OpenAuth

**Date:** April 23, 2026
**Batch:** Evening queue
**Status:** FORGE + SKILL

---

## Clawd Cursor — OS-Level Desktop Automation

**What it is:** OS-agnostic, model-agnostic desktop automation server. 196 stars, MIT.

**Key capabilities:**
- 42 callable tools: mouse, keyboard, screen, windows, browser CDP
- Works with ANY AI model (Claude, GPT, Gemini, Llama, Ollama)
- MCP mode for Claude Code, Cursor, Windsurf, Zed
- Ground-truth verifier (pixel diff, OCR, window state, focus change)
- Anti-detection built-in
- V2 architecture: screenshot → tool call → screenshot → verify loop

**How it fits JackConnect:**
- REPLACES Clicky/Watch Once entirely
- Instead of recording clicks → Clawd Cursor watches screen + acts
- Can delegate to Claude/GPT/Llama per task
- Built-in safety: Preview (type/forms), Confirm (send/delete)

**Install:** `powershell -c "irm https://clawdcursor.com/install.ps1 | iex"` (Windows)

**Recommendation:** FORGE — core of JackConnect automation layer

---

## OpenAuth — Self-Hosted Auth Server

**What it is:** Standards-based OAuth 2.0 auth provider. 6.8K stars, MIT.

**Key capabilities:**
- Deploy on Bun, Node.js, Lambda, Cloudflare Workers
- Providers: GitHub, Google, email/password, PIN code
- Self-hosted — no third-party auth dependency
- Themeable UI or custom
- KV store (DynamoDB, Cloudflare KV, Memory)

**How it fits JackConnect:**
- Replace Clerk/Auth0 with self-hosted auth
- Each client gets own credentials via OAuth
- Agent auth: agents authenticate as users
- Multi-tenant: Jack's clients each have their own auth domain

**Recommendation:** SKILL — install as JackConnect auth layer. Run on Zo server at auth.solomon.os

---

## Bottom Line

| Tool | Stars | License | Use |
|------|-------|---------|-----|
| Clawd Cursor | 196 | MIT | FORGE — replaces Clicky/Watch Once |
| OpenAuth | 6.8K | MIT | SKILL — JackConnect auth layer |

*Built for Solomon OS — Joseph's autonomous AI business system*
