# AI Agent Scanner — Discovery-First Security Assessment (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/ai-agent-scanner` (GPL v3)
**Source:** https://github.com/perfecxion-ai/ai-agent-scanner

## What It Does
Discovers and security-tests AI agents across:
- **Network surfaces:** endpoints scanning
- **Code:** SDKs, keys, configs
- **Traffic:** AI API calls in logs/HAR files
- **Cloud:** SageMaker, Bedrock, Azure OpenAI, Vertex AI

Generates risk scores + maps to GDPR, SOC 2, HIPAA, NIST AI RMF, EU AI Act compliance.

## Why It Matters for Solomon OS
- Discovery-first approach finds "shadow AI" before it causes problems
- Compliance mapping directly supports JCPaid enterprise security requirements
- SARIF output integrates with GitHub Code Scanning
- Local Ollama testing capability

## Fit: INTEGRATE
GPL v3 (copyleft — can't use code directly but concepts transferable). Discovery framework patterns inform Hermes security auditing.

## Action Items
- [ ] Extract compliance mapping schema for JCPaid security reports
- [ ] Study discovery patterns for Hermes skill audit trail
- [ ] Note: GPL limits direct code reuse; use as architecture reference only
