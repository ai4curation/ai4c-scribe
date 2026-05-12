---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 125
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/125
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 125 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology diff matches the human PR in all functional edits: obsolete label and definition prefix, removal of the `is_a: GO:0016616` parent, `term_tracker_item`, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-represents the practical quality, because the mismatch is just a shorter obsoletion comment.


## Strengths

- The agent selected the correct target term, `GO:0043713`, and the correct replacement term, `GO:0140175`, exactly as requested in issue `#31966`.
- It followed the standard GO obsoletion pattern: prefixed the term name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a` parent to `GO:0016616`, added `is_obsolete: true`, and retained the `molecular_function` namespace.
- It added `replaced_by: GO:0140175`, which is the important migration aid for a term whose activity is covered by the broader EC-aligned `GO:0140175`.
- It added the correct tracker link, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- The agent's PR rationale shows it understood the biochemical basis for the obsoletion: `GO:0140175` has `EC:1.1.1.345` as an exact match and includes `RHEA:10052` as a narrow match, corresponding to the reaction described by `GO:0043713`.


## Issues

- The obsoletion comment is less informative than the human PR's comment. The human version explicitly records that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that `EC:1.1.1.345` is an exact-match xref on `GO:0140175`, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader `GO:0140175` reaction. The agent's shorter comment is still correct, but it preserves less curator-facing justification in the ontology.
- No substantive ontology error found. The shorter comment accounts for the non-perfect metadiff score, but it does not change the correctness of the obsoletion or replacement.
