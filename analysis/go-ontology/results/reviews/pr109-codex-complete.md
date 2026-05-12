---
ontology: go-ontology
issue_number: 32046
pr_number: 32047
eval_repo_pr: 109
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.765
precision: 0.867
recall: 0.684
jaccard: 0.619
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32046
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32047
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/109
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32046 --repo geneontology/go-ontology
    gh pr diff 32047 --repo geneontology/go-ontology
    gh pr diff 109 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the core request by adding both requested molecular function terms, `GO:7770072` double-stranded RNA immune receptor activity and `GO:7770073` left-handed Z-RNA immune receptor activity, with the same parent-child structure as the human PR. The metadiff score (F1 0.765, precision 0.867, recall 0.684) is a fair signal: the main ontology edits match, but the agent added extra lines and missed one useful definitional refinement from the human solution. Overall this is a partial success because the terms are largely correct, but the agent over-edited with unrequested broad synonyms and an extra asserted relationship.


## Strengths

- Added the two requested new terms with the correct IDs and names: `GO:7770072` double-stranded RNA immune receptor activity and `GO:7770073` left-handed Z-RNA immune receptor activity.
- Correctly placed `GO:7770072` under `GO:0038187` pattern recognition receptor activity, matching the issue request and the human PR.
- Correctly made `GO:7770073` a child of `GO:7770072`, representing left-handed Z-RNA recognition as a more specific form of double-stranded RNA immune receptor activity.
- Used the same core logical pattern as the human PR for `GO:7770072`: `intersection_of GO:0038023` signaling receptor activity and `intersection_of has_primary_input CHEBI:67208` double-stranded RNA, plus `relationship: has_part GO:0003725` double-stranded RNA binding.
- Included the requested/supporting PMIDs on the definitions: `PMID:23273991`, `PMID:33243852`, and `PMID:34678144` for the dsRNA term, and `PMID:32200799` for the Z-RNA term.
- Appropriately removed the issue's "across the cell membrane" phrase from both definitions, as did the human PR, because the cited sensors include cytosolic/nuclear receptors rather than only membrane-spanning receptors.
- Included standard metadata on both terms: `term_tracker_item`, `created_by`, and `creation_date`.


## Issues

- The agent added unrequested broad synonyms to both terms: `double-stranded RNA receptor activity`, `dsRNA receptor activity`, `left-handed Z-RNA receptor activity`, and `Z-RNA receptor activity`. These are plausible search synonyms, but they broaden away from the immune-receptor specificity in the requested labels and were not present in the human PR.
- The agent asserted `relationship: has_part GO:0003725 ! double-stranded RNA binding` directly on `GO:7770073`. Since `GO:7770073` is already a child of `GO:7770072`, which has this relationship, this is at best redundant; the human PR deliberately left the Z-RNA term without an additional logical definition or binding relationship because there is no specific ChEBI class or GO binding term for left-handed Z-RNA.
- The definition for `GO:7770073` is less informative than the human PR. The human solution added the explanatory sentence that Z-RNA is a left-handed double-helical conformation of RNA with a zigzag phosphate backbone, which helps distinguish the term from generic dsRNA recognition.
- The `GO:7770072` definition differs slightly from the human PR by saying "double-stranded RNA molecule" rather than "double-stranded RNA". This is minor and probably harmless, but it is not the accepted wording.
