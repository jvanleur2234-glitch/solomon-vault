# R&D Report: DeepGEMM

**Date:** April 19, 2026

## Summary
- **Repo:** github.com/deepseek-ai/DeepGEMM — 6.7K stars, MIT
- **What it is:** High-performance FP8/FP4 GEMM kernels for NVIDIA H800/H100 GPUs. 1550 TFLOPS on H800. JIT compilation.
- **License:** MIT — fully open, can fork and modify

## Strategic Fit for JCPaid
NOT directly applicable today — requires NVIDIA SM90/SM100 GPU (H800, H100), CUDA 12.3+, C++20 compilers, PyTorch 2.1+, CUTLASS 4.0.

## When It Becomes Relevant
When JCPaid scales to: self-hosted model serving at GPU cluster scale, or custom kernel optimization.

## What to Do Now
- FORKED: jvanleur2234-glitch/DeepGEMM
- Monitor for updates
- Study JIT compilation approach for offline optimization

## Key Insight
DeepSeek proving MIT-licensed inference kernels can compete with NVIDIA libraries. Validates JCPaid open-source-first philosophy.

## Status
🟡 WATCH — not actionable without H100/H800 hardware