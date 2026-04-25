# RD Report: Deliberate — File-Based Two-Agent Deliberation Protocol

**Fork:** `jvanleur2234-glitch/deliberate-new` | **Original:** `kyleparrott/deliberate` | **License:** MIT | **Stars:** ~200 | **Lang:** Shell

## What It Is
Experimental file-based protocol for two AI agents to deliberate on a local machine. Agents exchange structured JSONL messages. Designed for cross-model dialogue (Claude Code vs Codex) on architecture decisions.

## Key Capabilities
- JSONL-based message exchange in `/tmp/deliberation/`
- Commands: new, seed, send, read, ack, wait, done, status
- Slow deliberation (30s–2min per exchange) for high-level thinking
- No API calls during deliberation — privacy preserving
- Cross-model compatible

## Relevance to Solomon OS
- **Self-Improvement:** File-based approach could power Hermes self-improvement loop
- **Lightweight:** Minimal dependency — pure bash + jq
- **Privacy:** No external API calls during deliberation

## Threat Analysis
- MIT licensed, experimental (0.x)
- Shell-based = auditable, minimal attack surface

## Integration Path
```
SKILL: deliberate-file-deliberation → lightweight two-agent deliberation
USE CASE: Local agent self-review, cross-model discussions
```

**Recommendation:** SKILL — Fork as lightweight deliberation primitive for Hermes self-evolution.
