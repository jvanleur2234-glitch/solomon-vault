# RD_REPORT: gethomepage/homepage

**Date:** 2026-04-17
**URL:** https://github.com/gethomepage/homepage
**Stars:** ~29,578
**License:** MIT
**Tags:** docker, homepage, nextjs, node, react, self-hosted, startpage

---

## What It Is
A fully static, fast, secure application dashboard / startpage for homelabs. Configure via YAML or Docker labels. 100+ service integrations (arr apps, Plex, Jellyfin, Traefik, Plex, etc.). Built with Next.js/React. Ships as a Docker container.

Key features:
- Static generation (instant load)
- All API calls proxied (API keys stay hidden)
- Docker auto-discovery via labels
- 100+ service widgets (Radarr, Sonarr, Plex, qBittorrent, etc.)
- Information widgets: weather, time, search, Glances
- 40+ languages
- Custom themes, layouts, CSS/JS
- Fully proxied backend requests

Security note: No auth layer. Must sit behind a reverse proxy with auth if exposed to untrusted networks.

---

## What We'd Use It For

Joseph already has a Zo Space and multiple services running. Homepage would give him a slick unified dashboard for:
- Monitoring Solomon Bus, Hermes, Ollama, MoneyPrinterTurbo, RENU API, etc.
- Quick-access bookmarks to all his services
- A professional-looking homelab-style hub (very developer/ops aesthetic)

It's the kind of thing that looks impressive in demos and gives Solomon OS a "mission control" feel.

---

## How It Compares to What We Have

Solomon OS currently has:
- No unified service dashboard
- Services running but scattered (Ollama on 11434, MoneyPrinter on 8080, RENU API on 5010, etc.)

Homepage fills that gap nicely. Alternative would be building a custom React dashboard in Zo Space — but that takes time to build and maintain. Homepage is turnkey.

---

## Recommendation

🟡 **SKILL** — Worth installing as a Zo service. It's Docker-based, runs in 5 minutes, and would immediately give Solomon OS a professional ops dashboard. One docker-compose entry, exposed via Zo's reverse proxy.

Not urgent, but a high-visibility quality-of-life win for showing off the rig.

---

## Related X Posts (from Joseph's shared links)

- **gethomepage announcement** (29.5K stars) — trending on X this week
- **t.co/RS7viwAwgw** — Audi RS7 content (unresolved; likely unrelated, possibly a car enthusiast post Joseph wanted to reference for something)
