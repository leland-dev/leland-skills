---
name: deal-action-engine
description: Read at-risk or stalled deals, diagnose the specific blocker, and draft a targeted re-engagement email that addresses the actual obstacle. Use when a deal has gone quiet and needs a nudge.
argument-hint: "[deal name, contact name, or 'all stalled deals']"
disable-model-invocation: true
tags:
  - "Sales"
  - "Leland+"
---

# Deal Action Engine

Diagnose stuck deals and draft re-engagement emails that address the real blocker.

## Step 1 — Identify the Deal(s)

If `$ARGUMENTS` specifies a deal, pull that deal from HubSpot MCP.
If `$ARGUMENTS` is "all stalled" or empty, pull all deals with no contact in 7+ days.

For each deal fetch:
- Stage, current status, price history
- Last email content (via gmail_thread_id)
- Notes and activity log
- Program name and cohort

## Step 2 — Diagnose the Blocker

Don't assume — read the actual notes and email history. Common blockers:

| Signal | Likely Blocker |
|--------|---------------|
| No reply after offer | Hasn't seen it / not interested / price |
| Replied then went quiet | Specific objection not addressed |
| Said "later" | Timing issue — needs reactivation date |
| Multiple price drops, no close | Price floor reached, decision pending |
| Active thread, no commitment | Undecided, needs urgency or social proof |

## Step 3 — Draft Re-Engagement Email

Write an email that:
- References the specific thing that's actually blocking them (not a generic "just checking in")
- Is short — 3-5 sentences max
- Has one clear ask or CTA
- Matches the tone of the prior thread

## Output Format

```
# Deal Action: [Deal/Contact Name]

## Diagnosis
[What's actually blocking this deal based on the notes/thread]

## Recommended Email Draft

Subject: [subject line]

[email body]

---

## Next Step If No Reply
[What to do if this doesn't get a response]
```
