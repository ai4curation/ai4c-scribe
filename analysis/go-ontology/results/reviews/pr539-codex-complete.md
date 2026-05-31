---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 539
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.636
precision: 0.583
recall: 0.7
jaccard: 0.467
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32044
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32054
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/539
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32044 --repo geneontology/go-ontology
    gh pr diff 32054 --repo geneontology/go-ontology
    gh pr diff 539 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent added the requested `GO:7770074` term and captured the core biological distinction of O-GlcNAcylation as a single GlcNAc addition that is not elongated. It missed the sibling `GO:0016266` harmonization and used slightly different definition/synonym wording from the human PR, including an extra `protein O-GlcNAcylation` synonym. This is a partial success: the new term is usable in broad outline, but the patch does not fully match the accepted GO edit.


## Strengths

- Correctly created a new `GO:7770074` stanza rather than altering an unrelated existing term.
- Correctly used the requested label and parent `GO:0006493`.
- The definition includes the key biochemical features: single N-acetylglucosamine, beta-glycosidic bond, serine/threonine protein side chain, and no larger oligosaccharide extension.
- Added `PMID:35536957`, the issue tracker, and exact synonyms for GlcNAcylation/N-acetylglucosaminylation concepts.


## Issues

- Missed the `GO:0016266` sibling change from `N-acetyl-galactosamine` to `N-acetylgalactosamine`, the old-label synonym, and the tracker addition.
- The definition starts with `starting with the covalent linkage...`, while the human PR used `in which a single N-acetylglucosamine is covalently linked...`; the agent wording is close but less direct.
- The synonym set differs: it adds `protein O-GlcNAcylation` and uses a hyphenated `protein O-linked-N-acetylglucosaminylation` form instead of the accepted spacing.
- `created_by` and `creation_date` do not match the curator-authored human PR.
