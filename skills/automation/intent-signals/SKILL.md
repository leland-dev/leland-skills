---
name: intent-signals
description: Identify in-market signals that indicate a prospect is ready to buy. Use to prioritize which leads to contact now vs. later, or to understand what signals predict conversion.
argument-hint: "[describe your audience or paste a list of prospects/deals to score]"
tags:
  - "Sales"
  - "Marketing"
  - "Bundle 2"
  - "Leland+"
---

# Intent Signals

Detect which prospects are showing in-market behavior and should be contacted now.

## Signal Types

### First-Party Signals (strongest)
Actions taken directly with your product or content:
- Submitted an application
- Opened an offer email (especially multiple times)
- Clicked a pricing link
- Responded to any previous message
- Visited the site recently (if trackable)

### Behavioral Signals
Patterns that indicate active consideration:
- Multiple emails opened but no reply (reading but hesitating)
- Application submitted but offer not acknowledged
- Responded then went quiet (had interest, hit an obstacle)

### Situational Triggers
Life events that create urgency:
- Cohort start date approaching (< 30 days)
- Previously said "later" and that date has passed
- Job loss or career transition signal
- Prior cohort expired (reactivation candidate)

### Negative Signals (deprioritize)
- No opens on last 3+ emails
- Explicitly said not interested
- Contact info bouncing
- Stage stuck for 30+ days with no engagement

## Signal Scoring

| Signal | Weight |
|--------|--------|
| Application submitted | +5 |
| Offer email opened 2+ times | +4 |
| Prior reply, now quiet | +3 |
| Reactivation date passed | +3 |
| Cohort starts < 14 days | +3 |
| Cohort starts 14-30 days | +2 |
| No opens in 14+ days | -3 |

## Step 1 — Score the Prospects

From `$ARGUMENTS`, evaluate each prospect against the signal list and produce a ranked priority list.

## Output Format

```
# Intent Signal Report — [Date]

## Priority 1 — Contact Now
| Prospect | Score | Top Signal | Action |
|----------|-------|-----------|--------|
| [name] | [n] | [signal] | [what to do] |

## Priority 2 — Contact This Week
| Prospect | Score | Top Signal | Action |
|----------|-------|-----------|--------|

## Deprioritize
| Prospect | Reason |
|----------|--------|
```
