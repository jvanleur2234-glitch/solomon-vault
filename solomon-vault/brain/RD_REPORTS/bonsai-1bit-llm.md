# RD REPORT: Bonsai 1-bit LLM by PrismML

**Date:** April 15, 2026
**Type:** AI Model / Edge Inference
**Source:** https://x.com/i/status/2044283011416375481 + PrismML announcement
**Priority:** 🔴 Critical

## WHAT IT IS

Bonsai is a family of **true 1-bit LLMs** (binary weights, not quantization) from PrismML, a Caltech-originated AI lab focused on "intelligence density."

Three sizes:
- **Bonsai 1.7B** — 290 MB, runs in any browser via WebGPU (~100 tok/s)
- **Bonsai 4B** — ~550 MB
- **Bonsai 8B** — 1.15 GB, competitive with full-precision 8B models

Claims: 14x smaller, 8x faster, 5x more energy-efficient than full-precision counterparts.

**License: Apache 2.0** — fully open, commercial use allowed.

Demo: https://huggingface.co/spaces/webml-community/bonsai-webgpu

## AIRLINES PLAN INTEGRATION

Bonsai directly solves the compute layer problem in the Airlines Plan:

| Airlines Plan Need | Bonsai Solution |
|--------------------|-----------------|
| Nodes that anyone can run | Browser tab = node. Zero install, any device. |
| Low-friction contribution | Open URL, contribute WebGPU compute, earn AirMiles |
| Hardware-agnostic | Works on Intel/AMD integrated GPU, Apple Silicon, even CPU |
| Privacy-preserving inference | On-device, data never leaves browser |
| Global scale | No CUDA required. Chromebooks, old laptops, phones all become nodes |

**The key unlock:** The Airlines Plan wanted a world where compute contributors get rewarded. Bonsai makes every browser a potential compute node — not just people with GPUs. Billions of devices instead of millions.

**Three integration tiers:**

1. **Layer 0 client** — Solomon Air Browser: open a tab, contribute WebGPU cycles, earn AirMiles. Zero friction to join network.
2. **Privacy market** — Bonsai's browser-native inference means private conversations stay on-device. Natural fit for the privacy market layer.
3. **ARIA Protocol validation** — 1-bit inference proven to work at scale. Validates the technical thesis.

## COMPARISON TO PLAN ELEMENTS

Bonsai 1.7B (290 MB) vs qwen3 1.7B via Ollama (~1.1 GB):
- Bonsai: runs anywhere, no GPU needed, ~100 tok/s
- qwen3: needs local GPU (2GB VRAM), ~30 tok/s

Bonsai is smaller and faster for browser use cases. For heavy work, qwen3 still wins.

**Important caveat:** 1.7B is good for chat/reasoning but limited for complex tasks. The 8B model (1.15 GB) is the sweet spot for capability while still being edge-deployable.

## RECOMMENDATION

**🟡 WORTHWHILE — FORGE with priority**

Immediate next steps:
1. Try the WebGPU demo and test real-world capability
2. Check if WebGPU compute delegation works (can browsers collectively offer compute to the network?)
3. Explore wrapping Bonsai as the "easy join" client for Solomon Air
4. License is Apache 2.0 — clean to use commercially

If WebGPU delegation works for distributed compute, this becomes the backbone of the entire Airlines Plan compute layer.

---

*Filed by: Zo*
*Source X post: https://x.com/i/status/2044283011416375481*
*Related: airlines-plan-2026-04-15.md*