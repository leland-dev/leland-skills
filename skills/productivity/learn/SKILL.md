---
name: learn
description: Session retrospective — audit what went well/wrong, propose documentation updates, and give direct feedback on how the user can work with you more efficiently. Use after long or complex sessions.
tags:
  - "AI Tools"
  - "Operations"
  - "Leland+"
---

Learn from this session. Extract what went well, what went wrong, and update documentation so future sessions are better. Also give direct feedback on how the user can work with you more efficiently.

## Instructions

Parse $ARGUMENTS for optional focus area (e.g., `mistakes`, `efficiency`, `workflow`). If empty, do a full review.

### Step 1: Session Audit

Review the current conversation and identify:

**What went wrong:**
- Errors, dead ends, retries, or wasted steps
- Misunderstandings between user and AI Agent (unclear prompts, wrong assumptions)
- Tools that failed or returned unexpected results
- Approaches that were abandoned partway through

**What went well:**
- Efficient patterns (good use of parallel agents, clear prompts, smart sequencing)
- Decisions that saved time or tokens
- Workflows that should be repeated

**What was learned:**
- New facts about systems, data, processes, or tools
- Corrections to previous assumptions
- Patterns that should be codified

Summarize this back concisely before proceeding.

### Step 2: Documentation Updates

Based on the session audit, identify which files should be updated. Check each category:

**Memory files** (agent memory directory):
- New memories to save (feedback, project, reference types)
- Existing memories that are now outdated or wrong

**Skill files** (installed skills directory):
- Skills that were used and need refinement based on what happened
- Missing instructions that caused errors or extra steps
- New edge cases to handle

**Agent config file** (e.g., `CLAUDE.md`, `AGENTS.md`, or equivalent project-level config):
- New conventions or preferences discovered
- Corrections to existing instructions

For each proposed change, display it clearly:

## Proposed Documentation Updates

### 1. {file path}
**Action:** {Create / Update / Delete}
**What changes:** {description}
**Why:** {what happened in this session that motivates this}

> {Show the specific content to add/change/remove}

**Do NOT write any changes until the user approves.** Ask: "Want me to apply all of these, some of them, or none?"

### Step 3: Feedback for the User

Give direct, specific feedback on how the user can work with Claude more efficiently. Be honest — this is a coaching moment, not a compliment session.

Structure:

## How to Get More Out of Your AI Agent

### Token Efficiency
{Were prompts unnecessarily long? Could context have been set once instead of repeated? Were there unnecessary back-and-forth cycles that a clearer initial prompt would have avoided?}

### Prompt Patterns
{What worked: e.g., "When you gave me the exact format you wanted, I nailed it first try."}
{What to try: e.g., "Next time you need X, try prompting with Y — it'll save a round trip."}

### Workflow Suggestions
{Could more work have been parallelized? Were there manual steps that could be skills? Did the user do something Claude should have done, or vice versa?}

### One Thing to Try Next Time
{The single highest-leverage change to how we work together.}

Be specific to THIS session. Reference actual moments. Don't give generic productivity advice.

### Step 4: Apply Approved Changes

After the user approves (all, some, or none):
- Write the approved memory files
- Edit the approved skill files
- Update the agent config file if approved
- Confirm what was updated

## Notes

- This skill is most valuable after long or complex sessions where things didn't go smoothly
- The documentation updates are the durable output — they compound across future sessions
- Be honest in the feedback section. The user explicitly asked for this. Don't soften it.
- If the session went perfectly and there's nothing to learn, say so — don't manufacture feedback
- Never update documentation without showing the user first and getting approval
- When updating memory files, follow the memory system format (frontmatter with name, description, type) and store them in your agent's memory directory so they are available across all projects
