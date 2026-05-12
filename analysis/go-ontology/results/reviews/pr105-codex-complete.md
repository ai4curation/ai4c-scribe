---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 105
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
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
  - missed_requirement
  - over_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/105
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 105 --repo ai4curation/eval-ont-agent-go
-->

## Summary
The agent correctly added a new cellular component term, `GO:7770070 p24 cargo receptor complex`, as a child of `GO:0062137 cargo receptor complex`, so it captured the main intent of issue #31295. The metadiff score is moderate (F1 0.636, precision 0.583, recall 0.700) and is directionally fair: the agent solved the core new-term request but missed an important relationship and diverged on synonyms/references.

## Strengths
- Added the requested term `GO:7770070 p24 cargo receptor complex` in the correct namespace, `cellular_component`.
- Used the requested parent `is_a: GO:0062137 ! cargo receptor complex`.
- Included a reasonable definition tying the complex to the p24 protein family, ER-to-Golgi cycling, COPII-mediated transport, and GPI-anchored protein cargo.
- Preserved the issue tracker metadata with `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31295" xsd:anyURI`.
- Cited the three PMIDs supplied in the issue (`PMID:27569046`, `PMID:32456004`, `PMID:34647572`) and avoided adding an unsupported logical `intersection_of`.

## Issues
- Omitted the structural relationship added in the human PR: `relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport`. This is not just a line-level mismatch; the human PR explicitly modeled `GO:7770070` after sibling cargo receptor complex precedent, and the agent's own PR narrative claimed it had added this relation even though the diff did not.
- Under-cited the term relative to the accepted solution. The human PR included `PMID:19566487` and `PMID:26224213` in addition to the three requester-supplied references, supporting the broader p24 complex composition/biology in the final definition.
- Missed useful synonyms from the human solution: `Emp24-Erv25 complex` RELATED, `p24 family complex` RELATED, and `TMED complex` RELATED.
- Added alternate EXACT synonyms not present in the human PR: `p24 family protein complex` and `p24 protein complex`. These are not necessarily invalid, but `p24 family protein complex` is more ambiguous than the human's RELATED `p24 family complex`, so this is mild over-editing.
- The final definition is serviceable but less aligned with the reviewed human wording. It lacks the explicit "conserved, hetero-oligomeric (often tetrameric)" characterization and the typical alpha/beta/gamma/delta subfamily composition included in the accepted `GO:7770070` definition.
