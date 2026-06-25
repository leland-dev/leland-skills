---
name: email-manager
description: >
  Triage the user's inbox and draft replies in their voice. Use this skill whenever the user says "check my email", "triage my inbox", "what emails do I need to reply to", "draft replies to my emails", "what's in my inbox", or anything that involves reading Gmail and responding on their behalf. Also trigger when the user says "do my emails", "handle my inbox", or pastes an email and asks how to respond. This skill pulls unread emails from the last 24 hours, sorts by urgency, skips noise, and produces ready-to-review reply drafts — never sends anything without the user's approval.
tags:
  - "Operations"
  - "Leland+"
  - "AIBP"
  - "L1S2"
---

# Email Manager

Before drafting a single word, read the user's voice guide. Use Glob to search for `**/*voice*guide*.md` in the workspace if needed. Apply its rules to every draft.

The user's email register: "Hey [Name]!" opener, short-medium sentences, numbered lists for 2+ items, zero em-dashes, closes with the user's standard sign-off.

---

## Step 1: Pull Emails

Use the Gmail MCP to fetch all unread emails from the last 24 hours. If the tool supports it, pull the full thread for each — context matters for replies.

---

## Step 2: Sort Into Buckets

Classify every email before doing anything else. Do not draft or flag until every email has a bucket.

### SKIP — no draft, no mention, complete silence
- Newsletters and digests (Substack, Morning Brew, product updates, any "unsubscribe" footer present)
- Automated system notifications (GitHub, Notion, HubSpot alerts, app pings, no-reply senders)
- Cold outreach and spam (unknown senders pitching products, services, or partnerships with no prior relationship)
- Marketing emails of any kind

### FLAG — surface it, no draft
- Meeting requests (calendar invites or emails asking to schedule time) — show the request, note the proposed time, ask the user what they want to do
- Emails where the user is CC'd — list these in a separate "CC'd (no action needed)" section, no drafts

### DRAFT — write a reply
- Direct questions from real people
- Decisions needed from the user
- Relationship emails (check-ins, thank-yous, follow-ups from people he knows)
- Time-sensitive items: any email mentioning a deadline, date, or "by EOD / this week" from a known sender
- Any email from the user's organization domain when a reply is clearly expected

---

## Step 3: Urgency Ranking

Within the DRAFT bucket, order by urgency:

**URGENT** — surface these first, bold the sender name:
- Time-sensitive: mentions a specific deadline, date, or time pressure AND is from a real person (not automated)
- From @joinleland.com when a reply is clearly expected
- Any email where missing a response today has a concrete consequence

**STANDARD** — everything else, numbered sequentially below urgent items

If nothing is urgent, say so plainly. Don't manufacture urgency.

---

## Step 4: Draft Replies

For each email in the DRAFT bucket:

**Format each reply block like this:**

---
**[NUMBER]. From: [Sender Name] — [Subject line]**
*Received: [time or date]*
*Why I'm drafting this: [one sentence — what makes this reply-worthy]*

**Draft:**
> [the reply, written in the user's voice per the humanize-writing skill]

**Assumed:** [if you made a decision or filled in a gap, note exactly what you assumed and why]
**Need from the user:** [if you're missing something, state exactly what — be specific, not vague]

---

### Decision-making rules
- If you can make a reasonable decision based on context, make it and note the assumption. Don't ask the user to fill in something you can figure out.
- If the email asks for a date or time, flag it rather than draft a reply — the user needs to check their calendar.
- If the email is from a coach or external partner and the question is factual/operational, draft a confident answer and note what you assumed.
- If the email contains a complaint or sensitive issue, draft a reply but flag it explicitly: "**Flag: sensitive — review carefully before sending.**"

### Tone rules (from humanize-writing)
- Open with "Hey [First Name]!"
- One thought per paragraph
- Number multi-item lists
- No em-dashes
- State facts, not pleasantries
- Close with the user's standard sign-off
- Name specific things when giving praise or acknowledgment
- Zero hedging. "I'll have this to you by Thursday" not "I might be able to get this to you sometime this week."

---

## Step 5: Output Format

Present results in this exact order:

### URGENT REPLIES NEEDED
[numbered list of urgent drafts, each in the reply block format above]

### REPLIES NEEDED
[numbered list of standard drafts, same format]

### MEETING REQUESTS — YOUR CALL
[for each: sender, what they're asking, proposed time if given, one line on context]

### CC'D — NO ACTION NEEDED
[sender, subject, one-sentence summary of what the thread is about — just enough to know you don't need to act]

### SKIPPED
[single line: "Skipped X emails: [Y newsletters, Z automated notifications, W cold outreach]." No details unless the user asks.]

---

## Step 6: Final Check Before Delivering

- Did you read and apply the humanize-writing skill to every draft?
- Does every draft open with "Hey [First Name]!" ?
- Are there any em-dashes anywhere? Delete them.
- Does every draft close with the user's standard sign-off?
- Are all assumptions explicitly noted?
- Is every missing-info flag specific? ("I need to know your answer to their question about pricing" not "more info needed")
- Are urgent emails actually time-sensitive with a real deadline — or did you inflate urgency?
- Did you skip every newsletter, notification, and cold email without mentioning it in DRAFT or FLAG?

**Never send anything. Every output is a draft for the user's review.**
