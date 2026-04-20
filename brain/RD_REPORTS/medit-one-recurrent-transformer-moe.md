# RD Report: medit-one — Recurrent Transformer + MoE

**Repo**: `MedITSolutionsKurman/medit-one`  
**Fork**: `jvanleur2234-glitch/medit-one-new`  
**Date**: 2026-04-19  
**License**: Not clearly specified (check before use)  
**Relevance**: RECURRENT TRANSFORMER MoE / OPENMYTHOS COMPETITOR  

## What It Is
High-speed transformer architecture combining **recurrent-style state management** (token-by-token prediction with evolving hidden state) with **Mixture-of-Experts (MoE)** for dynamic expert activation. Targets faster per-token inference with constant memory footprint and unbounded context.

## Key Features
- **Recurrent hidden state** (hx, cx) evolving per token — like RNN but attention-based
- **Constant memory** — unbounded context length in practice
- **MoE integration** — dynamic expert activation for parallel processing
- **CUDA-accelerated**: fused RoPE + attention kernels, mixed FP16/BF16
- Hidden-state self-attention on internal representations vs full token sequences
- Single-token prediction focus

## What We'd Use It For
**OpenMythos architecture research.** MedIT One combines the two key ideas from the OpenMythos competitor search — recurrent state + MoE — into a coherent architecture. Relevant if Solomon OS ever needs custom model design or inference optimization.

## Comparison to OpenMythos (swarms_corp)
- **OpenMythos**: Recurrent domain-specific attention + MoE for long context
- **medit-one**: Similar recurrent state concept but focused on inference speed + constant memory
- Both address the context window limitation differently

## Recommendation: **RESEARCH**
- License unclear — needs confirmation before use
- Forked for architecture reference
- Key insight: recurrent hidden state + MoE is a winning combo for unbounded context + efficient inference

## Links
- Fork: https://github.com/jvanleur2234-glitch/medit-one-new
