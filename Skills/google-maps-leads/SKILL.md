---
name: google-maps-leads
description: Scrape Google Maps for business leads — names, emails, phone numbers, reviews, ratings, websites, coordinates. CLI, Web UI, REST API, or AI agent command.
trigger: scrape Google Maps, find leads from maps, business leads, local business data, map scraping, extract business info, lead generation
compatibility: CashClaw integration, Solomon OS
metadata:
  author: josephv.zo.computer
  source: https://github.com/gosom/google-maps-scraper
  license: MIT
allowed-tools: Bash, Read, Write, Edit
---

# Google Maps Lead Scraper Skill

## Quick Start

### Command Line
```bash
cd /home/workspace/solomon-maps-leads
go build -o gmaps-cli cmd/gmaps-cli/main.go
./gmaps-cli --search "restaurants in Chicago" --output leads.csv
```

### Web UI
```bash
cd /home/workspace/solomon-maps-leads
go run cmd/webui/main.go
# Opens at http://localhost:8080
```

### REST API
```bash
go run cmd/api/main.go
# API at http://localhost:8081
```

### AI Agent Command
Use the AI agent skill in any coding agent:
```bash
# Ask your agent: "Run a Google Maps scrape for [query], output to CSV"
python /home/workspace/solomon-maps-leads/gmaps_agent.py "restaurants in Chicago" --format csv --output leads.csv
```

## Output Fields
- Business name
- Address
- Phone number
- Website
- Email (extracted from website)
- Reviews count
- Rating
- Coordinates (lat/lng)
- Category
- Opening hours
- Google Maps URL

## Use Cases for Solomon OS
1. **Lead generation for real estate agents** — scrape "real estate agents in [city]"
2. **SEO audits** — find businesses without websites for website building sales
3. **Cold email campaigns** — extract business emails from their websites
4. **Competitor analysis** — map all competitors in a neighborhood

## Pricing Integration
For paid scraping at scale (millions of listings):
- SerpApi: https://serpapi.com/google-maps-api
- Scrap.io: https://scrap.io (country-scale)
- SearchApi: https://www.searchapi.io/google-maps

## Files
- `/home/workspace/solomon-maps-leads/` — full Go source code
- `/home/workspace/solomon-maps-leads/README.md` — full documentation