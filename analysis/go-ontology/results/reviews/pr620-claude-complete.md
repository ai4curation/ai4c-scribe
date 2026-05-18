---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 620
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
case_quality: good
f1: 0.948
precision: 0.965
recall: 0.932
jaccard: 0.902
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/620
-->

## Summary

The agent fully and correctly resolved issue #31916. It obsoleted all five terms named in raymond91125's curator instruction (GO:0009255, GO:0061679, GO:0061680, GO:0061681 → `replaced_by: GO:0061678`; GO:0061688 → `replaced_by: GO:0006096`) and performed the GO:0061678 MetaCyc mapping cleanup exactly as the issue body requested. The substantive obsoletion is equivalent to gold PR #32024. F1=0.948 (recall 0.932) slightly under-represents correctness but does flag one genuine minor regression: the agent stripped `created_by`/`creation_date` provenance lines from the obsoleted stanzas that the gold PR preserved.

## Strengths

- Complete, correct obsoletion of GO:0009255, GO:0061679, GO:0061680, GO:0061681 with `replaced_by: GO:0061678`: obsolete name/def prefixes, `is_obsolete: true`, issue #31916 `term_tracker_item`, and removal of every active logical axiom (`is_a`, `intersection_of`) plus term-level MetaCyc xrefs and the GO:0061679/GO:0061688 RELATED synonyms.
- GO:0061688 obsoleted with `replaced_by: GO:0006096`, correctly picking up the curator decision made in the issue thread (sjm41/raymond91125) rather than the original issue body, which only discussed the four ED-pathway variants.
- The hardest detail is exactly right: on the surviving parent GO:0061678 it removed the grouping-class `xref: MetaCyc:Entner-Doudoroff-Pathways` and added the four variant IDs (ENTNER-DOUDOROFF-PWY, NPGLUCAT-PWY, PWY-2221, PWY-8004) each with the `{source="skos:narrowMatch"}` qualifier — matching gold byte-for-byte on those lines.
- Tightly scoped: one file, no gratuitous edits beyond the issue.

## Issues

- Over-deletion of provenance (the recall hit): on GO:0061679, GO:0061680, GO:0061681 and GO:0061688 the agent removed the `created_by: dph` and `creation_date:` lines, whereas gold PR #32024 retains them on obsoleted stanzas. Standard GO obsoletion practice keeps original provenance; this is a real, if cosmetic, regression.
- Also dropped the unrelated `property_value: term_tracker_item ".../28392"` on GO:0061680 that gold preserved. Removing an obsoletion-unrelated historical tracker is mildly over-aggressive cleanup.
- Style only: obsoletion `comment` text ("being merged into the broader parent term Entner-Doudoroff pathway") is terser than gold's, which explicitly cites MetaCyc's variant-pathway treatment and the GO-CAM rationale. No semantic effect.
- No correctness, syntax, or completeness problems; all curator-requested obsoletions and replacements are present and valid.
