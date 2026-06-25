---
name: meeting-analyzer
description: Analyze a meeting transcript or notes to extract action items, key decisions, open questions, and missed opportunities. Use after any meeting or call. Auto-invoke when asked to "analyze a meeting", "pull action items", "what did we decide", or "summarize my meeting". Works with Granola meeting notes.
argument-hint: "[optional: meeting name, date, or keywords to find it — leave blank to pick from recent meetings]"
disable-model-invocation: false
tags:
  - "Sales"
  - "Operations"
  - "Leland+"
---

# Meeting Analyzer

Analyze a meeting and produce a structured breakdown that's actually useful — not just a summary, but a clear record of what happened, what needs to happen next, and what almost got missed.

## Step 1 — Find the Meeting

If `$ARGUMENTS` is provided, use it to identify which meeting (by name, date, or keywords).

If no argument is given, use the Granola MCP to list recent meetings and ask the user to pick one.

Once identified, fetch the full transcript or notes via Granola.

---

## Step 2 — Analyze

Read the full transcript carefully. Extract:

### Action Items
For each action item found:
- **Who** owns it (name or role)
- **What** exactly they need to do
- **By when** if a deadline was mentioned

If ownership is ambiguous, flag it.

### Decisions Made
Things that were agreed on, confirmed, or resolved during the meeting. Be specific — "we decided X" not "there was discussion about X."

### Open Questions
Things that came up but weren't resolved. Questions that need answers before work can move forward.

### Missed Opportunities
This is the most valuable section. Look for:
- Moments where the user could have pushed harder on something but didn't
- Topics that were dropped or glossed over
- Commitments that were vague and should have been pinned down
- Times where a question wasn't asked but should have been
- Anything that will likely come back as a problem later

### Key Context
1-2 sentences on what this meeting was actually about and what the outcome was at a high level.

---

## Step 3 — Output Format

```
## [Meeting Name] — [Date]

**In one line:** [what this meeting was and what was resolved]

---

### Action Items
- [ ] [Person] — [what to do] — [by when if known]
- [ ] ...

### Decisions Made
- [Decision 1]
- [Decision 2]

### Open Questions
- [Question that still needs an answer]

### Missed Opportunities
- [Specific moment + what could have been said or done differently]

---
```

Keep it scannable. No fluff. If something isn't there (e.g., no missed opportunities), skip that section rather than writing "none found."
