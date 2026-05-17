---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 60
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.818
recall: 1.0
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second gpt-5.5 / opencode run, byte-identical in its final blob (`1232042`) to attempt #81 — same F1 0.900, precision 0.818, recall 1.000. The merge of MONDO:0008549 into MONDO:0979242 is correct and complete: obsoleted stanza reduced to the canonical gold six lines, synonym and xrefs and MalaCards resource transferred to the survivor, scheduling metadata stripped. As in #81, the only divergence from gold is the deliberate non-transfer of the redundant `is_a: MONDO:0003847` "hereditary disease" parent, which the agent justifies as redundant against the survivor's more specific `is_a: MONDO:0018770` "Jeune syndrome". F1 modestly under-represents the quality of this correct, well-reasoned merge.

## Strengths

- Obsoleted MONDO:0008549 stanza identical to gold: `MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`; all scheduling cruft (`obsoletion_candidate` subset, merge-schedule comment, `IAO:0006012`) correctly removed.
- Synonym evidence repaired to `[OMIM:187750]`, matching gold; the PR comment explicitly notes replacing the owltools-generated `[MONDO:0008549]` self-citation (it states `[MESH:C566063]` in prose but the actual diff correctly uses `[OMIM:187750]`).
- Xrefs `MESH:C566063` / `OMIM:187750` transferred with correct `MONDO:equivalentTo` / `MONDO:equivalentObsolete` precision qualifiers, matching gold.
- Sound, documented methodology: `make NORM`, targeted merge QC SPARQL via `robot verify` (0 violations), explicit grep sweep confirming no remaining references to MONDO:0008549 outside its own obsolete stanza, honest note that OMIM pages were network-blocked but issue + existing xrefs corroborated the merge.
- Principled scope discipline: the dropped `is_a: MONDO:0003847` is reasoned, not accidental.

## Issues

- Style/under-edit vs gold (defensible): omitted the `is_a: MONDO:0003847` "hereditary disease" parent that gold retained — sole driver of the gap from F1=1.0. Ontologically defensible (redundant superclass) but diverges from MONDO's tendency to keep asserted parents.
- Minor PR-comment inaccuracy: the prose claims the synonym citation was set to `[MESH:C566063]`, while the actual (correct) diff uses `[OMIM:187750]`. The diff is right; only the description is imprecise.
- Omission of `def:` and `intersection_of` — same as every attempt, out of scope for a merge request, correctly conservative.
- Outcome set to `success`: the merge is fully and correctly done; the lone divergence is a principled judgement, not a notable defect.
