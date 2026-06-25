---
name: lead-prioritization
description: Rank a list of prospects or deals by weighted score across fit, intent, and engagement. Use to decide who to work first when you have more leads than time.
argument-hint: "[paste a list of leads/deals or describe the segment to prioritize]"
tags:
  - "Sales"
  - "Bundle 2"
  - "Leland+"
---

# Lead Prioritization

Rank prospects by a weighted score so you always work the best opportunities first.

## Scoring Model

Three dimensions, weighted by predictive value:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Fit | 30% | How well they match the ideal profile |
| Intent | 40% | How ready they are to move (strongest predictor) |
| Engagement | 30% | How active they've been with your outreach |

### Fit Scoring (0-10)
- 9-10: Perfect match — right program, right background, right goals
- 6-8: Good fit with minor gaps
- 3-5: Marginal fit
- 0-2: Poor fit

### Intent Scoring (0-10)
- 9-10: Active trigger present (reactivation date, cohort imminent, recent reply)
- 6-8: Engaged recently, no strong trigger
- 3-5: Applied but cold since
- 0-2: No engagement signals

### Engagement Scoring (0-10)
- 9-10: Recent reply or multi-open email activity
- 6-8: Some opens, no replies
- 3-5: Opened once or twice, long ago
- 0-2: No opens

## Weighted Score Formula
`(Fit × 0.3) + (Intent × 0.4) + (Engagement × 0.3)`

## Step 1 — Score the List

From `$ARGUMENTS`, score each prospect on all three dimensions. Calculate weighted total. Rank highest to lowest.

## Output Format

```
# Lead Priority List — [Date]

| Rank | Prospect | Fit | Intent | Engagement | Score | Next Action |
|------|----------|-----|--------|------------|-------|-------------|
| 1 | [name] | [n] | [n] | [n] | [weighted] | [action] |
| 2 | ... | | | | | |

## Top 5 — Work These Today
[Brief note on each: why they scored high + specific next action]

## Watch List — Check Back This Week
[Prospects just below threshold who could move up]
```
