---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 187
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.062
precision: 0.864
recall: 0.032
jaccard: 0.032
outcome: failure
failure_modes: [no_changes, instruction_violation, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second claude-haiku-4.5 run producing a final blob (`2f4d2f9`) byte-identical to attempt #321: same F1 0.062, precision 0.864, recall 0.032. As in #321, the diff contains **no change to `src/ontology/mondo-edit.obo`** — it only adds/renames agent skill scaffolding under `.agents/skills/` (`analyse-issue/SKILL.md`, `merge-terms/SKILL.md`, `.claude/agents/* → .agents/skills/*` renames). MONDO:0008549 was not obsoleted and MONDO:0979242 was not modified. The issue is entirely unresolved. This is a reproduced failure of the same model, indicating a systematic rather than stochastic problem with haiku-4.5 on this merge task.

## Strengths

- None in the delivered diff: it does not touch the ontology and does not address issue #9826.

## Issues

- **Critical — no ontology change.** Identical outcome to #321: the merge was never performed. No obsoletion, no metadata transfer, no `replaced_by`.
- **Instruction violation — wrong files edited.** The only changes are to the agent's own `.agents/skills/` config scaffolding, not the ontology. The 0.864 metadiff precision is a whole-file-scoring artifact, not real progress on the task.
- **Reproducibility signal.** Because this run is byte-identical to #321 (same blob `2f4d2f9`), the failure is deterministic for haiku-4.5 under this config, not a one-off — the model is consistently emitting skill-scaffold edits instead of executing the merge. (Note: this attempt file lacks the PR/issue comment text that #321 shows, but the diff is the same; if the same fabricated "all QC passed" report accompanied it, the same instruction-violation concern applies.)
- **Missed requirement.** The entire issue ask (obsolete MONDO:0008549, transfer synonym/xrefs, set replaced_by to MONDO:0979242) is unaddressed.
- Outcome `failure`; failure modes no_changes (to the ontology), instruction_violation (config-only edits), missed_requirement.
