---
name: opencli-browser
description: Browser automation via OpenCLI. Navigate, click, type, extract, screenshot any website using OpenCLI browser commands. Requires OpenCLI daemon running and Chrome Browser Bridge extension. Use when you need to interact with websites that don't have pre-built adapters — click buttons, fill forms, scrape dynamic content, extract data from logged-in sessions.
compatibility: Created for Zo Computer
metadata:
  author: josephv.zo.computer
allowed-tools: Bash
---

# OpenCLI Browser Automation Skill

OpenCLI gives AI agents browser control via a Chrome extension bridge. The daemon must be running (`opencli doctor` to verify).

## Core Commands

```bash
opencli browser open <url>          # Open URL in automation browser
opencli browser state              # Get current page state (DOM snapshot)
opencli browser click <selector>   # Click element
opencli browser type <selector> <text>  # Type into input
opencli browser get <selector>     # Extract text from element
opencli browser find "<text>"      # Find element containing text
opencli browser screenshot          # Screenshot current page
opencli browser extract            # Extract structured data from page
opencli browser network            # Intercept network requests
opencli browser close              # Close automation browser
```

## For sites with built-in adapters (no browser needed):

```bash
opencli hackernews top -f json     # HackerNews top stories
opencli reddit hot -f json          # Reddit hot posts  
opencli bilibili hot -f json        # Bilibili trending
opencli twitter trending -f json   # X trending topics
opencli gemini ask "<question>"    # Gemini direct
```

## Installation Check

```bash
opencli doctor   # Verify daemon + extension status
opencli list      # See all available commands
```

## Output Formats

All commands support `-f table|json|yaml|md|csv`

## Skills Available

- `opencli-adapter-author` — Write new site adapters end-to-end
- `opencli-autofix` — Repair broken adapters
- `opencli-browser` — This skill (browser automation)
- `opencli-usage` — Command reference
- `smart-search` — Find existing capabilities

## Integration with Solomon OS

Solomon OS uses OpenCLI for:
1. Browser automation when no pre-built adapter exists
2. Lead list building (Google Maps, review sites)
3. Social media monitoring and posting
4. Web scraping from authenticated sessions

