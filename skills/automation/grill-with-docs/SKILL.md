---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
disable-model-invocation: true
tags:
  - "Product & R&D"
  - "Operations"
  - "automation"
  - "productivity"
  - "External"
---

# Grill With Docs

Combines adversarial Q&A (from `/grilling`) with live documentation: as decisions are made during the session, Architecture Decision Records (ADRs) and glossary entries are created in real time.

## Companion skills

- **`/grilling`** — runs the adversarial interview (required; see inline process below if unavailable)
- **`/domain-modeling`** — builds the shared language/glossary as decisions solidify

## Process

### 1. Start the grilling session

Follow the same adversarial Q&A process as `/grill-me`:

- Get a 2–3 sentence description of the plan or design
- Surface the core assumptions (3–5)
- Run adversarial questioning per assumption: failure modes, evidence, alternatives, stakeholders, edge cases

### 2. Capture decisions as ADRs (as you go)

Whenever the user commits to a decision during questioning, immediately draft an ADR:

```
# ADR-NNN: [Short title]

## Status
Accepted

## Context
[What situation or question prompted this decision]

## Decision
[What was decided]

## Consequences
[What this enables, what it closes off, what risks remain]
```

Save each ADR to `docs/decisions/ADR-NNN-title.md` (or ask for the target path if a project root isn't obvious).

### 3. Update the domain glossary

After each major decision block, use `/domain-modeling` to capture any new terms, entities, or relationships that emerged. Add them to `docs/glossary.md` (create if missing).

### 4. Summarize at the end

- Top 3 risks uncovered
- ADRs written (list them)
- Glossary terms added
- Recommended next actions
