---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 569
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/569
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade for #31868/#31871/#31872/#31881, so F1=0.000 is a scoring
artifact. The agent correctly found GO:7770062 and the vesicle-extended
GO:0140177 def already present, then made a single deliberate, well-reasoned
edit: replacing the second def reference on GO:7770062 from PMID:19575650 to
PMID:23164531 to satisfy the curator's explicit request for a synaptic-vesicle
citation.

## Strengths

- This is the **most thoughtful** of the eight attempts on this case. It read
  the issue thread closely and identified the genuine open gap: @raymond91125
  twice asked for a reference covering synaptic vesicle transport/targeting in
  addition to PMID:19887069 (ER-Golgi). PMID:23164531 (Hallermann & Silver
  2013, active-zone vesicle tethering) is exactly the synapse-focused
  companion dragon-ai-agent itself proposed in the issue discussion.
- Correctly preserved PMID:19887069 (ER-Golgi tethering) as requested, and
  documented the rationale clearly in RESEARCH.md and the PR comment.
- Honest validation reporting: ran ROBOT convert + the full SPARQL QC query
  set via tools/robot.jar; transparent that `make travis_build` was blocked by
  a missing `amm` and that linkml-reference-validator hit NCBI 429s.

## Issues

- Diverges from the merged human PR #31895, which retained PMID:19575650
  (Yu & Hughson). The curator's last explicit instruction was to *add* a
  general article that also covers synaptic vesicles; the agent *swapped*
  rather than added, dropping the broad-trafficking review. The intent is
  defensible but the human ultimately kept the broader review — a style/
  judgment difference, not an error.
- The edit is a single provenance change with no structural ontology work;
  there is no obsoletion-cascade content, correctly so (that belongs to other
  issues, not #31863).
- F1=0.000 vs gold #32012 is purely the misattribution artifact and does not
  reflect this attempt's strong issue comprehension.
