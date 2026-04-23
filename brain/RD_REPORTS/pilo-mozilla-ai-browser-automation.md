# RD Report: pilo — Mozilla Tabstack AI Browser

**Date:** 2026-04-23  
**URL:** https://github.com/mozilla/pilo  
**License:** Apache 2.0  

## What It Does
Mozilla Tabstack project's AI-powered web automation tool. Control browsers with natural language. Fill forms, navigate, extract data. CLI + programmatic JS/Playwright integration. Guardrails for safe automation (browse-only mode).

## Key Features
- Natural language task execution in browser
- CLI: `pilo run "find news about AI agents"`
- Playwright integration for programmatic use
- Multiple AI provider support (OpenAI, OpenRouter)
- Safety/guardrails (e.g., "browse only, don't book")

## Architecture
- WebAgent class + PlaywrightBrowser driver
- Natural language → structured browser actions
- v0.18.0 (March 2026), active development

## Solomon OS Fit
**SKILL** — Browser automation patterns for Solomon Browser. Apache 2.0 permits study. Natural language → browser action mapping useful for ClawLess competitor analysis.

## Status
**SKILL** — Architecture reference for browser automation. Guardrail pattern worth studying.
