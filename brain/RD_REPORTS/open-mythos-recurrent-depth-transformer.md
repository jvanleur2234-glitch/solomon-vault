# RD Report: OpenMythos — Recurrent-Depth Transformer (RDT)

**Date:** 2026-04-25  
**Category:** Architecture Study  
**Status:** SKILL  

## What It Is

OpenMythos is an open-source reconstruction of Claude Mythos as a Recurrent-Depth Transformer (RDT), also called a Looped Transformer (LT). Instead of stacking hundreds of unique transformer layers, a subset is reused across multiple loop iterations per forward pass — same weights, deeper effective computation.

## Key Architecture

- **Prelude (P):** Standard transformer layers, run once at input
- **Recurrent Block (R):** Looped T times with hidden state `h_{t+1} = A·h_t + B·e + Transformer(h_t, e)`. Input embedding `e` injected at every loop to prevent drift.
- **Coda (C):** Standard transformer layers, run once at output
- **MoE variant:** Supports sparse Mixture-of-Experts with configurable `n_experts`, `n_shared_experts`, `n_experts_per_tok`
- **Attention variants:** MLA (multi-head local attention) or GQA (global question attention)

## Key Claims

1. **Depth extrapolation:** More inference-time loops → deeper reasoning without larger model
2. **Latent thoughts:** Each loop acts as implicit CoT step in continuous latent space
3. **Systematic generalization:** Looped transformers generalize to OOD compositions better than vanilla
4. **No parameter explosion:** Same parameter count; increased depth via loops

## Why It Matters for Solomon OS

- **Recurrent agent memory:** Loop-based hidden state update maps directly to Hermes persistent context over long conversations
- **Adaptive computation:** Token-level routing for depth (like MoR paper) enables efficient agent processing
- **Competitive intelligence:** OpenMythos is the closest open implementation of Claude Mythos architecture — critical for understanding where Hermes should evolve

## Source

- https://github.com/kyegomez/OpenMythos
- License: MIT
- Author: Kye Gomez (@kyegomez, swarms-corp)