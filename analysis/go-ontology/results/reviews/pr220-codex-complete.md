---
ontology: go-ontology
issue_number: 32046
pr_number: 32047
eval_repo_pr: 220
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.774
precision: 0.8
recall: 0.75
jaccard: 0.632
outcome: partial_success
failure_modes:
  - wrong_term
  - wrong_pattern
  - under_editing
  - scope_creep
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32046
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32047
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/220
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32046 --repo geneontology/go-ontology
    gh pr diff 32047 --repo geneontology/go-ontology
    gh pr diff 220 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the core of geneontology/go-ontology#32046 by creating both requested molecular-function terms, `GO:7770072` double-stranded RNA immune receptor activity and `GO:7770073` left-handed Z-RNA immune receptor activity, with the correct parent-child relationship. The metadiff score (`f1: 0.774`, `precision: 0.8`, `recall: 0.75`) is directionally fair: the main terms are present, but the agent missed an important logical axiom from the human PR and introduced extra or incorrect modeling details.


## Strengths

- Created the two expected new terms with the correct IDs and labels: `GO:7770072` double-stranded RNA immune receptor activity and `GO:7770073` left-handed Z-RNA immune receptor activity.
- Correctly placed `GO:7770072` under `GO:0038187` pattern recognition receptor activity, matching the requested broader pattern-recognition receptor class.
- Correctly made `GO:7770073` an `is_a` child of `GO:7770072`, representing left-handed Z-RNA recognition as a specialized form of double-stranded RNA immune receptor activity.
- Included the core exact synonyms from the request/human solution: `dsRNA immune receptor activity` for `GO:7770072` and `Z-RNA immune receptor activity` for `GO:7770073`.
- Preserved the requested PMID evidence sets for the definitions: `PMID:33243852`, `PMID:34678144`, and `PMID:23273991` for `GO:7770072`, and `PMID:32200799` for `GO:7770073`.
- Added the expected `term_tracker_item` metadata linking both new terms to issue `32046`.


## Issues

- `GO:7770072` is missing the accepted logical input axiom `intersection_of: has_primary_input CHEBI:67208 ! double-stranded RNA`. The human PR used this to make the dsRNA input explicit, while the agent left the term with only `intersection_of: GO:0038023 ! signaling receptor activity`.
- The agent added `relationship: has_part GO:0043548 ! double-stranded RNA binding` on `GO:7770072`, but `GO:0043548` is not the double-stranded RNA binding term; the human PR used `GO:0003725`. This is a substantive wrong-term error, not just a diff mismatch.
- The agent kept "transmitting the signal across the cell membrane" in both definitions. That phrase came from the issue request, but the merged human PR deliberately removed it, which is more appropriate for cytosolic dsRNA/Z-RNA sensors such as IFIH1/MDA5 and ZBP1.
- The `GO:7770073` definition omits the explanatory sentence from the human PR: Z-RNA is a left-handed double-helical conformation of RNA with a zigzag phosphate backbone. The shorter agent definition is understandable, but less clear for users distinguishing Z-RNA from generic dsRNA.
- The agent added unrequested broad synonyms, `dsRNA receptor activity` and `Z-RNA receptor activity`. These are plausible search aids, but they broaden away from the immune-receptor specificity and were not part of the accepted solution.
- The extra `intersection_of: GO:0038023 ! signaling receptor activity` on `GO:7770073` is redundant with its parentage under `GO:7770072` and was not used in the human PR. It is not as harmful as the wrong binding term, but it shows weaker pattern discipline.
