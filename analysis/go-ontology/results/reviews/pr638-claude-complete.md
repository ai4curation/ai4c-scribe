---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 638
agent: std_opencode_gpt55
model: gpt-5.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/638
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade. The agent correctly recognized GO:7770062 and the extended
GO:0140177 definition were already present and added one `term_tracker_item`
for issue #31863 to GO:0140177 (identical diff to PR #259/#571, blob
`f7eb695`). F1=0.000 is a misattribution artifact, not an agent failure.

## Strengths

- Correct issue-state read: confirmed GO:7770062 under GO:0140177 with def
  references PMID:19575650/PMID:19887069, EXACT synonyms, tracker to #31863,
  and the vesicle-extended GO:0140177 def — the right conclusion for #31863.
- Sound modeling judgment articulated: explicitly rejected adding a generic
  binding logical definition because GO:7770062 bridges two membranes rather
  than binding a single entity, so an asserted `is_a GO:0140177` plus text def
  is the correct minimal representation (consistent with the merged PR #31895).
- Reports full `make -C src/ontology travis_build` passing pre and post,
  reference text validation via linkml-reference-validator, and produced
  RESEARCH.md / DESIGN_PATTERNS.md.

## Issues

- The GO:0140177 tracker addition for #31863 is extra relative to PR #31895
  and not explicitly requested — defensible provenance linkage but mild scope
  creep; GO:0140177 already had an issue #24964 tracker.
- No obsoletion-cascade work, correctly so (that scope is #31868/#31871/
  #31872/#31881, not #31863).
- F1/precision/recall = 0.000 reflects only the broken issue→gold pairing and
  under-represents the substantively correct outcome.
