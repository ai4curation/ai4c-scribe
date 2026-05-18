---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 667
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

The agent correctly executed the central task — obsoleting `GO:0003400` with `replaced_by: GO:0048208` and renaming both `GO:0048208` and `GO:0006901` to "...coat assembly" with the old labels promoted/restored as EXACT synonyms. However, it made two unrequested edits the gold PR did not: it **rewrote the definitions** of both active terms `GO:0006901` and `GO:0048208`, and it **deleted the `created_by: dph` / `creation_date` provenance** on the obsoleted `GO:0003400`. The metadiff (`f1: 0.864`, `precision: 0.95`, `recall: 0.792`) slightly over-represents quality: the high precision masks the twin def rewrites, and the recall drop conflates the legitimate missed comment maintenance with the gratuitous provenance deletion. This is a byte-identical replay of pr616 (same blob `d0ad58c`, same gpt-5.4/opencode config v9); the assessment is the same. The detailed PR/issue comments here confirm the agent's reasoning.

## Strengths

- **Obsoletion core is correct:** `name: obsolete regulation of COPII vesicle coating`, `def: "OBSOLETE. ..."` with original dbxrefs preserved, both `intersection_of` axioms removed, `comment` present, `property_value: term_tracker_item ".../issues/31945" xsd:anyURI`, `is_obsolete: true`, and `replaced_by: GO:0048208` — all matching the gold's obsoletion structure.
- **Both renames are semantically correct.** `GO:0048208` → `COPII vesicle coat assembly` with `COPII vesicle coating` restored as `EXACT [GOC:ascb_2009, GOC:dph, GOC:tb]` (dbxrefs match gold), and `GO:0006901` → `vesicle coat assembly` with `vesicle coating` retained as `EXACT []`. Synonym promotion direction matches the gold exactly.
- **Strong process transparency.** The PR comment provides a clear changes list, an accurate biological rationale (proteins are part_of the coating pathway, not upstream regulators; ValWood's rename request honored), pre/post `make travis_build` validation, and a completed workflow checklist (`obo-checkout.pl`/`obo-checkin.pl`, term-obsoletion guidance). Honest that RESEARCH/REFERENCE-VALIDATION were not needed for a direct obsoletion.

## Issues

- **Unrequested twin definition rewrites (over-editing, headline problem).** The agent rewrote `GO:0006901`'s def to "The assembly of a protein coat on a vesicle to form the proper shape..." and `GO:0048208`'s def to "The assembly of a COPII vesicle coat on ER membranes during the formation of transport vesicles." The issue and ValWood's comment requested **only label changes**; the gold PR left both definitions untouched. The PR comment explicitly frames this as "Updated the ... definition to align with the new label," which acknowledges the change but mischaracterizes it as in-scope — the issue asked for a label, not a def. The `GO:0048208` rewrite discards the specific "COPII proteins and adaptor proteins" mechanism and ISBN/PMID-grounded detail; this is a substantive edit on heavily-annotated active terms that should have been raised in an issue comment.
- **Provenance deletion on the obsoleted term (over-editing / instruction concern).** `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` were removed from `GO:0003400`. The gold explicitly retained these. The PR comment's claim "retained only historical provenance plus obsoletion metadata, following GO obsoletion conventions" is inaccurate — the historical provenance was actually dropped, which is contrary to GO obsoletion convention.
- **Comment text diverges from gold (minor).** The obsoletion `comment` ("the experimental data can be accurately described using GO:0048208 COPII vesicle coat assembly") differs from the gold's part_of-pathway rationale. Both are defensible; free-text convention difference, not an error.
- **Missed stale-comment maintenance on incoming edges (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183` (synaptic vesicle coating) or `GO:0048200` (Golgi transport vesicle coating), nor the `GO:0048208` self-edge parent-label comment — all updated by the gold. Non-semantic `!` comments, but leaves the file internally inconsistent.

Net: `partial_success` — the obsoletion + dual rename is correct and well-validated, but the twin definition rewrites on active terms plus the dropped creation provenance are real scope/correctness concerns that the high precision metric understates.
