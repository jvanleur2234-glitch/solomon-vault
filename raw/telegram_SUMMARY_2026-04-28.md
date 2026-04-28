# Telegram Session Summary — 2026-04-28

## Date & Context
Morning session. Joseph continued where Apr 27 left off.

## Key Decisions Made
- **Russell Tuna → NVIDIA NIM**: Upgraded Russell Tuna's backend from Ollama qwen3 to NVIDIA Nemotron-3-Nano (via ai.api.nvidia.com). Had to fix 3 bugs: undefined NVIDIAAPIKEY, undefined messages, wrong API URL path (/v1/ missing).
- **Business Idea Scout**: Killed failing Money Maker agent. Replaced with focused Business Idea Scout running every 3 days.
- **BrickPortrait business**: Analyzed the Lego AI custom portrait idea from the China 7-agent video. Found Bricklink API for parts lookup + Midjourney for rendering. Joseph wants to build it.
- **7-Agent Business Playbook**: Created from the China video. Documented the exact agent roles (classifier, reader, handler, tone-watcher, escalator, reporter, orchestrator).
- **Polymarket trading**: Researched 20+ repos. Cloned top 4: Polymarket/agents (official), TradingAgents, Polymarket-Arbitrage-Bot, PredictOS. Got Polymarket/agents live and returning real market data. Fixed web3 v7 compatibility.

## Repos Cloned Today
- `solomon-huginn` — Huginn self-hosted automation (11.5k stars)
- `solomon-cloner` — AI website cloner
- `solomon-maps-leads` — Google Maps → CSV lead gen
- `solomon-openphone` — HKUDS autonomous AI phone agent
- `solomon-opencli` — OpenCLI v1.7.8
- `solomon-polymarket-agents` — Official Polymarket AI agents
- `solomon-trading-agents` — Tauric multi-agent trading framework
- `solomon-poly-arb` — Polymarket arbitrage bot
- `solomon-predict-os` — PredictOS prediction market OS

## Skills Added
- clone-website (from solomon-cloner)
- google-maps-leads (from solomon-maps-leads)
- openphone-agent (from solomon-openphone)
- opencli-browser (from OpenCLI v1.7.8)

## Research Saved
- `brain/RESEARCH_ANTHROPIC_LABOR_STUDY.md` — AI kills entry-level tasks, elevates senior workers
- `brain/RESEARCH_PSYCHOLOGY_AI_MEMORY.md` — Layered memory architecture (episodic/semantic/procedural/working)
- `brain/BUSINESS_PLAYBOOK_7AGENT.md` — The China 7-agent blueprint

## Still Running
- Russell Tuna bot → NVIDIA NIM (tmux)
- Solomon Flow API on port 3021 (tmux)

## Unresolved
- Polymarket trading needs funded Polygon wallet + non-US location
- Huginn full install blocked (needs Docker daemon or 1GB RAM sacrifice)
- BrickPortrait needs: Midjourney API, Bricklink API, Stripe checkout
- TradingAgents → Polymarket hybrid not built yet

## Joseph's Priority Direction
"Don't tell me what businesses to do. Tell me what YOU would do and just build it."
→ Focus on: Polymarket trading + BrickPortrait (both fit his Connector brain + Sherlock audit skill)