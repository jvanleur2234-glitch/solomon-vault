# Aragora — Auditable Multi-Model Deliberation Control Plane

**Date:** 2026-04-20  
**Fork:** https://github.com/jvanleur2234-glitch/aragora  
**Stars:** ~300+ (growing)  
**License:** Apache 2.0  
**Language:** Python  

## What It Does

Aragora is an auditable multi-model decision and execution control plane that orchestrates heterogeneous models through structured debate and review. Key features:

- **Multi-agent deliberation with receipts**: Every decision includes confidence scores, next steps, and full provenance
- **Optional sandboxed execution**: Actions can be run in isolated environments
- **Default-deny governance**: Consequential actions require explicit approval unless pre-approved
- **Truthful gates**: Verifiable, inspectable outcomes with full audit trails

## For Solomon OS

Aragora's governance model (default-deny, receipt-based decisions) maps directly to Hermes's security layer. The structured debate approach provides a template for the "Council of High Intelligence" deliberation system. Receipt/provenance tracking is essential for any AI agent OS handling financial or sensitive operations.

## Comparison to Quorum

Quorum: 7-phase deliberation with voting + minority report. Aragora: receipt-based governance with explicit approval gates. Both are complementary — Aragora for compliance-heavy decisions, Quorum for creative/synthesis tasks.

## Status

✅ Forked to jvanleur2234-glitch  
📋 RD Report: This file  
🏷️ Category: Multi-Agent Deliberation  
💡 Recommendation: INTEGRATE — governance model for Hermes security layer
