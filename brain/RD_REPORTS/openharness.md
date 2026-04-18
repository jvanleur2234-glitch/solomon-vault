# RD Report: OpenHarness — Agent Harness Architecture

**Repository:** https://github.com/HKUDS/OpenHarness
**Archived:** 2026-04-17
**Analyst:** Zo
**Recommendation:** INTEGRATE

---

## What It Is

OpenHarness (`oh`) is an ultra-lightweight open-source Python implementation of an AI agent harness — the infrastructure that wraps around an LLM to make it a functional agent. Think of it as a lean, modular alternative to Claude Code.

**Core equation:** Harness = Tools + Knowledge + Observation + Action + Permissions

The model provides intelligence; the harness provides hands, eyes, memory, and safety boundaries.

---

## Key Architecture (10 Subsystems)

| Subsystem | What it does |
|-----------|-------------|
| `engine/` | Agent loop — query → stream → tool-call → loop |
| `tools/` | 43 tools — file I/O, shell, search, web, MCP |
| `skills/` | On-demand skill loading from `.md` files |
| `plugins/` | Extensions — commands, hooks, agents, MCP servers |
| `permissions/` | Multi-level safety modes + path rules |
| `hooks/` | PreToolUse/PostToolUse lifecycle events |
| `commands/` | 54 CLI commands — /help, /commit, /plan, /fork... |
| `mcp/` | Model Context Protocol client |
| `memory/` | Persistent cross-session knowledge (memdir + scan) |
| `coordinator/` | Multi-agent spawning + team coordination |
| `tasks/` | Background task management |

---

## Solomon OS Fit Analysis

### What's Already in Place

| OpenHarness Feature | Solomon OS Equivalent | Fit |
|---------------------|------------------------|-----|
| Multi-agent coordinator | Russell Tuna `/fork` | ✅ Parallel — same concept |
| Skills system (.md files) | Hermes skills registry | ✅ Strong — same model |
| Memory (cross-session) | Solomon Vault | ✅ Strong — vault already exists |
| Permissions/safety | Hermes safety layer | ✅ In place |
| Plugin system | Hermes plugin loader | ✅ In place |
| 43 built-in tools | Hermes + Zo tools | ✅ Overlapping |
| Team coordination | Solomon Bus | ✅ Bus exists |
| Hooks/lifecycle | Agent rules | ✅ Rules system in place |

### Gaps Identified

1. **Russell Tuna has no cross-session memory** — every session starts fresh. OpenHarness's `memory/` subsystem could fix this.
2. **No formal harness layer** for Russell Tuna Bot — it's running on Ollama + python-telegram-bot, but lacks the structured tool-permission-skill pipeline that OpenHarness provides.
3. **Multi-agent spawning** (`/fork`) exists but isn't tracked/monitored persistently.

---

## MetaClaw — Dead End

MetaClaw v0.0.1 on PyPI is a placeholder package — no actual code, no implementation. Not usable. Do not invest time here.

---

## Integration Recommendation

### FORGE — Build Solomon OS Harness Layer

Use OpenHarness architecture as the reference design for a Solomon OS "harness" that wraps Russell Tuna Bot:

```
Solomon Harness Layer
├── Tool registry (extends Hermes skills)
├── Memory manager (connects to Solomon Vault)
├── Permission guard (channels to Hermes safety)
├── Skill loader (14 money skills + domain-specific)
├── Coordinator (mirrors /fork but with tracking)
└── Hooks (pre/post tool use events → logging to Bus)
```

**Action:** Clone OpenHarness, study the `engine/`, `memory/`, and `coordinator/` subsystems in depth. Wire Russell Tuna's `/fork` command to use OpenHarness-style parallel agents with proper lifecycle hooks.

### Skills to migrate to OpenHarness format

- `money-*` skills (14 total) → OpenHarness `.md` skill files
- Russell Tuna Bot commands → OpenHarness command plugin

---

## Comparison to What We Have

| Metric | OpenHarness | Current Solomon OS |
|--------|-------------|-------------------|
| Multi-agent | ✅ Built-in coordinator | ⚠️ /fork, no tracking |
| Cross-session memory | ✅ memdir system | ⚠️ Solomon Vault (manual) |
| Skills | ✅ 40+ .md skills | ✅ 14 money skills |
| Tool permission | ✅ Multi-level | ✅ Hermes safety |
| Code | 11,733 lines Python | Mixed Python/Bash |
| License | MIT | Various |

---

## Verdict

**INTEGRATE** — OpenHarness gives Solomon OS a proven architecture for the harness layer Russell Tuna Bot is missing. The memory subsystem alone is worth the integration — it would solve the cross-session amnesia issue that's been a known gap.

**Next step:** Deep-read `engine/query_engine.py` and `memory/manager.py` to understand how to wire Solomon Vault as the memory backend.