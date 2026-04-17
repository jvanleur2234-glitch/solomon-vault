---
description: "Capture a new lead. Usage: /capture-lead <name> <source> [notes]"
---
Capture a new lead for Solomon OS:

**Input**: $ARGUMENTS (name, source, optional notes)

**Process**:
1. Create `work/leads/<name>.md` using lead template
2. Auto-score lead based on source:
   - HYRVE referral = 8/10
   - TikTok/Social = 7/10
   - Cold outreach = 5/10
   - Referral = 9/10
3. Add to `work/leads/Index.md`
4. Log to Solomon Bus as `lead_found` event

**Template fields**:
- name, source, status: new, score: X/10, follow_up: date, notes
