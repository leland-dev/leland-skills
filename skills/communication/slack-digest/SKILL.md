---
name: slack-digest
description: Summarize recent Slack activity — surfaces only what the user needs to know, focusing on their key projects, collaborators, and action items waiting on them. Use this skill whenever the user says "what's in Slack", "Slack digest", "what did I miss", "catch me up on Slack", "any important Slack messages", "Slack summary", "what's new in Slack", or any time they want a signal-over-noise summary of their Slack workspace. Also trigger proactively if the user has been away or mentions they haven't checked Slack.
tags:
  - "Operations"
  - "Leland+"
---

# Slack Digest

Surface signal, not noise. Grab the last 24 hours of Slack activity (or whatever time period the user specifies) across channels relevant to their work, then synthesize it into the 3-5 things they actually need to know.

## Channels to Focus On

Prioritize these types of channels:
- Channels directly related to the user's active projects
- Channels involving their key collaborators and manager
- Any channel where the user is mentioned or tagged
- Anything flagged as urgent or requiring a decision

## Step-by-Step Instructions

### 1. Ask for Time Period (if not specified)
If the user didn't specify a timeframe, assume last 24 hours. If they say "this week" or "since Monday," adjust accordingly.

### 2. Search Slack for Recent Activity
Use `slack_search_public_and_private` with these queries (make separate calls):
- Keywords related to the user's active projects
- Messages from their key collaborators
- Anything that mentions the user directly (`@[username]`)
- `"action item" OR "assignment" OR "can you" OR "need from you"` — requests waiting on them

Set sort to most recent first. Use concise response format to minimize noise.

### 3. Read Relevant Channels
For any channels surfaced in search results, use `slack_read_channel` to grab the last 50 messages and get full context. This helps spot threads, replies, and decisions that may have been missed in search.

### 4. Synthesize into Three Categories

Organize findings into exactly three buckets:

**NEED YOUR ATTENTION**
- Action items assigned to the user (explicit asks, requests, @mentions)
- Questions waiting on their answer
- Decisions they need to make or input on
- Anything time-sensitive or blocking someone else

List each one with: who said it, what they need, and by when (if specified).

**KEY DECISIONS & UPDATES**
- Decisions that affect the user's projects
- New direction or policy changes from their manager or team leads
- Project milestones, launches, or pivots
- Anything that changes how they should approach their work

List briefly with context.

**FYI** (low priority, but useful)
- Announcements or celebrations (new hires, wins, launches)
- Good-to-know updates that don't require action
- Interesting context for situational awareness

## Output Format

```
SLACK DIGEST — Last 24 Hours

NEED YOUR ATTENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Item 1]
• From: [Name] in #[channel]
• What: [What they need from the user]
• By when: [Deadline, if any]

[Item 2]
• From: [Name] in #[channel]
• What: [What they need from the user]
• By when: [Deadline, if any]

KEY DECISIONS & UPDATES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Update 1]
[Update 2]
[Update 3 if relevant]

FYI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Brief line]
[Brief line]

NOTHING URGENT
[If no action items or key updates, explicitly state this]
```

## Rules

**Signal over noise:**
- Skip casual banter, memes, and off-topic chats
- Skip resolved discussions the user wasn't involved in
- Skip long threads unless they contain a decision or action for the user
- If a thread is 10+ messages long, read it and summarize the key point — don't dump it

**Specificity:**
- Always name the person who said it
- Always name the channel
- Always state exactly what they need — don't be vague
- Quote directly if it's a direct ask or decision

**Recency matters:**
- Messages from the last 2-4 hours get priority for "need your attention"
- Messages older than 24 hours should rarely appear unless they're ongoing decisions

**When in doubt:**
- Include it. Better to surface something and let the user skip it than hide something important
- But bias toward action items and decisions, not announcements

## Tips

- Manager and team lead posts are high-signal — read those threads
- "Can you..." addressed to the user is an action item even if it's in a side thread
- Decisions usually come with language like "we're going to", "we've decided to", "starting Monday", "new process is"
- Questions waiting on the user show up as replies to their past messages or direct @mentions

**Tool dependencies:** `slack_search_public_and_private`, `slack_read_channel`
