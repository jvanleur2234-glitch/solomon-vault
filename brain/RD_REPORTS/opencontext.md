# RD_REPORT: 0xranx/OpenContext

**Date:** 2026-04-25
**Repo:** https://github.com/0xranx/OpenContext
**License:** MIT
**Stars:** ~600 (estimate)
**Language:** TypeScript/Node.js + Rust (Tauri desktop app)
**Clone path:** `/home/workspace/Skills/opencontext/`

## What It Is

OpenContext is a **personal context/knowledge store for AI coding agents** — Cursor, Claude Code, Codex. Instead of starting every session from scratch, OpenContext gives your agent a persistent memory layer it can load, search, and update.

**Two models:**
1. **Agent as the coding engine** — OpenContext's knowledge management Agent can BE your coding agent (reusing Codex/Claude/OpenCode CLI), adding GUI + skills/tools on top
2. **Add-on for existing agents** — Works alongside Cursor/Claude Code/Codex as a context layer (skills + slash commands + MCP server)

## Key Components

- **`oc` CLI** — global `contexts/` library (folders/docs, manifests, search)
- **MCP Server** — tools for Cursor/Claude Code/Codex/Agents to call OpenContext
- **Skills + Slash Commands** — generated per-user by `oc init` (Cursor, Claude Code, Codex)
- **Desktop App** — Tauri (Rust) native UI
- **Web UI** — local browser-based management

## What We'd Use It For

1. **Solomon OS memory layer** — OpenContext's `contexts/` library + hybrid search is a proven pattern for persistent agent memory. We could adopt it for Hermes/Solomon's brain files.
2. **Skills generation** — `oc init` auto-generates user-level skills for coding agents. This is the same pattern we use in Solomon OS AGENTS.md files. Could be formalized into a skill factory.
3. **MCP integration** — OpenContext's MCP server could connect to Hermes as an additional knowledge source.

## Comparison to What We Have

OpenContext overlaps with our Solomon OS brain file system:
- We use `/solomon-vault/brain/*.md` files as persistent memory
- OpenContext uses `contexts/` folder + manifests + hybrid search
- We have AGENTS.md; OpenContext has skills + slash commands

**Key insight we could adopt:** OpenContext's "manifest" concept — generating a file list that the agent reads before acting. Our AGENTS.md files do this manually. Could be automated.

## Recommendation

**🟢 NICE TO HAVE** — The context library + MCP + skills generation pattern is solid but not revolutionary for our use case. Our brain file system already covers similar ground.

**Exceptions where it's worth integrating:**
- If we need Cursor/Claude Code/Codex integration for client work
- The manifest generation (`oc context manifest`) is a clean pattern we'd benefit from formalizing

## Files

- Repo: `/home/workspace/Skills/opencontext/`
- Full README: `/home/workspace/Skills/opencontext/README.md`