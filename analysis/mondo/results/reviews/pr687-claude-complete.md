---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 687
agent: std_opencode_gpt
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.583
precision: 0.538
recall: 0.636
jaccard: 0.412
outcome: partial_success
failure_modes: [under_editing, wrong_pattern, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly read the issue thread, recognized the curator consensus (relabel rather than obsolete), and relabeled MONDO:0023124 to "Dursun syndrome" with the two issue-specified xrefs. The metadiff F1=0.583 (P=0.538, R=0.636) is roughly **accurate to slightly over-represents** quality here: the core relabel and both xrefs are correct, but the agent both under-edited (missed the def, the G6PC3 logical definition, and the obsolete-date deletion) and mishandled the existing GARD synonyms by re-sourcing/dropping them — a genuine modeling error, not just a stylistic divergence. (Identical run to eval PR #742; same blob `181b71d`.)

## Strengths

- Relabeled `name: Dursun syndrome` and demoted the old label to `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [OMIM:612541]` — byte-identical to the gold synonym, including the correct `OMIM:612541` source (several other attempts mis-sourced this to GARD or PMID).
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` and `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}` exactly as MeeSiing/kanems specified in the issue comments (includedEntryInOMIM for the OMIM "included" entry; equivalentObsolete for the deprecated ORPHA ID).
- Correctly removed the obsoletion machinery: the scheduled-obsoletion `comment:` and `subset: obsoletion_candidate`.
- Did not invent a parent change or an unsourced definition — kept `is_a: MONDO:0002254 ! syndromic disease` (the gold also keeps this), avoiding the over-reach seen in pr443/pr188.
- Followed the issue discussion rather than the original obsoletion title, and (per the #742 PR comment for this same run) validated with `robot convert`.

## Issues

- Error / wrong_pattern: mishandled the two pre-existing GARD synonyms. The gold leaves `synonym: "familial PAH, leucopenia and ASD" RELATED [GARD:0010455]` and `synonym: "familial pulmonary arterial hypertension, leucopenia and ASD" RELATED [GARD:0010455]` untouched. The agent **deleted** the first GARD synonym entirely and **re-sourced** the second to `RELATED [OMIM:612541]`. Re-attributing an existing GARD-derived synonym to OMIM is an unjustified provenance change, and dropping a valid synonym loses information; this is a real modeling error, not just a metadiff artifact.
- Omission (under_editing): did not add the gold's OMIM-sourced `def:` ("A syndromic disease caused by mutation in the G6PC3 gene..."), the comma-variant EXACT synonyms, or the G6PC3 logical definition (`intersection_of: MONDO:0002254` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:24861` + the matching `relationship:`). These go beyond the literal issue ask (relabel + xrefs) and are a defensible conservative scope, but they are the bulk of the lost recall.
- Omission (missed_requirement): retained `property_value: IAO:0006012 "2026-02-01"`, the obsoletion-date stamp; the gold removes it as part of un-scheduling the obsoletion. Leaving it is internally inconsistent with the relabel decision.
- Minor scope: removed the GARD `property_value: seeAlso` line, which the gold curator chose to keep. Defensible (the GARD page is the broken link cited as the obsoletion rationale) but diverges from gold and is one of the false-positive deletions lowering precision.
- Net: the headline relabel + xrefs are mergeable, but a curator would need to restore/repair the GARD synonyms, drop the obsolete-date property, and add the definition and logical axiom — more rework than the joint-best kimi attempt (#262) required.
