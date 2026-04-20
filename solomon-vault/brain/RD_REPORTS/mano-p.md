# R&D Report: Mano-P 1.0 — Vision-Based GUI Agent

**Date:** April 18, 2026
**Repo:** github.com/Mininglamp-AI/Mano-P (281 stars)
**Forked:** jvanleur2234-glitch/Mano-P
**License:** MIT
**Status:** QUEUED — macOS-only (M4 required), Windows/Linux in progress

---

## What It Does

Mano-P 1.0 is a pure-vision GUI-VLA (Vision-Language-Action) agent. It "looks" at the screen like a human, understands the interface, and takes actions. No APIs, no DOM access, no browser dependency.

**How it works:**
1. Takes screenshot of current screen
2. Vision model analyzes the UI
3. Plans next action (click, type, scroll, drag, etc.)
4. Executes on local machine
5. Repeats until task is complete

**Key technical details:**
- Runs locally on Mac with M4 + 32GB+ RAM (or USB compute stick)
- **Zero data leaves the device** — fully offline capable
- Long-horizon task planning: tasks with hundreds of steps
- 58.2% success rate on OSWorld benchmark (SOTA for open-source GUI agents)
- Can run quantized 4B model at ~476 tokens/s prefill on M4 Pro

---

## Why It Matters for JCPaid / Solomon OS

**The cross-desktop problem:**
Every existing AI agent tool (OpenClaw, Hermes Agent, browser harnesses) is browser-only or API-dependent. They can't touch:
- Desktop productivity apps (Word, Excel, PowerPoint)
- Native macOS/Windows apps
- Legacy enterprise software
- Custom/internal tools without APIs

**Mano-P solves this.** It sees any UI and can interact with it.

---

## Relevance to JCPaid Stack

| Component | Fit |
|-----------|-----|
| Solomon Browser | Complementary — browser-based, Mano-P = desktop |
| Paseo | Complementary — agent orchestration, Mano-P = execution |
| browser-harness | Complementary — web automation, Mano-P = native desktop |
| Hermes skills | Could add Mano-P as a skill for cross-desktop tasks |
| JackConnect | HIGH — real estate agents use desktop CRMs/MLS daily |

---

## Current Limitations

- **macOS only** (M4 required) — Windows/Linux "in progress"
- Hardware barrier — needs Apple Silicon
- Requires screen recording + accessibility permissions
- Single display only
- Beta software

---

## Strategic Assessment

**For JCPaid:** MEDIUM-HIGH relevance, but hardware-dependent. 
- If we ever ship to Mac users, this is a killer feature
- Could be a future differentiator for the "AI employee" product
- Worth watching — monitor for Windows/Linux support

**For Be Like You! OS:** HIGH relevance if phone OS ever runs desktop apps
- Vision-based = works on any device type
- Could power cross-app automation on the phone

**Recommended action:** Star and watch. Fork now while it's early. Revisit when Windows/Linux support lands.

---

## Related / Competing Projects

- **OmniParser** (Microsoft) — vision-based screen parsing for GUI agents
- **Aguvis** — pure-vision cross-platform GUI automation (web + desktop + mobile)
- **Mano-Skill** — cloud-assisted GUI automation (MIT, v1.0.7)

---

## Priority

🟡 WORTHWHILE — 281 stars, MIT, active development, but macOS-only limits immediate deployment.
