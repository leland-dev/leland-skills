---
name: deal-patterns
description: Analyze 12 variables across closed deals to identify what predicts wins. Use to understand what deal characteristics lead to revenue so you can replicate them.
argument-hint: "[time range or segment to analyze — e.g. 'last 60 days' or 'enterprise deals']"
tags:
  - "Sales"
  - "Leadership"
  - "Leland+"
---

# Deal Patterns

Find the 12 variables that predict whether a deal closes.

## The 12 Variables

| # | Variable | What to Measure |
|---|----------|----------------|
| 1 | Time to first reply | How quickly did they respond to initial offer? |
| 2 | Email open count | How many times did they open emails? |
| 3 | Price sensitivity | Did deal close at ask price, or require drops? |
| 4 | Number of price drops | How many drops before close or loss? |
| 5 | Days in pipeline | Total time from offer to close/loss |
| 6 | Stage velocity | How long in each stage? |
| 7 | Product category | Which categories have highest win rate? |
| 8 | Deal size | Do larger or smaller deals close at higher rates? |
| 9 | Inbound vs. triggered | Did they apply themselves or were they reactivated? |
| 10 | Objection count | How many objections raised? |
| 11 | Thread activity | Active email exchange or one-sided? |
| 12 | Cohort proximity | Did cohort timing correlate with urgency? |

## Step 1 — Pull the Deals

Use HubSpot MCP to fetch closed-won and closed-lost deals from `$ARGUMENTS` time range. For each, collect data on as many of the 12 variables as available.

## Step 2 — Compare Won vs. Lost

For each variable, compare the averages between won and lost deals. Flag variables where the gap is significant.

## Step 3 — Identify Predictors

Which 3-4 variables most clearly separate wins from losses? These are your leading indicators.

## Output Format

```
# Deal Pattern Analysis: [Segment/Time Range]
[N] won | [N] lost analyzed

## Variable Comparison

| Variable | Won Avg | Lost Avg | Predictive? |
|----------|---------|----------|-------------|
| Time to first reply | [n days] | [n days] | ✓/– |
| Price drops before close | [n] | [n] | ✓/– |
| Days in pipeline | [n] | [n] | ✓/– |
| [etc.] | | | |

## Top Predictors of a Win
1. [variable] — [what the data shows]
2. [variable] — [what the data shows]
3. [variable] — [what the data shows]

## Top Predictors of a Loss
1. [variable] — [what the data shows]

## Recommended Changes
Based on these patterns:
1. [specific change to process, sequence, or qualification]
2. [specific change]
```
