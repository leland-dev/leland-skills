---
name: icp-matrix-builder
description: Define and score your ideal customer profile across five dimensions to create a tiered targeting framework. Use when building or refining who you should be going after and why.
argument-hint: "[describe your product/offering and what you know about your best customers]"
tags:
  - "Sales"
  - "Marketing"
  - "Bundle 1"
  - "Leland+"
---

# ICP Matrix Builder

Build a scored, tiered Ideal Customer Profile framework.

## The Five Dimensions

Score each dimension 1-3 for a prospect. Total score (5-15) determines tier.

### 1. Fit
Does this person/company match your core use case?
- 3: Perfect fit — matches every key criterion
- 2: Good fit — matches most, minor gaps
- 1: Marginal — could work but requires heavy adaptation

### 2. Need
How acute is their pain right now?
- 3: Active problem, actively looking for a solution
- 2: Pain exists but not top priority
- 1: Latent need, not feeling it yet

### 3. Ability to Buy
Can they actually purchase?
- 3: Budget confirmed or clearly available, decision maker involved
- 2: Budget likely available, working through decision process
- 1: Budget uncertain, multiple approvals required

### 4. Timing
Are they ready to move?
- 3: Urgency present — deadline, event, or trigger
- 2: Considering near term (30-60 days)
- 1: Future consideration (90+ days)

### 5. Expandability
What's the long-term value?
- 3: High LTV, referral potential, repeat buyer
- 2: Single purchase, some upside
- 1: One-time, limited expansion potential

## Tier Definitions

| Score | Tier | Action |
|-------|------|--------|
| 13-15 | Tier 1 — Priority | Immediate personal outreach |
| 9-12 | Tier 2 — Qualified | Standard sequence |
| 5-8 | Tier 3 — Nurture | Long-term drip only |
| <5 | Not Qualified | Do not pursue |

## Step 1 — Build the ICP

From `$ARGUMENTS`, define what a high-scoring prospect looks like on each dimension. Be specific — not "interested in career growth" but "applied to a program in software engineering, opened initial offer email, cohort starts within 30 days."

## Step 2 — Create Scoring Rubric

For each dimension, write 1-2 specific signals that indicate a 3, 2, or 1 score for this particular audience.

## Output Format

```
# ICP Matrix: [Offering/Audience Name]

## Dimension Rubric

### Fit
- 3: [specific signals]
- 2: [specific signals]
- 1: [specific signals]

[repeat for each dimension]

## Tier Examples

### Tier 1 Profile (score 13-15)
[describe a real example of this person]

### Tier 2 Profile (score 9-12)
[describe a real example]

### Do Not Pursue
[describe what disqualifies someone]

## Recommended Actions by Tier
| Tier | Outreach | Timing | Owner |
|------|----------|--------|-------|
| 1 | [action] | [when] | [who] |
| 2 | [action] | [when] | [who] |
| 3 | [action] | [when] | [who] |
```
