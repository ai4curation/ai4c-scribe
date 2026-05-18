---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 264
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.872
precision: 0.773
recall: 1.0
jaccard: 0.773
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second kimi-k2.6 / opencode run, byte-identical in its final blob (`be61acc`) to attempt #591 — same F1 0.872, precision 0.773, recall 1.000. The OMIM-driven merge of MONDO:0008549 "thoracic dysostosis, isolated" into MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" (issue #9826, OMIM:187750 MOVED TO OMIM:621260) is correct and complete. The F1 under-represents quality: the only divergence from gold is the human's opportunistic enrichment (a free-text `def:` and a new `intersection_of` logical definition) the merge request never asked for, plus a principled non-transfer of the redundant hereditary-disease parent.

## Strengths

- Obsoleted MONDO:0008549 stanza byte-equivalent to gold: `name: obsolete thoracic dysostosis, isolated`, `property_value: IAO:0000231 MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`. No stray `alt_id`, no residual def/comment/subset.
- Scheduling cruft (`subset: obsoletion_candidate`, merge-schedule `comment:`, `IAO:0006012 "2026-03-01"`) correctly removed rather than carried onto the survivor.
- Synonym evidence repaired to `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold exactly (not the owltools-default `[MONDO:0008549]` self-citation).
- Xrefs transferred with correct precision qualifiers: `xref: MESH:C566063 {source="MONDO:equivalentTo"}`, `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}` — identical to gold.
- Transferred the `property_value: IAO:0000233` issue-tracker link onto the survivor, matching gold (a piece the gpt-5.4 attempts #693/#749 missed).
- Methodology mirrors #591 (same blob): documented `owltools --obsolete-replace`, `make NORM`, `robot convert`, and six targeted merge QC SPARQL queries with 0 violations, plus a grep sweep confirming no dangling MONDO:0008549 references.

## Issues

- Style/under-edit vs gold (defensible): deliberately omitted `is_a: MONDO:0003847` "hereditary disease" as redundant against the survivor's more specific `is_a: MONDO:0018770` "Jeune syndrome". Ontologically sound; gold kept the asserted parent, so a minor divergence rather than an error.
- Omission (not derivable from issue, no penalty): no `def:` [OMIM:621260], no `intersection_of` equivalence axiom, no MalaCards `curated_content_resource`. The first two are opportunistic curator enrichment outside the merge SOP; correct conservative scope, accounts for most of the precision gap.
- No genuine errors, no scope creep, no syntax issues. The earlier codex review's `over_editing` tag is mis-scored: recall=1.000 and the agent did *less* than gold's enrichment, not more — `under_editing` at most, and only against non-mandated enrichment.
