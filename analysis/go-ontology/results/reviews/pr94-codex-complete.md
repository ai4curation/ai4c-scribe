---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 94
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/94
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 94 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the main request for `GO:1990334`: it renamed `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`, added the requested species-specific narrow synonyms, revised the definition, and added issue tracker provenance. The metadiff score (`F1=0.667`, `precision=0.714`, `recall=0.625`) reflects a mostly correct solution with extra wording and metadata relative to the human PR; it somewhat understates the biological adequacy of the edit, but the agent did over-edit a simple synonym/name update.


## Strengths

- Correctly changed the `GO:1990334` primary label from `Bfa1-Bub2 complex` to the species-agnostic `SIN/MEN two-component GAP complex`, matching both the issue and the human PR.
- Preserved the old budding yeast label as `synonym: "Bfa1-Bub2 complex" NARROW []`, as requested in the issue.
- Added the requested fission yeast synonym, `synonym: "Byr4-Cdc16 GAP complex" NARROW [PMID:18252797]`; the human PR used the same synonym without an xref, so the agent's citation is a defensible support addition.
- Kept the existing ontology placement unchanged: `is_a: GO:1902773 ! GTPase activator complex` and `part_of GO:0005816 ! spindle pole body`.
- Added the expected provenance link, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31636" xsd:anyURI`, matching the human PR's pattern.


## Issues

- The agent over-edited the definition compared with the human PR. The human solution made a minimal species-agnostic revision retaining the original emphasis on Tem1/Spg1, MEN/SIN signaling, mitotic exit, cytokinesis, spindle orientation, and inhibition of MEN/SIN activation; the agent rewrote it more broadly as a "conserved" complex that coordinates cytokinesis with "spindle position or chromosome attachment." That wording may be biologically plausible, but "chromosome attachment" was not in the issue or human PR and is less directly tied to the requested rename.
- Added an extra narrow synonym, `synonym: "Bub2-Bfa1 complex" NARROW [PMID:16449187]`, that was not requested and not present in the human PR. This is not obviously wrong, but for a simple curator-specified synonym update it is an unnecessary scope expansion.
- Added `PMID:18252797` to the definition xrefs and fission yeast synonym while the issue and human PR kept the definition supported only by `PMID:16449187`. The additional PMID supports the Byr4/Cdc16-Spg1 side of the generalized term, but it changes the reference footprint beyond the ground-truth edit.
