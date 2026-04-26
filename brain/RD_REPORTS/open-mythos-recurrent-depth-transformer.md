# OpenMythos — Recurrent-Depth Transformer (Looped Transformer) + MoE

## Quick Summary
Open-source reconstruction of Claude Mythos as a Recurrent-Depth Transformer (RDT). Reuses a fixed set of layers by looping them multiple times per forward pass with input injection. Combines with sparse MoE for compute-adaptive reasoning.

## What It Is
OpenMythos implements a looped transformer architecture where a subset of layers (Recurrent Block) recycle across multiple forward passes, maintaining a constant weight set while increasing effective depth through loops. Input embedding `e` is injected at every loop to prevent signal drift.

## Architecture
- **Prelude (P)**: Standard transformer layers, run once
- **Recurrent Block (R)**: Looped T times. Hidden state update: `h_{t+1} = A·h_t + B·e + Transformer(h_t, e)`
- **Coda (C)**: Standard transformer layers, run once after looping

## Key Capabilities
- **Looped depth**: Deeper reasoning without stacking more parameters
- **Input injection**: Prevents drift, preserves original signal across recurrence
- **MoE support**: Sparse mixture-of-experts with routed + shared experts
- **Attention options**: MLA (Multi-Head Local Attention) or GQA (Global-Query Attention)
- **Systematic generalization**: Better at novel compositions when trained with loops
- **Depth extrapolation**: More inference-time loops = longer reasoning chains (e.g., 5-hop training, 10-hop testing)
- **Latent thoughts**: Continuous latent iterations act like implicit chain-of-thought

## Relevance to Solomon OS
- **SKILL** — Study for potential Hermes reasoning engine enhancement
- The looped transformer approach could enable deeper reasoning without larger models
- OpenMythos + Hermes integration could give Solomon OS a state-of-the-art reasoning core
- Kye Gomez (OpenMythos author) is the same person behind OpenClaw — key ecosystem player

## License & Fork Status
- **License:** MIT
- **Stars:** ~500 (estimated, active project)
- **Forked:** Already forked to jvanleur2234-glitch/OpenMythos

## Verdict
**SKILL** — Architecture study for Hermes reasoning enhancement. The looped transformer + MoE combination is cutting-edge. Monitor Kye Gomez (author) for ecosystem integration opportunities. OpenMythos + OpenClaw + Hermes = potentially powerful stack.

## Links
- https://github.com/kyegomez/OpenMythos
- Fork: https://github.com/jvanleur2234-glitch/OpenMythos