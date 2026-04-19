# R&D Report: Paseo

**Date:** April 18, 2026
**Repo:** github.com/getpaseo/paseo (4K stars, AGPL-3.0)
**Forked:** github.com/jvanleur2234-glitch/paseo

---

## What It Is

Mobile-first AI coding agent orchestrator. Phone + desktop + CLI + web, all connected to the same local daemon. Voice control, multi-agent, cross-device. Claude Code + Codex + OpenCode through one interface.

## What It Does

- Daemon (Node.js) manages all agent processes on port 6767
- Mobile app (Expo) connects via QR code — no cloud, no account
- Relay package for E2E encrypted remote access behind firewalls
- WebSocket protocol, binary multiplexing (terminal + streaming share one connection)
- MCP server for agent-to-agent control built in
- Permission requests go: agent → daemon → client → user → daemon → agent
- Agent state persists to `$PASEO_HOME/agents/`
- Orchestration skills: `/paseo-handoff`, `/paseo-loop`, `/paseo-orchestrator`

## Architecture

```
Mobile App / CLI / Desktop → WebSocket → Daemon (port 6767) → Claude / Codex / OpenCode
                                        ↓
                                   MCP Server
                                   (sub-agent creation)
```

## Why It's Critical for JCPaid

**We were trying to build exactly this from scratch.** Russell Tuna needed cross-device orchestration, mobile control, voice input. Paseo has ALL OF IT, production-ready.

**The integration path:**
1. Fork Paseo (done: jvanleur2234-glitch/paseo)
2. Add Russell Tuna as a new provider (like Claude/Codex/OpenCode)
3. Russell Tuna Telegram bot connects to Paseo daemon as a client
4. Joseph sends `/run "research competitor pricing"` from Telegram → daemon spawns Russell fork → streams results back
5. Mobile app gives Joseph a native iOS/Android UI for full control

**This is the missing piece between Russell Tuna and a real product.**

## How It Compares to What We Have

| Capability | Before Paseo | After Paseo |
|---|---|---|
| Mobile control of agents | ❌ | ✅ Native iOS/Android app |
| Voice input | ❌ | ✅ Voice mode built in |
| Cross-device | Partial (Telegram only) | ✅ Same daemon, any device |
| Agent-to-agent | ❌ | ✅ Built-in MCP server |
| Permission flow | Manual | ✅ Native permission request protocol |
| Remote access | ❌ | ✅ E2E encrypted relay |

## What We'd Use It For

1. **Russell Tuna mobile app** — Replace Telegram with native Paseo app
2. **Multi-agent orchestration** — `/fork` spawns Paseo agents, streams to Joseph's phone
3. **Voice-driven tasks** — "Hey, run a competitor audit" from anywhere
4. **Cross-device continuity** — Start task on phone, continue on desktop

## Recommendation

**🔥 FORGE IMMEDIATELY**

This is the cross-device orchestration layer we needed. Add Russell Tuna as a Paseo provider. Integrate the relay so Joseph can access his dev environment from anywhere without opening ports.

**Priority:** CRITICAL — closes the biggest gap in the JCPaid stack.
**Effort:** Medium (2-3 weeks to integrate Russell Tuna as provider)
**License:** AGPL-3.0 — can fork, must publish modifications
