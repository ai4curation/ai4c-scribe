---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 262
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.727
precision: 0.615
recall: 0.889
jaccard: 0.571
outcome: partial_success
failure_modes: [under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly read the issue thread, recognized the curator consensus (relabel rather than obsolete), and produced a clean, conservative relabel of MONDO:0023124 to "Dursun syndrome". The metadiff F1=0.727 (P=0.615, R=0.889) is the joint best of the 10 attempts and slightly **under-represents** quality: every change the agent made is correct and matches the gold; the lost recall is entirely from the gold's *additional* enrichment (a definition and a full G6PC3 logical definition) that the issue never explicitly requested.

## Strengths

- Relabeled `name: Dursun syndrome` and demoted the old label to `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [OMIM:612541]` — byte-identical to the gold synonym, including the correct `OMIM:612541` source (most other attempts mis-sourced this to GARD or PMID).
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` and `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}` exactly as MeeSiing/kanems specified in issue comments (includedEntryInOMIM + equivalentObsolete for the deprecated ORPHA ID).
- Correctly removed the obsoletion machinery: `comment:` (scheduled obsoletion), `subset: obsoletion_candidate`, and `property_value: IAO:0006012 "2026-02-01"`.
- Crucially **did not** invent a parent change or a definition it could not source — it kept `is_a: MONDO:0002254 ! syndromic disease` (the gold also kept this), avoiding the over-reach seen in pr443/pr188/pr134/pr115.
- Validated with `robot convert` and `make NORM`.

## Issues

- Omission (the source of the lost recall, not an error): did not add the OMIM-sourced `def:`, the second comma-variant EXACT synonym, or the gold's G6PC3 logical definition (`intersection_of: MONDO:0002254` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:24861` + the matching `relationship:`). These are genuine value-adds in the gold but go beyond the literal issue ask (relabel + xrefs); a defensible conservative scope.
- Minor scope: removed the GARD `property_value: seeAlso` line, which the gold curator chose to keep. Defensible (the GARD page is the broken link cited as the obsoletion rationale in the issue) but diverges from gold and is the single false-positive deletion lowering precision.
- Net: a clean, mergeable-with-light-enrichment result; the only thing a curator would add is the definition and logical axiom.
