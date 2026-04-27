# RD Report: AI Agent Scanner — Shadow AI Discovery + Security Assessment

## Summary
Perfecxion AI's ai-agent-scanner discovers "shadow AI" running in environments, tests for vulnerabilities, maps to compliance frameworks (GDPR, SOC 2, HIPAA, NIST, EU AI Act). 4 discovery surfaces: Network, Code (SDK usage), Traffic (API calls in logs), Cloud (SageMaker, Bedrock, Azure, Vertex). SARIF output. GPL-3.0, v1.1.0.

## What It Does
- **Discovery**: Finds AI agents across 4 surfaces (Network, Code, Traffic, Cloud)
- **Security Testing**: Probes discovered agents for vulnerabilities
- **Risk Scoring**: Per-agent score to prioritize remediation
- **Compliance Mapping**: GDPR, SOC 2, HIPAA, NIST AI RMF, EU AI Act
- **SARIF Output**: CI/CD integration
- **Cloud Scanning**: Optional dependencies for AWS/Azure/GCP AI services

## Tech Stack
- Language: Python
- License: GPL-3.0
- Latest: v1.1.0 (2026-03-31)

## Strategic Fit for Solomon OS

**WATCH** — Shadow AI discovery is unique. First open-source tool that discovers unknown agents.

Key learnings:
1. **Shadow AI Discovery**: Find agents you didn't know existed = critical for enterprise security
2. **4 Discovery Surfaces**: Network, Code, Traffic, Cloud = comprehensive coverage
3. **Compliance Mapping**: GDPR/SOC2/HIPAA = enterprise sales enablement
4. **Risk Scoring**: Prioritization framework for remediation

## Risk/Concerns
- GPL-3.0 (copyleft) — cannot bundle in proprietary products
- Cloud scanning requires optional dependencies
- 3 contributors, smaller community

## Verdict
WATCH — Shadow AI discovery concept is valuable for enterprise audit. Compliance mapping directly enables JCPaid enterprise sales. License prevents integration into proprietary products.

## Links
- Repo: https://github.com/perfecxion-ai/ai-agent-scanner
- Fork: Not yet forked