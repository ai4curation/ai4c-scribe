---
repo: obophenotype/uberon
issue_number: 3572
pr_number: 3573
issue_title: "Revise esophagus and esophageal artery partonomy"
issue_labels:
  - uberon-classhierarchy
issue_created_at: "2025-06-30"
issue_closed_at: "2025-07-02"
pr_author: dragon-ai-agent
pr_merged_at: "2025-07-02"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: thoracic-anatomy
tags:
  - partonomy
  - esophagus
  - esophageal-artery
  - spatial-relationships
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Partonomy fix requiring understanding that the esophagus spans multiple body cavities
case_quality: ok
case_quality_reason: clean_issue_complete_gold_but_serialization_artifact_affects_2_attempts
companion_prs: []
scoring_caveat: "Issue #3572 is unambiguous and gold PR #3573 is the complete, sole resolution (PR #3576 in the comments is only a gogoeditdiff tooling fix, unrelated). F1=1.0 for attempts #310/#188/#138/#103/#86 is genuine, not gold leakage. However, attempts #248 (claude-opus-4.7) and #32 (gpt-5.5/codex) score F1=0.300 purely due to a robot-convert reserialization-churn artifact (~8 semantically-neutral annotation-attribute reorderings); their two issue-relevant hunks match gold exactly (precision=1.0). Attempt #70 scores F1=0.857 only because it added benign term_tracker_item provenance. Judge #248/#32/#70 on substance (clean success) not metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The esophagus had a "located in thoracic cavity" relationship, but this is anatomically incorrect because the esophagus has cervical and abdominal portions that extend beyond the thorax. Additionally, the esophageal artery used "branching part of" instead of the correct "connecting branch of" relationship to the thoracic aorta.

## Changes Made

Removed the incorrect "located in thoracic cavity" relationship from the esophagus term (UBERON:0001043). Replaced the "branching part of" relationship with "connecting branch of" for the esophageal artery (UBERON:0035539) in relation to the thoracic aorta.

## Resolution

Medium difficulty because the agent must understand that the esophagus is a long tubular organ spanning the neck, thorax, and upper abdomen, so restricting its location to the thoracic cavity is incorrect. It also requires knowing the distinction between "branching part of" and "connecting branch of" in vascular partonomy.

## Curation Note (data quality)

Reviewed 2026-05-16 (claude-opus-4.7). This is fundamentally a **good** evaluation
case: issue #3572 states exactly two precise asks, and gold PR #3573 is the complete
and sole human resolution (the only other PR referenced in the PR comments, #3576, is
an unrelated `gogoeditdiff` tooling fix). Steps 3a/3b checked — no companion PRs, no
base contamination, no gold leakage. The five F1=1.0 attempts (#310, #188, #138, #103,
#86) are **genuine** exact matches, not artifacts.

However, the metadiff F1 materially under-represents quality on three attempts and this
should be accounted for in any aggregation:

- **#248 (claude-opus-4.7) and #32 (gpt-5.5/codex): F1=0.300 is a robot-convert
  reserialization-churn artifact, not an agent error.** Both made the two requested
  axiom edits exactly correctly (precision=1.0, byte-identical to gold for the
  issue-relevant hunks). They then ran `robot convert -f obo` which reserialized ~8
  unrelated annotation blocks (attribute reordering inside `{}` on
  UBERON:0001464/0001686/0003623/0003624/0012292/etc., and a `has_part`/`part_of`
  line-order swap on airway hillock UBERON:8910024). These edits are semantically
  neutral; recall=0.176 reflects serialization line-noise only. Substantively both
  are clean successes. Contrast codex #86, which ran `robot convert` but then
  explicitly reverted the incidental reorderings (commit `14b89f7`) and scored 1.0.
- **#70 (gpt-5.5/opencode): F1=0.857** only because it added benign
  `term_tracker_item` provenance to both edited terms (a defensible UBERON convention
  the human gold PR omitted). Substantively correct.

Downstream scoring should treat #248/#32 as successes (or down-weight the
serialization-churn penalty) and #70 as a defensible-extra success, rather than taking
F1 at face value. The case itself does not need exclusion; gold and issue are sound.
