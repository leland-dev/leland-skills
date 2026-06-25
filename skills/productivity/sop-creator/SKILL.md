---
name: sop-creator
description: Create a clear, scannable standard operating procedure (SOP), runbook, or checklist from a process description. Use when documenting how something works, creating a handoff doc, or turning a brain dump into a repeatable process someone else can follow.
argument-hint: "[describe the process you want to document]"
tags:
  - "Operations"
  - "Leland+"
---

# SOP Creator

Turn a process description into a clean, scannable SOP that people actually follow.

## Step 1 — Understand the Process

Read `$ARGUMENTS`. If the description is vague or missing key steps, ask up to 3 clarifying questions:
- Who performs this process and how often?
- What does "done" look like — what's the output or end state?
- Are there any tools, systems, or accounts involved?

## Step 2 — Build the SOP

Structure it as follows:

### Header
- **Process name**
- **Owner** (who is responsible)
- **Frequency** (daily / weekly / per deal / etc.)
- **Tools required**
- **Last updated**

### Purpose
One sentence. What problem does this process solve?

### Prerequisites
What needs to be true or ready before starting?

### Steps
Numbered, imperative ("Go to...", "Click...", "Enter..."). Each step should be:
- One action only
- Specific enough that someone new could follow it
- Include screenshots or examples if provided

Use sub-bullets for optional variations or important notes. Bold critical warnings.

### Verification
How do you know it worked? What does success look like?

### Troubleshooting
2-3 most common failure modes and how to fix them.

## Output Format

```
# [Process Name]
**Owner:** [name/role] | **Frequency:** [how often] | **Tools:** [list] | **Updated:** [date]

## Purpose
[one sentence]

## Prerequisites
- [ ] [thing that must be ready]

## Steps
1. [Action]
   - Note: [important detail]
2. [Action]
3. ...

## Verification
[How to confirm it worked]

## Troubleshooting
| Problem | Fix |
|---------|-----|
| [issue] | [solution] |
```

Keep language plain. No jargon. Write for someone doing this for the first time.
