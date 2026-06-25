---
name: share-skills
description: >
  Package, clean, and generalize agent skills for sharing with others. Use this skill
  whenever the user says "share my skills", "package a skill for a coworker", "prepare
  skills for sharing", "clean up a skill to share", or any variation of wanting to export
  one or more installed skills in a shareable format. This skill handles the full pipeline:
  discovering what's installed, packaging all skills as zips regardless of file count,
  outputting them to a sharing folder, providing install commands for the
  recipient, removing tool-specific language, and generalizing any user-specific references.
tags:
  - "AI Tools"
  - "Leland+"
---

# Share Skills

Package installed agent skills into shareable files, clean them for broad use, and provide
recipients with ready-to-paste install commands.

---

## Step 1: Discover Installed Skills

### 1a: Terminal skills (CLI)

Check both CLI skills directories:

```bash
ls ~/.claude/skills/ 2>/dev/null && echo "---" && ls ~/.agents/skills/ 2>/dev/null
```

For each skill found, count its files:

```bash
for dir in ~/.claude/skills/*/ ~/.agents/skills/*/; do
  [ -d "$dir" ] || continue
  count=$(find "$dir" -type f | wc -l)
  echo "$count $dir"
done
```

### 1b: Claude desktop (Cowork) skills

The Claude desktop app stores skills in session-specific directories under `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/`. They are plain SKILL.md directories — not encrypted, no special handling needed.

Find the most recently modified session and list unique skills:

```bash
DESKTOP_BASE=~/Library/Application\ Support/Claude/local-agent-mode-sessions/skills-plugin
LATEST_SESSION=$(ls -t "$DESKTOP_BASE" 2>/dev/null | head -1)
find "$DESKTOP_BASE/$LATEST_SESSION" -name "SKILL.md" 2>/dev/null \
  | sed 's|.*/skills/||' | sed 's|/SKILL.md||' | sort -u
```

If the same skill name appears in multiple sub-sessions, pick the most recently modified copy:

```bash
find "$DESKTOP_BASE/$LATEST_SESSION" -name "SKILL.md" -print0 2>/dev/null \
  | xargs -0 ls -t \
  | awk -F'/skills/' '{print $2}' | awk -F'/' '{print $1}' \
  | awk '!seen[$0]++'
```

### 1c: Present the full list

Present the user with a combined table:

| Skill | Source | Files | Output folder |
|---|---|---|---|
| skill-name | ~/.claude/skills/ | 3 | skills-sharing/ |
| skill-name | ~/.agents/skills/ | 1 | skills-sharing/ |
| skill-name | Desktop (Cowork) | 2 | skills-sharing/desktop-skills/ |

Note: a skill may appear in both terminal and desktop locations (e.g., `humanize`). If so, package both — the desktop version may differ. Label duplicates clearly in the table.

Ask the user which skills to package, or proceed with all if they said "all".

---

## Step 2: Package Skills

**Output directories:**
```bash
mkdir -p ~/Desktop/skills-sharing
mkdir -p ~/Desktop/skills-sharing/desktop-skills
```

Terminal skills → `~/Desktop/skills-sharing/`
Desktop (Cowork) skills → `~/Desktop/skills-sharing/desktop-skills/`

### All skills → zip (regardless of file count)

```bash
# For skills in ~/.claude/skills/:
cd ~/.claude/skills && zip -r ~/Desktop/skills-sharing/{skill-name}-skill.zip {skill-name}/

# For skills in ~/.agents/skills/:
cd ~/.agents/skills && zip -r ~/Desktop/skills-sharing/{skill-name}-skill.zip {skill-name}/

# For desktop (Cowork) skills — find the skill directory in the most recent session,
# then zip it to the desktop-skills subfolder:
DESKTOP_BASE=~/Library/Application\ Support/Claude/local-agent-mode-sessions/skills-plugin
LATEST_SESSION=$(ls -t "$DESKTOP_BASE" 2>/dev/null | head -1)
SKILL_DIR=$(find "$DESKTOP_BASE/$LATEST_SESSION" -type d -name "{skill-name}" | xargs ls -td 2>/dev/null | head -1)
cd "$(dirname "$SKILL_DIR")" && zip -r ~/Desktop/skills-sharing/desktop-skills/{skill-name}-skill.zip {skill-name}/
```

Confirm files were created with:
```bash
ls -lh ~/Desktop/skills-sharing/
ls -lh ~/Desktop/skills-sharing/desktop-skills/
```

---

## Step 3: Descriptions + Install Commands

For each packaged skill:

### 3a: Write a one-sentence description

Read the skill's `SKILL.md` (or the packaged `.md` file) and write a single sentence
describing what the skill does. Focus on the action and outcome — not the trigger words.

