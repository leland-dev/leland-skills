# Skill metadata schema

Every skill's `SKILL.md` opens with YAML frontmatter. **Standard fields** are read by Claude Code. **Leland fields** drive gating, the public sync, and the lelandcourses.com display pages.

## Standard fields (read by Claude Code)

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | kebab-case, matches the folder name. Also becomes the `/command`. |
| `description` | yes | What it does **and** when to use it. This is the auto-invocation trigger, so be specific and a little pushy about the contexts that should fire it (name tasks, phrases, file types). Claude tends to under-trigger skills, so a passive description means it won't get used. Put *all* "when to use" detail here, not in a separate field or the body. ~1,536 char cap. |
| `allowed-tools` | optional | Space-separated pre-approved tools, e.g. `Read Grep Bash(git *)`. |
| `disable-model-invocation` | optional | `true` for side-effectful skills that should be manual-only. |

## Leland fields (drive our pipeline)

| Field | Values | Drives |
|-------|--------|--------|
| `tier` | `free` \| `paid` | Public mirror vs. gated delivery. **The gate is here, never in GitHub.** |
| `industry` | `general`, `marketing`, `sales`, `ops`, `finance`, `hr`, `legal`, ... | Industry slicing on display pages. |
| `level` | `general`, `L1`–`L5` | Maps to the AI Builder program. |
| `status` | `draft` \| `published` | Only `published` skills sync out. |

## Example

```yaml
---
name: write-in-your-voice
description: Drafts email and Slack messages in the user's own voice. Use when the user wants to write a message, reply, or announcement that sounds like them.
tier: free
industry: general
level: L1
status: draft
---
```
