---
ontology: cell-ontology
issue_number: 3259
pr_number: 3450
eval_repo_pr: 46
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.696
precision: 0.727
recall: 0.667
jaccard: 0.533
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact_plus_gold_out_of_scope_serialization_edit
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt is byte-identical to eval PR #65 (same `gpt-5.5`/`opencode` agent, same run timestamp/blob `3623b1a`, same diff): a correct, well-scoped `transitional principal-intercalated cell of kidney collecting duct` term with the gold-matching `CL_9900001` ID, correct parent/location, both synonyms, both ORCIDs, and an issue-tracker link. It paraphrases the definition and adds a defensible extra exact synonym and `rdfs:comment`. Substantively a **success**; the 0.696 F1 reflects defensible extras and the gold's own out-of-scope serialization edit.

## Strengths

- **Identical to #65** — produces the same correct content; see that review for full detail.
- **ID matches gold** (`CL_9900001`), avoiding the placeholder-vs-canonical ID artifact.
- **Correct `Declaration(Class(obo:CL_9900001))`**, parentage `SubClassOf CL_1000454`, and `part_of UBERON_0001232`.
- **Synonyms correctly typed/attributed** (`tPC-IC cell` related-abbreviation, `hybrid principal-intercalated cell` broad with the issue-faithful PMID:33893305).
- **Both ORCIDs** + `IAO_0000233` issue link.
- **Documented methodology**: existing-term search, parent check, additional note that it attempted `aurelian fulltext` for both PMIDs and fell back to PubMed/web review, plus `robot convert` validation — slightly more research transparency than #65's comment.

## Issues

- **Definition paraphrased, not verbatim (style)** — same as #65: ontologically equivalent genus-form rewrite rather than the issue-supplied wording gold used verbatim.
- **Extra exact synonym + `rdfs:comment` (scope)** — `transitional principal-intercalated cell` exact synonym and a CKD-enrichment comment, neither requested; defensible.
- **`dc:creator`/`terms:date`** pipeline-convention metadata present.
- **Duplicate run**: identical to #65; for aggregation these two should be treated as one sample, not two independent successes.
- **Metadiff caveat**: recall 0.667 partly reflects the gold's unrelated `hasDbXref` comment-text edit that the agent correctly omitted; F1 modestly understates quality.
