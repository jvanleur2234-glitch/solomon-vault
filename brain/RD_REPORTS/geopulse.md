# RD Report: GeoPulse

**Repo:** https://github.com/tess1o/geopulse  
**Stars:** 797 | **Forks:** 34 | **Language:** Python + TypeScript  
**License:** BSL 1.1 (Business Source License)  
**Cloned:** /home/workspace/geopulse

## What It Is
Open-source, privacy-first Google Timeline alternative. Transforms raw GPS data from OwnTracks, Overland, Dawarich, GPSLogger, Home Assistant, Traccar into a searchable timeline of stays, trips, and movement patterns.

## Key Capabilities
- **Multi-source ingestion:** OwnTracks (HTTP/MQTT), Overland, GPSLogger, Home Assistant, Traccar, Dawarich, Colota
- **Timeline visualization:** Automatic trip/stay detection, journey insights, milestones/badges
- **Immich integration:** Photos from your library appear on map timeline
- **Bulk import:** Google Timeline, GPX, GeoJSON, CSV
- **Friends system:** Per-user visibility, live location sharing, guest links with optional passwords
- **OIDC/SSO support** alongside standard auth
- **AI assistant:** Natural-language queries for location data (bring your own OpenAI key)
- **Deployment:** Docker Compose or Kubernetes/Helm, ~100MB RAM, <1% CPU

## What Solomon OS Gets
- Location tracking infrastructure — useful if we're building something involving user location
- Docker Compose architecture we can reference for our own services
- Multi-user auth patterns (OIDC/SSO) applicable across the stack

## Verdict
**SKIP** — BSL license limits commercial use, not AGPL/mit. Joseph runs a business — adding dependencies with non-commercial restrictions could create legal exposure. GeoPulse is also heavy on GPS/location data which isn't core to Solomon OS's AI agent focus. The tech patterns (Docker Compose, multi-user auth) are already well-understood.