# RD Report — Hyperspace Pods x Solomon Air

**URL:** https://x.com/i/status/2044882359565312468
**Date:** 2026-04-17
**Joseph Handle:** josephv
**Status:** INTEGRATE

---

## What It Is
Hyperspace Pods pools a small group's laptops/desktops into one AI cluster. Models like Qwen 3.5 32B or GLM-5 Turbo get auto-sharded across devices — layers split proportionally, inference pipelined through a ring. Exposes an OpenAI-compatible API with a pk_* key. Falls back to cloud at wholesale rates when a query needs a frontier model. No central server. Uses Raft consensus for pod state.

**Key features:**
- No port forwarding / NAT traversal built in
- Model sharding handled automatically
- Treasury system for shared cloud fallback budget
- Compute marketplace for idle pod capacity
- Pod federation (pods ally with other pods)

**Community red flags:**
- Repo is release-only, no source (one user called it "malware until proven otherwise")
- Network latency in distributed sequential inference is a real bottleneck
- Requires actual hardware coordination (CLIs, GPU machines)

---

## What This Means for Solomon Air

**Hyperspace is solving the same problem the Airlines Plan was指向 — pooled compute, no middleman, OpenAI-compatible API.**

The good news: Solomon Air already has a better node model (every browser tab = a node, zero install friction). Bonsai 1.7B is the browser-layer equivalent to what Hyperspace does with GPU clusters.

**The two-tier opportunity:**
- **Tier 1 (Browser):** Casual users running Bonsai in a tab. Low compute, massive reach.
- **Tier 2 (GPU Pods):** Power users / businesses with actual GPU rigs. Hyperspace-style pooled inference.

Solomon Air's "one button Ask" app could surface both tiers under a single API. Browser nodes handle lightweight tasks free. GPU pods handle heavy workloads and earn TAO / payment. The Hyperspace pod marketplace vision maps directly onto the Bittensor-style compute exchange.

**The piece Solomon Air needs that Hyperspace doesn't have yet:** The directory/routing layer (Solomon Air's "Solomon Air app" + Bittensor) that directs prompts to the right tier.

---

## How They Compare

| | Hyperspace Pods | Solomon Air (Airlines Plan) |
|---|---|---|
| Node model | CLI + physical hardware | Browser tab (Bonsai) + CLI pods |
| Identity | Raft consensus | Reticulum key pairs |
| Transport | Their P2P network | Reticulum (mesh) + internet |
| API | OpenAI-compatible | OpenAI-compatible (Solomon Air gateway) |
| Payment | Treasury + marketplace | Bittensor TAO |
| Open source | ❌ Closed | ✅ Open |
| Federation | Coming soon | Pod alliance baked in |
| NAT traversal | ✅ Built in | ✅ Reticulum handles |

---

## What Solomon Air Should Take from This

1. **Treasury/fallback model** — exactly what Solomon Air needs. Casual users get free browser inference. Requests that exceed browser capacity fall back to GPU pods at wholesale rates, paid from a shared treasury.

2. **Pod federation = pod alliances** — the Airlines Plan already had this with the Bittensor subnet concept. Hyperspace validating this model makes it stronger.

3. **OpenAI-compatible API as the abstraction layer** — this is the key UX insight. Solomon Air users just change base_url + key. Everything underneath is invisible.

4. **Real NAT traversal** — Reticulum already handles this. Hyperspace had to build it themselves. Solomon Air has it for free.

---

## Recommendation

**INTEGRATE — not as competition, but as the missing pieces.**

The Airlines Plan was conceptually right but had gaps in the compute layer. Hyperspace Pods fills those gaps by demonstrating:
- Model sharding over unreliable networks is solvable
- Raft consensus for pod state works without a central server
- Treasury/fallback billing is a real UX pattern users understand

Solomon Air's differentiated advantage: open-source, browser-first node discovery layer on top of a Hyperspace-style GPU pod infrastructure. Where Hyperspace is closed and hardware-gated, Solomon Air should be open and browser-first for casual nodes, with GPU pods as the power tier.

**Priority:** HIGH — validates the Airlines Plan architecture. Build the Bonsai browser node first (zero-friction entry), then layer on GPU pod marketplace.