---
name: meeting-prep
description: Generate a pre-meeting brief for any upcoming meeting by pulling calendar details, Notion context, and Slack activity. Use this skill whenever the user says "prep me for my meeting", "I have a meeting with [person]", "meeting brief", "what do I need to know before [meeting]", "prep for my call with [name]", or any time a meeting is coming up and context is needed fast. Also trigger when the user is preparing for a 1:1, stakeholder sync, or external call and hasn't explicitly asked for a brief — if a meeting is imminent, offer to run this.
tags:
  - "Operations"
  - "Leland+"
---

# Meeting Prep

Pull together everything the user needs to know before a meeting in under 5 minutes.

## Step 1: Get the Meeting Details

Use `gcal_list_events` to find the next upcoming meeting, or the meeting the user specified. Extract:
- Meeting title and description
- Time and duration
- Attendees (names and emails)
- Any agenda or notes in the calendar description

If the user specified a meeting by name or person ("my call with [name]", "the project sync"), match it to the nearest upcoming calendar event.

## Step 2: Search Notion for Context

Use `notion-search` with the meeting title, attendee names, and topic keywords. Look for:
- Active tasks or projects related to this meeting's subject
- Previous meeting notes or agendas
- Outstanding action items related to the attendees
- Any open decisions that might come up

Pull the most relevant 2-3 pages and extract key context (status, blockers, open questions).

## Step 3: Search Slack for Recent Context

Use `slack_search_public_and_private` to find recent conversations about the meeting topic or attendees. Focus on the last 3-7 days. Look for:
- Decisions already made that will affect the discussion
- Blockers or tensions surfaced in recent threads
- Questions or requests from the people in the meeting
- Tone shifts or context that matters for how the meeting will go

## Step 4: Synthesize the Brief

Compile everything into this template:

```
# Meeting Brief: [Meeting Title]

**When:** [Date, time, duration]
**With:** [Attendee names and roles]
**Purpose:** [What this meeting is actually for — be specific]

---

## Background

[2-3 sentences of relevant context from Notion and Slack. What's the current state of the project or relationship? What's been happening recently?]

## What to Accomplish

- [Specific outcome 1 — a decision, approval, or alignment]
- [Specific outcome 2]
- [Specific outcome 3 if applicable]

## Open Questions

- [Question the user should raise or be ready to answer]
- [Question]
- [Question if applicable]

## Relevant Context

**From Notion:**
[Key task/project status, blockers, or decisions relevant to this meeting]

**From Slack:**
[Recent conversation highlights — decisions, tensions, or context that matters]

## Prep Notes

[Anything worth knowing walking in — tone to expect, likely pushback, or a decision that's about to come up]
```

## Step 5: Deliver

Present the brief inline in chat. If the user wants a saved copy, write it to their notes folder with a filename like `[date]-[meeting-name]-brief.md`.

## Key Rules

- **Specificity is credibility.** Name every person, project, and outcome exactly. Never "the team" — always the actual name.
- **One page max.** If there's more context than fits, prioritize: What to Accomplish > Open Questions > Relevant Context.
- **Surface conflicts.** If Slack or Notion reveals a blocker, tension, or unresolved issue, call it out in Prep Notes.
- **Never fabricate.** If Notion and Slack return nothing useful, say so in the brief — don't fill it with generic content.
- **Never send the brief anywhere** — it's for the user's eyes only. Show it in chat.

## Tools Used

- `gcal_list_events` — get meeting details
- `notion-search` — find relevant project/task context
- `slack_search_public_and_private` — find recent relevant Slack threads
- `slack_read_thread` — get full context on key threads if needed