Good format per entry:

```
"{skill-name}" — [one-sentence description].
To install, run this in your terminal after downloading the file:unzip ~/Downloads/{skill-name}-skill.zip -d ~/.claude/skills/{skill-name}/
```

Example:
```
"humanize-writing" — Rewrites drafts to remove AI tells, hedging language, and vague references, applying the correct tone register per writing type.
To install, run this in your terminal after downloading the file:unzip ~/Downloads/humanize-writing-skill.zip -d ~/.claude/skills/humanize-writing/
```

Note: All skills are packaged as zips (see Step 2). Install commands always use `unzip`, never `cp`.

Save all entries together into `skills-index.txt` in the sharing folder. Each skill gets
its two lines (description + install command) followed by a blank line separator.

If `skills-index.txt` already exists, update the relevant entries rather than appending
duplicates. After all skills are processed, the file should be alphabetically sorted by
skill name.

### 3b: Install commands

Install commands are saved alongside each description in `skills-index.txt` — point the
user there rather than repeating them inline.

---

## Step 4: Clean for Tool-Agnosticism

Unzip each skill to a temp location, review the SKILL.md, replace any tool-specific
language with generic equivalents.

**Common substitutions:**

| Find | Replace with |
|---|---|
| "Claude" (as the agent) | "the AI agent" |
| "Claude Code" | "the AI agent" |
| `CLAUDE.md` | "the agent config file (e.g., `CLAUDE.md`, `AGENTS.md`)" |
| `~/.claude/skills/` | "the agent's skills directory" |
| `~/.claude/projects/.../memory/` | "the agent's memory directory" |
| "Claude's memory" | "the agent's memory" |
| "How to Get More Out of Claude" | "How to Get More Out of Your AI Agent" |

---

## Step 5: Generalize User-Specific References

Review each file for anything tied to a specific person, company, or environment.
Generalize rather than templatize — use natural language descriptions instead of
`[PLACEHOLDER]` brackets where possible.

**Common patterns to catch:**

| Type | Example | Generalized |
|---|---|---|
| Person's name | "Triage Weston's inbox" | "Triage the user's inbox" |
| Name possessive | "Weston's voice guide" | "the user's voice guide" |
| Pronoun (gendered) | "responding on his behalf" | "responding on their behalf" |
| Email signature | `"High Regards, Weston H."` | "the user's standard sign-off" |
| Hardcoded file path | `/Users/westonhansen/Desktop/...` | Glob search pattern |
| Hardcoded filename | `weston_hansen_voice_guide.md` | `**/*voice*guide*.md` |
| Company domain | `@joinleland.com` | "the user's organization domain" |
| Company name in copy | "Leland-branded pages" | "company-branded pages" |
| Company URLs | `https://www.joinleland.com/legal/terms` | "company terms of service URL" |
| Hardcoded API/account IDs | `22467258` | descriptive label (e.g., `YOUR_HUBSPOT_ID`) |
| Internal program names | "AI Builder Program" | remove or generalize |
| Company-specific domain examples | "coach-client dynamics" | "service-client dynamics" |

**Checklist before finishing:**
- [ ] No person's name appears in the skill body or description
- [ ] No hardcoded file paths pointing to a specific machine or user folder
- [ ] No company-specific URLs, IDs, or brand names (unless the skill is intentionally company-specific, e.g., a design system skill)
- [ ] No gendered pronouns tied to a named person
- [ ] Tool references (Claude, Codex, etc.) replaced with "the AI agent" or "your agent"

---

## Step 6: Flag Intentionally Specific Skills

Some skills are inherently tied to a company or brand (e.g., a design system skill, a
page builder for a specific platform). Flag these to the user before generalizing:

> "This skill references [company/brand] throughout by design — it's a company-specific
> skill. Do you want to generalize it for broad sharing, or keep it as-is for internal use?"

If keeping as-is, skip Step 5 for that file.

---

## Output Summary

After completing all steps, present:

1. A list of all files in `~/Desktop/skills-sharing/` (terminal skills)
2. A list of all files in `~/Desktop/skills-sharing/desktop-skills/` (Cowork skills)
3. The contents of `skills-index.txt` — one description line per skill, with source noted
4. The install commands for each (all use `unzip`)
5. Any skills that were flagged as intentionally specific and left unchanged

Note install path differs by source:
- Terminal skills: `unzip ~/Downloads/{skill-name}-skill.zip -d ~/.claude/skills/{skill-name}/`
- Desktop skills: `unzip ~/Downloads/{skill-name}-skill.zip -d ~/.claude/skills/{skill-name}/` (same install, different origin)
