---
name: business-case-builder
description: Build a structured business case for a new initiative, automation, tool, or investment. Use when pitching an idea to a manager or stakeholder, requesting budget or resources, or justifying a process change. Invoke when asked to "build a business case", "make the case for", "pitch this to leadership", or "justify this investment".
argument-hint: "[what you want to build the case for — e.g. 'hiring a second SDR' or 'building an automated reactivation agent']"
tags:
  - "Leadership"
  - "Operations"
  - "Leland+"
---

# Business Case Builder

Walk through a 6-step framework to produce a tight, persuasive business case. The output should be something the user can share directly with a manager or use in a meeting.

## Step 1 — Understand the Ask

If `$ARGUMENTS` is provided, use it as the starting point.

If it's vague, ask 2-3 clarifying questions:
- What is the specific thing being proposed?
- Who is the audience (who needs to approve or be convinced)?
- What's the timeline pressure, if any?

Don't ask more than 3 questions total. Make reasonable assumptions for anything else and note them at the end.

---

## Step 2 — Build the Case

Work through each section:

### 1. The Problem
What is broken, slow, expensive, or risky right now? Quantify where possible.
- How much time does it take?
- What's the error rate or failure mode?
- What's the cost of inaction?

### 2. The Proposed Solution
What exactly is being proposed? Be specific — not "automate the process" but "build an n8n workflow that does X, Y, Z."

### 3. Expected Outcomes
What gets better and by how much?
- Revenue impact (more deals closed, higher conversion, faster cycle)
- Time saved (hours/week, headcount equivalent)
- Risk reduced (fewer errors, less manual work, more consistency)

Use any context the user has already provided about current metrics, targets, or deadlines to make the projections concrete.

### 4. Cost / Effort
What does this require?
- Time to build (the user's hours or engineer hours)
- Tools or services (cost)
- Ongoing maintenance

### 5. Risk & Downsides
What could go wrong? What's the worst case if this fails or goes poorly?
Be honest — this builds credibility.

### 6. Recommendation
Clear ask: what should the decision-maker approve, fund, or greenlight?
Include a suggested timeline and who owns what.

---

## Step 3 — Output Format

Produce a clean document the user can paste into a Slack message, Google Doc, or bring to a meeting:

```
# Business Case: [Title]
Prepared by [Your Name] — [Date]

## The Problem
[2-4 sentences, quantified where possible]

## Proposed Solution
[Specific description of what's being built or done]

## Expected Outcomes
| Metric | Current | Projected |
|--------|---------|-----------|
| [metric] | [now] | [after] |

## What It Costs
- Time: [estimate]
- Tools/services: [cost if any]
- Ongoing: [maintenance burden]

## Risks
- [Risk 1 + mitigation]
- [Risk 2 + mitigation]

## Recommendation
[Clear ask + proposed timeline]

---
*Assumptions made: [list any gaps you filled in]*
```

Keep it to one page equivalent. Decision-makers skim — every section should have a clear point, not paragraphs of hedging.
