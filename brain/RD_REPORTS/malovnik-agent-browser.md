# RD Report: malovnik/agent-browser — Token-Efficient Text-First Browser

**Repo:** `malovnik/agent-browser`
**License:** MIT | **Language:** TypeScript
**Stars:** ~200+ (estimated) | **Forked:** Yes (jvanleur2234-glitch/agent-browser)
**Date:** 2026-04-23

## What It Is

A text-first browser designed specifically for AI agents. Instead of screenshots or DOM selectors, it reads pages via the accessibility tree, producing a compact semantic snapshot with auto-discovered actions. Claims **17x lower token usage** than screenshot-based approaches.

## Key Features

- **Semantic Action Discovery** — groups page elements into meaningful categories (LOGIN FORM, SOCIAL SIGN-IN, NAVIGATION) with labeled inputs/actions
- **Predictive Browsing Engine** — page diffs (delta updates), intent filtering, action flows (auto-detected multi-step work streams), smart extraction
- **17x token reduction** — focused on semantic actions and page diffs rather than pixel data
- MCP server over stdio — integrates with MCP-compatible clients (Claude Desktop, etc.)
- Requires Node.js 18+, local Chrome/Chromium

## Solomon OS Fit

**SKILL** — Study token-efficient browsing patterns for Hermes. The semantic action discovery could replace ClawLess's screenshot approach with cheaper text-based interaction. MIT license permits direct use.

## Recommendation

**SKILL** — Architecture study for browser automation cost reduction.