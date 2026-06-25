---
name: revenue-monitor
description: Take a weekly snapshot of the sales pipeline, detect meaningful changes from the prior week, and generate a digest of pipeline shifts. Use for weekly pipeline monitoring or to understand what moved in the pipeline.
disable-model-invocation: true
tags:
  - "Sales"
  - "Finance"
  - "Leland+"
---

# Revenue Monitor

Weekly pipeline surveillance — detect what changed and why it matters.

## Step 1 — Pull Current Pipeline

Use HubSpot MCP to fetch all open deals. For each, capture:
- Deal name, stage, amount, ask price, floor price
- Days in current stage
- Last contact date
- Current status

## Step 2 — Identify Changes

Look for:
- Deals that moved stages (forward or backward)
- Deals where price changed
- Deals newly created this week
- Deals that went cold (no contact in 7+ days)
- Deals recently closed (won or lost)

## Step 3 — Score the Week

### Positive Signals
Deals advancing, new pipeline created, closings.

### Warning Signals
Deals stalling, going cold, or showing signs of churn.

### Net Pipeline Movement
Is the pipeline growing, shrinking, or flat vs. the monthly revenue target?

## Output Format

```
# Pipeline Monitor — Week of [date]

## Net Summary
[1-2 sentences: is the pipeline healthy, improving, or at risk?]

## Moved Forward
- [Deal] — [old stage] → [new stage]

## Moved Backward / Stalled
- [Deal] — [issue]

## New This Week
- [Deal] — [$amount] — [program]

## Went Cold (7+ days no contact)
- [Deal] — last contact [date]

## Closed This Week
- Won: [deals + revenue]
- Lost: [deals + reason]

## Action Items
- [ ] [specific thing to act on]
```
