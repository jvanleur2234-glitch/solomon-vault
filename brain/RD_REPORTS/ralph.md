# RD Report: Ralph

**URL:** https://github.com/snarktank/ralph
**Status:** Queued (normal priority)
**Type:** R&D Research
**Date:** 2026-04-18

---

## What It Is

Ralph is an **autonomous AI agent loop** that repeatedly calls AI coding tools (Amp CLI or Claude Code) until all PRD items are complete. Each iteration spawns a **fresh AI instance** with clean context. Memory persists between iterations via git history, `progress.txt`, and `prd.json`.

**Key innovation:** Solves the context window exhaustion problem by breaking large projects into small, independently-executable user stories. Each story fits in one context window. Ralph loops until all stories pass.

## Core Loop

1. Read `prd.json` — find highest priority story where `passes: false`
2. Spawn fresh AI instance (Amp or Claude Code)
3. AI implements that single story
4. Run quality checks (typecheck, tests)
5. If checks pass → commit → mark `passes: true`
6. Append learnings to `progress.txt`
7. Repeat

## What We'd Use It For

- **Russell Tuna autonomy engine** — adapt Ralph's loop pattern so Russell can handle large tasks (too big for one session) by breaking them into stories and looping across sessions
- **Zo agents** — Ralph pattern could power Solomon Bus workers: each worker picks a story, executes, reports back, loops
- **Autonomous dev projects** — Zo could manage a Ralph loop for building features in the background while Joseph sleeps

## Comparison to What We Have

| | Ralph | Solomon Bus (current) |
|---|---|---|
| Loop pattern | ✅ Fresh-context iterations | ⚠️ Single-prompt workers |
| PRD-based task breakdown | ✅ Yes | ❌ No |
| Memory between sessions | ✅ progress.txt + git | ⚠️ Limited |
| Built-in quality gates | ✅ Yes | ❌ No |
| Multiple AI backends | ✅ Amp + Claude Code | ❌ Zo only |

## Fit for Solomon OS

🟡 **Interesting pattern, consider adapting**
- Ralph's **fresh-context iteration pattern** is the key insight — we could replicate this for Russell Tuna or Solomon Bus workers
- The PRD → user stories → loop pattern is solid autonomous dev methodology
- Does NOT run on Zo natively (requires Amp or Claude Code CLI), so we'd need to adapt the shell loop to work with our stack

## Recommendation

**SKILL** — Adapt Ralph's loop pattern into Solomon Bus / Russell Tuna workflow. Not a direct install, but the concept (small tasks + fresh-context loops + progress tracking) is directly applicable to building persistent autonomous workers.
