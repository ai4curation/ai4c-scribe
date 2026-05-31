---
ontology: go-ontology
issue_number: 31923
pr_number: 31938
eval_repo_pr: 90
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: other
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31923
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31938
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/90
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31923 --repo geneontology/go-ontology
    gh pr diff 31938 --repo geneontology/go-ontology
    gh pr diff 90 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent exactly matched the merged human solution for issue #31923. It updated `GO:0045022 early endosome to late endosome transport` by removing the over-specific microtubule-dependent gloss from the textual definition and adding the issue tracker metadata. The perfect metadiff score (`F1=1.0`, `precision=1.0`, `recall=1.0`) accurately reflects the quality of this tightly scoped edit.


## Strengths

- Edited the correct term, `GO:0045022 early endosome to late endosome transport`, and did not touch unrelated terms.
- Removed exactly the problematic definition clause identified in the issue: "transport occurs along microtubules and can be experimentally blocked with microtubule-depolymerizing drugs." This resolves the species-neutrality problem raised by the fission yeast actin-dependent counterexample.
- Preserved the useful core definition: directed movement of substances in membrane-bounded vesicles from early sorting endosomes to late sorting endosomes.
- Preserved the existing definition xrefs, `ISBN:0815316194` and `PMID:29980602`, as well as the synonym and logical axioms (`GO:0016192`, `GO:0005769`, `GO:0005770`, and `GO:0005737`).
- Added the expected provenance metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31923" xsd:anyURI`, while retaining the existing tracker link to issue #26386.


## Issues

No issues. The agent's diff is line-for-line identical to the human PR and introduces no extra edits, omissions, wrong-term changes, or syntax problems.
