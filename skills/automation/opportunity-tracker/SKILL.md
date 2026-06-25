---
name: opportunity-tracker
description: Track professional opportunities — job applications, networking contacts, follow-ups, and career conversations. Logs to a Google Sheet, surfaces due reminders, and generates pipeline views. Use this skill whenever the user says "track this opportunity", "log this contact", "I just applied to", "had a call with [person]", "got an intro to [person]", "networking follow-up", "add to my tracker", or any time they want to record or review career and networking activity.
tags:
  - "HR/Recruiting"
  - "Life/Personal"
  - "Leland+"
---

# Opportunity Tracker

Structure and log professional opportunities into a Google Sheet for centralized career tracking. Parses natural language input, organizes by status, and surfaces follow-ups due within 7 days.

## Triggered Behavior

When the user mentions tracking an opportunity, applying to a role, connecting with someone, or following up on a career conversation, this skill:

1. **Loads or creates the Google Sheet** (via config.md)
2. **Parses the input** into structured fields
3. **Appends a new row** to the sheet
4. **Surfaces urgent follow-ups** (due within 7 days)
5. **On request, generates a pipeline view** showing all active opportunities by status

---

## How It Works

### Step 1: Load Sheet ID from Config

Check for a `config.md` file in this skill's directory (`~/.claude/skills/opportunity-tracker/config.md`).

- **If config.md exists and has a `sheet_id`:** Use that sheet ID for all read/write operations.
- **If config.md does not exist or has no sheet_id:** A new sheet will be created in Step 2.

### Step 2: Parse Input

Extract these fields from the user's natural language input:

- **Person**: Name of the contact (if applicable)
- **Company**: Organization name
- **Role/Context**: Job title, project, or reason for connection ("Senior PM at Acme", "Networking contact", "Informational interview", etc.)
- **Date Logged**: When this opportunity was created (default: today)
- **Source**: How they connected ("LinkedIn", "Referral from [name]", "Company website", "Conversation at [event]", etc.)
- **Status**: One of: Applied / Reached Out / In Conversation / Waiting / Follow Up Due / Closed Won / Closed Lost
- **Next Action**: Specific next step ("Send follow-up email", "Schedule call", "Review offer", "Decline gracefully")
- **Deadline**: When the next action is due (YYYY-MM-DD format)
- **Notes**: Any additional context

### Step 3: Create or Update the Google Sheet

**If no Sheet ID was loaded (first run):**
- Use `mcp__claude_ai_Google_Drive__create_file` to create a new Google Sheet
- Name it: `Career Opportunities Tracker`
- Write the header row followed by the new entry row
- Save the returned Sheet ID to `config.md`:
  ```
  sheet_id: [returned Sheet ID]
  last_updated: [today's date]
  ```
- Tell the user: "Created a new tracker sheet. Saved the Sheet ID to config — it'll be used automatically on future runs."

**If a Sheet ID was loaded (subsequent run):**
- Use `mcp__claude_ai_Google_Drive__download_file_content` to read the current sheet
- Append the new row after the last existing row
- Re-upload using `mcp__claude_ai_Google_Drive__create_file` (overwrite) with the full updated content
- Update `last_updated` in config.md to today's date

**Sheet column layout:**

| A: Date Logged | B: Person | C: Company | D: Role/Context | E: Source | F: Status | G: Next Action | H: Deadline | I: Notes |

### Step 4: Surface Urgent Follow-Ups

After logging, read all rows from the sheet and check the Deadline column (H). Flag any row where:
- Status is "Follow Up Due", OR
- Deadline is within 7 days from today

Display as:

```
🔴 FOLLOW-UPS DUE WITHIN 7 DAYS

[Person] at [Company] — [Status]
  Next Action: [action]
  Deadline: [date] ([N] days away)
  Notes: [brief context]
```

If none are due, confirm: "No follow-ups due within 7 days."

### Step 5: Generate Pipeline View (on request)

When the user asks "show my pipeline", "opportunity status", or "where do I stand", read all rows from the sheet and group by Status column:

```
📊 OPPORTUNITY PIPELINE

Applied ([N])
├─ [Person] at [Company] — Applied [date] via [source]

Reached Out ([N])
├─ [Person] at [Company] — Follow-up due [date]

In Conversation ([N])
├─ [Person] at [Company] — Next: [action] by [date]

Waiting ([N])
├─ [Person] at [Company] — [reason, e.g., "Offer review"]

Follow Up Due ([N])
├─ [Person] at [Company] — URGENT — [action]

Closed – Won ([N])
├─ [Person] at [Company] — [closed date]

Closed – Lost ([N])
├─ [Person] at [Company] — [reason, brief]

---
Total Active: [count] | Total Closed: [count]
📊 Full tracker: https://docs.google.com/spreadsheets/d/[SHEET_ID]
```

---

## Example Interactions

**User:** "I just applied to the Senior PM role at Acme Corp. Found it on their careers page."

**Skill logs:**
- Person: —
- Company: Acme Corp
- Role/Context: Senior PM
- Source: Company website
- Status: Applied
- Next Action: Track for response
- Deadline: 14 days from today

---

**User:** "Had a coffee chat with Sarah Chen from TechFlow. She said she'd introduce me to the hiring manager next week."

**Skill logs:**
- Person: Sarah Chen
- Company: TechFlow
- Role/Context: Networking contact
- Status: In Conversation
- Next Action: Wait for intro to hiring manager
- Deadline: 7 days from today

---

## Status Definitions

| Status | Meaning | Default Deadline |
|---|---|---|
| **Applied** | Application submitted | 14 days |
| **Reached Out** | Initial contact made | 7 days |
| **In Conversation** | Active dialogue; next steps pending | 7 days |
| **Waiting** | Waiting on them | 14 days |
| **Follow Up Due** | Action required within 7 days | Immediate |
| **Closed Won** | Offer accepted, role started, relationship established | — |
| **Closed Lost** | Rejected, withdrew, or relationship inactive | — |

---

## Key Rules

1. **Always parse a full entry** — extract company, status, and next action before writing to the sheet
2. **Set deadlines for all active opportunities** — use the defaults in Status Definitions if the user doesn't specify
3. **Surface urgent follow-ups proactively** — run the check after every new entry, not just on request
4. **Keep notes specific** — context matters (where you met, what was discussed, why they matter)
5. **Close entries explicitly** — don't leave "Waiting" entries open indefinitely
6. **Pipeline view on demand** — generate whenever the user asks for status or overview
7. **Never modify the sheet without confirmation** — always show what will be logged before writing

---

## Integrations

- **Google Sheets (Drive MCP)**: Primary store for all opportunity data
- **Google Calendar** (optional): Create reminders for deadlines if integrated
- **Gmail** (optional): Draft follow-up templates if needed
