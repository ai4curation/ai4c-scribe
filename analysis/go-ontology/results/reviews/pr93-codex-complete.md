---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 93
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.696
precision: 0.667
recall: 0.727
jaccard: 0.533
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/93
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 93 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully added the requested new cellular component term, `GO:7770070 p24 cargo receptor complex`, with the correct parent `GO:0062137 cargo receptor complex` and the relevant process link to `GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport`. However, compared with the human PR it produced a thinner term: it omitted several curator-added references and useful related synonyms, while adding two exact synonyms that were not in the issue or human solution. The metadiff score (`F1=0.696`, `precision=0.667`, `recall=0.727`) is a fair signal of a mostly correct but incomplete and slightly over-scoped edit.


## Strengths

- Created the correct new term ID and label, `GO:7770070 p24 cargo receptor complex`, in the `cellular_component` namespace.
- Used the requested superclass, `is_a: GO:0062137 ! cargo receptor complex`, matching both the issue and the human PR.
- Added a plausible logical relationship, `capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport`, matching the human PR and reflecting the ER-to-Golgi COPII cargo selection role described in the issue.
- Included the three PMIDs explicitly supplied in the issue (`PMID:32456004`, `PMID:34647572`, `PMID:27569046`) and wrote a definition centered on ER exit sites, COPII-coated vesicles, and GPI-anchored cargo.
- Added the expected issue tracker provenance, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31295" xsd:anyURI`.


## Issues

- Under-edited relative to the human PR by omitting two additional references, `PMID:19566487` and `PMID:26224213`, which support the broader curated definition of the p24 complex as a conserved, hetero-oligomeric ER-Golgi cycling complex.
- Missed useful related synonyms from the human PR: `"Emp24-Erv25 complex" RELATED`, `"p24 family complex" RELATED`, and `"TMED complex" RELATED`. These are important for findability across yeast and metazoan naming conventions noted by the issue's gene product table (`Emp24`, `Erv25`, and human `TMED` orthologs).
- The agent's definition is correct at a high level but less complete than the human definition because it does not capture the alpha/beta/gamma/delta p24 subfamily composition or the typical hetero-oligomeric/tetrameric nature of the complex.
- Added extra exact synonyms not present in the issue or human PR: `"p24 protein complex" EXACT` and `"p24 cargo receptor protein complex" EXACT`. These are not obviously wrong, but the exact-synonym scope is not justified by the supplied issue text and they displace the more informative related synonyms used by the curator.
