---
name: project-status
description: Generate crisp, stakeholder-ready status updates for any active project by pulling Notion tasks and Slack activity. Use this skill whenever the user says "project status", "status update", "write a status report", "update on [project]", "catch [person] up on [project]", "where are we on [project]", or "progress report". Also trigger when the user needs to brief a manager or stakeholder on a project's current state.
tags:
  - "Operations"
  - "Leadership"
  - "Leland+"
---

# Project Status Generator

Generate a crisp status update for any active project. Pulls live data from Notion and Slack, then structures output in a direct, outcomes-focused voice.

---

## Intake

1. **Identify the project** (or infer from context). If ambiguous, ask: "Which project do you want a status update on?"

2. **Confirm audience**:
   - Slack update to team? Email to manager? Report to leadership?
   - Default: Draft suitable for Slack or email forward.

---

## Data Collection

### Notion Tasks
Search Notion for the project's task database. Look for:
- ✅ Completed tasks (this cycle/week/sprint)
- 🔄 In-progress items
- 🛑 Blocked or waiting for decision
- 📌 Next milestone or upcoming critical path

Use `notion-search` to find project pages, then `notion-fetch` to pull task status.

### Slack Activity
Search Slack for project-related messages from this week. Look for:
- Async decisions made
- Blockers surfaced
- Wins shipped or completed
- Open questions to stakeholders

Use `slack_search_public_and_private` filtered by relevant channels and date range (last 7 days).

### Synthesize
Combine Notion (formal tracking) + Slack (live pulse) into a single narrative. Identify patterns: velocity, blockers, decision gaps.

---

## Output Template

Fill each section with **specific outcomes, numbers, and names**.

```
**[PROJECT NAME] — Week of [DATE]**

🟢 **STATUS**: [Green/Yellow/Red] — [one-sentence statement about project health]

**Completed**
- [Specific deliverable], [who shipped it]
- [Specific deliverable], [who shipped it]
- [Impact number if available]

**In Progress**
- [Task name]: [current blocker or next step], expected completion [date]
- [Task name]: [current blocker or next step], expected completion [date]

**Blocked / Needs Decision**
- [Blocker name]: needs [specific decision or resource] from [person]
- [Blocker name]: needs [specific decision or resource] from [person]

**Next Milestone**
[Date]: [Specific deliverable or gate — be precise, not vague]

---

**Notes**
[Any context stakeholders need, or shout-outs to teammates]
```

---

## Voice Guidance

Write status updates with these principles:

1. **Conviction**: "We're on track" not "it seems like we might be tracking okay"
2. **Specificity**: "[Person] approved the [thing] on [day]" not "we got approval"
3. **Names**: Every person named. "[Person] completed the [task]" not "the task got done"
4. **Numbers**: Include them. "3 items completed, 2 pending" not "several items are done"
5. **Outcomes, not narration**: "Shipped the [deliverable]" not "we worked on it this week"
6. **No hedging**: Strike "might", "could", "seems", "hopefully"
7. **No em-dashes** in professional contexts (Slack/email)

**Tone**: Direct, action-oriented, confident. The audience wants facts and decisions, not explanation.

---

## Workflow Steps

1. **Ask for project context** if not provided.

2. **Query Notion**: Find the project's main tracking page/database. Extract completed, in-progress, blocked, next milestone.

3. **Query Slack**: Search the project channel for this week's activity. Pull blockers, decisions, and wins from message threads.

4. **Write status**: Fill the template with real data. Apply voice checks (conviction, names, numbers, no hedging). Keep to 1-2 screens of text.

5. **Output**: Show the draft to the user. Flag any missing data. Do NOT send or publish without the user's approval.

---

## Notes for the AI Agent

- If Notion search returns no results, ask: "Should I check a specific page or database?"
- If Slack returns sparse activity, note it in the draft: "Limited Slack activity this week — status inferred from Notion only"
- If a blocker is waiting on an external party, name the person and the specific ask
- If a milestone is fuzzy, drill down: ask the user what "done" looks like specifically
- Always err on specificity. Better to ask for clarification than to guess.
