# R&D Report: ClawLess — Browser-Based AI Agent Runtime

**Date:** April 18, 2026
**Repo:** github.com/open-gitagent/clawless — 283 stars, MIT License
**Forked:** jvanleur2234-glitch/clawless

## What It Does
WebContainer-powered AI agent runtime that runs entirely in the browser (WASM sandbox). No server required.
- Full Node.js environment in browser via WebContainers (3.4M+ npm packages)
- Monaco Editor + xterm.js terminal with full PTY support
- Built-in GitHub integration (clone, commit, push via API)
- YAML-based policy engine with glob patterns for agent guardrails
- Complete audit logging (process, file, network, git events)
- Plugin system with lifecycle hooks
- Template system for agent bootstrapping
- Multi-provider AI (Anthropic, OpenAI, Google)

## Architecture
| Component | Role |
|---|---|
| ClawContainer | SDK facade — single entry point |
| ContainerManager | WebContainer orchestration |
| PolicyEngine | YAML guardrails for file/process/network rules |
| AuditLog | Full event trail |
| GitService | GitHub API integration |
| PluginManager | Lifecycle hooks |
| UIManager | Monaco Editor + xterm.js |

## Why It Fits Solomon Browser
1. **Solo execution runtime** — agent runs fully isolated in browser tab
2. **Built-in audit logging** — compliance + safety
3. **Policy engine** — define guardrails per task
4. **GitHub integration** — auto-commit work results
5. **Template system** — pre-configured agent templates for common tasks

## How It Complements vs Replaces
- **Complements OpenClaw/Browser-use:** ClawLess is solo/agent-facing, those are orchestrator-facing
- **Replaces need for server-side agent:** no backend needed for simple tasks
- **Policy engine maps to Solomon Guardian:** same concept, different layer

## Integration Plan
1. Fork ClawLess → `jvanleur2234-glitch/clawless`
2. Build Solomon Browser UI wrapper
3. Add Solomon OS skill templates (pre-configured prompts for business tasks)
4. Wire audit logs → Solomon Bus

## Full RD Report
https://github.com/jvanleur2234-glitch/clawless

## LINK Fit
★★★★★ — #browser #agent-runtime #policy-engine #audit-logging #solomon-browser