# RD Report: parallel-code

**URL:** https://github.com/johannesjo/parallel-code  
**Submitted:** 2026-04-25  
**Recommendation:** SKILL

## What It Is

Desktop app (Electron + SolidJS, MIT) that gives every AI coding agent its own git branch and worktree automatically — enabling true parallel AI coding with zero branch conflicts.

## Key Features

- Git worktree isolation per task — each agent gets its own branch + worktree
- Supports Claude Code, Codex CLI, Gemini CLI — or any CLI agent
- Built-in tiled panel layout with drag-to-reorder
- Diff viewer + changed files list per task
- Shell terminals scoped to each worktree
- Direct mode (main branch, no isolation)
- QR code phone monitoring over WiFi/Tailscale
- Inline code Q&A with Claude Code or MiniMax M2.7 (204K context)
- State persists across restarts
- macOS + Linux

## How It Works

1. Create a task → app creates a new git branch + worktree
2. Symlinks `node_modules` + gitignored dirs into the worktree
3. Spawns the AI agent in that isolated directory
4. When satisfied → merge branch from sidebar

## What We'd Use It For

- **Russell Tuna parallelization** — give Solomon OS development team multiple agents working simultaneously on different features, no git conflicts
- **Visual coordination dashboard** — replace tmux/spaghetti-terminal with clean GUI for monitoring multi-agent work
- **Solomon Bus job parallelization** — agents can work on isolated worktrees for different jobs
- **Code review workflows** — each reviewer agent gets its own branch

## How It Compares to What We Have

| Approach | What's missing |
|---|---|
| Multiple tmux panes | No GUI, no automatic git isolation |
| VS Code extensions (Kilo/Roo Code) | Tied to VS Code, no true worktree isolation |
| Sequential agent runs | Blocks while each agent finishes |
| **parallel-code** | Git isolation + GUI + true parallelism |

## Integration

Already have `oh-my-agent` (parallel agent harness) and `zeroshot` (issue → code pipeline). parallel-code adds the **visual orchestration layer** these lack. It's a desktop app, not a skill — but we can run it on the Zo server as a GUI tool or study its worktree isolation pattern for Hermes/Solomon Bus integration.

## Status

Cloned to `/home/.z/workspaces/con_tn471wcBKEtEaxaO/parallel-code/`
