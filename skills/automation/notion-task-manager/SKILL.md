---
name: notion-task-manager
description: Parse brain dumps, bullet lists, or rambling input into structured Notion tasks — inbox to actionable database in one pass. Use this skill whenever the user says "add to Notion", "create tasks for", "turn this into tasks", "capture this", "log this to Notion", "brain dump", or hands over any list of things to do. Also trigger when the user pastes notes from a meeting, a Slack thread, or a voice note transcript and clearly has action items buried in them. Don't wait for the magic words — if there are tasks in the input and Notion is the right home, run this.
tags:
  - "Operations"
  - "Leland+"
---

# Notion Task Manager

Take messy input — brain dumps, bullet lists, rambling paragraphs, voice note transcripts — and turn it into properly structured Notion tasks.

## Step 1: Parse the Input

Extract discrete tasks from whatever the user gave you. For each task, identify:
- **Title** — the concrete action (not a description or a feeling — what's the actual task?)
- **Project/context** — which project or area? (default: General if unclear)
- **Owner** — who does this? (default: the user unless explicitly mentioned)
- **Priority** — high/medium/low (infer from urgency, deadline language, or blocker status)
- **Deadline** — if inferable from the text, capture it; otherwise leave blank

## Step 2: Find the Right Notion Home

Ask ONE clarifying question max if the destination page/database is unclear: "Should these go in your main task list, or is there a specific project database?"

If the user doesn't specify, default to the main task list.

Use `notion-search` to find the primary task database. Look for keywords like "tasks", "todo", "main", or "inbox". Note the database ID once found.

## Step 3: Create Tasks in Notion

Use `notion-create-pages` with the database ID. For each task:
- Set the title property to the task title
- Add project, owner, priority, and deadline properties as available
- Keep content brief — the title carries the task; content is optional detail

## Step 4: Confirm

Show the user what was created in a clean summary table:

| Task | Project | Owner | Priority | Deadline |
|---|---|---|---|---|
| [task title] | [project] | [owner] | [priority] | [deadline or "—"] |

Then ask: "All set? Let me know if any of these need adjusting."

## Special Rules

**Names matter.** If a task mentions a specific person, they are likely the owner. Capture their name exactly.

**Infer priority ruthlessly.** Blockers, external deadlines, and "ASAP" language = high. Regular work = medium. Nice-to-haves = low.

**Deadlines.** Today, tomorrow, this week, next Monday — convert to actual dates. If none inferable, leave blank.

**One task per line.** Don't nest or combine. Each item in a list is one task.

**Act on context, not medium.** If the input references a Slack message or email, don't create a task to read it — create a task to *act* on it. "Reply to [person] about [topic]" not "Read [person]'s Slack message."

## Example

**Input:** "Brain dump: 1) Finish the project proposal by Friday. 2) Check in with Sarah on the budget. 3) Fix the upload issue on the dashboard. 4) Schedule office hours — ask Jamie if Thursday works. 5) Write that intro post for the newsletter, not sure if urgent."

**Parsed tasks:**

| Task | Project | Owner | Priority | Deadline |
|---|---|---|---|---|
| Finish project proposal | Active Projects | You | High | Friday |
| Check in with Sarah on budget | Active Projects | Sarah | High | — |
| Fix upload issue on dashboard | Tech/Ops | You | Medium | — |
| Schedule office hours (confirm Thursday with Jamie) | Admin | Jamie | Medium | — |
| Write intro post for newsletter | Content | You | Medium | — |

## Tools Used

- `notion-search` — find the right database
- `notion-create-pages` — add tasks to that database
- `notion-fetch` (optional) — confirm the data source schema if needed

Never modify existing tasks. Only create new ones.
