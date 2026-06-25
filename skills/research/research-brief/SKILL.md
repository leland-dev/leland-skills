---
name: research-brief
description: Fast research synthesis — get up to speed on any topic, tool, person, or company in 5 minutes. Use this skill whenever the user says "research brief on", "get me up to speed on", "what do I need to know about", "quick research on", "who is [person]", "what is [company/tool]", "look into X for me", "brief me on", "give me the essentials on", "I have a call with [person]", or "I'm meeting with [company]". Also trigger when the user mentions they're unfamiliar with something and need context before a meeting or decision.
tags:
  - "Operations"
  - "Leland+"
---

# Research Brief

Gather current information and synthesize it into a tight, scannable 1-page brief the user can read in 3 minutes.

## Instructions

1. **Parse the request.** What is the user researching? (person, company, tool, trend, concept, etc.)

2. **Search for current information.** Use WebSearch with 2-3 targeted queries:
   - General query about the topic
   - If a person/company: their recent news, funding, announcements
   - If a tool: pricing, users, key features, recent developments
   - If a trend: latest coverage, adoption, implications

3. **Fetch key sources.** Use WebFetch on 2-3 of the most relevant search results to get deeper context and specifics (numbers, dates, quotes).

4. **Synthesize into a brief.** Write a tight markdown brief (~300-500 words) with these sections:
   - **What it is** (2-3 sentences max): essentials only
   - **Why it matters** (1-2 sentences): connection to the user's current work or the specific context of the request
   - **Key facts & numbers** (3-4 bullets): dates, pricing, users, funding, features, recent moves
   - **What to watch** (1-2 bullets): open questions, upcoming changes, risks, opportunities
   - **Sources** (inline citations or list): where the info came from

5. **Save output.** Save the markdown brief to the user's notes folder as `[topic]-brief.md`. Show them the brief before saving — confirm it has what they need.

## Tone & Style

- **Specific.** Names, numbers, dates — never vague.
- **Opinionated.** "This matters because..." or "Watch for..." — state relevance directly.
- **Scannable.** Written for someone skimming in 3 minutes before a meeting or decision.
- **Not comprehensive.** Short and useful beats long and thorough.

## Example Output Structure

```markdown
# Research Brief: [Topic/Person/Company]

## What It Is

[2-3 sentence essentials. Who founded it? What does it do? When did it launch?]

## Why It Matters

[Connection to the user's current work, context of the ask, or reason this is relevant now.]

## Key Facts

- [Fact with number/date]
- [Fact with number/date]
- [Fact with number/date]
- [Recent development or milestone]

## What to Watch

- [Open question or upcoming change]
- [Risk, opportunity, or competitive move]

## Sources

- [Source 1](url)
- [Source 2](url)
```

## Notes

- Always search for current information (within the last 6 months when possible).
- If the user has a specific meeting or decision context, lean into why that matters for them.
- If the topic is a tool or platform, prioritize pricing, user count, and recent product changes.
- If the topic is a person, prioritize recent moves, current role, and notable projects.
- If the user provides no additional context, ask one question: "Is there a specific angle you want me to focus on?"
