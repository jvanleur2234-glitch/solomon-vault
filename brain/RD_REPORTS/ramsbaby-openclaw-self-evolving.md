# RD Report: ramsbaby/openclaw-self-evolving

**Date:** April 26, 2026  
**Fork:** Check workspace  
**License:** MIT  
**Language:** Python/Bash  

## What It Is
Shell-based weekly pipeline that analyzes agent logs to propose improvements to behavior rules (AGENTS.md/CLAUDE.md) without automatic changes.

## How It Works
1. **Analyze logs:** Scans ~/.openclaw/logs and ~/.claude/logs
2. **Identify patterns:** Detect repeated bad behaviors (retry loops, violations, user frustration)
3. **Generate proposals:** Before/After diffs for rule enhancements
4. **User approval:** Human reviews and approves/rejects
5. **Output:** Discord messages or GitHub issues with proposals

## Key Features
- **Rule-change proposals:** Before/After diff documentation
- **Rejected ID filtering:** Tracks previously rejected proposals
- **Offline operation:** No API calls, pure bash + python3
- **Periodic execution:** Weekly improvement cycles

## Connection to OpenClaw
This is an OpenClaw ecosystem tool. OpenClaw (by Kye Gomez) is the predecessor to OpenMythos. This self-evolving mechanism shows how OpenClaw agents improve over time.

## Solomon OS Fit
**SKILL** — Weekly log analysis → rule improvement pipeline. This is a lower-cost alternative to real-time self-improvement. Could be a scheduled Hermes agent that reviews its own behavior weekly.

## Action
Clone if not in workspace. Study. Add weekly self-review to Hermes agent scheduler.