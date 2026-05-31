---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 337
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.940
precision: 0.965
recall: 0.917
jaccard: 0.887
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/337
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully and correctly resolved issue #31916: it obsoleted all five terms named in @raymond91125's directive (`GO:0009255`, `GO:0061679`, `GO:0061680`, `GO:0061681` → `GO:0061678`; `GO:0061688` → `GO:0006096`) and reworked the parent `GO:0061678` xrefs exactly as the issue body requested. The substantive ontology content is essentially identical to the merged human PR #32024; `F1=0.940` slightly under-represents the quality because the small recall loss comes entirely from richer (not wrong) comment text plus one defensible extra provenance line. This is the strongest of the non-codex attempts and is functionally on par with the top-scoring runs.

## Strengths

- Obsoleted all four Entner-Doudoroff variant terms (`GO:0009255`, `GO:0061679`, `GO:0061680`, `GO:0061681`) with `replaced_by: GO:0061678`, and `GO:0061688` with `replaced_by: GO:0006096`, matching the human PR's replacement targets exactly.
- Performed a complete, conventional obsoletion on each term: `obsolete ` name prefix, `OBSOLETE.` definition prefix, `is_obsolete: true`, removal of all active logical axioms (`is_a`, `intersection_of`, `relationship`), removal of the `xref` and `synonym: "gluconate pathway" RELATED []` lines, and a `term_tracker_item` for issue #31916.
- Used the **correct, project-standard xref mapping syntax** `xref: MetaCyc:... {source="skos:narrowMatch"}` on `GO:0061678` — identical to the human PR and consistent with the ~4600 existing `{source="skos:narrowMatch"}` xrefs in `go-edit.obo`. Removed the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` and added the four variant IDs (`ENTNER-DOUDOROFF-PWY`, `NPGLUCAT-PWY`, `PWY-2221`, `PWY-8004`) exactly as the issue body asked.
- Preserved historical provenance correctly: `created_by`/`creation_date` retained on every obsoleted term, and the pre-existing `property_value: term_tracker_item ".../issues/28392"` on `GO:0061680` was kept (this is the line most other attempts dropped).
- Obsoletion comments are more informative than the human PR's: they name the MetaCyc "variant pathways" rationale, the GO-CAM recommendation, and explicitly state where the moved MetaCyc mapping went, which is good curatorial practice.
- Strong methodology: PR body documents robot convert/reason validation, the full SPARQL QC suite passing, and the `/term-obsoletion` and `/mapping` skills being consulted. The agent also flagged the CGD/GO:0061688 IEA migration concern, mirroring the real-world dragon-ai-agent comment thread.

## Issues

- No correctness or completeness issues; the change is ontologically sound and complete.
- Minor scope/precision item: the agent added `property_value: term_tracker_item ".../issues/31916"` to the still-active parent `GO:0061678`, which the human PR did not. This is harmless and arguably good traceability, but it is the main source of the recall gap vs. the gold diff.
- Style-only: comment wording differs from the human PR's (the agent's is longer and per-term tailored rather than the human's single boilerplate sentence). This is a difference, not a defect, and accounts for most of the remaining metadiff delta.
