---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 571
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
case_quality: poor
case_quality_reason: gold_pr_wrong_issue
companion_prs: [31895]
scoring_caveat: "issue #31863 is a new-term request resolved by PR #31895 (created GO:7770062 + extended GO:0140177). Gold PR #32012 is a downstream obsoletion cascade for issues #31868/#31871/#31872/#31881. F1=0 vs #32012 is a misattribution artifact, not an agent failure."
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31863
  Human PR (selected gold, MISATTRIBUTED): https://github.com/geneontology/go-ontology/pull/32012
  True resolution of #31863: https://github.com/geneontology/go-ontology/pull/31895
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/571
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade for #31868/#31871/#31872/#31881. The agent correctly
recognized GO:7770062 and the extended GO:0140177 definition were already
present and added one `term_tracker_item` for issue #31863 to GO:0140177
(identical diff to PR #259, blob `f7eb695`). F1=0.000 is a misattribution
artifact.

## Strengths

- Thorough independent verification of the pre-existing edits: GO:7770062
  placement (is_a GO:0140177), def, PMID:19887069/PMID:19575650, EXACT
  synonyms, namespace, created_by/creation_date, and GO:0140177's
  vesicle-extended def — the correct conclusion for issue #31863.
- Strong validation: reports 0/16 SPARQL-QC violations, ELK reasoning with no
  unsatisfiable classes, and successful OBO conversion.
- The added GO:0140177 tracker line for #31863 is valid OBO and a reasonable
  provenance link for the def extension the issue requested.

## Issues

- The tracker addition is extra relative to PR #31895 and not explicitly
  requested — defensible provenance hygiene but mild scope creep; GO:0140177
  already carries an issue #24964 tracker.
- No obsoletion-cascade work, correctly so (that scope is issues
  #31868/#31871/#31872/#31881, not #31863).
- F1=0.000 vs gold #32012 is purely the misattribution artifact and does not
  reflect the agent's correct "already resolved" assessment.
