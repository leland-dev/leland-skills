---
name: qbr-generator
description: Generate a quarterly business review covering revenue performance, pipeline coverage, forecast confidence, and deal analysis. Use at end of quarter or before a leadership review.
argument-hint: "[quarter — e.g. Q1 2026]"
disable-model-invocation: true
tags:
  - "Sales"
  - "Leadership"
  - "Leland+"
---

# QBR Generator

Build a structured quarterly business review.

## Step 1 — Define the Quarter

Use `$ARGUMENTS` to determine the quarter. If not specified, use the most recently completed quarter.

## Step 2 — Pull Data

Use HubSpot MCP and available data to gather:
- Deals closed-won in the quarter (revenue, product breakdown)
- Deals closed-lost (reasons, patterns)
- Pipeline entering vs. exiting the quarter
- Average deal size, time-to-close, conversion rates by stage
- Revenue vs. target

## Step 3 — Build the Review

### Revenue Performance
Actual vs. target. What drove the gap (positive or negative)?

### Pipeline Coverage
How much pipeline entered the quarter? What converted? What's the coverage ratio?

### Forecast Confidence
Based on current open pipeline, what's the realistic outlook for next quarter?

### Deal Analysis
Top wins — what made them close? Top losses — what pattern explains them?

### Process Health
Are automation flows working? Any systematic issues (missing thread IDs, stuck stages, failed workflows)?

## Output Format

```
# Quarterly Business Review — [Quarter]
Prepared: [date]

## Revenue Summary
| Metric | Target | Actual | Delta |
|--------|--------|--------|-------|
| Revenue | $[target] | $[actual] | [+/-] |
| Deals Closed-Won | — | [n] | — |
| Avg Deal Size | — | $[amount] | — |

## What Drove Results
[3-4 bullets on key drivers]

## Pipeline Health
[Coverage ratio, conversion rates, stage breakdown]

## Forecast: Next Quarter
[Realistic outlook with assumptions]

## Top Wins
1. [Deal + why it closed]

## Top Losses
1. [Deal + root cause]

## Process Issues
- [Any systematic problems]

## Recommendations
1. [Action for next quarter]
```
