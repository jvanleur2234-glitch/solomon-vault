---
description: "Log a win. Usage: /capture-win <description> [revenue]"
---
Log a win to Solomon OS:

**Input**: $ARGUMENTS (description, optional revenue)

**Process**:
1. Create `perf/brag/YYYY-MM-DD.md` using win template
2. Update `perf/brag/Brag Doc.md` with link
3. Log to Solomon Bus as `win_logged` event
4. If revenue specified, update running total in North Star

**Template fields**:
- date, description, revenue (if any), evidence_links[], quarter
