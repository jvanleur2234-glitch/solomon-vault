# RD Report: Claude OS (brobertsaz)

**Repository:** https://github.com/brobertsaz/claude-os
**Stars:** ~249
**License:** MIT
**Language:** Python, TypeScript, JavaScript
**Date:** 2026-04-26

---

## What It Is

Claude OS is a **persistent memory system for Claude Code** — giving the Claude Code CLI a long-term memory across sessions. It creates knowledge bases per project, indexes codebases, manages sessions, and has a skills library.

**Core Architecture:**
- **Knowledge Bases (4 per project):** `{project}-project_memories`, `{project}-project_profile`, `{project}-project_index`, `{project}-knowledge_docs`
- **SQLite storage** for knowledge bases with vector embeddings (OpenAI)
- **Hybrid indexing:** Tree-sitter structural index (fast) + semantic indexing (accurate)
- **MCP server:** Built-in MCP server for AI-to-AI communication
- **Skills library:** 36+ community skills from Anthropic Official + Superpowers repos
- **Web UI:** React frontend with Kanban board for Agent-OS spec tracking
- **Commands:** `/claude-os-init`, `/claude-os-search`, `/claude-os-remember`, etc.

---

## What We'd Use It For

### 1. Session Memory Pattern for Solomon OS
Claude OS's session management is well-designed — the idea of a "one-liner" summary, `stopped_at` timestamp, and `last_branch` could inspire Solomon OS's own session tracking.

### 2. Knowledge Lifecycle Engine
The dedup, consolidate, archive, and health report system is mature. Could inform how Solomon OS manages its brain files over time.

### 3. Skills Library Integration
36+ community skills already packaged. Could be a source of skills for Russell Tuna / Hermes to install.

### 4. MCP Server
Built-in MCP server means Claude OS can be queried by other AI agents. Could be wired into Solomon OS for cross-agent memory sharing.

---

## How It Compares to What We Have

| Feature | Claude OS | Solomon OS (Zo-based) |
|---|---|---|
| Memory storage | SQLite + vector embeddings | Workspace brain files + GitHub sync |
| Indexing | Tree-sitter + OpenAI embeddings | Manual file reading |
| Skills | 36+ community skills | Limited, custom |
| MCP server | Built-in | AgentArmor, Arena2API skills |
| Web UI | React Kanban board | Zo native UI |
| Session tracking | JSON state file | Telegram summaries |
| Knowledge lifecycle | Auto dedup/merge/archive | Manual via Sunday self-review |

**Key difference:** Claude OS is designed for Claude Code CLI sessions. Solomon OS runs 24/7 as an AI business. The memory model is similar but the runtime context is different.

---

## Key Ideas to Borrow

1. **One-liner session summaries** — replace long Telegram session summaries with a structured `one_liner` + `stopped_at` + `last_task` JSON state
2. **Knowledge lifecycle** — auto-dedup and archive old brain files (the Sunday self-review already does this manually)
3. **Skills registry browsing** — the `/claude-os-skills` install workflow is a good UX pattern for Russell Tuna to browse and install new capabilities
4. **Cross-project memory** — patterns from one project informing another is exactly what Solomon OS's shared knowledge base does

---

## Recommendation: SKILL (Extract Ideas, Don't Clone)

This is NOT a repo to install directly — it's Claude Code specific. However, the **ideas** are valuable:

- Borrow the session state JSON structure for Solomon OS session tracking
- Consider a knowledge lifecycle script (auto-dedup brain files weekly)
- The skills library browsing pattern is worth replicating for Russell Tuna

**Action:** Extract session state pattern → add to Solomon OS. Add knowledge lifecycle dedup → integrate into Sunday self-review agent.
