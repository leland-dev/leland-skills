# Adding a skill

1. Copy [`skills/_template/`](skills/_template/) into the right function folder. Rename it to your skill's kebab-case name.
2. **Folder name = skill name = the `/command`.** Keep it short and verb-led: `write-case-study`, `analyze-revenue`, `build-dashboard`.
3. Fill in the `SKILL.md` frontmatter per [`METADATA.md`](METADATA.md). `tier`, `industry`, and `level` are required for our pipeline.
4. Keep `SKILL.md` under ~500 lines. Offload heavy detail to `reference.md`, example outputs to `examples.md`, and any code to `scripts/`.
5. **One skill = one PR.** Don't batch unrelated skills.

## Naming rules

- kebab-case, verb-first: `build-`, `write-`, `analyze-`, `automate-`.
- No level or industry in the name. That lives in metadata.

## Before you open the PR

- `description` clearly states **what** and **when**.
- `tier` is correct. This controls who sees the skill.
- `status: draft` until it's reviewed. Reviewer flips it to `published`.
