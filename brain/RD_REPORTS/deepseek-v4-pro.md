# RD Report — DeepSeek-V4-Pro

**Date:** 2026-04-25  
**Source:** https://x.com/ErickSky/status/2047805724500070583  
**Also:** NVIDIA Developer Blog, build.nvidia.com, HuggingFace  

---

## What It Is

DeepSeek-V4-Pro is the new flagship model from DeepSeek AI, just released tonight. It's the **largest open-source model in the world** with **1.6 trillion parameters** and a **1 million token context window**. NVIDIA is hosting it for free on their build.nvidia.com platform using Blackwell GPUs.

There's also a smaller sibling: **DeepSeek-V4-Flash** — 284B parameters, 13B active, faster for chat/routing use cases.

Both models support up to 384K max output tokens and are MIT licensed.

---

## Architecture — Hybrid Attention

The key innovation is **Hybrid Attention** inside each transformer block, combining:

- **CSA (Compressed Sparse Attention):** Dynamic sequence compression that compresses KV entries, then applies sparse attention to reduce computation.
- **HCA (Heavily Compressed Attention):** Aggressive consolidation — multiple tokens share a single compressed KV entry.

Combined result: **73% reduction in per-token inference FLOPs** and **90% reduction in KV cache memory** vs DeepSeek-V3.2.

This is purpose-built for agentic workflows — agents carry system instructions, tool outputs, retrieved context, code, logs, reasoning traces. Long context is a core requirement, and standard attention becomes a bottleneck at this scale.

---

## Performance on NVIDIA Blackwell

Out of the box on GB200 NVL72 (Blackwell Ultra):
- **>150 tokens/sec/user** interactivity for agentic workflows
- Running at ISO-interactivity (95 tok/s/user): **1300 tok/s/gpu** (up 3.25x in 4 months per SemiAnalysis)

Expect this to improve further with Dynamo, NVFP4, optimized CUDA kernels, and advanced parallelization.

---

## How to Access

1. **Free hosted endpoint:** https://build.nvidia.com/deepseek-ai/deepseek-v4-pro (NVIDIA Developer Program, free tier available)
2. **Self-hosted:** NIM microservices, HuggingFace (deepseek-ai/DeepSeek-V4-Pro), or via SGLang/vLLM recipes on Blackwell/Hopper

Tools for agentic workflows:
- NVIDIA NeMoClaw — personal assistant, code gen, autonomous support
- NVIDIA AI-Q Blueprint — deep research assistant based on LangChain
- NVIDIA Data Explorer Agent — data analysis agent (1st place DABstep benchmark)

---

## Competitive Context

- Directly competes with GPT-4.5 and Claude 3.7 in terms of context window and model scale
- The 1.6T params vs GPT-4's estimated 1T puts it at top of open-source landscape
- MIT license = fully open, commercial use allowed, no restrictions
- Free access via NVIDIA's hosted endpoint is a major democratizer — this is the equivalent of giving away Ferrari test drives

---

## Key Specs

| Spec | DeepSeek-V4-Pro | DeepSeek-V4-Flash |
|---|---|---|
| Total params | 1.6T | 284B |
| Active params | 49B | 13B |
| Context | 1M tokens | 1M tokens |
| Max output | 384K | 384K |
| License | MIT | MIT |

---

## Strategic Observations

1. **Long context is the next battlefield** — V4's hybrid attention architecture signals a shift from basic chat toward multi-turn, memory-heavy agentic systems. This requires rethinking the entire inference stack (software, memory, compute, networking).

2. **Open-source frontier models just leapfrogged closed ones** — 1.6T params, 1M context, MIT license, free to run. The gap between open and closed is closing fast.

3. **NVIDIA is positioning Blackwell as the default infrastructure for this era** — they're not just hosting models, they're curating the access layer with day-0 support for the hottest releases.

---

## Recommendation

**🔴 FORGE** — This is a major release. 1.6T params + 1M context + free Blackwell access + MIT license is a significant competitive development in the AI landscape.

Immediate actions:
- Test the hosted endpoint at build.nvidia.com
- Evaluate how it compares to current pipeline models for long-context tasks
- Monitor adoption trajectory and community benchmarks
- Consider integration into AI-Q workflows for Solomon OS

---

*Sources: NVIDIA Developer Blog (2026-04-24), @ErickSky/X, @NVIDIAAI/X, build.nvidia.com, HuggingFace*