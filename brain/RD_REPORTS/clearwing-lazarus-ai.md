# RD Report: Clearwing

**URL:** https://github.com/Lazarus-AI/clearwing
**Type:** Security / Offensive AI Tool
**Stars:** ~2.3K (estimated)
**License:** MIT
**Priority:** 🔴 Critical — new AI paradigm + competitor

---

## What it is

Clearwing is an **autonomous vulnerability scanner and source-code hunter** built on LangGraph by Eric Hartford (Lazarus AI). Inspired by Anthropic's Glasswing but designed to work with models everyone has access to (OpenRouter, Ollama, LM Studio, vLLM).

**Two modes:**
1. **Network Pentest Agent** — ReAct-loop agent with 63 bind-tools that scans live targets, detects services/vulns, runs sandboxed Kali tools, attempts exploits (gated by human approval), writes reports to a persistent knowledge graph.
2. **Source-Code Hunter** — File-parallel pipeline that ranks source files, fans out per-file hunter agents, uses ASan/UBSan crashes as ground truth, verifies with adversarial second-pass agent, optionally generates validated patches. Evidence levels go: `suspicion → static_corroboration → crash_reproduced → root_cause_explained → exploit_demonstrated → patch_validated`.

Built in Python. Supports OpenAI-compatible endpoints (Ollama, OpenRouter, vLLM, etc.). Runs as CLI.

---

## What we'd use it for

Joseph runs an **AI White-Collar Staffing Agency** (Russell Tuna as hired AI worker). Security auditing is white-collar work. This could be a **premium offering**:

- Offer AI-powered vulnerability scanning as a service to businesses
- Scan client codebases/repos for vulnerabilities
- Network penetration testing for SMBs

Also relevant to **Arena.ai pipeline** — if Joseph is building an AI model selector/ranking business, security of the platform matters.

---

## How it compares to what we have

| Feature | Clearwing | What we have |
|---|---|---|
| Network pentest | 63-tool ReAct agent | ❌ None |
| Source-code vuln hunting | ASAN/UBSAN + LLM hunters | ❌ None |
| Works with Ollama | ✅ Yes | Russell Tuna uses Ollama |
| LangGraph-based | ✅ Yes | ❌ (Solomon Bus uses different architecture) |
| CLI-first | ✅ Yes | Partially (Hermes CLI) |

This fills a **huge gap** in Solomon OS's capabilities. Right now we have no security auditing capability.

---

## What it would take to integrate

1. Install: `git clone https://github.com/Lazarus-AI/clearwing && cd clearwing && uv sync --all-extras`
2. Configure API keys (Ollama or OpenRouter)
3. Run `clearwing setup` and `clearwing doctor`
4. Usage: `clearwing scan <target>`, `clearwing sourcehunt <repo>`
5. Could be wrapped as a Hermes skill

**Dependencies:** Python 3.10+, Rust toolchain (for genai-pyo3 bridge), Docker (for Kali/sandbox features).

---

## Recommendation

**FORGE** — This is a high-value capability addition. Joseph should add autonomous security auditing as a tier in his AI staffing agency. It's a natural fit: white-collar knowledge work, premium pricing, clearly deliverable output (reports). 

**Next step:** Clone it, run `clearwing doctor` to check dependencies, test against a sample target.
