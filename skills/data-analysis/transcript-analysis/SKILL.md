---
name: transcript-analysis
description: Extract seven layers of insight from a sales call or meeting transcript. Use after a call to understand what was said, what was missed, and what to do next.
argument-hint: "[paste transcript or meeting notes, or specify a Granola meeting to pull]"
tags:
  - "Sales"
  - "Operations"
  - "Leland+"
---

# Transcript Analysis

Extract seven layers of insight from a call or meeting transcript.

## Step 1 — Get the Transcript

If `$ARGUMENTS` contains a transcript or notes, use it directly.
If `$ARGUMENTS` names a meeting, fetch it from Granola MCP.

## The Seven Layers

### Layer 1 — What They Actually Said
Not your interpretation — the actual words. Key phrases that reveal how they think about their situation, their goal, or their hesitation.

### Layer 2 — What They Meant
The subtext. What did their questions or hesitations signal? What were they really asking or saying?

### Layer 3 — Pain Signals
Specific moments where they expressed frustration, uncertainty, or urgency. Quote the line.

### Layer 4 — Buying Signals
Moments that indicated interest, readiness, or intent. ("When does it start?" "How does payment work?")

### Layer 5 — Objections (stated and unstated)
What did they push back on? What did they avoid or deflect? What objection never got voiced but was implied?

### Layer 6 — Missed Opportunities
Questions you didn't ask. Threads you didn't pull. Moments where the conversation could have gone deeper.

### Layer 7 — Next Steps
What was committed to? What's unclear? What needs to happen before the next conversation?

## Output Format

```
# Transcript Analysis: [Meeting/Call Name]
Date: [date]

## What They Said (key quotes)
- "[quote]" — [context]

## What They Meant
[interpretation of subtext]

## Pain Signals
- "[quote]" — [what it reveals]

## Buying Signals
- "[quote]" — [what it signals]

## Objections
| Stated | Unstated/Implied |
|--------|-----------------|
| [objection] | [implied concern] |

## Missed Opportunities
- [moment + what could have been said]

## Next Steps
- [ ] [committed action + owner]
- [ ] [unclear item that needs resolution]
```
