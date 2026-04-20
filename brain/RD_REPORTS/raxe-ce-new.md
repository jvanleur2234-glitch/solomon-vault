# RD Report: raxe-ai/raxe-ce

## Summary
Runtime security for AI agents. Local, real-time defense layer monitoring prompts, reasoning, tool usage, and memory. 515+ L1 detection rules plus ML-based L2 detection (5-head ensemble). 94.7% true positive rate.

## Relevance to Solomon OS
- **Runtime defense**: Real-time protection for Hermes during execution
- **Local processing**: 100% on-device, no cloud dependency — matches Solomon OS privacy-first approach
- **Sub-5ms rule matching**: Fast enough for production use

## Key Features
- 515+ L1 rule-based detection rules
- ML-based L2 detection (5-head ensemble) for novel attacks
- 100% local processing
- Sub-5ms L1 rule matching, ~45ms combined latency
- 94.7% TP rate, ~3.8% false positives
- Covers prompts, reasoning, tool calls, and memory

## License
Not stated — verify

## Use for Solomon OS
INTEGRATE — Runtime security guard for Hermes execution layer

## Fork Status
Forked to: jvanleur2234-glitch/raxe-ce-new
