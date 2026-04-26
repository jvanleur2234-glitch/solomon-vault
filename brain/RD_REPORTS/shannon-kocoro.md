# RD REPORT: Shannon by Kocoro-lab

**URL:** https://github.com/Kocoro-lab/Shannon
**Stars:** Not available in README (check separately)
**License:** MIT
**Language:** Go + Rust + Python
**Analysis Date:** 2026-04-26

---

## What It Is

Shannon is a **production-grade AI agent orchestration platform** — think Temporal meets LangChain but with multi-agent swarm collaboration, time-travel debugging, and hard token budget enforcement built in. It runs as a distributed system via Docker Compose: a Go gateway (8080), Go orchestrator (50052/gRPC), Rust agent core (50051), Python LLM service (8000), and optional Playwright browser automation (8002).

Key differentiators vs. what we have:
- **Time-travel debugging** — replay any execution step-by-step (Temporal-powered)
- **Hard token budgets per task/agent** with automatic model fallback
- **WASI sandbox** for secure code execution
- **Swarm mode** — lead-orchestrated multi-agent with convergence detection
- **10+ LLM providers** including MiniMax (we already have MiniMax)
- **Skills system** — drop custom skills into `config/skills/user/`
- **Human-in-the-loop approval** via OPA policies
- **OpenAI-compatible API** — drop-in replacement for existing apps

---

## What We'd Use It For

1. **Replace/integrate into Hermes Agent** — Shannon's orchestration, budget control, and multi-agent swarm capabilities could dramatically upgrade Solomon OS's agent capabilities
2. **Research workflows** — the Research strategy with tiered model routing (50-70% cost reduction) is exactly what Solomon OS needs for R&D research tasks
3. **Skills system** — their gitignored user skills dir pattern is worth stealing for Solomon OS
4. **Time-travel debugging** — apply to Solomon OS agent failures for better observability

---

## How It Compares to What We Have

| Capability | Solomon OS (current) | Shannon |
|---|---|---|
| Agent orchestration | Hermes (manual) | Multi-strategy (DAG, ReAct, Swarm, Research) |
| Token budgets | None | Hard budgets + auto fallback |
| Debugging | Logs | Time-travel replay |
| Sandbox | Unknown | WASI |
| Multi-agent | Manual | Swarm with convergence detection |
| LLM diversity | MiniMax + others | 10+ providers |
| Deployment | Docker | Docker Compose (full stack) |

---

## Technical Notes

- **Stack:** Go (gateway/orchestrator), Rust (agent core enforcement), Python (LLM service/tools)
- **Dependencies:** Docker + Docker Compose, PostgreSQL, Redis, Temporal
- **Desktop app:** Tauri + Next.js (cross-platform)
- **Install:** Single `curl -fsSL https://raw.githubusercontent.com/Kocoro-lab/Shannon/main/scripts/install.sh | bash`
- **Browser automation:** Optional Playwright service (3.4GB image)

---

## FORGE / SKILL / INTEGRATE / SKIP

**VERDICT: INTEGRATE**

Shannon's architecture is production-grade and complementary to Solomon OS. The main integration path:

1. **Study the skills system** — `config/skills/user/` gitignored pattern for user-defined skills is directly applicable to Solomon OS
2. **Evaluate for Hermes upgrade** — Shannon's orchestrator could replace or augment Hermes Agent workflows
3. **Clone and benchmark** — run the one-command install, test the Research strategy vs current Solomon OS R&D workflow
4. **Extract browser automation** — the Playwright service could replace any future scraping needs

The time-travel debugging alone (Temporal-powered) is worth exploring — it could solve the "agent failure opacity" problem that plagues complex agent workflows.

**Risk:** Heavy dependency (full Docker stack) — consider what's already running on the server before installing.
