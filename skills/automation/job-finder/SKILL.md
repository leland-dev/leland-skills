---
name: job-finder
description: Find job listings matching a user's industry, level, and location, deduplicate against a running Google Sheet, append new jobs, and send a Gmail digest. Use when the user asks to find or search for jobs.
tags:
  - "HR/Recruiting"
  - "Life/Personal"
  - "Leland+"
---

# Job Finder

Find job listings matching a user's industry, level, and location. Deduplicates against a running Google Sheet, appends new jobs, and sends a Gmail digest.

## When to Use This Skill

TRIGGER when the user says any of: `/job-finder`, "find me jobs", "search for jobs", "job search", "look for jobs", "job opportunities", "find job listings".

Do NOT trigger for general career advice, resume help, or interview prep — those are separate tasks.

---

## Step 1: Collect Parameters

**First, check for a saved Sheet ID:**
Read the file `~/.claude/skills/job-finder/config.md` using the Read tool.
- If it exists and contains a `sheet_id`, use that value automatically — do not ask the user for it.
- If it doesn't exist or is empty, a new sheet will be created on first run.

Ask the user for the following (do NOT ask for Sheet ID — it's handled automatically):

1. **Industry** — e.g. "Product Management", "Software Engineering", "UX Design", "Finance", "Marketing"
2. **Level** — one of: intern / entry-level / mid-level / senior / executive
3. **Location** — a city/region (e.g. "San Francisco, CA") or "remote". Always required.
4. **Email** — address to send the digest to

Example prompt to user:
> To start your job search, I need a few details:
> - Industry or job function?
> - Experience level? (intern / entry-level / mid-level / senior / executive)
> - Location or remote?
> - Email address for the digest?

---

## Step 2: Search for Jobs

Run the following WebSearch queries. Replace `[INDUSTRY]`, `[LEVEL]`, and `[LOCATION]` with the user's inputs.

```
1. site:linkedin.com/jobs [INDUSTRY] [LEVEL] [LOCATION]
2. site:greenhouse.io [INDUSTRY] [LEVEL] [LOCATION]
3. site:lever.co [INDUSTRY] [LEVEL] [LOCATION]
4. [INDUSTRY] [LEVEL] jobs [LOCATION] 2026
5. [INDUSTRY] [LEVEL] hiring [LOCATION]
```

For remote searches, add "remote" to each query and remove the location from queries 1–3.

> Note: These queries surface publicly indexed listings via web search. Respect each job board’s terms of service and robots rules; do not bypass logins or rate limits, and treat all retrieved data as informational only.

From each search result, extract:
- **Job Title**
- **Company**
- **Location** (as listed)
- **URL** (direct link to the job posting)
- **Summary** — 1–2 sentences describing the role and key requirements
- **Date Posted** — if available, otherwise leave blank

Aim for 15–30 unique results across all queries. Discard duplicates by URL before proceeding.

---

## Step 3: Deduplicate Against Google Sheet

If a **Sheet ID was loaded from config**:
1. Read the sheet using the Google Drive read file tool with that Sheet ID
2. Extract all URLs from column F
3. Remove any job from your results whose URL already exists in column F

If no Sheet ID was found in config, skip deduplication — all results are new.

Track:
- `new_count` = number of jobs that passed deduplication
- `skipped_count` = number of jobs filtered out as duplicates

---

## Step 4: Update Google Sheet

**Column layout:**
| A: Date Found | B: Job Title | C: Company | D: Location | E: Level | F: URL | G: Summary | H: Status |

Status for all new rows defaults to `New`.

**If no Sheet ID was found in config (first run):**
- Use the Google Drive create file tool to create a new Google Sheet
- Name it: `Job Tracker — [INDUSTRY] [LEVEL] — [today's date]`
- Write the header row followed by all new job rows
- After the sheet is created, save the returned Sheet ID to `~/.claude/skills/job-finder/config.md` using the Write tool:
  ```
  sheet_id: [SHEET_ID]
  last_run: [today's date]
  ```

**If Sheet ID was loaded from config (subsequent run):**
- Use the Google Drive download file tool to get current sheet content
- Append new rows after the last existing row
- Re-upload using the Google Drive create file tool (overwrite) or update via available Drive tools
- Update `last_run` in `~/.claude/skills/job-finder/config.md` to today's date

---

## Step 5: Send Gmail Digest

Use `mcp__claude_ai_Gmail__create_draft` to create a draft for user review before sending.

**Subject:** `Job Digest — [INDUSTRY] [LEVEL] — [today's date]`

**Body format:**

```
Hi [first name from email or "there"],

Here's your job digest for [INDUSTRY] [LEVEL] roles in [LOCATION].

─────────────────────────────────
[JOB TITLE] — [COMPANY]
📍 [LOCATION] · [LEVEL]
[1–2 sentence summary of the role]
🔗 Apply: [URL]

[repeat for each new job]
─────────────────────────────────

[new_count] new jobs found. [skipped_count] duplicates skipped.

📊 View your full tracker: https://docs.google.com/spreadsheets/d/[SHEET_ID]

—
Sent by your Job Finder skill
```

If `new_count` is 0, skip the email entirely and tell the user: "No new jobs found this run — all results were already in your tracker."

---

## Step 6: Report Back to User

After completing the run, summarize:
- How many jobs were found across all searches
- How many were new vs. duplicate
- The Google Sheet link
- That a Gmail draft has been created for their review

Example:
> Done! Found 24 jobs total — 18 new, 6 already in your tracker.
> Gmail draft created — review and send when ready.
> 📊 Your tracker: https://docs.google.com/spreadsheets/d/[SHEET_ID]
