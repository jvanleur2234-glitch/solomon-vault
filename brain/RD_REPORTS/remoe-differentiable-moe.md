# RD Report: thu-ml/ReMoE — Fully Differentiable MoE with ReLU Routing

**Repo:** `thu-ml/remoe`
**License:** Apache 2.0
**Forked:** Yes
**Date:** 2026-04-23
**Category:** Recurrent Transformer MoE

## What It Is

ReMoE (Relu Mixture-of-Experts) is a fully differentiable MoE architecture built on NVIDIA Megatron-LM. Instead of TopK softmax routing, it uses ReLU activation for continuous, differentiable expert allocation. Adaptive L1 regularization controls sparsity.

## Key Capabilities

- **Fully differentiable routing** — ReLU enables continuous gradients vs. discrete TopK
- **Dynamic expert allocation** — tokens get different numbers of experts based on importance (via ReLU activation)
- **Plug-and-play** — swap TopK+Softmax for ReLU routing with minimal Megatron changes
- **Consistently outperforms TopK MoE** across model sizes and expert counts
- **Adaptive sparsity** — L1 regularization controls expert utilization

## Solomon OS Fit

**SKILL** — MoE architecture research. If Hermes ever needs to route tasks across multiple expert models (e.g., coding vs. creative vs. analysis), ReMoE's differentiable routing is worth studying. Apache 2.0 allows code reference.

## Comparison to OpenMythos

- **OpenMythos** — Looped transformer with MoE inside recurrent blocks, Claude Mythos architecture clone
- **ReMoE** — Differentiable MoE routing for better expert utilization, NVIDIA Megatron-based
- Both relevant to MoE+recurrent research; OpenMythos is more directly relevant to agent architecture

## Recommendation

**SKILL** — Architecture reference only. Apache 2.0 licensed. Monitor if Hermes ever implements MoE-based task routing.