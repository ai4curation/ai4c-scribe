---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 686
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

The agent correctly resolved both of issue #3572's explicit asks: it removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` to `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), keeping the `{source="FMA"}` annotation. F1=1.0/P=1.0/R=1.0 is genuine (issue fully resolved by this single PR; no companion PRs per METADATA Step 3a/3b review). The agent ran `robot convert` but, unlike attempts #248/#32, incurred essentially no reserialization churn — only a single benign trailing-blank-line removal at EOF after the `vessel_supplies_blood_to` typedef stanza, which metadiff normalizes away (recall stays 1.0).

## Strengths

- Both axiom edits are exactly correct and complete; the `{source="FMA"}` qualifier on the artery relationship is correctly retained.
- Despite running `robot convert -f obo`, the agent avoided the broad annotation-attribute-reordering churn that cratered #248/#32 to F1=0.300; the only incidental change is a harmless EOF trailing-newline trim (target blob `33e7979`).
- Sound anatomical rationale in the PR comment (cervical/thoracic/abdominal esophageal portions justify removing the blanket location axiom).
- Followed the repo workflow (obo-checkout.pl / obo-checkin.pl), validated both original axioms were present pre-edit, and ran `git diff --check` for whitespace.

## Issues

- The single incidental EOF blank-line removal on the `vessel_supplies_blood_to` stanza is cosmetic, semantically neutral, and normalized away by metadiff — not a real defect, just noted for completeness. No errors, omissions, or scope creep otherwise. F1=1.0 accurately represents quality.
