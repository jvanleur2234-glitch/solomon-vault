# R&D Report: DeepGEMM

**Date:** April 19, 2026

## Summary
- **Repo:** github.com/deepseek-ai/DeepGEMM — 6.7K stars, MIT
- **What it is:** High-performance FP8/FP4 GEMM kernels for NVIDIA H800/H100 GPUs. 1550 TFLOPS on H800. JIT compilation. DeepSeek's proprietary inference optimization library.
- **License:** MIT — fully open, can fork and modify

## Why It Matters
DeepSeek released this alongside their V3 model, proving that commodity CUDA kernels can match or exceed NVIDIA's own libraries. MIT license means we can study, fork, and integrate without restriction.

## Strategic Fit for JCPaid
❌ NOT directly applicable today — requires:
- NVIDIA SM90/SM100 GPU (H800, H100, B100)
- CUDA 12.3+ 
- C++20 compilers
- PyTorch 2.1+
- CUTLASS 4.0

## When It Becomes Relevant
When JCPaid scales to:
1. Self-hosted model serving (we host our own Ollama/llama.cpp at scale)
2. GPU cluster deployment (10+ H100s)
3. Model fine-tuning pipeline
4. Custom kernel optimization for specific workloads

## What to Do Now
- FORKED: jvanleur2234-glitch/DeepGEMM ✅
- Monitor DeepSeek's repo for updates
- When we add GPU compute, revisit this for inference optimization
- Study their JIT compilation approach for potential offline optimization techniques

## Key Insight
DeepSeek proving MIT-licensed inference kernels can compete with NVIDIA's proprietary libraries. Validates JCPaid's open-source-first philosophy. If DeepSeek can do it, we can build on top of it.

## Status
🟡 WATCH — not actionable without H100/H800 hardware