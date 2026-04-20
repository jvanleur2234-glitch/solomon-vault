# RD_REPORT: gn hf — Good Night, Have Fun

**Date:** 2026-04-18
**Source:** https://github.com/kunchenguid/gnhf
**Stars:** ~2,000+ (active OSS project)
**License:** MIT
**Recommendation:** SKILL — Graft iteration engine onto Solomon Bus overnight worker

---

## What It Is

`gnhf` (Good Night, Have Fun) is a nightly autonomous coding agent orchestrator. You give it a high-level objective, it runs while you sleep, and you wake up to a git branch full of incremental, committed, documented changes.

The core loop:
1. Validates clean git state
2. Creates a dedicated `gnhf/` branch
3. Writes the objective to `prompt.md`
4. Each iteration: inject `notes.md` context → invoke agent in non-interactive mode → commit on success / rollback + backoff on failure
5. After 3 consecutive failures → aborts

Key features:
- **Incremental commits** — each successful iteration is a separate git commit (cherry-pickable)
- **Runtime caps** — `--max-iterations`, `--max-tokens`, `--stop-when`
- **Worktree mode** — multiple agents on same repo simultaneously in isolated git worktrees
- **Shared memory** — `notes.md` accumulates across iterations (cross-iteration context)
- **Resume support** — pick up from where a previous run left off
- **Live terminal title** — interactive runs show live status + token totals

Supported agents: Claude Code, Codex, Rovo Dev, OpenCode

---

## How It Works (Iteration Flow)

```
gnhf start
  → validate clean git
  → create gnhf/ branch
  → write prompt.md

Each iteration:
  → build iteration prompt (inject notes.md context)
  → invoke agent (non-interactive mode)
  → success? 
      YES → commit, append notes.md
      NO  → git reset --hard, backoff, retry
  → 3 consec failures? → abort
```

Key design choices:
- Agent output goes to per-iteration `iteration-<n>.jsonl`
- Debug log: `.gnhf/runs/<runId>/gnhf.log` (JSONL)
- Rollback is **git-based** (clean, auditable, reversible)
- notes.md is the **shared memory** between iterations

---

## Comparison to What We Have

Solomon Bus already does:
- ✅ Async task dispatch via bus messages
- ✅ Multiple sub-agents (Russell Tuna, Hermes, Deep Researcher, etc.)
- ✅ Background/PID-based long-running processes

gn hf adds:
- ❌ **Formal iteration loop** (discrete attempts with commit/rollback semantics)
- ❌ **Shared memory across iterations** (notes.md analog)
- ❌ **Runtime caps** (max iterations, max tokens, stop-when)
- ❌ **Worktree parallelism** (isolated agents on same repo)
- ❌ **git-based rollback** (versioned, auditable state changes)

The missing piece isn't dispatch — it's the **discrete iteration + validation** model.

---

## What We'd Use It For

Solomon OS overnight worker cycles. Instead of Russell Tuna being purely reactive, we could set a nightly goal:

```bash
gnhf "audit the RENU API response cache and reduce latency by 20%" --max-iterations 50
```

- Runs while Joseph sleeps
- Each commit is small + documented + reversible
- Wakes up to clean branches ready to review
- Aborts cleanly if it hits a wall

Or for the AI staffing agency: run a quality audit pass on each deployed worker skill every night.

---

## Integration Plan

1. **Study gn hf's iteration engine** — extract the loop logic (iterations, backoff, rollback)
2. **Graft onto Solomon Bus** — add as `solomon-bus overnight` subcommand
3. **Use Solomon Vault as notes.md** — `solomon-vault/raw/overnight/<date>.md` accumulates context
4. **git worktree mode** — parallel overnight agents on different repos (RENU API, WifeApp, etc.)
5. **Russell Tuna as the agent backend** — via `/fork` or direct Ollama invocation

This gives Solomon OS the "while you sleep" autonomy that gn hf is known for, but integrated with our existing stack.

---

## Verdict

🟡 **SKILL** — Not a full rebuild. gn hf's iteration model (commit on success, rollback on failure, notes.md across iterations) maps cleanly onto Solomon Bus. 

The right move: **fork the gn hf iteration engine** and graft it onto Solomon Bus as the overnight worker loop. Russell Tuna becomes the agent backend. Solomon Vault becomes the notes.md equivalent.

**Priority:** Normal (SEPL from Autogenesis is the architectural priority; gn hf is the iteration pattern to borrow for implementation)