---
name: objection-mining
description: Catalog and analyze objections from deals, emails, or calls into a six-category taxonomy with response playbook. Use to build a systematic objection handling guide or diagnose why deals are stalling.
argument-hint: "[paste objections, deal notes, or email replies — or describe what objections you're hearing]"
tags:
  - "Sales"
  - "Bundle 1"
  - "Leland+"
---

# Objection Mining

Turn raw objections into a structured playbook.

## Six-Category Taxonomy

### 1. Price / Value
"It's too expensive." "I can't afford it right now."
Root fear: Wasting money on something that won't work.

### 2. Timing
"Not the right time." "Maybe in a few months."
Root fear: Can't commit to the schedule or pace right now.

### 3. Credibility / Risk
"I'm not sure this will actually work for me." "How do I know it's legit?"
Root fear: Fear of being misled or setting themselves up to fail.

### 4. Comparison / Alternatives
"I'm looking at other options." "Why this over [competitor]?"
Root fear: Making a suboptimal choice.

### 5. Internal / External Blockers
"I need to talk to my spouse." "I need to check my finances."
Root fear: Conflict with someone else or a practical constraint.

### 6. Disinterest / Not a Fit
"I'm not sure this is for me." "I've changed my mind about this path."
Root fear: Goal or motivation has shifted.

## Step 1 — Categorize the Objections

From `$ARGUMENTS`, read all the objections. Map each to one of the six categories. If an objection doesn't fit cleanly, put it in the closest category and note it.

## Step 2 — Build the Response Playbook

For each category that appears, write:
- The best response approach (acknowledge → reframe → address → ask)
- 1-2 example responses in natural language
- What NOT to do (common mistake)

## Output Format

```
# Objection Playbook: [Audience/Context]

## Objection Frequency
| Category | Count | % of Total |
|----------|-------|-----------|
| Price/Value | [n] | [%] |
| Timing | [n] | [%] |
| [etc.] | | |

## Top Objections & Responses

### [Category Name]
**They say:** "[most common version]"
**Root fear:** [underlying concern]

**How to respond:**
1. Acknowledge: "[example]"
2. Reframe: "[example]"
3. Address: "[example]"
4. Ask: "[example closing question]"

**Don't:** [common mistake]

---

## Patterns & Insights
[What the objection mix reveals about your audience or offer]

## Recommended Changes
[Changes to the offer, messaging, or sequence based on objection patterns]
```
