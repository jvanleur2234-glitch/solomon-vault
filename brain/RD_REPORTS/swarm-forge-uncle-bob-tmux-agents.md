# RD Report: Swarm-Forge — Uncle Bob's tmux-Based Multi-Agent Control System

**URL:** https://github.com/unclebob/swarm-forge  
**Source:** https://x.com/unclebobmartin/status/2046350013706523093  
**Date Queued:** 2026-04-20  
**Priority:** 🟡 Worthwhile (but HIGH VALUE for Solomon OS)  
**Tags:** multi-agent, tmux, git-worktree, orchestration, clean-code  

## What It Is
Swarm-Forge is a tmux-based multi-agent control system forked by Robert C. Martin (Uncle Bob) from his son Justin's original project. It lets multiple AI agents:
- Talk to each other and delegate tasks
- Manage individual git worktrees
- Merge each other's code changes
- Write hundreds of tests and Gherkins
- Refactor and mutate tests
All under human supervision ("watchful eye").

Uncle Bob says: "I sometimes just sit back in awe as the agents do massive amounts of work."

## Stack
- tmux as orchestration layer
- Git worktrees for parallel agent workspaces
- Gherkin (BDD) for test generation
- Test mutation for quality
- Human-in-the-loop oversight

## What We'd Use It For
1. **Solomon Bus parallel task execution** — agents on tmux panes handling different job queue items simultaneously
2. **Git worktree pattern** — each Solomon OS worker gets its own worktree, preventing merge conflicts
3. **Gherkin integration** — automate spec generation from job definitions before code
4. **Russell Tuna collaboration** — multiple Russell Tunas working on sub-tasks, merging results

## How It Compares to What We Have
- **vs CrewAI / LangGraph**: Swarm-Forge is lighter, tmux-native, git-worktree native. No Python dependency.
- **vs Zeroshot**: Swarm-Forge is more collaborative (agent-to-agent task delegation) vs single-task → code pipeline
- **vs Ralph loop**: Similar overnight-automation concept but uses tmux panes instead of process loops

## Recommendation
SKILL — Study tmux worktree architecture for Solomon Bus parallelization. Clone to /home/workspace/Skills/swarm-forge/ for pattern reference. Low stars (~430) but Uncle Bob's endorsement = credible architecture.

## Links
- Repo: https://github.com/unclebob/swarm-forge