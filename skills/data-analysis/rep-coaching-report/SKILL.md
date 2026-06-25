---
name: rep-coaching-report
description: Generate a coaching report for a sales rep covering their pipeline health, deal risks, activity patterns, and high-impact improvement areas. Use before a 1:1 or coaching session.
argument-hint: "[rep name]"
disable-model-invocation: true
tags:
  - "Sales"
  - "Leadership"
  - "Leland+"
---

# Rep Coaching Report

Build a data-driven coaching report for a specific sales rep.

## Step 1 — Pull Rep's Pipeline

Use HubSpot MCP to fetch all open deals associated with the rep specified in `$ARGUMENTS`. For each deal retrieve stage, amount, last contact date, days in stage, price history, and status.

## Step 2 — Analyze

### Pipeline Health
- How many deals at each stage?
- What's the total pipeline value?
- Which deals are stalled (no movement in 7+ days)?

### Activity Patterns
- How many deals have recent email activity?
- Where are deals sitting longest?
- Any deals missing key properties?

### Win/Risk Balance
- Which deals are closest to closing?
- Which are most at risk of going cold?

### Coaching Focus Areas
Identify 2-3 specific, high-impact areas with deal-level examples and dollar amounts at stake.

## Output Format

```
# Coaching Report: [Rep Name]
Generated: [date]

## Pipeline Snapshot
| Stage | Count | Value |
|-------|-------|-------|
| [stage] | [n] | [$] |
| Total | [n] | [$] |

## Stalled Deals (7+ days no movement)
- [Deal name] — [stage] — [days stalled] — [$value]

## Highest Priority Deals
1. [Deal] — [why it matters] — [next action]
2. [Deal] — ...

## Coaching Focus Areas
### 1. [Focus Area]
[Specific deals + dollar impact + recommendation]

### 2. [Focus Area]
[Specific deals + dollar impact + recommendation]

## Suggested 1:1 Agenda
1. [topic]
2. [topic]
3. [topic]
```
