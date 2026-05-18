---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 259
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/259
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade. The agent correctly recognized GO:7770062 and the extended
GO:0140177 definition were already present in the base branch and made one
small additive metadata edit: adding a `term_tracker_item` for issue #31863 to
GO:0140177 (so the parent def extension traces back to this issue). F1=0.000
is a misattribution artifact, not an agent failure.

## Strengths

- Accurate state assessment: independently verified GO:7770062's placement
  (is_a GO:0140177), def, PMID:19887069/PMID:19575650 provenance, EXACT
  synonyms, and the vesicle-extended GO:0140177 def — the correct conclusion
  for issue #31863 given PR #31895 was merged.
- The added `term_tracker_item` line for #31863 on GO:0140177 is valid OBO and
  a reasonable provenance enhancement: the issue did request the GO:0140177 def
  extension, and the merged PR #31895 did not add a tracker line to that term.
- Ran `robot convert` and confirmed no SPARQL violations; well-documented.

## Issues

- This tracker addition is not in PR #31895 and was not explicitly asked for;
  it is a defensible-but-extra provenance edit (mild scope creep), not an
  error. Note GO:0140177 already carries a tracker for issue #24964.
- No obsoletion-cascade work — correctly so, as that scope belongs to other
  issues (#31868/#31871/#31872/#31881), not #31863.
- F1/precision/recall = 0.000 reflects only the broken issue→gold pairing and
  under-represents the agent's substantively correct "already resolved"
  determination. (The prior pr259-codex-complete review judged this against
  gold #32012's obsoletion content without the issue correction; under the
  established misattribution framing the outcome is partial_success, not
  failure.)
