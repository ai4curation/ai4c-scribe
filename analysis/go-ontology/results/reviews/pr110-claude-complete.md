---
ontology: go-ontology
issue_number: 27593
pr_number: 31997
eval_repo_pr: 110
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.786
precision: 0.786
recall: 0.786
jaccard: 0.647
outcome: success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_pr_curator_repudiated
scoring_caveat: "Gold PR #31997 reparenting + reaction direction were flagged wrong by curators post-merge; metadiff penalises stylistic divergences (PMID xref lines, synonym, tracker-item ordering) not substance."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The gpt-5.5/opencode attempt is substantively correct against the issue and the gold PR #31997 (F1 = 0.786): it added `GO:7770068` with RHEA:71767 (exactMatch), the three requested PMIDs, parent `GO:0016723`, and reparented/de-siderophored `GO:0000293`. The F1 of 0.786 is driven almost entirely by stylistic divergences from the gold — separate `xref: PMID:...` lines, a different synonym, the `Fe(2+)` charge notation, and a different tracker-item insertion order — none of which are substantive errors. The score under-represents quality relative to the issue; the over-arching caveat is that the gold target itself was curator-repudiated.

## Strengths

- All three explicit issue asks satisfied: new term with RHEA:71767 + PMID:8321236/34614242/39940646; `GO:0000293` reparented under it (direct GO:0016722 link correctly dropped — better is_a hygiene than the kimi attempt); definition siderophore→chelate on both sides.
- Correct collision-safe ID allocation (`GO:7770068`).
- Added the #27593 tracker item to `GO:0000293` (matching the human intent), and added explicit `xref: PMID:...` lines giving the references first-class xref status as well as def provenance — defensible enrichment over the gold.
- Strong methodology: pre/post `make travis_build` both passed (full ODK pipeline, unlike the copilot attempt), RHEA validated against local rhea.rdf.gz, PMID excerpts validated with linkml-reference-validator.
- Flagged the substrate/product asymmetry in ValWood's request with correct chemical reasoning.

## Issues

- Three extra `xref: PMID:...` lines and an extra synonym ("NADPH-dependent ferric iron reductase activity") are the main precision/recall drag vs the gold; these are defensible additions (the PMIDs are legitimately xrefs as well as def refs) rather than errors.
- Tracker-item ordering on `GO:0000293`: inserted #27593 between #21029 and #26726 rather than after #26726 as the human did. Cosmetic, but contributes to the diff distance.
- Used `Fe(2+)`/`NADP(+)` parenthesised charge notation rather than the gold's `Fe2+`/`NADP+`; both are seen in GO but this diverges from the requested form and the sibling terms; minor style.
- Inherits the gold's structural defect (inverted `GO:0000293 is_a GO:7770068`, oxidation-direction reaction) — followed the issue instruction faithfully; the resulting ontology is the one curators later rejected.
