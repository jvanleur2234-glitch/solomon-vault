---
description: "Onboard a new client. Usage: /new-client <name> <services>"
---
Onboard a new client for Solomon OS:

**Input**: $ARGUMENTS (name, services separated by comma)

**Process**:
1. Create `org/clients/<name>.md` using client template
2. Create `work/active/<name>-project.md` as initial project note
3. Add to `org/clients/Index.md`
4. Log to Solomon Bus as `client_acquired` event
5. Create Stripe payment link for services

**Template fields for client**:
- name, contact, services[], status: active, start_date, revenue, notes

**Template fields for project**:
- client, services, status: in-progress, progress: 0%, next_steps[]
