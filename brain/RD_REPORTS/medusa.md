# RD Report: medusa

**Fork Status:** Already cloned  
**License:** AGPL-3.0 (NOT MIT/Apache — flag for analysis)  
**Stars:** ~2K (AI-first security scanner, 9,600+ detection patterns)  
**Relevance:** HIGH — AI security, supply chain threats, CVE detection

## What It Is
AI-first security scanner designed for AI/ML apps, agents, and LLM-based systems. Ships with 9,600+ detection patterns and 200 CVE detections.

## Key Capabilities
- Repo-poisoning detection across 28+ file types
- Zero-setup: pip install, no extra tooling
- Fast parallel multi-core scanning (10-40x faster)
- Rich CLI output: JSON, HTML, Markdown, SARIF
- IDE integration: VS Code, Claude Code, Cursor, Gemini CLI
- Cross-platform: Windows, macOS, Linux

## Relevance to Hermes/Solomon
- AI-specific vulnerability detection aligns with Solomon OS security needs
- 200 CVE detections for supply chain threat monitoring
- Could integrate as pre-deployment security check

## Integration Recommendation
**SKILL** — Security scanning patterns valuable but AGPL license limits integration options. Consider similar implementation under MIT for Solomon OS security tooling.

## Notes
- AGPL-3.0 licensed (requires careful handling)
- 9,600+ detection patterns
- Active project with ongoing releases