# MedIT One — Recurrent Transformer MoE Architecture

**URL:** https://github.com/jvanleur2234-glitch/medit-one
**Forked from:** https://github.com/MedITSolutionsKurman/medit-one
**License:** MIT | **Language:** Python/CUDA

## What It Does
Innovative transformer architecture combining recurrent-style state management with MoE (Mixture of Experts) for efficient inference on long/unbounded contexts. Single-token prediction with constant memory footprint.

## Key Innovations
- **Single-Token Prediction**: Processes one token at a time, constant memory regardless of context length
- **Hidden-State Self-Attention**: Attention on hidden representations (not tokens) — linear scaling vs quadratic
- **Recurrent-Style State Management**: Forward-evolving state vectors (hx, cx) like LSTM/GRU, continuous refinement
- **MoE Integration**: Dynamic expert selection with parallel processing, CUDA-accelerated
- **CUDA Kernels**: Custom fused RoPE+attention, flash attention variants, FP16/BF16 mixed precision
- Checkpoints: 140M (9B tokens), 98M (6B tokens) available on HuggingFace

## Relevance to OpenMythos Competitors
- Recurrent transformer + MoE is the exact architecture category for OpenMythos competitors
- Linear attention scaling is key for long-context agentic workloads
- CUDA optimization patterns useful for Solomon Air GPU optimization

## Solomon OS Fit
**SKILL** — Architecture study only. The recurrent state + MoE combination is relevant for Solomon Air inference optimization. MIT license permits studying the architecture.

## Recommendation
SKILL — Study MedIT One's recurrent state management + linear attention for potential Solomon Air inference optimization.