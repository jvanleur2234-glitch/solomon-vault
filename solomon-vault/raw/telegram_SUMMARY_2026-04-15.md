# SESSION SUMMARY — 2026-04-15

## Big Strategic Discussion: The Airlines Plan

### What Joseph Believes
- AI is moving toward 1-3 companies dominating everything
- Governments + big tech want to control AI to control people
- Need to build open-source AI that runs on infrastructure nobody controls
- Blockchain/crypto rewards for contributors is part of the answer

### The Airlines Not Railroads Plan
Companies built railroads — everyone had to use them. Airlines own the infrastructure, planes can fly anywhere.

**Solomon Air = the airline of AI.**
- Not building AI models
- Building the infrastructure layer that connects AI providers to AI users
- Hardware people own + networks they control + incentive systems (crypto later)

### Key Research Today
- Oracle, Nvidia, Microsoft, Google = dominant players
- Open source is the main defense (DeepSeek proved this)
- Bittensor TAO = blockchain AI incentive model
- TEE (Trusted Execution Environments) = privacy-preserving compute

---

## Repos Reviewed and Forked

### Forked (all on GitHub: jvanleur2234-glitch)
| Repo | Stars | Why Forked |
|------|-------|-----------|
| solomon-air (NOMAD) | 23.8K | Core offline AI stack |
| screenpipe | 30K | Screen capture for JackConnect |
| Thoth | 1.4K | Local AI agent + knowledge graph |
| maxun | 15.4K | No-code web scraping |
| coolify | 53K | Self-hostable PaaS |
| KittenTTS | — | Local TTS |
| rustdesk | 111K | Self-hostable remote desktop |
| moonshine | — | Local LLM |
| deterministic-inference | — | TEE inference |
| gbrain | 1.4K | SKILLPACK patterns (from earlier) |

### Researched (not forked)
| Repo | Stars | Why Not Forked |
|------|-------|---------------|
| RAGFlow | 78.2K | Reference only |
| Dayflow | — | Reference only |
| OpenSwarm | — | Reference only |
| meta-harness | Stanford | Reference only |
| Bonsai 1.7B (PrismML) | NEW | 290MB 1-bit LLM in browser — TOP PRIORITY to add |
| Ratspeak + Reticulum | — | Off-grid mesh comms — RESEARCH |

---

## FakerFaker — Built Today

**URL:** https://josephv.zo.space/fakerfaker
**GitHub:** github.com/jvanleur2234-glitch/fakerfaker

### What It Does
Paste a Facebook profile link → AI analyzes it → tells you if it's a scammer

### Stack
- Frontend: React on zo.space
- API: `/api/fakerfetcher` on zo.space
- AI: Ollama (qwen3:1.7b) for username analysis
- Maxun: could replace Ollama for real scraping (not integrated yet)

### Key Learnings
- Share links (facebook.com/share/xxx) = NOT profile links, can't verify
- Mobile Facebook: tap ⋮ → Copy Link = real profile URL
- Scraping Facebook profiles = blocked by Cloudflare
- FakerFaker scores are only as good as the signals we can see
- Real scam detection needs: friends list, post history, account age — all blocked

### What's Broken
- Ollama API call might fail if Ollama not running
- Share link detection works but users don't know how to get real profile URL
- FakerFaker is MVP — needs Maxun scraping to be real

---

## JackConnect — Status

Already fully specced out in /home/workspace/jack-connect/
- 7 AI agents for real estate
- Watch Once automation
- Solomon Companion (Tauri desktop app)
- Screenpipe integration planned
- Thoth planned for knowledge graph

---

## Solana Air Plan — Updated

Updated SOLOMON_AIR.md in MegaPlan with:
- 4 layers: Privacy First → Compute Network → Sovereign Comm → Open Ecosystem
- All forked repos mapped to layers
- Business use cases (JackConnect, FakerFaker, Lume, SubTrim)
- Phase 1 build order

---

## Key Decisions Made
1. Brand name: SOLOMON AIR ✓
2. Fork NOMAD → solomon-air ✓
3. Build FakerFaker ✓
4. Fork rustdesk ✓
5. Bonsai 1.7B is the holy grail — add to plan ✓

---

## Unresolved
- Bonsai 1.7B not yet forked or integrated
- FakerFaker needs Maxun for real scraping
- Ollama API call reliability in fakerfetcher
- Thoth not yet forked

---

## Sync to GitHub
- syn
