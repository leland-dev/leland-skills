---
name: skill-name-here
description: State what this skill does AND when to use it in 1-3 sentences. This is the primary trigger for the skill, so be specific and a little pushy about the contexts that should invoke it. Name the tasks, phrases, file types, and situations. Fold all "when to use" detail in here, never in a separate field or the body.
tier: free
industry: general
level: general
status: draft
# allowed-tools: Read Grep Bash(git *)
# disable-model-invocation: true   # uncomment for side-effectful, manual-only skills
---

# Skill name

One sentence on what this skill does. (Triggering is driven by the `description` above, not this body. Keep this body focused on *how*.)

## Instructions

Write steps in the imperative ("Read the file", "Generate the report"). Explain *why* each step matters so the model can adapt instead of following blindly. Avoid rigid ALWAYS/NEVER unless something genuinely breaks without it.

1. ...
2. ...
3. ...

## Notes

- Keep this file under ~500 lines. Offload heavy docs to `references/`, output templates and assets to `assets/`, and executable code to `scripts/`. Point to those files explicitly from here so the model knows when to load them.
