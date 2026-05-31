---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 616
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.864
precision: 0.95
recall: 0.792
jaccard: 0.76
outcome: partial_success
failure_modes:
  - over_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly executed the central task — obsoleting `GO:0003400` with `replaced_by: GO:0048208` and renaming both `GO:0048208` and `GO:0006901` to "...coat assembly" with the old labels promoted/restored as EXACT synonyms. However, it made two unrequested edits the gold PR did not: it **rewrote the definitions** of both active terms `GO:0006901` and `GO:0048208`, and it **deleted the `created_by: dph` / `creation_date` provenance** on the obsoleted `GO:0003400`. The metadiff (`f1: 0.864`, `precision: 0.95`, `recall: 0.792`) slightly over-represents quality: the high precision masks the twin def rewrites (which fall in matched context regions), and the recall drop reflects both the legitimate missed comment maintenance and the gratuitous provenance deletion. Same diff as pr667 (blob `d0ad58c`).

## Strengths

- **Obsoletion core is correct:** `name: obsolete regulation of COPII vesicle coating`, `def: "OBSOLETE. ..."` with original dbxrefs preserved, both `intersection_of` axioms removed, `comment` present, `property_value: term_tracker_item ".../issues/31945" xsd:anyURI`, `is_obsolete: true`, and `replaced_by: GO:0048208` — all matching the gold's obsoletion structure.
- **Both renames are semantically correct.** `GO:0048208` → `COPII vesicle coat assembly` with `COPII vesicle coating` restored as `EXACT [GOC:ascb_2009, GOC:dph, GOC:tb]` (dbxrefs match gold), and `GO:0006901` → `vesicle coat assembly` with `vesicle coating` retained as `EXACT []`. Synonym promotion direction matches the gold exactly.
- **Sound, well-documented process.** PR comment shows pre/post `make travis_build` validation, `obo-checkout.pl`/`obo-checkin.pl` workflow, and an accurate change summary. The biological rationale (annotated proteins are part_of the coating pathway, not upstream regulators) is correctly understood.

## Issues

- **Unrequested twin definition rewrites (over-editing, headline problem).** The agent rewrote `GO:0006901`'s def to "The assembly of a protein coat on a vesicle to form the proper shape..." and `GO:0048208`'s def to "The assembly of a COPII vesicle coat on ER membranes during the formation of transport vesicles." The issue and ValWood's comment requested **only label changes**; the gold PR left both definitions untouched. The `GO:0048208` rewrite is the more concerning: it discards the specific "COPII proteins and adaptor proteins" biology and the ISBN/PMID-grounded mechanistic detail in favor of generic phrasing. This is a substantive semantic edit on heavily-annotated active terms that should have been raised in an issue comment, not committed unilaterally.
- **Provenance deletion on the obsoleted term (over-editing / instruction concern).** The agent removed `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` from `GO:0003400`. The gold explicitly **retained** these — GO obsoletion convention preserves original creation provenance. The PR comment's claim of "retained only historical provenance plus obsoletion metadata" is inaccurate; the historical provenance was in fact dropped.
- **Comment text diverges from gold (minor).** The obsoletion `comment` reads "the experimental data can be accurately described using GO:0048208 COPII vesicle coat assembly" rather than the gold's part_of-pathway rationale. Both are defensible obsoletion comments; this is free-text convention difference, not a substantive error.
- **Missed stale-comment maintenance on incoming edges (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183` (synaptic vesicle coating) or `GO:0048200` (Golgi transport vesicle coating), nor the `GO:0048208` self-edge comment that referenced the renamed parent — all updated by the gold. These are non-semantic OBO `!` label comments but leave the file internally inconsistent.

Net: `partial_success` — the obsoletion + dual rename is correct and well-validated, but the twin definition rewrites on active terms plus the dropped creation provenance are real scope/correctness concerns that the high precision metric understates.
