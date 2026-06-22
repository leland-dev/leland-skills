# Leland Skills

Canonical source of truth for every AI skill Leland ships. Free and paid, all in one versioned place.

This repo **stores** the skills. **Where they show up** is a separate layer driven by each skill's `tier` tag:

- **Free skills** sync to a public marketplace repo. One-command install. The lead magnet.
- **Paid skills** are delivered through Leland+ / the course portal, behind login.
- **All skills** can render as browsable pages on lelandcourses.com, which reads from this repo.

A skill never moves between surfaces by being copied around. Its metadata decides where it goes.

## Structure

`skills/` is organized **by function**. Industry is a **tag**, not a folder, so any skill can be sliced by either dimension.

| Folder | What lives here |
|--------|-----------------|
| `communication` | Email, Slack, writing in your voice, outreach |
| `data-analysis` | Analyzing data, dashboards, reporting |
| `automation` | Workflows, multi-step automations, agents |
| `documents` | Decks, docs, sheets, PDFs |
| `research` | Gathering, synthesizing, fact-checking |
| `productivity` | Planning, task management, personal systems |

Every skill is one folder containing a `SKILL.md`. See [`skills/_template/`](skills/_template/) for the standard and [`METADATA.md`](METADATA.md) for the frontmatter schema.

## Install (once a public mirror is published)

```bash
/plugin marketplace add leland-dev/leland-skills-public
/plugin install <plugin-name>@leland-skills
```

## Adding a skill

See [`CONTRIBUTING.md`](CONTRIBUTING.md). One skill = one PR.

## Status

Private canonical store. The public mirror and the lelandcourses.com display pages are downstream of this repo. Licensing is decided per surface at publish time, not here.
