# RD Report: Factory AI Droid Computers

**Date:** 2026-04-22
**URL:** https://x.com/FactoryAI/status/2047039612011545003
**Source:** X thread by @FactoryAI (Factory)
**Status:** Queued — FORGE

## What It Is

Factory AI launched **Droid Computers** — persistent cloud machines for remotely orchestrating AI agents. 60,973 views, 438 likes in hours. Two modes:
- **Managed Computers**: spin up in Factory's cloud
- **BYOM (Bring Your Own Machine)**: register any laptop/Mac Mini/VM as a Droid Computer

**Core pitch:** Stateful > Ephemeral. Agents get their own filesystem, credentials, and configurations that persist across sessions. Kick off work from your phone, queue overnight tasks, build always-on agents that triage alerts and run deep research. Sessions build on each other = agents get smarter over time.

## What We Have That's Equivalent

| Feature | Factory AI | Solomon OS / JackConnect | Winner |
|---|---|---|---|
| Persistent machine | ✅ Droid Computer | ✅ Your server (Zo Computer) | Solomon OS |
| Own filesystem | ✅ Per Droid | ✅ Full root access | Solomon OS |
| Credentials stored | ✅ Per Droid | ✅ API keys in Zo secrets | Solomon OS |
| Session memory | ✅ Builds over time | ✅ Russell Tuna brain files | Solomon OS |
| BYOM | ✅ Register any machine | ✅ We install on spare T15 | Solomon OS |
| Kick off from phone | ✅ Telegram integration | ✅ Telegram-native (already here) | Solomon OS |
| Always-on agents | ✅ Droids | ✅ Solomon Bus + heartbeat | Solomon OS |
| Agent marketplace | ✅ Factory fleet | ❌ JackConnect skills registry | Factory AI |
| Free tier | Unknown | ✅ Free tier in JackConnect | ? |
| Multi-agent orchestration | ✅ Multiple Droids | ✅ Hermes + Solomon Bus | Solomon OS |
| Computer use / screen | ✅ Video shows browser | ✅ Solomon Browser (Playwright) | Push |

## What Factory AI Does Better

1. **Managed cloud option** — users who don't have a spare machine can still use it. We need JackConnect to have a hosted option.
2. **Agent marketplace** — Factory has a fleet marketplace. JackConnect needs the skills marketplace we're building.

## Strategic Implications for JCPaid

**This VALIDATES our entire thesis.** Factory AI just proved:
- Persistent stateful agents > ephemeral sandboxes ✅
- BYOM model works ✅
- Phone-to-agent workflow is wanted ✅
- Always-on background agents are the future ✅

**The gap we fill vs Factory AI:**
- Factory AI is expensive/proprietary. JackConnect is self-hosted = users own their data and agents.
- Factory AI doesn't have vertical-specific agents. We do (real estate, law, dental, etc.).
- Factory AI doesn't have the "watch once" automation we have.

## Action Items

1. **Competitive positioning**: JackConnect = "Factory AI but you own the machine and the agents"
2. **Add managed hosting option**: For users who don't have a spare computer, offer hosted JackConnect (we host on our server, they connect via web)
3. **BYOM install must be dead simple**: The T15 one-command install we're building IS the BYOM flow. Make it frictionless.
4. **Study Factory AI's pricing**: When they publish pricing, position JackConnect as 80% cheaper.

## Recommendation

**FORGE** — This is a direct competitor and validation. Clone the best ideas:
- Session persistence visualization (show agents remembering things)
- Phone-to-agent workflow (Telegram already does this — lean in harder)
- BYOM model (our T15 install IS this — make it the hero feature)

Build JackConnect as the self-hosted, affordable, vertical-first alternative to Factory AI's Droid Computers.