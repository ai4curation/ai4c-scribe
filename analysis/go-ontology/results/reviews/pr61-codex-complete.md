---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 61
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.826
precision: 0.95
recall: 0.731
jaccard: 0.704
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/61
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 61 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed the main request from issue #31945: it obsoleted GO:0003400, set `replaced_by: GO:0048208`, renamed GO:0048208 to "COPII vesicle coat assembly", and renamed GO:0006901 to "vesicle coat assembly". The metadiff score (F1 0.826, precision 0.95, recall 0.731) is a fair signal that the core ontology edit is close to the human PR, but the agent made additional file edits and dropped provenance metadata that the human solution preserved.


## Strengths

- Correctly obsoleted GO:0003400 `regulation of COPII vesicle coating` by changing the label to the obsolete form, adding `is_obsolete: true`, adding a `term_tracker_item` for issue #31945, and adding `replaced_by: GO:0048208`.
- Correctly removed the logical definition from GO:0003400 (`intersection_of: GO:0065007` and `intersection_of: regulates GO:0048208`), which is appropriate for an obsolete term.
- Correctly implemented the requested label cleanup for GO:0048208, making "COPII vesicle coat assembly" the primary name and retaining "COPII vesicle coating" as an exact synonym.
- Correctly implemented the broader label cleanup for GO:0006901, making "vesicle coat assembly" the primary name and retaining "vesicle coating" as an exact synonym.
- Updated inline parent-label comments for children of GO:0006901, including GO:0016183 `synaptic vesicle coating` and GO:0048200 `Golgi transport vesicle coating`, so the OBO comments remain consistent with the new GO:0006901 label.


## Issues

- The agent removed `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` from GO:0003400. The human PR preserved these lines, and retaining original creation metadata is preferable because obsoletion should not erase term provenance.
- The obsoletion comment for GO:0003400 is less accurate than the human PR's comment. The agent wrote that the term "is equivalent to COPII vesicle coat assembly", but the issue rationale was that existing annotations represent proteins that are part of the pathway rather than upstream regulators; equivalence is not quite the stated biological reason.
- The agent edited additional tracked files outside the human PR: `docs/patterns/cc_assembly.md`, `src/design_patterns/cc_assembly.tsv`, `src/design_patterns/regulation.tsv`, `src/design_patterns/regulation_by.tsv`, and `src/ontology/ld.txt`. Some label updates are defensible, but the human solution deliberately limited the committed change to `src/ontology/go-edit.obo`, so these extra edits reduce scope discipline and may touch generated/derived artifacts unnecessarily.
