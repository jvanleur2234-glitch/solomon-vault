---
name: clone-website
description: Reverse-engineer any website into a Next.js + shadcn/ui + Tailwind v4 codebase using multi-agent AI. Drops into CashClaw as `cashclaw clone <url>`.
trigger: clone website, reverse engineer website, copy website design, build from existing site
compatibility: CashClaw integration
metadata:
  author: josephv.zo.computer
  source: https://github.com/JCodesMore/ai-website-cloner-template (12.9k stars)
  license: MIT
allowed-tools: Bash, Read, Write, Edit
---

# Clone Website Skill

## Usage
Run: `cashclaw clone <url1> [<url2> ...]`

## What It Does
1. Playwright scrapes the target URL
2. Screenshots → vision model → describes layout
3. Multi-agent extracts: HTML structure, CSS, JS, images, fonts, icons
4. Each agent handles one concern (structure / style / assets / icons)
5. Output: clean Next.js 16 + shadcn/ui + Tailwind v4 project

## Tech Stack Used
- Next.js 16 (App Router, React 19, TypeScript strict)
- shadcn/ui (Radix primitives)
- Tailwind CSS v4 with oklch design tokens
- Lucide React + extracted SVG icons
- Vercel deployment

## Design Rules
- Pixel-perfect emulation — match spacing, colors, typography 1:1
- No personal aesthetic changes during emulation
- Real content from target — not placeholders
- Beauty-first — every pixel matters
- Mobile-first responsive

## Code Style
- TypeScript strict, no `any`
- Named exports, PascalCase components, camelCase utils
- Tailwind utilities only, no inline styles
- 2-space indentation

## Integration with CashClaw
```bash
cd /home/workspace/cashclaw
# Add clone command to src/cli/commands/clone.js
# Then: cashclaw clone <url> → runs the multi-agent pipeline
```

## Source Files
- `/home/workspace/solomon-cloner/.claude/skills/clone-website/SKILL.md`
- `/home/workspace/solomon-cloner/AGENTS.md`
- `/home/workspace/solomon-cloner/src/app/` (Next.js base template)