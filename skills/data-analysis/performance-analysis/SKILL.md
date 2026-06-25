---
name: performance-analysis
description: Diagnose campaign or outreach performance through a six-layer metrics stack. Use when a sequence isn't converting and you need to find where it's breaking down.
argument-hint: "[describe the campaign or sequence and any metrics you have]"
tags:
  - "Sales"
  - "Marketing"
  - "Leland+"
---

# Performance Analysis

Diagnose where a campaign is breaking down using a 6-layer metrics stack.

## The Six Layers (in order)

Work top-down. Find where the numbers drop off — that's your problem layer.

### Layer 1 — Deliverability
Are emails reaching inboxes?
- Bounce rate (should be < 2%)
- Spam complaints (should be < 0.1%)
- Send volume vs. delivered

### Layer 2 — Open Rate
Are people opening?
- Open rate benchmark: 30-50% for warm, 15-25% for cold
- If low: subject line or sender reputation issue

### Layer 3 — Click / Engagement Rate
Are people engaging with the content?
- If opens are fine but clicks are low: body copy or CTA issue

### Layer 4 — Reply Rate
Are people responding?
- Reply rate benchmark: 2-5% cold, 10-20% warm
- If opens are high but replies are low: offer or ask isn't compelling

### Layer 5 — Conversion Rate
Of people who reply, how many move forward?
- If replies are happening but not converting: qualification or objection issue

### Layer 6 — Revenue Attribution
What's the revenue per contact in sequence?
- Final measure of whether the whole system is working

## Step 1 — Gather the Data

From `$ARGUMENTS`, extract whatever metrics are available. Fill in as many layers as possible.

## Step 2 — Find the Leak

Identify the layer where performance drops most significantly. That's where to focus.

## Step 3 — Diagnose and Recommend

For the problem layer, identify 2-3 likely root causes and specific tests to run.

## Output Format

```
# Performance Analysis: [Campaign Name]
Analyzed: [date]

## Funnel
| Layer | Metric | Benchmark | Actual | Status |
|-------|--------|-----------|--------|--------|
| Deliverability | Bounce rate | <2% | [%] | ✓/⚠ |
| Open rate | | 30-50% | [%] | ✓/⚠ |
| Click rate | | varies | [%] | ✓/⚠ |
| Reply rate | | 2-20% | [%] | ✓/⚠ |
| Conversion | | varies | [%] | ✓/⚠ |

## Where It's Breaking
[Layer name + what the data shows]

## Root Causes (most likely)
1. [cause]
2. [cause]

## Tests to Run
1. [specific test with hypothesis]
2. [specific test]
```
