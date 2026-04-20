# RD Report: planning-with-files

**URL:** https://github.com/OthmanAdi/planning-with-files
**Stars:** Not visible in clone, but clearly massive viral adoption (40+ IDE integrations, 5 forks with dedicated projects)
**License:** MIT
**Priority:** 🟡 Worthwhile

## What It Is

A Claude Code plugin / universal agent skill that implements the **Manus-style persistent markdown planning** pattern — 3 files per task:

- `task_plan.md` — phases, progress, goal tracking
- `findings.md` — research and research results
- `progress.md` — session log, errors, test results

The core principle: **Filesystem = disk (persistent, unlimited), Context = RAM (volatile, limited).** Anything important gets written to disk.

Backed by a detailed writeup on [Manus.im](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — the AI company Meta acquired for **$2 billion** on Dec 29, 2025. Manus hit $100M+ revenue in 8 months using exactly this pattern.

## What We'd Use It For

Could integrate this **3-file planning pattern** into Solomon OS workflow for:
- Complex multi-step builds (each agent task gets a task_plan.md)
- Research sessions with persistent findings
- Project phases tracked on disk instead of volatile context
- Session recovery after context resets

The hooks system (PreToolUse, PostToolUse, Stop) is particularly powerful — agents auto-re-read the plan before decisions and verify completion before stopping.

## How It Compares to What We Have

Our current Solomon OS already has:
- Zo Foam for notes and session logging
- Task queue system (zo.space-tasks/task_queue.json)
- Solomon Bus for inter-agent communication

Planning-with-files is more **granular per-task** — each coding session gets its own 3-file set. It's best-in-class for agent coding workflows. Our system is more **business-level** (client tracking, job management).

## Recommendation: INTEGRATE

The hooks pattern is worth adopting for complex Russell Tuna / Hermes tasks. Specifically:

1. **Install** the skill into Russell Tuna's Claude Code setup for complex jobs
2. **Adopt the 3-file pattern** for multi-step AI worker tasks in Solomon OS
3. **Hook system** could make Russell Tuna more reliable on long tasks

It's not something we'd use for every message — but for complex builds or multi-hour tasks, the session recovery + error tracking would reduce failures.

**Action:** Clone into `/home/workspace/Skills/planning-with-files/` and wire into Russell Tuna workflow.
