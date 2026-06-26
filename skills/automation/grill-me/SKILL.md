---
name: grill-me
description: A relentless interview to sharpen a plan or design.
disable-model-invocation: true
tags:
  - "Product & R&D"
  - "Operations"
  - "automation"
  - "productivity"
  - "External"
---

# Grill Me

Runs a structured, adversarial Q&A session to stress-test a plan or design. The goal is to surface hidden assumptions, gaps, and weaknesses before they become real problems.

## Dependency note

This skill delegates to `/grilling` if that skill is installed. If `/grilling` is not available, follow the inline process below.

## Process

### 1. Understand what's being grilled

Ask the user to describe the plan, design, or idea in 2–3 sentences if they haven't already. Confirm what type of decision this is (product, technical, business, personal).

### 2. Identify the core assumptions

List the 3–5 assumptions this plan depends on most. State them explicitly.

### 3. Adversarial questioning (the grill)

For each assumption, ask at least one hard question from each angle:

- **Failure mode**: "What's the single most likely way this breaks?"
- **Evidence**: "What evidence supports this? What contradicts it?"
- **Alternative**: "What would you do if this assumption is wrong?"
- **Stakeholder**: "Who would push back hardest on this, and why?"
- **Edge case**: "What's the edge case this plan doesn't handle?"

Do not accept vague answers. Follow up until the answer is concrete.

### 4. Summarize weak points

After the Q&A, list the top 3 risks or gaps uncovered. For each: what it is, why it matters, and one concrete way to address it before moving forward.
