---
name: persona-development
description: Build a detailed buyer persona with pain hierarchies, motivations, objections, and language patterns. Use when you want Claude to deeply understand a specific type of customer before writing for or about them.
argument-hint: "[describe the customer type you want to build a persona for]"
tags:
  - "Sales"
  - "Marketing"
  - "Bundle 1"
  - "Leland+"
---

# Persona Development

Build an 8-component buyer persona that Claude can reference when writing, drafting, or strategizing.

## The 8 Components

### 1. Identity
Who is this person? Role, background, life stage, goals.

### 2. Primary Pain
The #1 problem they're trying to solve. In their words, not yours.

### 3. Pain Hierarchy
Secondary and tertiary pains — what else keeps them up at night?

### 4. Motivations
What do they actually want? (Career change, income, status, stability, flexibility?)

### 5. Objections
What stops them from buying? Price, timing, credibility, fear of failure, uncertainty?

### 6. Language Patterns
Words and phrases they use. How do they describe their own problem? What language signals are they in market?

### 7. Where They Are in the Journey
Awareness stage: unaware → problem aware → solution aware → product aware → most aware.

### 8. What a Win Looks Like
What does success look like to them 6 months after buying?

## Step 1 — Build the Persona

From `$ARGUMENTS`, develop each component. Use specific, concrete language — not "career growth" but "wants to get out of [current job] and into [target role] within 12 months."

If data or examples are provided, use them. If not, reason from what's known about this audience type.

## Output Format

```
# Persona: [Name/Type]

## Identity
[who they are]

## Primary Pain
"[in their voice]"

## Pain Hierarchy
1. [primary pain]
2. [secondary pain]
3. [tertiary pain]

## Motivations
- [motivation 1]
- [motivation 2]

## Objections
| Objection | Underlying Fear | Best Response |
|-----------|----------------|---------------|
| "Too expensive" | Risk of wasting money | [response] |
| "Not sure it'll work for me" | Fear of failure | [response] |

## Their Language
Words they use: [list]
Words they don't use: [list]
How they describe their problem: "[example phrase]"

## Journey Stage
[where they are + what they need at this stage]

## What a Win Looks Like
"[success in their voice]"
```
