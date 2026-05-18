---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 685
agent: std_opencode_gpt54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
case_quality: ok
case_quality_reason: clean_issue_complete_gold_but_serialization_artifact_affects_2_attempts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second gpt-5.4/opencode run on the same case, with the same outcome as #686: it removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` to `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), preserving `{source="FMA"}`. F1=1.0/P=1.0/R=1.0 is genuine — issue #3572 has exactly these two asks and is fully resolved by gold PR #3573 alone (no companion PRs; Step 3a/3b confirmed in METADATA).

## Strengths

- Both axiom edits are exactly correct and complete, including retention of the `{source="FMA"}` qualifier on the artery relationship.
- Ran `robot convert -i ... -f obo` per repo guidance but escaped the broad attribute-reordering churn that dropped #248/#32 to F1=0.300; only the same benign EOF trailing-blank-line trim on the `vessel_supplies_blood_to` typedef stanza (blob `33e7979`, identical to #686), which metadiff normalizes away.
- Transparent and accurate PR comment: explicitly acknowledges that `robot convert` normalized some serializer-only formatting and that those are formatting-only changes — honest self-reporting of the reserialization behavior.
- Correct workflow (obo-grep.pl inspection, obo-checkout.pl / obo-checkin.pl, post-edit re-validation of both stanzas) and sound anatomical/vascular rationale.

## Issues

- Identical to #686: the lone incidental EOF blank-line removal is cosmetic and metadiff-invisible — not a defect. No errors, omissions, or scope creep. F1=1.0 accurately represents quality; exemplary tightly scoped solution.
