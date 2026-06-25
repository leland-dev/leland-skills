---
name: weekly-recap
description: Friday end-of-week summary — what shipped, what's in progress, decisions made, blockers, and next week priorities. Pulls from Notion tasks, Slack updates, and Gmail. Produces a manager-ready format. Use this skill whenever the user says "weekly recap", "end of week summary", "what did I accomplish this week", "Friday summary", "week in review", "recap the week", or any variation of wanting a structured summary of their work week.
tags:
  - "Operations"
  - "Leadership"
  - "Leland+"
---

# Weekly Recap

This skill pulls together the user's week across Notion, Slack, and Gmail to generate a structured Friday recap. The output is ready to share with a manager or keep for personal records.

## Step 1: Fetch Notion Tasks

Pull all tasks from the user's Notion workspace that were completed or are currently in progress this week (Monday–Friday).

Look for:
- Task name and status (Completed, In Progress)
- Associated projects or work areas
- Due dates this week
- Any blockers or notes attached

**Notion instruction**: Search for tasks with completion date or status update between Monday of this week and today. Prioritize tasks tied to active projects.

## Step 2: Search Slack for Key Updates

Search the Slack workspace for messages sent or received this week that contain:
- Decisions made (keywords: "decided", "approved", "confirmed", "green light")
- Project updates (keywords: "shipped", "launched", "deployed", "completed")
- Blockers or risks (keywords: "blocked", "stuck", "waiting on", "delayed")
- Important announcements or context from managers or team leads

**Slack channels to prioritize**: Channels directly related to the user's active projects and team communication.

Search for messages from this week (Monday–Friday). Focus on threads the user started or was tagged in.

## Step 3: Check Gmail for Resolved Threads

Search Gmail for important email threads that were resolved or concluded this week.

Look for:
- Emails with "Re:" or followup responses indicating closure
- Decisions or confirmations from stakeholders
- Project milestones or approvals
- Any blockers that were addressed

**Gmail search filters**: Focus on threads with action items that are now marked "resolved" or with final approvals.

## Step 4: Synthesize and Format

Compile everything into the structured template below. Keep language direct and specific — name people, projects, and outcomes. Nothing vague.

---

## Weekly Recap Output Template

```
WEEKLY RECAP — WEEK OF [DATE RANGE]
Prepared for: [Manager name]
Prepared by: [Your name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SHIPPED THIS WEEK
• [Project name]: [What shipped — be specific about the output]
• [Project name]: [What shipped]
[One line per shipped item. Include tools used if notable.]

IN PROGRESS
• [Project]: [Current task name] — [Status: % complete or blocker]
• [Project]: [Current task name] — [Status]
[List tasks that moved forward but aren't done yet]

KEY DECISIONS MADE
• [Decision]: [Who decided, what was approved, outcome]
• [Decision]: [Details]
[Name the decision, who made it, and what it means for next week]

BLOCKERS
• [Blocker]: [What's blocked, why, who needs to unblock it]
• [Blocker]: [Details]
[Be specific about what's stopped. Leave blank if none exist.]

NEXT WEEK PRIORITIES
1. [Project/task]: [What needs to happen, why it matters]
2. [Project/task]: [Details]
3. [Project/task]: [Details]
[Rank by impact and urgency. Tie each to a project or stakeholder.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Output Guidelines

- **Specificity is credibility.** Name every project, person, and outcome. Never "the team" or "something shipped."
- **One line per item.** If you need to explain something, add a brief detail line below. Keep it scannable.
- **Focus on impact.** What moved forward? What was decided? What's blocking progress? Not a task checklist — a work summary.
- **Blockers are honest.** If waiting on someone, name them. If something is risky, flag it.
- **Next week is actionable.** Each priority should have a clear owner and next step. No vague items.

---

## How to Use This Output

Once generated, you can:
1. **Share with your manager** — Copy the recap into an email or paste into Slack
2. **Archive** — Save to a recurring weekly folder in Notion for your own records
3. **Base for 1:1** — Use as the agenda for your next sync with your manager
4. **Escalate blockers** — If any blocker is critical, flag it immediately

---

## Tips for Accurate Recaps

- Check Notion at the start of the week to see what's on your plate
- Bookmark any Slack threads with decisions or key updates as they happen
- Flag important emails for easy Gmail retrieval on Friday
- If unsure whether something counts as "shipped" or "in progress", ask: did it move forward visibly? If yes, include it.

---

*Run this skill every Friday to close out your week and plan ahead.*
