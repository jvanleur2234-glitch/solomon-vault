# RD Report: paperless-ngx

**URL:** https://github.com/paperless-ngx/paperless-ngx
**Date:** 2026-04-18
**Queue Source:** Telegram DM from Joseph

---

## What It Is

Paperless-ngx is an open-source document management system (DMS) that lets you scan, index, and archive physical documents into a searchable online archive. It's the official successor to the original Paperless and Paperless-ng projects, now community-maintained.

**Stack:** Python/Django backend + Angular TypeScript frontend. Docker-based deployment. PostgreSQL backend. Uses Tesseract OCR under the hood.

**License:** GPL-3.0
**Activity:** 38.2k stars, 2.4k forks, 147 releases, 11,334 commits on dev branch.

---

## Key Features

- **Document scanning & ingestion** via upload or consumed folder (watch folder)
- **OCR** via Tesseract — extracts text from scanned PDFs/images
- **Full-text search** across all documents
- **Tagging,Correspondents, Document Types** for organization
- **Automated document matching** (rules to tag/name based on content)
- **Email import** (consume emails as documents)
- **PDF/A conversion** for long-term archival
- **Built-in sharing** via link
- **REST API** for integrations

---

## What We'd Use It For

**Internal ops / back-office:** Solomon OS deals with a LOT of documents — contracts, invoices, client files, business docs. Paperless-ngx would be a solid document ingestion pipeline. Could ingest PDFs via API, auto-tag using rules, search across all business documents instantly.

**Client-facing service:** Could offer "AI document management" as part of the staffing agency's service tier. Set up Paperless-ngx for clients to manage their own documents, with AI layer on top.

**Faith Family Farms / WifeApp:** Both involve document intake. Could use as a unified document repository for intake forms, contracts, media releases, etc.

**OCR pipeline:** Tesseract-based OCR could be chained into other pipelines (e.g., ingesting scanned docs into the AI knowledge base).

---

## Comparison to What We Have

We don't have a DMS. We have file storage and various scripts, but nothing purpose-built for document ingestion, OCR, and full-text search.

Paperless-ngx fills that gap cleanly. Docker one-liner install. Well-maintained.

---

## Recommendation

**🟡 WORTHWHILE — Add to Infrastructure Stack**

Score: 7/10

**Pros:**
- Solves a real operational pain (document chaos)
- Docker one-liner deploy, low maintenance
- Active community, well-documented
- Strong OCR pipeline already built
- REST API for automation

**Cons:**
- Self-hosted only (no cloud SaaS option from them)
- Needs careful backup strategy
- Security note: "should never be run on untrusted host" — store sensitive biz docs on a local server

**Action:** Deploy on the Zo server via Docker for internal use. Could also offer as a bundled service for staffing clients. Good building block for "AI back-office" positioning.

**Integration path:** Hook into Solomon Bus via file watcher + REST API → auto-tag documents as they come in, push summaries to the knowledge base.

**Priority:** Medium. Not urgent, but solid infrastructure addition.

---

*Synced to GitHub: /home/workspace/solomon-vault/brain/RD_REPORTS/paperless-ngx.md*