---
name: investor-revenue-report
description: Generate a board or leadership-ready revenue report covering ARR trends, growth, pipeline coverage, and key metrics benchmarked against targets. Use for executive updates or leadership presentations.
argument-hint: "[time period — e.g. Q1 2026 or March 2026]"
disable-model-invocation: true
tags:
  - "Finance"
  - "Leadership"
  - "Leland+"
---

# Investor / Revenue Report

Reframe pipeline data for executive and leadership audiences.

## Step 1 — Pull Data

Use HubSpot MCP to gather for the period in `$ARGUMENTS`:
- Total revenue (closed-won)
- Revenue vs. target
- Pipeline value (open deals)
- New deals created
- Deals closed-won and closed-lost
- Pipeline coverage ratio (pipeline / target)

## Step 2 — Frame for Leadership

Executive audiences care about:
1. Are we on track to hit the number?
2. What's driving the gap (positive or negative)?
3. Is the pipeline healthy enough to cover next period?
4. What's the risk?

Avoid operational detail. Lead with the headline number and work down.

## Output Format

```
# Revenue Report — [Period]
Prepared: [date]

## Headline
[One sentence: on track / behind / ahead, by how much]

## Revenue
| Metric | Target | Actual | % of Target |
|--------|--------|--------|-------------|
| Revenue | $[target] | $[actual] | [%] |
| Deals Closed | — | [n] | — |
| Avg Deal Size | — | $[amount] | — |

## Pipeline Health
- Open pipeline: $[value] across [n] deals
- Coverage ratio: [X]x (pipeline / monthly target)
- Pipeline created this period: $[value]

## Key Drivers
[2-3 bullets on what drove results — automation, product mix, conversion rate changes]

## Risk
[What could prevent hitting next period's target]

## Outlook
[One paragraph on next period confidence and assumptions]
```
