---
ontology: go-ontology
issue_number: 31923
pr_number: 31938
eval_repo_pr: 181
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: other
difficulty: simple
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - instruction_violation
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31923
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31938
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/181
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31923 --repo geneontology/go-ontology
    gh pr diff 31938 --repo geneontology/go-ontology
    gh pr diff 181 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made the core biological edit requested in issue #31923: it updated the definition of GO:0045022 "early endosome to late endosome transport" to remove the over-specific microtubule-dependent gloss. The human PR made the same definition change but also added a `term_tracker_item` pointing to issue #31923, which the agent omitted despite the GO agent metadata instructions requiring tracker links for modified terms. The metadiff F1 of 0.8 is directionally fair: the substantive ontology text is correct, but the solution is incomplete on required metadata.


## Strengths

- Correctly identified GO:0045022 as the only term requiring an ontology edit for this issue.
- Removed exactly the problematic definition clause, changing the definition from one that asserted microtubule-dependent transport to the narrower and taxon-neutral definition: "The directed movement of substances, in membrane-bounded vesicles, from the early sorting endosomes to the late sorting endosomes."
- Preserved the existing definition xrefs, `ISBN:0815316194` and `PMID:29980602`, and did not invent new provenance.
- Left the logical definition intact: `GO:0016192` with `has_target_start_location GO:0005769`, `has_target_end_location GO:0005770`, and `occurs_in GO:0005737`. That was appropriate because the issue was only about the textual mechanistic gloss.
- Maintained good scope discipline on biological content: no unnecessary synonym, relationship, or classification changes.


## Issues

- Missing required tracker metadata. The human PR added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31923" xsd:anyURI` to GO:0045022 while preserving the existing #26386 tracker link. The agent did not add this line.
- The omission appears to be an instruction-following error, not just a stylistic difference. The GO agent configuration says to link back to the issue being addressed using `term_tracker_item`; the agent instead stated that no metadata updates were needed because this was an existing term. That correctly applies to `created_by` and `creation_date`, but not to `term_tracker_item`.
- No biological or syntax errors were evident in the agent diff. The weakness is under-editing relative to GO metadata practice, not an incorrect term edit.
