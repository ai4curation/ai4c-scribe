---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 81
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.941
precision: 1.0
recall: 0.889
jaccard: 0.889
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/30894
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32011
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/81
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 30894 --repo geneontology/go-ontology
    gh pr diff 32011 --repo geneontology/go-ontology
    gh pr diff 81 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent largely solved issue `#30894` by adding the requested new biological process term `GO:7770069 ferritinophagy` with the same core content as the accepted human PR: label, definition, synonym, parent, references, and tracker metadata. The metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) accurately reflects a near-match, but the mismatch is not just cosmetic: the agent added an extra cargo relationship that the accepted PR deliberately avoided for consistency with sibling selective macroautophagy terms.


## Strengths

- Correctly created `GO:7770069` in the `biological_process` namespace with primary label `ferritinophagy`, rather than using the issue's suggested label text `Ferritin-specific autophagy`.
- Used the accepted definition, `"The selective degradation of ferritin to release iron by macroautophagy."`, with the same three supporting references: `PMID:25327288`, `PMID:26436293`, and `PMID:38714719`.
- Correctly placed the term under `GO:0016236 macroautophagy`, which is more specific than the issue's suggested parent `GO:0006914 autophagy` and matches the merged human PR.
- Preserved the issue wording as an exact synonym: `"ferritin-specific autophagy" EXACT []`.
- Added standard provenance metadata, including `term_tracker_item` pointing to `https://github.com/geneontology/go-ontology/issues/30894`, `created_by`, and `creation_date`.
- The agent's PR notes show reasonable methodology: it checked existing selective macroautophagy siblings and decided not to add an `intersection_of` logical definition.


## Issues

- The agent added `relationship: has_primary_input GO:0070288 ! ferritin complex`, which is absent from the accepted human PR. The human PR explicitly kept `GO:7770069` as a plain child of `GO:0016236 macroautophagy` to match sibling selective macroautophagy terms such as mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, and nucleophagy.
- The extra `has_primary_input` assertion is biologically plausible, but it is over-editing for this issue and creates a pattern inconsistency: `GO:7770069 ferritinophagy` would be the only comparable selective macroautophagy term with a cargo relationship.
- The agent's written rationale says it avoided over-specific logical modeling, but the final diff still includes the cargo relationship. That mismatch suggests the agent understood the broader pattern but failed to keep the actual edit aligned with its own stated modeling decision.
