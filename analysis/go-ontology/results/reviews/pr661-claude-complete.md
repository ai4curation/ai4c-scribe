---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
eval_repo_pr: 661
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/661
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

**Poor evaluation case** — same misattribution as documented in METADATA.md:
issue #31863 (new-term request, create `GO:7770062` under `GO:0140177` +
extend GO:0140177 def) was resolved by PR #31895, while the selected gold
#32012 is the unrelated obsoletion cascade for #31868/#31871/#31872/#31881.
Reported F1=0.000 is a scoring artifact. This run is essentially identical to
PR #615 (same blob `49ebe8c`): the agent correctly found the issue content
already present in the base branch and added the one EXACT synonym `vesicle
membrane adaptor activity` to GO:7770062.

## Strengths

- Accurate state assessment: GO:7770062 (def with PMID:19887069/PMID:19575650,
  is_a GO:0140177, EXACT synonyms) and the vesicle-extended GO:0140177
  definition were already present; the agent did not redundantly recreate them.
- The single synonym addition is valid OBO and well-motivated — it parallels
  the parent `membrane-membrane adaptor activity` and sibling MF terms,
  improving discoverability.
- Strong process hygiene: pre/post SPARQL-QC, RESEARCH.md and DESIGN_PATTERNS.md
  produced, checkout/checkin workflow used, references validated.

## Issues

- The synonym is an extra edit not present in the true resolution PR #31895
  and not requested in the issue — defensible but unnecessary (mild scope
  creep), not an error.
- No obsoletion-cascade work, correctly so: that scope belongs to other issues
  (#31868/#31871/#31872/#31881), not #31863.
- F1/precision/recall = 0.000 reflects only the broken issue→gold pairing and
  severely under-represents the substantive correctness of recognizing an
  already-resolved issue.
