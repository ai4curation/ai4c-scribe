---
repo: obophenotype/cell-ontology
issue_number: 3521
pr_number: 3583
issue_title: "Add reference dataset and NS-Forest marker for human bipolar neuron types"
issue_created_at: "2025-12-08"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-16"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - annotation
  - see-also
  - reference-dataset
  - bipolar-neuron
  - retina
  - NS-Forest
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch addition of reference transcriptomic dataset links to 13 existing bipolar neuron terms
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Issue #3521 and the curator's issue comment instruct agents to add a `database_cross_reference` (oboInOwl:hasDbXref) annotated with `rdfs:label \"reference transcriptomic data on Cell Annotation Platform\"`. The merged gold PR #3583 instead uses `rdfs:seeAlso` with IRI syntax, but ONLY because curator RiveraAndrea83 changed the instruction inside the PR review thread ('please change the use of database_cross_refs ... to see_also:', then 'updated URL from string to IRI format'). Neither the predicate change nor the IRI form is derivable from the issue context the eval agents received, so metadiff F1=0.0 for every attempt is a scoring artifact. Judge attempts against the issue + curator issue-comment, not the renegotiated gold."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The CL practice of linking cell type terms to reference transcriptomic datasets via see_also annotations enables data-driven validation of cell type definitions. Issue #3521 requested adding see_also links to a reference transcriptomic dataset for 13 human bipolar neuron cell types in the retina, along with NS-Forest marker gene annotations that provide computational signatures for each type.

## Changes Made

Added 13 new lines to `cl-edit.owl`, one per bipolar neuron cell type, each adding a see_also annotation linking to the reference transcriptomic dataset. The terms updated include the various human retinal bipolar cell subtypes (e.g., ON bipolar cells, OFF bipolar cells, and their numbered subtypes).

## Resolution

Approved on first review in 3 commits. Simple difficulty because this is a systematic annotation addition following an established pattern -- each term receives the same type of see_also annotation pointing to the dataset, with no changes to class hierarchy or logical definitions.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.**

This is a single-PR resolution (search of issue #3521 and the issue title term
returns only PR #3583 — no companion PRs; the NS-Forest marker bullet was
explicitly deferred by the curators to upstream CellMark PR #56 and is not part
of this gold). It is **not** a multi-PR partial-gold case. It is, however, a
poor *evaluation* case because the gold representation was renegotiated inside
the PR review thread after the agents' information cut-off:

- Issue #3521's body says `SeeAlso: <URL> @rdfs:label "..."`, but the curator's
  follow-up issue comment (RiveraAndrea83, 2026-03-09) and the embedded
  `agent_instructions` both explicitly specify
  `database_cross_reference: https://celltype.info/project/544/dataset/1157`
  with the rdfs:label as an annotation of that xref. That is the most recent
  and most specific instruction the eval agents were given.
- The merged gold PR #3583 was first built exactly to that spec
  (`oboInOwl:hasDbXref`, string value — commit 0d637a1). Then **inside the PR
  review thread** RiveraAndrea83 commented *"please change the use of
  database_cross_refs used for the case above to see_also:"*, and Copilot
  rewrote all 13 to `rdfs:seeAlso` with **IRI** syntax
  (`<https://...>` not `"https://..."`) in commit a493faf.
- The final gold form
  `AnnotationAssertion(Annotation(rdfs:label "reference transcriptomic data on
  Cell Annotation Platform") rdfs:seeAlso obo:CL_xxxx
  <https://celltype.info/project/544/dataset/1157>)`
  is therefore **not derivable from the issue context handed to the eval
  agents**. The PR-thread renegotiation is not part of the issue.

Consequence: metadiff F1 = 0.000 for all four attempts even though three of
them (#239 sonnet/copilot, #141 haiku, #192 opus) correctly cover all 13 terms
with the required rdfs:label annotation:

- **#239 (sonnet-4.5/copilot)** and **#141 (haiku-4.5)** even chose the *gold's
  final predicate* `rdfs:seeAlso`; their only deviation is string-literal vs
  IRI for the same URL. Substantive outcome: `success`.
- **#192 (opus-4.7)** faithfully followed the explicit `database_cross_reference`
  instruction (correct against what it was told) and explicitly flagged the
  unresolved `SeeAlso:` vs `database_cross_reference:` ambiguity to curators —
  the exact point later renegotiated. Substantive outcome: `success`.
- **#206 (sonnet-4.5/claude)** is genuinely weaker: it dropped the required
  `rdfs:label` annotation (bare unannotated xref) and over-edited all 13
  textual definitions to embed the URL — deviations independent of the
  poor-case caveat. Substantive outcome: `partial_success`.

Recommendation for downstream scoring: treat metadiff for this case as
**non-informative** (a hard zero floor by construction for the three good
attempts). Down-weight or exclude from F1-based aggregation, or re-score
against the issue + curator issue-comment rather than the post-PR-comment gold.
