---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 201
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.016
precision: 0.008
recall: 0.8
jaccard: 0.008
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - wrong_pattern
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/201
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 201 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly identified `GO:0010381` (`peroxisome-chloroplast membrane tethering`) as the term to obsolete and made the core stanza-level obsoletion edit. However, it used `replaced_by: GO:7770065` where the human PR deliberately used `consider: GO:7770065`, and it missed the taxon-constraint removals that accompany obsoleting this BP term. The very low metadiff score (`f1=0.016`, precision `0.008`, recall `0.8`) overstates the failure because the main term edit is recognizable, but the remaining differences are real curation issues.


## Strengths

- Correctly changed the label for `GO:0010381` to `obsolete peroxisome-chloroplast membrane tethering`.
- Correctly marked `GO:0010381` with `is_obsolete: true` and removed its asserted parent `is_a: GO:0140056` (`organelle localization by membrane tethering`).
- Correctly prefixed the definition with `OBSOLETE.` while preserving the original PMID-supported definition text.
- Correctly linked the term to the tracker issue with `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31877" xsd:anyURI`.
- Correctly recognized `GO:7770065` (`peroxisome-chloroplast membrane tether activity`) as the replacement/consideration target requested by the issue.


## Issues

- Used the wrong obsoletion relation for the reannotation target. The human PR used `consider: GO:7770065` because the old term is a biological process (`GO:0010381`) and the target is a molecular function (`GO:7770065`), so automatic replacement via `replaced_by` would be inappropriate.
- Missed the taxon-constraint cleanup. The human PR removed `GO:0010381` from `src/taxon_constraints/never_in_taxon.tsv`, including the `NCBITaxon:28009` Choanoflagellida, `NCBITaxon:33208` Metazoa, `NCBITaxon:4751` Fungi, and `NCBITaxon:554915` Amoebozoa rows.
- Also missed the generated ontology-form taxon constraint removals for `GO:0010381` in `src/taxon_constraints/never_in_taxon.ofn` and the corresponding regenerated `src/ontology/imports/go_taxon_constraints.owl` changes.
- The obsoletion comment is close but less exact than the accepted wording. It says the BP term was "superseded by a more precise molecular function term", while the human PR simply states that the term was made obsolete because it represents a molecular function rather than a biological process.
