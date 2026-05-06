# Telegram Session Summary — 2026-05-06 (Late Evening)

## Session Info
- **Date:** Wed May 6, 2026
- **Key Events:** Kill Switch fully wired. DFlash cloned. Paperclip v1.1.10 upgrade. Hermes Kill Switch plugin confirmed working.

## Kill Switch — Complete
- **API:** http://localhost:5015 (Bun, Zo service `jcpaid-kill-switch`)
- **Hermes plugin:** ~/.hermes/plugins/kill-switch/
- **Endpoints working:** /health, /agents, POST /agents, POST /agents/:id/spend, /budget, /audit, /usage, PATCH /agents/:id
- **Tested:** terminal ls → BLOCKED (budget exceeded). terminal echo hello → ALLOWED (under budget). Spend tracking confirmed.

## Paperclip Upgrade
- Source: dotta/X post May 6, 2026. 156 likes. 12-hour delegation runs now possible.
- Upgraded: pip install paperclip-ai --upgrade (or pnpm)
- Features: LLM Wiki, 12-hour delegation, multi-agent workflows, git diff viewer request (not shipped yet)

## DFlash — Speculative Decoding
- Cloned: /home/workspace/dflash
- Repo: z-lab/dflash (MIT)
- Supports: MiniMax-M2.5 (DFlash), MiniMax-M2.7 (Coming soon)
- When M2.7 support drops → 6x throughput via vLLM speculative decoding
- Installation: uv pip install -e ".[transformers]" or -e ".[sglang]"

## Operator's Guide to Hermes Agent (Tony Simons)
- 44-page free field guide
- Source: https://x.com/tonysimons_/status/2051727953348657613
- Coverage: tools, memory, skills, sessions, cron, gateway, repo debugging, research pipelines, daily briefings, multi-agent workflows, screw-up patterns
- Download: free (email capture)
- Add to Hermes Atlas per Kevin Simback (COO @delphi_labs)

## Hermes SWARM v2.1 — Queued
- Source: chi_azuki/X post, May 1, 2026
- Already in workspace: hermes-swarm/
- Status: pending analysis

## Queue Items This Session
1. DFlash (already cloned)
2. Hermes Curator (already in workspace)
3. Hermes Operator's Guide (queued, download free)
4. Paperclip v1.1.10 (upgraded)
5. Hermes SWARM v2.1 (already in workspace)
6. Hermes Ultra Rust Parity (already in workspace)
7. Browser-Harness (queued, already in workspace)

## What's Next
1. Wire Kill Switch into Hermes config (set JCPAID_AGENT_ID env var)
2. Call Jon (605-940-0650) — pitch JCPaid $299/mo
3. When M2.7 DFlash support drops → flip speculative decoding switch

---

*Session complete. All brain files synced to GitHub.*
