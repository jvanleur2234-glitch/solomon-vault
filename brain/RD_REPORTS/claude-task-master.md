# RD Report: claude-task-master

**Repository:** eyaltoledano/claude-task-master
**Stars:** 26.9k | **License:** MIT + Commons Clause | **Last updated:** Apr 23, 2026

---

## What It Is

An AI-powered task management system designed for AI-driven development workflows. It integrates directly into AI code editors (Cursor, Windsurf, Lovable, Roo, VS Code) as an MCP server, letting you manage tasks via natural language chat with the AI.

**Core workflow:**
1. Write a PRD (Product Requirements Document)
2. AI parses it and generates tasks automatically
3. Work through tasks in sequence, with dependency tracking
4. Use `/research` for fresh info with project context
5. Use `/loop` for automation

**Key capabilities:**
- PRD → task generation (`parse-prd`)
- Task dependencies and cross-tag movement
- Research command (web search + project context)
- Loop/automation command
- Multi-provider AI support (Claude, GPT, Gemini, Groq, Perplexity, etc.)
- 36 MCP tools for IDE integration

---

## What We'd Use It For

**FORGE workflow integration** — Joseph already has the task queue system (`zo.space-tasks/task_queue.json`), but claude-task-master has more sophisticated features:
- PRD parsing that auto-generates task lists
- Research command that searches the web WITH project context
- Loop command for automation
- Better task dependencies and cross-tag movement

**Could enhance:**
- Better PRD → task flow for client projects
- Research with context (vs. just raw web search)
- Loop automation for repetitive tasks

---

## Comparison to What We Have

| Feature | Our System | claude-task-master |
|---|---|---|
| Task storage | JSON queue file | Local `.taskmaster/` directory |
| PRD parsing | Manual | Auto-generates tasks from PRD |
| Research | Web search | Web search + project context |
| Dependencies | Basic | Full dependency graph |
| IDE integration | None | MCP in 5+ editors |
| Loop/automation | No | Yes (`/loop` command) |
| Token optimization | N/A | 3 tool modes (7/15/36 tools) |

---

## Recommendation: INTEGRATE

**Why:** 26.9k stars with active maintenance (last commit Apr 23 2026), MIT license, multi-provider support, PRD parsing + research commands that could strengthen the FORGE workflow.

**How:**
1. Study their PRD → task parsing logic to enhance our own workflow
2. Consider their research command approach (context-aware web search)
3. Could potentially run as a background agent for task management

**Watch:** Commons Clause license means we can't offer it as a hosted service — but using it internally for our own dev workflow is fine.

**Priority:** 🟡 Worthwhile — 1K-10K stars, clear use case for enhancing FORGE task management
