---
repo: monarch-initiative/mondo
issue_number: 9938
pr_number: 10221
issue_title: "request to relabel MONDO:0012277"
issue_created_at: "2026-02-11"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Minimal single-term synonym addition following a ClinGen relabel request with clear instructions.
case_quality: poor
case_quality_reason: issue_renegotiated_in_comments
companion_prs: []
scoring_caveat: "Issue #9938 used the relabel template ('Suggested new label'), but the curator (@MeeSiing) explicitly resolved it as a ClinGen-qualified synonym ADD with NO rename (gold PR #10221: +2 lines, primary label 'myofibrillar myopathy 4' kept). 7/8 attempts took the title literally and RENAMED the term — a destructive change the curator deliberately avoided. metadiff F1 systematically UNDER-penalizes this: the term_tracker line lifts rename attempts to F1=0.333 even though the headline action is the opposite of gold, and pr558's precision=1.0 is a pure artifact (it masks 5 fabricated synonym-source citations). Judge attempts against the curator's stated decision + the agent config 'ClinGen Label Handling' pattern, not the issue title."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9938 requested relabeling MONDO:0012277 (myofibrillar myopathy 4) to "LDB3-related myofibrillar myopathy" following ClinGen gene-centric naming conventions. The request included an ORCID for nano-attribution and a clear preferred label.

## Changes Made

The PR added "LDB3-related myofibrillar myopathy" as an exact synonym to MONDO:0012277 in the mondo-edit.obo file. This is a 2-line addition with no deletions, representing the simplest possible ontology edit pattern: adding a synonym annotation to an existing term stanza.

## Resolution

This is a straightforward synonym addition that requires minimal domain knowledge. The curator identified the correct term stanza in mondo-edit.obo and added the synonym with appropriate metadata. An automated agent should handle this type of task reliably given knowledge of OBO format synonym syntax and the Mondo synonym addition SOP.

## Curation Note (data quality)

Flagged `case_quality: poor` — reason `issue_renegotiated_in_comments` (flagged by
claude-opus-4.7, 2026-05-15).

The gold itself is sound: PR #10221 is the single, complete human resolution (no companion PRs;
`gh search prs --repo monarch-initiative/mondo "9938" / "MONDO:0012277" / "LDB3 myofibrillar"` all
return only #10221). The problem is the **case framing vs. the metadiff**, not the gold.

Issue #9938 was filed with Mondo's *relabel* request template ("Suggested new label:
LDB3-related myofibrillar myopathy"). The curator @MeeSiing then explicitly narrowed the resolution
in an issue comment: *"The request term will be added to MONDO:0012277 myofibrillar myopathy 4 as
ClinGen Preferred label."* Gold PR #10221 accordingly added only two lines and **kept** the
primary label `myofibrillar myopathy 4`:

- `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
- `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9938" xsd:anyURI`

The agent config (`ai4curation/mondo-agent-config@v3` `template/CLAUDE.md`) documents exactly this
under **"ClinGen Label Handling"** (use the `{OMO:0002001=".../clingen"}` qualifier on a synonym).

Effect on scoring: 7 of 8 attempts (all except pr558, which also renamed) **renamed** the term —
the destructive change the curator deliberately avoided. The metadiff **under-penalizes** this:
the rename attempts (pr453, pr405) still reach F1=0.333 purely because they reproduce the
`term_tracker_item` line, and pr558's **precision=1.0 is a pure artifact** (the only 2 lines it
shares with gold are the ClinGen synonym + tracker; its 5 fabricated synonym-source citations on
pre-existing `[]` synonyms are invisible to precision). No attempt qualifies as success; the case
should be down-weighted or scored against the curator's stated decision + the ClinGen pattern
rather than the issue title or the raw F1.
