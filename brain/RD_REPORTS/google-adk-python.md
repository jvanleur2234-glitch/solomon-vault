# RD Report: google/adk-python

**Slug:** google-adk-python  
**URL:** https://github.com/google/adk-python  
**Stars:** 19,044 ⭐ | **Forks:** 3,239  
**License:** Apache 2.0  
**Language:** Python

---

## What It Is
Google's open-source, code-first Python AI agent toolkit. Built for building, evaluating, and deploying sophisticated AI agents with flexibility and control. Full development/deployment pipeline built-in. From the description: "An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control."

The Chinese post described it as: "内置完整构建、评估、部署流水线，让复杂代理从原型秒变生产级" (built-in complete build/evaluate/deploy pipeline, making complex agents go from prototype to production instantly).

---

## What We'd Use It For
- **Production agent deployment** — standardized way to deploy agents to production
- **Evaluation pipelines** — built-in testing/evaluation of agent quality
- **Hermes hardening** — use ADK patterns to make Hermes more robust
- **Client delivery** — package AI workers for the staffing agency with proper deployment tooling

---

## Comparison to What We Have
- Solomon OS has Hermes (skill registry) + Solomon Bus (messaging) + Russell Tuna (Telegram bot)
- ADK brings: evaluation pipelines, deployment primitives, Google's operational patterns
- Apache 2.0 license — can build commercial products on it

---

## Recommendation: SKILL (Integrate)
**Reason:** Google's official agent toolkit, 19K stars, production-grade with built-in eval/deploy. Good complement to OpenAI Agents Python — could use both depending on which model provider is best for a given task.

**Action:** Clone and study the codebase. Extract evaluation/deployment patterns for Hermes. Consider ADK as the deployment layer for the AI Staffing Agency (deploy agents to client environments).
