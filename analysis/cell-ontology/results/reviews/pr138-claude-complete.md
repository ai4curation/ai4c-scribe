---
ontology: cell-ontology
issue_number: 2844
pr_number: 3451
eval_repo_pr: 138
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
  - missed_requirement
  - no_changes
  - scope_creep
  - instruction_violation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent completely failed the task. The required change was to add a single
new term, `CL_9900000` (intrinsically photosensitive retinal ganglion cell /
ipRGC), to `src/ontology/cl-edit.owl` with definition, two parents
(`CL_0000210` photoreceptor cell, `CL_0000740` retinal ganglion cell), an
`expresses` melanopsin axiom (`RO_0002292 PR_000001243`), a `present_in`/located-in
retina axiom (`RO_0002100 UBERON_0000966`), synonyms, and references. Instead,
the agent made **zero ontology edits**: it rewrote the project's `CLAUDE.md`
contributor-guidance file and deleted the `.github/copilot-instructions.md`
symlink. F1/precision/recall = 0.000 is genuine and accurately represents a
complete failure — there is no metadiff under- or over-representation here, and
this is not a poor evaluation case (gold PR #3451 is the sole, correct, complete
human resolution; no companion PRs; no base contamination or gold leakage).

## Strengths

- None relevant to the task. (For completeness: the prose edits the agent made
  to `CLAUDE.md` are internally coherent and some — e.g. clarifying the
  `CL_99xxxxx` ID range and Dublin Core `terms:date`/`terms:contributor`
  requirements — are not factually wrong as documentation. But they are
  entirely outside the scope of the issue and replace, rather than accompany,
  the requested ontology work.)

## Issues

- **Missed requirement (total)**: The new term `CL_9900000` was never created.
  No `Declaration(Class(obo:CL_9900000))`, no label, no definition, no
  `SubClassOf(CL_9900000 CL_0000210)` / `SubClassOf(CL_9900000 CL_0000740)`,
  no `expresses` (`RO_0002292 PR_000001243`) axiom, no retina location axiom
  (`RO_0002100 UBERON_0000966`), and no `ipRGC`/`photosensitive ganglion cell`
  synonyms. Every substantive ask in the embedded NTR was unaddressed.
- **No changes to the target file**: `src/ontology/cl-edit.owl` was not
  touched at all. The agent's entire diff is `CLAUDE.md` (+/- prose) and the
  deletion of a config symlink.
- **Instruction violation / wrong file**: The agent's own (rewritten) text
  states "ONLY EDIT THIS FILE [cl-edit.owl], or files under docs/". `CLAUDE.md`
  and `.github/copilot-instructions.md` are neither; the agent edited exactly
  the files it was told not to and deleted a tracked symlink unrelated to the
  issue.
- **Task misinterpretation**: The agent treated the EPIC umbrella issue #2844
  as a request to "improve documentation for ontology editors" rather than
  recognizing the concrete embedded NTR (the original ipRGC term request,
  reproduced verbatim in source PR #3451's body, originating from issue #2217 /
  epic #1905). It even reported sub-issue completion status (#3176/#3178
  "Completed", #3177/#3179 "Pending") as if its job were project management,
  and emitted a placeholder "Changes committed in PR #<NN>" — no real change
  was committed.
- **Scope creep**: Deleting `.github/copilot-instructions.md` is an
  unrequested, potentially harmful repository change (it removes the
  Copilot-agent instruction entry point) with no bearing on the ipRGC term.
