# R&D Report: Android Reverse Engineering Skill

**Date:** April 18, 2026
**Repo:** github.com/SimoneAvogadro/android-reverse-engineering-skill (3.1K stars, Apache 2.0)
**Forked:** github.com/jvanleur2234-glitch/android-reverse-engineering-skill

## What It Does
Claude Code skill that decompiles Android APK/XAPK/JAR/AAR files and extracts HTTP APIs — Retrofit endpoints, OkHttp calls, hardcoded URLs, authentication patterns.

**Toolchain:** jadx (Java decompiler) + Vineflower (JetBrains decompiler) + dex2jar

**Workflow:**
1. Decompile APK → human-readable Java
2. Trace call flows from Activities/Fragments → ViewModels → Repositories → HTTP calls
3. Extract: Retrofit endpoints, OkHttp interceptors, auth headers, hardcoded URLs, token storage
4. Analyze: manifest, package structure, architecture patterns, obfuscation handling

## For Be Like You! OS

### YES — Here's How We'd Use It:

**1. Study Existing VoIP/Signal Apps**
Decompile Signal, WhatsApp, Telegram Android → understand how they handle:
- WebRTC audio/video calls
- Push notifications (FCM alternatives)
- E2E encryption key exchange
- SIP registration flows
This informs our vphone-cli + Linphone integration.

**2. Extract Carrier APIs**
Decompile Samsung/Sony/Google Android dialer apps → understand:
- Visual Voicemail implementation
- WiFi Calling integration
- Carrier provisioning (LTE/5G IMS)
- Emergency call routing
Build our own versions without carrier deals.

**3. Build Compatible Alternatives**
Extract the API patterns from Instagram, TikTok, etc. → build open-source federated alternatives that are API-compatible.

**4. Security Research**
Study how malware apps work → build better Guardian protection in Solomon OS.

## Installed Toolchain
- jadx v1.5.1 ✅ installed at /opt/jadx
- Java JDK 17 ✅
- Vineflower (optional, not yet installed)

## Legal Note
Only for authorized security research, interoperability analysis (EU Directive 2009/24/EC, US DMCA §1201(f)), malware analysis, educational use. Don't clone proprietary apps — use for learning + building compatible alternatives.

## Priority for JCPaid
★★★☆☆ — Useful but not urgent. Good for Phase 2 of Be Like You! OS when we're reverse-engineering existing apps.
