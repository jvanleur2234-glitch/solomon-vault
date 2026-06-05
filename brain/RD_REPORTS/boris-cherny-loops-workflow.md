# RD Report: Boris Cherny's "Loops" Workflow — Mapped to Solomon OS

**Date:** 2026-06-05
**Source:** Boris Cherny (creator of Claude Code @ Anthropic), Lenny's Podcast + multiple X talks
**Slug:** boris-cherny-loops-workflow
**Verdict:** **INTEGRATE** — This validates our existing architecture and gives us 3 concrete improvements to ship

---

## What Boris's Setup Actually Is

The "loops" pattern is a single system with four primitives, working in layers:

### The Four Primitives (Claude Code)
1. **Slash Commands** — repeating prompts converted into `/commands`
2. **Skills** — multi-step workflows with scripts/runbooks/assets (SKILL.md)
3. **Subagents** — work that runs in parallel with the main session in a clean context
4. **Loops** — cron-scheduled or event-driven agents that keep running

**Decision rule (Boris):** "Shape, not size."
- Repeating prompt → slash command
- Multi-step workflow with scripts → skill
- Needs to run parallel with main session → subagent
- Needs to run continuously / on schedule → loop

### Daily Setup (Boris Cherny Actual)
- **15+ concurrent Claude sessions** (5 terminal tabs in git worktrees + 5-10 browser sessions on claude.ai/code + mobile app)
- **Hundreds of agents per day, thousands overnight**
- **`/loop` command** — cron-like recurring tasks (every minute, 30 min, daily)
- **Routines** — server-side version of `/loop` that runs even when laptop closed
- **Verified-iteration loop** — every agent has a self-check (tests pass, build green)
- **Living CLAUDE.md** — auto-distilled from session corrections
- **Context discipline** — start new sessions before 300-400k tokens to avoid rot
- **System notifications** — tells him when an agent needs input

### Concrete Loops Boris Runs
- Auto-babysit PRs and fix build failures
- Keep test environments healthy
- Pull + cluster Twitter feedback
- Run adversarial reviews on code
- Auto-update dependencies
- Deploy monitoring

### Internal Anthropic Pattern
- Claudes write code in loops
- Claudes communicate with other Claudes via Slack
- No hand-written DB queries — everything is model-built
- 200% per-engineer productivity increase
- Doubled engineering headcount
- 90%+ of Claude Code team's output is generated with Claude Code

---

## How This Maps to Solomon OS

### What We Already Have (✓ Built)
| Boris Pattern | Solomon OS Equivalent | Status |
|---|---|---|
| Subagents (parallel) | `zo/ask` API (parent → child Zo sessions) | ✓ Built |
| Skills (SKILL.md) | `Skills/<slug>/SKILL.md` | ✓ Built |
| Slash commands | Persona tools + rules | ✓ Built |
| Living CLAUDE.md | `AGENTS.md` + `SOUL.md` + Rules system | ✓ Built |
| Scheduled agents | `create_agent` rrule automations | ✓ Built |
| Phone monitoring | Telegram/email delivery | ✓ Built |
| Context isolation | Conversation workspaces `/home/.z/workspaces/` | ✓ Built |
| Verification loops | Test agents, agent-browser self-checks | ✓ Built |

### What We're Missing (✗ Gap)
1. **`/loop` equivalent** — A first-class "run this every N minutes" primitive that fires within the same Zo session, not a separate scheduled agent. Boris uses this constantly.
2. **Git worktree-style isolation** — Boris's biggest productivity unlock: 3-5 parallel worktrees. We have parallel Zo sessions but no shared-repo worktree pattern.
3. **Stop hooks / success criteria** — Loops that terminate on a green signal (tests pass, build green) rather than running on a clock. We have time-based agents but not event-based ones.
4. **Living-rules auto-distillation** — Boris's CLAUDE.md auto-updates from session corrections. Our rules/AGENTS.md are manual.

---

## Concrete Improvements for Solomon OS

### 1. Build a `/loop` Primitive
- Same-session recurring task with cron-like scheduling
- Takes a prompt + interval, returns aggregated results
- Native to Zo (not a separate agent)

### 2. Add Git Worktree Pattern to Hermes
- Hermes orchestrates 3-5 parallel Zo sessions in isolated worktrees
- Shared repo, separate branches, no merge conflicts
- This is Boris's "single biggest productivity unlock"

### 3. Event-Based Agent Triggers (Stop Hooks)
- Loops that fire on webhook events, not just time
- "Run QA when PR is opened" / "Test agent fires on Stripe order"
- Could be built on top of `/loop` with event source

### 4. Auto-Distill Rules from Session History
- Background agent reviews past sessions weekly (we already do this on Sundays)
- Identifies repeated patterns and proposes new rules/AGENTS.md updates
- Boris's living CLAUDE.md pattern, automated

---

## Priority
🔴 **Critical** — Boris is the creator of the dominant coding agent. His architecture IS the future of agentic work. We need to close the 4 gaps above.

🟡 **Worthwhile** — Auto-distillation and stop hooks are nice-to-haves that compound over time.

---

## Sources
- Lenny's Podcast: "Head of Claude Code: What happens after coding is solved" (Feb 19, 2026)
- X posts by @bcherny (Boris Cherny)
- Vibecoder blog multi-claude analysis
- WorkOS interview with Boris
- Claude.com blog: "A harness for every task: dynamic workflows in Claude Code"
- GitHub: FDHam/claude-code-starter-kit, vignesh2027/claude-best-practice

## Next Steps
- Add `/loop` primitive to Zo (will need platform work)
- Build git worktree pattern into Hermes
- Add event-based triggers for existing scheduled agents
