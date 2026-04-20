# RD Report: Goal-Driven

**Repo:** https://github.com/lidangzzz/goal-driven
**Stars:** ~low (new, minimal activity) | **License:** Not specified (README-only) | **Last updated:** ~2025/2026

## What it is

A methodology prompt template (not a code project) for running extremely long-duration multi-agent tasks (300+ hours) with a master agent + subagent architecture.

The master agent:
1. Creates a subagent with a specific goal
2. Checks subagent activity every ~5 minutes
3. If subagent goes inactive or claims completion, evaluates against criteria
4. If criteria not met, respawns the subagent and continues
5. Loops until success criteria are satisfied

It's a while-loop with a master/subagent pattern — no code, just a prompt template and philosophy.

## Key claims / demos

The README shows real projects built with this approach:
- TypeScript compiler in C++ (~100 hours)
- SQLite in Rust (~30 hours)
- Lean4 compiler in TypeScript (in progress)

## How it compares to what we have

| Capability | Solomon OS | Goal-Driven |
|---|---|---|
| Long-duration task loop | ❌ | ✅ Master agent pattern |
| Auto-respawn on failure | ❌ | ✅ Via master checking |
| Criteria-based completion | ❌ | Explicit in template |
| Skill/memory across loops | Partial (Hermes) | ❌ No persistence |
| Actual implementation | Code + agents | Prompt template only |

## What we'd use it for

1. **Solomon OS orchestrator pattern** — The master agent loop concept could inform how Zo (orchestrator) watches and respawns Russell Tuna Bot workers for long tasks.

2. **AI Staffing Agency work loops** — For complex client deliverables (multi-file codebases, research reports), a Goal-Driven loop could run a subagent for days until completion criteria are met.

3. **Goal-driven task queue** — Tasks in `task_queue.json` could be structured with explicit success criteria and auto-retry logic.

4. **Building ambitious things** — The real demos (TypeScript compiler, SQLite in Rust) show it works for compiler-level projects. Could be a power-user tool for large builds.

## Integration complexity

Zero. It's a prompt template. You copy-paste it into any AI agent that supports multi-agent spawning (Claude Code, Codex, OpenClaw, Zo via /zo/ask).

The real question isn't integration — it's whether Joseph wants to use this methodology for large tasks.

## Risks / concerns

- **No code = no maintenance, but also no guarantees.** The prompt is static. Quality depends entirely on the underlying model's capability.
- **300+ hour runs** with API calls could get expensive fast. README warns about token consumption.
- **No skill/memory persistence** between respawns. Each subagent restart starts fresh on context.
- **Not a product** — it's a methodology. Doesn't directly generate revenue unless used as part of a service offering.

## Recommendation

**NOTE / STORE** — Low integration priority, medium strategic value.

Goal-Driven isn't something to install — it's a思维方式 to apply when tackling massive tasks. The pattern (master checks subagent → respawns if inactive → loops until criteria met) is genuinely useful for Solomon OS.

**Action:** Keep the template in mind when Joseph has a 50+ hour project. Also consider implementing a lightweight version of the master agent loop for task_queue.json — tasks with explicit success criteria and auto-retry logic. Could be a `solomon-bus` enhancement.
