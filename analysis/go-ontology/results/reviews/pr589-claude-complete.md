---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 589
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/589
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade for #31868/#31871/#31872/#31881. The committed diff is
identical to PR #259/#571/#638 (blob `f7eb695`): a single `term_tracker_item`
for issue #31863 added to GO:0140177, on top of GO:7770062 and the extended
GO:0140177 def that were already present in the base branch. F1=0.000 is a
misattribution artifact. (No PR/issue comment captured in the attempt file;
the diff is the basis for assessment.)

## Strengths

- The single edit is syntactically valid OBO and a defensible provenance
  enhancement: it links GO:0140177's vesicle def extension (which issue #31863
  did request) back to the issue, mirroring the same well-formed change made
  by the other gpt-5.5/kimi runs on this case.
- Tightly scoped to one line in one file; no spurious or destructive edits;
  the pre-existing GO:7770062 + GO:0140177 content was correctly left intact
  rather than redundantly recreated.

## Issues

- No agent narrative (PR/issue comment) is recorded for this run, so process
  evidence (validation, research, term search) cannot be assessed from the
  attempt file — weaker than its sibling runs #638/#571 which documented
  travis_build/SPARQL-QC.
- The GO:0140177 tracker addition is extra relative to the true resolution
  PR #31895 and not explicitly requested — defensible but mild scope creep;
  GO:0140177 already carried an issue #24964 tracker.
- No obsoletion-cascade work, correctly so (that scope is other issues, not
  #31863). F1/precision/recall = 0.000 is purely the misattribution artifact
  and under-represents the substantively reasonable outcome.
