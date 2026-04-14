# CTI Expert OSINT Audit - jvanleur2234@yahoo.com & jvanleur

Date: 2026-04-07
Subject: Security audit for Joseph's exposed identities

## Usernames Scanned
- `jvanleur` (primary)
- `jvanleur2234` (secondary)

## Tools Used
- **Tookie-OSINT** (Alfredredbird) - username enumeration across ~3000 platforms
- **Web searches** for breach/leak data

---

## FINDINGS

### Username Enumeration Results

**jvanleur** - 60+ active accounts found including:
- twitch.tv, twitter.com, youtube.com, facebook.com
- github.com, hackerrank.com, kaggle.com, geeksforgeeks.org
- steamcommunity.com, spotify.com, snapchat.com
- tryhackme.com, tiktok.com, strava.com
- roblox.com, duolingo.com, codecademy.com
- LessWrong, Hacker News, archive.org

**jvanleur2234** - Similar pattern, also found on:
- replit.com, ifttt.com
- airlinepilot.life (likely forum)
- forums.gunsandammo.com

### Breach/Leak Status
- HaveIBeenPwned: API requires paid key (blocked)
- BreachDirectory: No exposed passwords found via free API
- No public breach dumps found linking jvanleur2234@yahoo.com

---

## ACTION ITEMS FOR JOSEPH

1. **Password manager** - if not already using one (Bitwarden, 1Password)
2. **Check passwords** against breaches - use haveibeenpwned.com manually
3. **Remove sensitive accounts** from adult sites found (motherless, royalcams, etc.)
4. **Enable 2FA** on critical accounts (github, email, twitch, google)
5. **Audit reused passwords** - same password across multiple sites = risk

---

## Notes
- Tookie-OSINT is a legitimate CTI/OSINT tool, NOT malware
- The adult site hits are concerning for privacy/reputation
- Yahoo email has been in multiple major breaches (2013-2014 Yahoo breach, 500M+ accounts)