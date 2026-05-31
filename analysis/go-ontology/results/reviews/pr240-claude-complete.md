---
ontology: go-ontology
issue_number: 31923
pr_number: 31938
eval_repo_pr: 240
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: other
difficulty: simple
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The gemma-4-31b/opencode run correctly removed the microtubule mechanistic gloss from the GO:0045022 definition but did not add the `term_tracker_item` for issue #31923 that the human gold PR included as its second commit. The definition edit itself is exactly correct; the omission of the tracker is the sole reason F1 is 0.800. The score fairly represents the outcome: one of two required changes done correctly, the other missed.

## Strengths

- Definition edit is byte-identical to gold: only the `; transport occurs along microtubules...drugs` clause removed; leading sentence and `[ISBN:0815316194, PMID:29980602]` xrefs preserved exactly.
- No collateral damage: logical axioms, synonym, and namespace untouched; no spurious references added; no `created_by`/`creation_date` added to the existing term. Clean precision on the lines it did edit.
- Notably, the smallest model in the set (gemma-4-31b, 31B params) got the core textual edit exactly right with zero drift — a non-trivial result for a definition simplification that requires identifying and excising precisely one clause.

## Issues

- **Missed requirement / under-editing**: omitted the `term_tracker_item ".../issues/31923"` line that the human added in a dedicated commit. The agent config (v9) explicitly directs agents to "Link back to the issue you are dealing with using the `term_tracker_item`", and the curator in the source issue thread explicitly insisted on it ("always add the term tracker url"). This is a documented convention, not optional.
- The agent's issue comment is extremely terse (two sentences) with no PR description, validation checklist, or methodology evidence — so beyond the diff there is no record that the agent considered metadata at all. This is weaker process documentation than the other F1=0.800 attempts (#339, #203, #181), even though the resulting diff is identical to theirs.
- Same systematic blind spot as #339/#203/#181 (term-tracker omission → F1=0.800). No errors or scope creep, hence partial_success rather than failure.
