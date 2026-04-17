# RD REPORT: SOVEREIGN DISTRIBUTED AI — BONSAI + RETICULUM + AIRLINES PLAN
**Source:** X posts (PrismML Bonsai 1.7B, Ratspeak/Reticulum), Airlines Plan
**Date:** 2026-04-16
**Status:** 🔴 CRITICAL — browser = node solves compute layer problem

---

## WHAT EACH PIECE DOES

### Bonsai 1.7B (PrismML)
- 290MB, true 1-bit weight model
- Runs 100 tokens/sec in browser via WebGPU
- Apache 2.0 license
- Demo: https://huggingface.co/spaces/webml-community/bonsai-webgpu
- 8B version = 1.15GB (still tiny vs 8B full-precision)
- **Key insight:** Every browser tab = a compute node. No installation, no API key.

### Ratspeak + Reticulum
- Messaging firmware on Reticulum protocol
- Crypto key pair = identity (no CA, no phone #, no account)
- Works over LoRa, WiFi, Bluetooth, internet, serial, packet radio
- Self-organizing mesh, zero infrastructure
- Already shipping on Lilygo T-Deck, M5Stack, ESP32
- iOS/Android/desktop clients in development
- Source: https://ratspeak.org

### Airlines Plan
- 5-layer architecture: directory → routing → proof → payment → privacy
- Built on: NOMAD, Hyperspace, Tensorlink, LlamaNet, Bittensor
- Year 1: points system. Year 2: Bittensor subnet
- Grandma UX: download → click → works

---

## HOW THEY FIT TOGETHER

The Airlines Plan had 4 of 5 layers. Missing: the physical transport + identity + compute node problem.

**Bonsai + Reticulum solve exactly what's missing:**

```
┌─────────────────────────────────────────┐
│ LAYER 5: PRIVACY MARKET (ZK proofs)     │
├─────────────────────────────────────────┤
│ LAYER 4: PAYMENT (Bittensor TAO)        │
├─────────────────────────────────────────┤
│ LAYER 3: PROOF SYSTEM (ZK validators)   │
├─────────────────────────────────────────┤
│ LAYER 2: ROUTING (Tensorlink/LlamaNet)  │
├─────────────────────────────────────────┤
│ LAYER 1: PHONE BOOK (DHT directory)     │
├─────────────────────────────────────────┤
│ ⚡ BONSAI WEBGPU = COMPUTE NODE ⚡       │ ← NEW
│ Every browser tab = a node              │
│ 100 tokens/sec, no installation         │
│ 290MB model, runs anywhere              │
├─────────────────────────────────────────┤
│ ⚡ RETICULUM = TRANSPORT + IDENTITY ⚡  │ ← NEW
│ Crypto key = node identity              │
│ Mesh over LoRa / WiFi / internet        │
│ Self-organizing, zero infra              │
└─────────────────────────────────────────┘
```

**Why this is different from every other approach:**
- Traditional P2P AI: need to install software, run a node, configure GPU
- Bonsai approach: open Chrome, you're already a node
- Reticulum: no internet required for identity/connectivity

---

## THE SYNERGY

### The Node Problem (Solved)
Every other distributed AI project struggles with: "how do we get people to run nodes?"

Bonsai's WebGPU answer: **every browser tab is already a node.** No installation. No GPU. No configuration. The node problem becomes trivial.

### The Identity Problem (Solved)
Reticulum's crypto key pair = identity baked into every packet. No central authority. No phone number. No account to create.

### The Off-Grid Problem (Solved)
Reticulum works over LoRa — radio waves, no internet. Bonsai runs locally on device. Together: AI that works in a field hospital in Malawi with no connectivity.

### The Payment Problem (Solved)
Airlines Plan's Layer 4 = Bittensor TAO rewards. Relay operators earn for bandwidth. Compute providers earn for inference. Bonsai browser nodes could earn for idle GPU cycles via WebGPU.

---

## WHAT THIS ENABLES

### On-Grid (Normal)
- User opens browser → asks Solomon Air → request routes to best available compute
- Bonsai handles simple queries locally (no network round-trip)
- Complex queries route to GPU nodes via Airlines Plan routing
- Payment via Bittensor

### Off-Grid (Resilient)
- Reticulum mesh over LoRa radio
- Bonsai runs locally on each device
- No internet dependency at any layer
- Works in disaster zones, rural areas, censored regions

### Privacy-First
- Reticulum E2E encrypted by default
- Airlines Plan Layer 5 = ZK proofs for anonymous insights
- Bonsai can run locally (data never leaves device)

---

## WHAT'S MISSING / NEXT STEPS

### What's Working
- Bonsai 1.7B: production-ready, Apache 2.0 ✅
- Reticulum: production-ready, MIT ✅
- Airlines Plan: architecture defined, needs build

### What Needs Building
1. **Reticulum → Bonsai bridge**: Route Bonsai inference requests over Reticulum transport
2. **Browser node incentive**: Connect Bonsai WebGPU idle cycles to Airlines Plan rewards
3. **Solomon Air app**: Simple UI that ties it all together (Layer 1-2 of Airlines Plan + Reticulum identity)
4. **Relay layer**: Fork RustDesk hbbs/hbbr for off-grid relay infrastructure (already in RD queue)

### Technical Questions
- Can Reticulum carry arbitrary TCP/UDP traffic, or only its own protocol?
- Can Bonsai WebGPU participate in distributed inference (multi-node), or only single-node?
- What's the actual bandwidth requirement for Bonsai inference over Reticulum?

---

## RECOMMENDATION

### FORGE — ALL OF IT

This is a coherent architecture. Build priority:

1. **Bonsai integration** (immediate): Browser-based compute nodes are the missing piece in the Airlines Plan compute layer. Start with the Web demo, fork into Solomon Air.

2. **Reticulum integration** (this month): Study how Reticulum handles transport. Test if it can carry inference traffic. Deploy on our Ollama servers as a proof-of-concept.

3. **RustDesk relay** (already queued): The relay infrastructure for off-grid nodes. Fork hbbs/hbbr, add Reticulum identity layer.

4. **Airlines Plan Layer 1-2** (Q2): Directory + routing. Fork NOMAD, integrate Bonsai + Reticulum.

**Priority order:** Bonsai → Reticulum transport test → Airlines Plan Layer 1-2 → RustDesk relay → Bittensor subnet

---

## FILES
- Source (Bonsai): https://huggingface.co/spaces/webml-community/bonsai-webgpu
- Source (Reticulum): https://github.com/markqvist/Reticulum
- Source (Ratspeak): https://ratspeak.org
- Source (Airlines Plan): `/home/workspace/solomon-vault/raw/airlines-plan-full-2026-04-15.md`
- Previous synthesis: `/home/workspace/solomon-vault/raw/SOVEREIGN_DISTRIBUTED_AI_REPORT.md`

---

*Synthesized by Zo — 2026-04-16*
