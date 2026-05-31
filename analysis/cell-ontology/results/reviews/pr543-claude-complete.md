---
outcome: success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_label_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
agent: std_opencode_gpt55
---

## Summary

Eval PR #543 (gpt-5.5 / opencode) against human PR #3524 / issue #3523
(cell-ontology, `other`, simple). Metadiff F1=0.353 / P=0.429 / R=0.300 — a
**severe lower bound** for this prior-flagged poor case
(`gold_label_renegotiated_in_pr_comments`). The agent correctly relabeled
CL:0004117, revised the definition, and added the legacy synonym, addressing
every substantive ask in the issue; the low F1 reflects the renegotiated
`(Mmus)` gold label plus a paraphrased (not verbatim) definition and one
unrequested annotation, not a failed curation.

## Strengths

- Label set to "alpha retinal ganglion cell", exactly the "Revised cell label"
  in issue #3523. The gap to the gold "alpha retinal ganglion cell (Mmus)" is
  the post-issue renegotiated suffix, unobtainable from the issue.
- Legacy name preserved as `oboInOwl:hasExactSynonym` "Retinal ganglion cell A"
  annotated with PMID:12209831, matching the issue's verbatim casing
  ("exact synonym: Retinal ganglion cell A PMID:12209831"); gold lowercased it.
- Definition replaced with a faithful, on-concept alpha-RGC description and the
  PMID:28753612 xref added as the issue requests.
- Scope discipline on the term axioms: the `RO_0002162 NCBITaxon_10090` taxon
  restriction, BAMS xref, "alpha cell" synonym and rat `rdfs:comment` were all
  left intact (contrast #321, which deleted the taxon axiom and comment).

## Issues

- Over-editing (minor): added an unrequested
  `AnnotationAssertion(obo:IAO_0000233 obo:CL_0004117 <…/issues/3523>)`
  issue-tracker annotation. Gold did not add this; it lowers precision and is
  outside the issue's textual-definition/label scope.
- The definition is paraphrased rather than the issue's verbatim "Suggested
  revision" text, and it retains the original PMID:12209831 xref on the
  definition alongside PMID:28753612 (issue cites only PMID:28753612 for the
  revised definition). Both are defensible but cost metadiff recall vs. #475's
  verbatim approach.
- Cosmetic end-of-file newline addition (no semantic effect).
