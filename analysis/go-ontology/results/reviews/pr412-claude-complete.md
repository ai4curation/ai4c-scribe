---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 412
agent: std_claude_hai45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.818
precision: 0.818
recall: 0.818
jaccard: 0.692
outcome: partial_success
failure_modes:
  - wrong_pattern
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent obsoleted GO:0061817 with correct core mechanics and a good rationale `comment`, but used `replaced_by: GO:0160214` for a cross-namespace BP→MF mapping, added no `consider` targets, and reordered the `created_by`/`creation_date` provenance lines. The human used `consider` for both GO:0051643 and GO:0160214 and left provenance in place. F1 = 0.818 fairly captures a structurally-correct obsoletion with one pattern error and one missing requirement.

## Strengths

- Correct obsoletion skeleton: `obsolete`-prefixed name, `OBSOLETE.`-prefixed def, `is_obsolete: true`, both `is_a` axioms and the EXACT synonym removed.
- Added `property_value: term_tracker_item` for issue #31873.
- The `comment` is informative — it names GO:0160214 as the migration target, partially compensating in prose for the missing `consider` line.
- Issue comment correctly references the parallel annotation-review ticket geneontology/go-annotation#6383 and the ~15 EXP annotations, showing it read the issue thread.

## Issues

- **Wrong pattern (`replaced_by` cross-namespace).** `replaced_by: GO:0160214` (MF) for a `biological_process` term being obsoleted asserts a direct-equivalent substitution the issue and human PR deliberately avoided. The issue leaves "Replace by" blank; the human used `consider` for both targets, citing the GO:0000185/0000186/0000187 precedent.
- **Missing `consider` targets.** No `consider` lines at all; GO:0051643 (the BP fallback explicitly named in the issue) is dropped from the structured metadata.
- **Provenance line churn.** `created_by: dph` / `creation_date: 2016-12-05...` were deleted and re-added after the new metadata rather than left in place (as the human did). Semantically harmless but unnecessary diff noise that, combined with the metadata differences, holds F1 at 0.818.
