---
name: personalization-engine
description: Scale email personalization using signal categories and variable templates. Turn generic emails into specific ones by mapping recipient signals to message variations. Use when you need to personalize outreach at volume.
argument-hint: "[describe the email template and what you know about the recipients]"
tags:
  - "Sales"
  - "Marketing"
  - "Bundle 2"
  - "Leland+"
---

# Personalization Engine

Turn a generic email template into a personalized one by mapping recipient signals to message variables.

## Signal Categories

### Demographic Signals
- Job title, seniority, function
- Company size, industry, location

### Behavioral Signals
- Applied for a specific program
- Visited pricing page
- Opened previous email
- Previously enrolled / alumni

### Situational Signals
- Career stage (switching careers, upskilling, re-entering workforce)
- Timeline urgency (cohort starting soon)
- Prior interaction (ghosted, said "later", active thread)

### Intent Signals
- Specific program interest
- Price sensitivity signals
- Questions asked previously

## Step 1 — Identify Available Signals

From `$ARGUMENTS`, list what's known about the recipient or recipient segment. Map each piece of info to a signal category above.

## Step 2 — Build Variable Templates

For each signal, create a personalization variable:

```
{{program_hook}} =
  - If data/analytics: "breaking into data analytics"
  - If software eng: "landing a software engineering role"
  - If product: "transitioning into product management"

{{urgency_line}} =
  - If cohort < 2 weeks: "The next cohort starts [date] — spots are limited."
  - If cohort > 2 weeks: "The [program] cohort kicks off [month]."
  - If no cohort: "Programs run on a rolling basis."
```

## Step 3 — Apply to Template

Take the base email from `$ARGUMENTS` and insert variables at natural points. Show the filled-in version for 2-3 example recipient profiles.

## Output

```
## Variable Map
| Variable | Condition | Value |
|----------|-----------|-------|
| {{program_hook}} | data program | "breaking into data analytics" |
| ... | | |

## Example: Recipient Profile A ([describe])
[full personalized email]

## Example: Recipient Profile B ([describe])
[full personalized email]
```
