# RD Report: MedIT One — Recurrent Transformer with MoE

**Date:** 2026-04-22  
**Category:** Architecture / MoE  
**Source:** web_research (github)  
**Fork Status:** Already forked (medit-one, medit-one-new)

## What It Is
Fast, memory-efficient transformer variant combining recurrent-style state management with Mixture of Experts (MoE) component and single-token inference.

## Key Capabilities
- **Recurrent-style state management** — maintains evolving state vectors (hx, cx)
- **MoE integration** — dynamic expert selection with parallel processing
- **Single-token inference** — token-by-token processing with constant memory
- **Hidden-state self-attention** — linear scaling instead of quadratic
- **CUDA-accelerated** — FP16/BF16, Flash Attention variants, fused RoPE-attention

## Why It Matters
- Addresses the "recurrent transformer MoE" gap in our research
- Constant memory footprint regardless of context length
- Good for long-context agentic workflows in Hermes

## Recommendation
**ALREADY FORKED** — No action needed. Already tracked as `medit-one` and `medit-one-new`.

---

## Stats
- License: MIT
- Language: Python, C++
- Status: Active