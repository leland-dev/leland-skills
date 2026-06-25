---
name: voice-dna
description: Analyze writing samples to extract and document the user's unique voice, tone, and style. Use when the user wants to capture their writing voice, update their voice profile, or when drafting anything that needs to sound like them. Invoke when asked to "write like me", "match my tone", "capture my voice", or "update my voice profile".
argument-hint: "[optional: paste writing samples here, or leave blank to use saved profile]"
tags:
  - "Marketing"
  - "Operations"
  - "Leland+"
---

# Voice DNA

Your job is to either (A) build or update the user's voice profile from writing samples, or (B) display the current profile so it can be applied to a draft.

## Step 1 — Determine Mode

If `$ARGUMENTS` contains writing samples (emails, Slack messages, etc.):
→ **Build/Update Mode**: analyze the samples and produce an updated voice profile, then save it to `voice-profile.md` in this skill's directory.

If `$ARGUMENTS` is empty or says "show" or "apply":
→ **Display Mode**: read the existing `voice-profile.md` and summarize the key rules so they can be applied to whatever draft is in context.

If no profile exists yet and no samples were provided:
→ Ask the user to paste 3–5 examples of their writing (emails, Slack messages, notes — anything they wrote themselves).

---

## Build/Update Mode — How to Analyze

Read every sample carefully. Extract patterns across these dimensions:

### Tone & Energy
- Is it warm, direct, casual, formal, enthusiastic, measured?
- How does it feel to read — like a friend, a colleague, a manager?

### Sentence Structure
- Short punchy sentences or longer flowing ones?
- Does he use fragments? Lists? Em-dashes?
- How does he open and close messages?

### Vocabulary
- Specific words or phrases he uses often
- Words he avoids
- Industry terms he uses naturally vs. ones he doesn't

### Persuasion Style
- How does he make an ask or pitch something?
- Does he lead with context or get to the point first?
- How does he handle objections or pushback?

### Formatting Habits
- Does he use bullet points, bold text, line breaks?
- Long paragraphs or short ones?
- Does he use emojis, and if so how?

---

## Output Format (Build Mode)

After analyzing, write a `voice-profile.md` file to this skill's directory with this structure:

```
# Voice Profile
Last updated: [date]

## Tone
[2-3 sentences describing overall feel]

## Sentence Style
[bullet points with specific patterns]

## Signature Phrases / Vocabulary
[list of words/phrases he uses]

## What to Avoid
[list of things that would sound off]

## How He Makes an Ask
[describe his persuasion pattern]

## Formatting Defaults
[bullet points, line lengths, emoji use, etc.]

## Reference Samples
[paste 1-2 of the strongest example sentences that capture his voice]
```

Then confirm: "Voice profile saved. From now on I'll write in your voice automatically when drafting."

---

## Display Mode

Read `voice-profile.md` and output a short summary of the key rules. Apply them to whatever draft or task is currently being worked on.

If no profile file exists, say: "No voice profile found yet. Run `/voice-dna` and paste some writing samples to get started."
