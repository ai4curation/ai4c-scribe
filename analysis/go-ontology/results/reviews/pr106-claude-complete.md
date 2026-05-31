---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 106
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.965
precision: 0.965
recall: 0.965
jaccard: 0.932
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/106
-->

## Summary

The agent fully resolved issue #31916. It obsoleted the four Entner-Doudoroff variant terms with `replaced_by: GO:0061678`, obsoleted GO:0061688 with `replaced_by: GO:0006096`, and reworked the GO:0061678 MetaCyc mappings into `{source="skos:narrowMatch"}` xrefs as specified. The substantive edits are identical to gold PR #32024 (and to sibling runs #65 and #85 — same blob `8854823`). F1=0.965 slightly under-represents quality; deltas are limited to comment wording and one extra tracker line.

## Strengths

- All four issue-requested variants (GO:0009255, GO:0061679, GO:0061680, GO:0061681) obsoleted correctly: obsolete name/def prefixes, `is_obsolete: true`, `replaced_by: GO:0061678`, issue #31916 tracker, and complete removal of `is_a`/`intersection_of`/term-level MetaCyc xrefs and the GO:0061679 RELATED synonym.
- GO:0061688 obsoleted with `replaced_by: GO:0006096`, correctly applying the curator-agreed decision (raymond91125 + sjm41) from the issue comments, with its active glycolytic axioms stripped.
- GO:0061678 mapping cleanup exactly correct: grouping-class xref removed and all four variant MetaCyc IDs added with the `{source="skos:narrowMatch"}` qualifier — matching the gold PR precisely on the trickiest requirement.
- Existing issue #28392 tracker and `created_by`/`creation_date` provenance preserved on the obsoleted variants, avoiding the metadata-loss failure mode seen in weaker runs on this case.
- Clear PR/issue comment documenting the obsoletion + mapping rationale, consistent with the issue's stated intent (variants better represented as GO-CAMs).

## Issues

- Style only: obsoletion comments use a generic GO-CAM phrasing rather than the gold PR's more specific text naming GO:0061678 and MetaCyc variant pathways. No ontological impact.
- Minor scope: extra `property_value: term_tracker_item ".../31916"` added to the still-active GO:0061678, not present in the human PR. Harmless traceability metadata; the only reason F1 is below 1.0.
- No correctness, syntax, or completeness problems.
