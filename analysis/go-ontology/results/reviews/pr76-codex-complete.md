---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 76
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 0.714
recall: 0.625
jaccard: 0.5
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31636
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31925
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/76
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 76 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the core request for `GO:1990334` by renaming `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`, adding the two requested narrow synonyms, revising the definition, and adding the issue tracker property. The moderate metadiff (`F1=0.667`, precision `0.714`, recall `0.625`) reflects real divergence from the accepted PR: the agent's solution is mostly correct but less disciplined than the human solution, with extra synonym/provenance edits and a broader definition rewrite.


## Strengths

- Edited the correct term, `GO:1990334`, and changed the primary label to the requested species-agnostic `SIN/MEN two-component GAP complex`.
- Preserved the existing asserted classification: `is_a: GO:1902773 ! GTPase activator complex` and `part_of GO:0005816 ! spindle pole body`, matching the accepted PR.
- Added `synonym: "Bfa1-Bub2 complex" NARROW []`, preserving the former budding yeast-specific label as a narrow synonym.
- Added `synonym: "Byr4-Cdc16 GAP complex" NARROW [...]`, covering the fission yeast-specific synonym requested in the issue.
- Revised the definition so that it no longer describes only Tem1/MEN biology and instead includes both MEN and SIN / Tem1 and Spg1 terminology.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31636" xsd:anyURI`, matching the traceability update in the accepted PR.


## Issues

- Over-edited the definition relative to a simple synonym/label update. The accepted PR made a conservative species-agnostic edit while retaining the original structure and the spindle-orientation wording; the agent rewrote the definition as a broader statement about coordinating mitotic exit and cytokinesis with "spindle position or chromosome attachment", which was not requested in issue #31636 and is a semantic expansion beyond the human solution.
- Changed definition provenance from `[GOC:bhm, PMID:16449187]` to `[PMID:16449187, PMID:18252797]`, dropping the existing `GOC:bhm` attribution and adding a new PMID. That may be defensible if the new paper was checked, but it is unrequested scope for this issue and differs from the accepted PR, which explicitly retained the existing provenance.
- Added an extra narrow synonym, `synonym: "Bub2-Bfa1 complex" NARROW [PMID:16449187]`, which was not requested and was not present in the accepted PR. The synonym is plausibly useful as a reversed-order variant, but it is still scope expansion in a simple requested update.
- The PR commentary claimed definition provenance was kept unchanged, but the actual diff added `PMID:18252797` and removed `GOC:bhm`, so the agent's reported methodology did not fully match its committed ontology edit.
