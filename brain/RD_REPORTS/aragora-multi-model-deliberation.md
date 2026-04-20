# Aragora — Multi-Model Deliberation Control Plane

## Summary
Auditable, multi-model decision and execution control plane for AI-assisted work. Coordinates diverse models through structured debate and review, preserves receipts and provenance, enforces truthful bounded execution.

## Key Features
- Multi-agent deliberation with receipts, provenance, and review gates
- Sandboxed effectors with default-deny unless admin-approved artifacts exist
- Not a generic autonomous-agent runtime — governance layer for reliability, traceability, inspectability
- pip install aragora-debate, API access via aragora-sdk, Docker Compose self-host

## Relevance to Solomon OS
- Directly competes with **Quorum** (already in our vault) — Aragora brings audit receipts + review gates
- Could be the governance backbone for Hermes multi-agent deliberation workflows
- Provides verifiable, bounded AI execution — aligns with Solomon OS security requirements

## License & Fork Status
- MIT licensed ✓
- Forked to: jvanleur2234-glitch/aragora

## Recommendation
**SKILL** — Integrate into Hermes deliberation layer for audit trails + review gates on agent decisions.
