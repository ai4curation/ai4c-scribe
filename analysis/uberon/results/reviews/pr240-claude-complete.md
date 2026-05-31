---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 240
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.250
precision: 1.000
recall: 0.143
jaccard: 0.143
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The substantive repair is **fully correct and identical to the five F1=1.0 attempts**: opus-4.7 removed exactly the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` lines from UBERON:0007181 and UBERON:0007182, preserving the correct `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` definitions. The F1 of 0.250 (recall 0.143, precision 1.000) is the lowest of the eight attempts but **most severely under-represents quality** of any run here — it is depressed entirely by a `robot convert -f obo` reserialization-churn artifact spanning *three* unrelated stanzas (one more than #197/#24), none with any semantic change. The agent explicitly disclosed and correctly characterized the artifact as "benign alphabetical reordering ... a normal side effect of `robot convert -f obo`."

## Strengths

- **Correct, minimal core fix** (precision 1.000): the two issue-relevant hunks exactly match the maintainer instruction and the gold PR substance.
- **Best-documented diagnostic validation of all eight attempts:** the agent confirmed via `obo-grep.pl` that both terms carried the bad axiom, *and* independently verified that UBERON:0003983 is itself `part_of UBERON:0002080 ! heart right ventricle` — directly corroborating the reporter's cardiac/reproductive homonym hypothesis (also correctly citing UBERON:0005953 "outflow part of right ventricle" as the colliding synonym source).
- Transparent disclosure: the PR comment explicitly lists the synonym/xref reordering as benign serialization noise rather than hiding it.

## Issues

- **ROBOT reserialization-churn artifact (cosmetic, the only issue, and slightly worse here):** the diff carries three extra hunks of pure ordering noise — a synonym-line transposition on UBERON:0003532 (hindlimb skin: the two `"lower limb skin" EXACT` lines swapped between FMA and ORCID source), plus the same UBERON:0013540 (Brodmann 1909 area 9) and UBERON:0034891 (insular cortex) definition-xref reorderings seen in #197/#24. No terms, axioms, or text changed. Whole-file metadiff penalizes all three, driving recall to 0.143 — the lowest score despite a substantively perfect fix.
- The agent understood the artifact (it explicitly noted the diff was "inspected") but did **not** revert ROBOT's incidental hunks, unlike attempts #46/#61/#74 which produced clean two-hunk diffs. This is a diff-hygiene lapse, not an ontology error.
- Net assessment: substantively a **success-quality** fix; the 0.250 F1 is a serialization-artifact false negative and the single most misleading metadiff number in this case. Graded `partial_success` for the diff-hygiene lapse only — the ontology edit itself is flawless.
