---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 546
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/546
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** (issue→gold misattribution per METADATA.md): #31863
is a new-term request resolved by PR #31895; gold #32012 is the unrelated
obsoletion cascade. The agent correctly recognized GO:7770062 and the extended
GO:0140177 definition were already present in the base branch (PR #31895
merged) and stated no edits were required, recording an empty completion
commit. The committed diff, however, swaps the GO:7770062 definition
references from `[PMID:19575650, PMID:19887069]` to `[PMID:19887069,
PMID:23164531]` — a change the PR comment does not mention and that
contradicts the "no ontology edits required" narrative.

## Strengths

- Correct read of issue state: GO:7770062 exists under GO:0140177 with the
  requested def and provenance; GO:0140177 def already includes "vesicle".
  This is the right conclusion for issue #31863 given PR #31895 was merged.
- Validated PMID:19887069 (Sztul & Lupashin, ER-Golgi tethering) and
  PMID:19575650 (Yu & Hughson, tethering organizers) against cached metadata.
- Honest about environment limits (ROBOT not installed; full validation not run).

## Issues

- **Inconsistency between narrative and diff.** The PR comment claims no
  ontology changes were needed, but the diff replaces PMID:19575650 with
  PMID:23164531 on GO:7770062's def. Either the comment is wrong or an
  unintended edit landed; this is a reporting/scoping defect.
- The reference swap itself is a plausible response to the curator's request
  for a synapse-relevant citation (PMID:23164531 = Hallermann & Silver 2013,
  active-zone vesicle tethering — exactly the alternative dragon-ai-agent
  offered in the issue thread), but it diverges from the merged PR #31895
  (which kept PMID:19575650) and was not surfaced in the summary.
- F1=0.000 is a misattribution artifact vs gold #32012; it does not reflect
  agent quality, which is otherwise a reasonable "issue already resolved"
  determination marred by the silent ref edit.
