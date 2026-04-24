# RD Report: GBrain 0.19 / OpenClaw-Hermes Skill System

**Source:** https://x.com/Voxyz_ai/status/2047601444426027490 (via Garry Tan / YC)
**Date:** April 24, 2026
**Handle:** @Voxyz_ai

---

## What It Is

GBrain is the AI "brain" layer in GStack (Garry Tan'sYC-backed dev environment product). The 0.19 release brings a skill system called OpenClaw/Hermes into focus.

---

## Key Features Announced

### `gbrain check-resolvable` — Surface "Dark Skills"
Skills installed but unreachable get surfaced in one command. This is essentially a skill discovery/audit command for skills that got installed but didn't register properly or aren't accessible through normal paths.

### `gbrain skillify` — Turn Failures Into Permanent Skills
Take a failed task/scaffold and promote it into a reusable skill. The example given:
```
gbrain skillify scaffold webhook-verify --description "..." --triggers "..."
```
One command generates everything the skill needs (trigger phrases, description, scaffold).

### `gbrain routing-eval` — Fix Skill Routing
Evaluates whether what the user types actually routes to the right skill. Checks if user phrasing gets sent to the wrong skill — essentially a debugging tool for skill routing accuracy.

### Self-healing jobs supervisor (v0.20.2)
Long-running tasks won't die silently anymore. Jobs supervisor self-heals.

---

## What This Means for Solomon OS

**These patterns are directly applicable to our Hermes skill system:**

1. **Dark skill discovery** — We should have a `hermes list-dark-skills` or similar command that surfaces skills that are installed but not responding/hidden from the normal skill index.

2. **Failure → skill conversion** — We already do something like this with the "save as skill" workflow, but the GBrain version is more programmatic: one command that takes a failed scaffold and generates a full skill with triggers + description.

3. **Routing evaluation** — We don't have a good way to debug why a user's phrase routes to Skill A instead of Skill B. A `hermes routing-eval "自然语言"` tool that shows which skill would be matched and why would be incredibly useful for debugging.

4. **Self-healing jobs** — The background worker tracking we do (saving PIDs to `bg_workers_tracking.json`) could be upgraded with self-healing semantics — if a bg worker dies, auto-restart it and notify the user.

---

## Verdict

**FORGE** — The OpenClaw/Hermes skill system architecture is very close to what we're building in Solomon OS. The dark skill surfacing and routing-eval concepts are worth stealing for Hermes.

**Priority:** 🟡 Worthwhile — not urgent but good architectural inspiration.