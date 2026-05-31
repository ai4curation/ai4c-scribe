---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 615
agent: std_opencode_gpt54
model: gpt-5.4
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/615
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This is a **poor evaluation case**: issue #31863 is a new-term request
(create `GO:7770062 vesicle membrane tethering activity` under `GO:0140177
membrane-membrane adaptor activity` + extend GO:0140177's def to include
"vesicle"), resolved by human PR #31895. The selected gold PR #32012 is the
*downstream obsoletion cascade* for unrelated issues #31868/#31871/#31872/#31881,
so the reported F1=0.000 is a misattribution artifact, not a measure of agent
quality (see established Curation Note in METADATA.md). Judged against the
issue's actual ask, the agent correctly recognized that GO:7770062 and the
extended GO:0140177 definition were already present in the eval base branch
(because PR #31895 was already merged) and made only one small additive synonym
edit.

## Strengths

- Correctly identified that the issue's substantive content (GO:7770062 under
  GO:0140177, def referencing PMID:19887069/PMID:19575650, synonyms `vesicle
  membrane tether activity` / `vesicle tethering activity`, and the
  vesicle-extended GO:0140177 def) was already present — an accurate read of
  the actual ontology state for issue #31863.
- The single edit (adding EXACT synonym `vesicle membrane adaptor activity` to
  GO:7770062) is syntactically valid OBO and has a defensible rationale: it
  aligns the child label space with the parent `membrane-membrane adaptor
  activity` and with sibling adaptor/tether MF terms under GO:0140177.
- Documented validation (SPARQL-QC pre/post), term search, and reference
  validation, following the agent config workflow.

## Issues

- The added synonym is not in PR #31895 (the true resolution of #31863) and
  was not requested in the issue; it is a defensible-but-unnecessary extra
  edit (mild over-editing / scope creep), not an error.
- No engagement with the obsoletion cascade of gold #32012 — but that work
  belongs to issues #31868/#31871/#31872/#31881, not #31863, so this is
  expected and correct given the prompt, not an omission.
- F1/precision/recall = 0.000 entirely reflects the broken issue→gold pairing;
  the metadiff dramatically under-represents actual quality here.
