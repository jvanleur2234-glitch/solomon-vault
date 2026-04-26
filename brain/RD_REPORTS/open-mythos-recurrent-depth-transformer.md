# RD Report: OpenMythos — Recurrent-Depth Transformer + MoE

**Date:** April 26, 2026  
**Author:** AIQ Scout  
**Status:** SKILL  
**License:** MIT  
**Stars:** Active (key project from Kye Gomez)  

## What It Is
Open-source reconstruction of Claude Mythos as a Recurrent-Depth Transformer (RDT). Fixed layers looped T times per forward pass. Input injection prevents signal drift. Sparse MoE with routed + shared experts.

## Key Features
- 3-block architecture: Prelude (standard) → Recurrent Block (looped T times) → Coda (standard)
- Recurrent update: h_{t+1} = A·h_t + B·e + Transformer(h_t, e)
- Input injection at every loop prevents drift
- Switchable attention: MLA or GQA
- Sparse MoE with routed + shared experts
- Systematic generalization, depth extrapolation, latent thoughts
- Author: Kye Gomez (OpenClaw creator, key ecosystem player)

## Solomon OS Fit
SKILL — Study looped transformer + MoE architecture for Hermes reasoning engine enhancement. Kye Gomez = key ecosystem player (@swarms_corp, OpenClaw, OpenMythos). Potential competitor to Council of High Intelligence.

## Action
- Already in workspace as OpenMythos
- Already forked: jvanleur2234-glitch/OpenMythos
- Monitor Kye Gomez for new releases

## Links
- https://github.com/kyegomez/OpenMythos