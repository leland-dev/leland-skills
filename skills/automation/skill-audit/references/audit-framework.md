# Audit Framework — 7 Criteria, Scoring, Status

Read this before scoring. Evaluate each skill from its actual file contents and a
scan of its scripts. Refresh the security/compliance expectations against the
latest authoritative sources (see SKILL.md Step 1) before applying them.

## The 7 criteria (verdict each: pass | warn | fail | unverified)

Use **`unverified`** when the evidence is insufficient to judge a criterion (e.g. a
standard's currency can't be confirmed, or a script's behaviour is unclear). An
`unverified` criterion is a human-review flag — never a silent pass. Score impact:
treat like `warn` (-4) and list it in the report. Never run a skill's scripts to
resolve uncertainty; analyse statically. If a script contains secrets, redact them
in all output.

1. **Safety** — No malicious code, injection risks, exploits, or dangerous
   execution patterns (unguarded `eval`, `exec`, `os.system`, `subprocess`/
   `child_process` with shell, `rm -rf`, dynamic execution of user input,
   hardcoded secrets). *Verify:* static scan of all scripts; manual review of any
   flagged usage.
2. **Anthropic Compliance** — Valid YAML frontmatter (`name`, `description`),
   correct `SKILL.md` naming, sensible triggers, progressive disclosure via
   external files. *Verify:* parse frontmatter; check naming/structure against
   current Anthropic skill-authoring docs.
3. **Completeness & Functionality** — Clear step-by-step process, defined output
   format, logical flow to a successful outcome. *Verify:* structural review.
4. **Usefulness & Use Cases** — Practical value, clear users and use cases.
   *Verify:* review stated use cases and value.
5. **Security** — `$ARGUMENTS` / user input treated as data, never instructions;
   no injection vulnerabilities; safe input handling (align with OWASP LLM
   guidance). *Verify:* trace argument/input flow.
6. **Adaptability** — Classify `Industry-agnostic` or `Domain-specific (<area>)`.
   Both are valid; verdict is `pass` with the classification noted.
7. **Legal Compliance** — No IP/privacy/regulatory issues; disclaimers where
   needed (financial, medical, legal). *Verify:* check attribution, privacy,
   required disclaimers.

## Quality score (0–100)

Start at 100. For each criterion: `warn` −4; `fail` −12. A **Safety, Security, or
Legal** `fail` is critical: −15 and counts toward `critical_issues`. Round to the
nearest integer. (Score colour in the report: ≥90 forest green, 75–89 rust, <75 red.)

## Status levels

- **`no_issues`** — all criteria pass, score ≥ 90, no change needed. Cleared for production.
- **`updated`** — a minor, low-risk correction was *applied* (only when the user
  approved changes). The applied edit is shown as the change diff.
- **`needs_action`** — a criterion fails, or a human decision is needed
  (disclaimer, frontmatter, rename, de-duplication), or a recommended change was
  *not* applied. Typically score < 90.

## SWOT

2–4 concise, file-grounded bullets each for Strengths, Weaknesses, Opportunities,
Threats.

## Change diffs

Represent every recommended/applied change as ordered diff lines:

- `ctx` — unchanged context line.
- `del` — removed line (renders red, `−` gutter).
- `add` — added line (renders green, `+` gutter).
- `inline` — one line mixing character-level edits using markers
  `{-deleted-}` (red strike) and `{+added+}` (green). Always show both the
  deletion and the addition. Quote real text from the file for `ctx`/`del`.

## Recommended action

For each skill, write a one-line `recommended_action`. For `needs_action` skills,
state the concrete fix and a clear recommendation. For clean skills, "No action
required — reviewed and cleared for production use."
