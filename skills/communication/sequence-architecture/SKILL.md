---
name: sequence-architecture
description: Design a multi-touch outreach sequence with timing, channel, and escalation logic. Use when building a new follow-up cadence, SDR drip sequence, or reactivation flow.
argument-hint: "[describe the audience, goal, and how many touches you want]"
tags:
  - "Sales"
  - "Marketing"
  - "Bundle 2"
  - "Leland+"
---

# Sequence Architecture

Design a complete multi-touch sequence with timing and escalation logic.

## Step 1 — Define the Sequence Parameters

From `$ARGUMENTS`, determine:
- **Audience**: who receives this? (cold, warm, ghosted, reactivation?)
- **Goal**: what action should they take at the end?
- **Touches**: how many emails/messages?
- **Channels**: email only, or mix with SMS/call?

## Step 2 — Design the Sequence

Each touch should:
- Have a specific purpose (introduce, follow up, add value, create urgency, break up)
- Use a different angle than the prior touch
- Escalate appropriately — don't repeat yourself

### Sequence Structure Template

| Touch | Day | Channel | Purpose | Angle |
|-------|-----|---------|---------|-------|
| 1 | 0 | Email | Introduce offer | Value + relevance |
| 2 | 3 | Email | Follow up | Social proof or urgency |
| 3 | 7 | Email | Add value | New angle or objection address |
| 4 | 12 | Email/SMS | Soft urgency | Deadline or limited availability |
| 5 | 18 | Email | Breakup | Permission to close, final ask |

Adjust timing and touch count based on audience warmth.

## Step 3 — Write Subject Line Variants

For each touch, provide 2 subject line options. Good subject lines:
- Are specific (mention their name, program, or situation)
- Create curiosity without being clickbait
- Under 8 words

## Output Format

```
# [Sequence Name] — [N]-Touch Sequence

## Overview
Audience: [who] | Goal: [action] | Duration: [N days]

## Sequence

### Touch 1 — Day 0
**Channel:** Email
**Purpose:** [goal of this touch]
**Subject options:**
- [option 1]
- [option 2]
**Angle:** [what makes this touch different]

### Touch 2 — Day [N]
...

## Escalation Logic
- If reply received: [what to do]
- If no reply after touch 3: [adjustment]
- If they say "not now": [move to reactivation]
```
