---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 204
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.887
precision: 0.895
recall: 0.879
jaccard: 0.797
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/204
-->

## Summary

The agent got the core obsoletion right — all five terms obsoleted with the correct `replaced_by` targets — but made two substantive deviations from the issue spec and gold PR: it added the four MetaCyc variant IDs to GO:0061678 as plain `xref` lines instead of `{source="skos:narrowMatch"}` xrefs, and it deleted historical `created_by`/`creation_date` provenance (and the unrelated issue #28392 tracker) from several stanzas. F1=0.887 modestly over-represents quality here: the missing SKOS qualifier is an explicit, named requirement in the issue, and line-overlap scoring underweights that single-token-but-semantically-important omission.

## Strengths

- Correctly obsoleted GO:0009255, GO:0061679, GO:0061680, GO:0061681 with `replaced_by: GO:0061678`: obsolete name/def prefixes, `is_obsolete: true`, issue #31916 tracker, and removal of `is_a`/`intersection_of` axioms, term-level MetaCyc xrefs, and the GO:0061679 RELATED synonym.
- Correctly obsoleted GO:0061688 with `replaced_by: GO:0006096`, applying the curator-agreed target from the issue discussion and stripping the active glycolytic axioms (`is_a`, `intersection_of`, `starts_with GO:0061678`).
- Removed the grouping-class `xref: MetaCyc:Entner-Doudoroff-Pathways` from GO:0061678 and added the correct four variant MetaCyc IDs (PWY-8004, NPGLUCAT-PWY, PWY-2221, ENTNER-DOUDOROFF-PWY) — the right identifiers, just not the right xref form.
- PR comment includes a useful annotation-impact breakdown (4 EXP on GO:0009255; 10 CGD IEAs on GO:0061688) and flags the CGD/PomBase mismatch, consistent with the curator discussion.

## Issues

- Missed requirement / wrong pattern (most important): the issue explicitly states "The individual MetaCyc IDs should be made narrowMatch xrefs on the parent term GO:0061678", and the gold PR encodes them as `xref: MetaCyc:... {source="skos:narrowMatch"}`. The agent emitted bare `xref: MetaCyc:PWY-8004` etc., dropping the SKOS mapping semantics entirely. This is a real semantic loss, not a style choice.
- Over-editing / metadata loss: the agent deleted `created_by: dph` and `creation_date` from GO:0061679, GO:0061680, GO:0061681, and GO:0061688, which the gold PR preserved. Historical creation provenance should be retained on obsoleted terms.
- Over-editing: the pre-existing `property_value: term_tracker_item ".../28392"` on GO:0061680 — unrelated to this issue — was removed. The gold PR keeps it.
- Style: obsoletion comments are acceptable but less specific than the gold PR's, which explicitly ties the obsoletions to MetaCyc variant pathways / GO-CAM representation and gives a clearer GO:0061688 annotation rationale.
