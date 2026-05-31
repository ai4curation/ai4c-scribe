---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 489
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.895
precision: 0.85
recall: 0.944
jaccard: 0.81
outcome: success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/489
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 489 --repo ai4curation/eval-ont-agent-go
-->

## Summary

A clean, well-scoped solution that produces the identical blob (`b83c095`) to attempt pr465. The obsoletion and both renames are correct, the restored-synonym dbxrefs match the gold exactly, and there is no scope creep. The only shortfall is that it did not refresh the stale `! vesicle coating` inline comments on the incoming `is_a` edges (the gold updated `GO:0016183`, `GO:0048200`, and `GO:0048208`'s own self-edge). The metadiff (`f1: 0.895`, `precision: 0.850`, `recall: 0.944`) is a fair reflection: high recall because all gold *substantive* edits are present, slightly lower precision because the agent left the inline label comments stale.

## Strengths

- **Obsoletion matches gold precisely.** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by`/`creation_date` retained — full provenance preserved per the `term-obsoletion` skill.
- **Best obsoletion comment of the cohort alongside pr344.** "The proteins annotated to this term are components of the COPII vesicle coating process itself, not regulators of that process" is biologically accurate and matches ValWood's reasoning in the issue.
- **Restored-synonym dbxrefs match the gold exactly:** `synonym: "COPII vesicle coating" EXACT [GOC:ascb_2009, GOC:dph, GOC:tb]` — the only attempts that get this attribution right are this one, pr465, pr211, pr183, pr61, pr104, pr83. (pr344 used the def xrefs; pr278/pr381 emptied them.)
- **Tight scope and no errors.** Only the three target terms are touched; no scope creep onto active terms, no definition rewrites, no spurious `term_tracker_item` on active terms.
- Excellent process documentation: literature review (PMID:16990852, PMID:23378591), annotation impact analysis (539 annotations, 3 experimental), and an honest note that the disputed MAPK15 annotation is out of scope.

## Issues

- **Missed the stale-comment maintenance (omission).** The diff does not refresh `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183` (synaptic vesicle coating) or `GO:0048200` (Golgi transport vesicle coating), nor on `GO:0048208`'s own `is_a: GO:0006901` line, all of which the gold updated. These are cosmetic OBO `!` label comments (regenerated/ignored by the reasoner) but they are accepted GO hygiene and the gold did them. This is the only thing separating this attempt from pr344.
- Style note: the agent's literature-driven rationale (PMID:16990852 etc.) is good practice but unnecessary here, since the issue supplied the replacement directly — not a defect, just over-justification.

Net: a `success` with one consistent omission shared across most of the cohort. The score fairly represents the outcome.
