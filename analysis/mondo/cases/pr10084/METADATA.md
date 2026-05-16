---
repo: monarch-initiative/mondo
issue_number: 9849
pr_number: 10084
issue_title: "Request for new term 'reticular pseudodrusen'"
issue_created_at: "2025-12-22"
pr_author: MeeSiing
pr_merged_at: "2026-03-30"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: New term creation for an ophthalmic condition requiring evidence evaluation and synonym scope decisions based on clinical literature.
case_quality: ok
case_quality_reason: clean_single_pr_but_id_scoring_caveat
companion_prs: []
scoring_caveat: "Gold #10084 is the complete single-PR human resolution (approved first time, not renegotiated, no companion PRs) — NOT a poor case. However, metadiff F1 systematically under-represents agent quality here: the eval scores against the curator's post-merge canonical ID MONDO:1060213, while mondo-agent-config@v3 CLAUDE.md explicitly instructs agents to use the MONDO:777xxxx placeholder range. ~6 of ~13 stanza lines mismatch on the ID alone for every well-formed attempt, capping achievable F1 well below 1.0 regardless of correctness. Additional unavoidable metadiff costs: gold splits the AMD-risk clause into a separate comment: field, uses singular 'subretinal drusenoid deposit', and uses the curator ORCID (0000-0002-7638-4659) for dcterms:creator (matching the config NTR template). Judge attempts on substance (correct parent, synonym types, xref form, and especially exclusion of the bogus PMID:34752962 flagged in the issue body) rather than the metadiff number."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9849 requested a new term for "reticular pseudodrusen" (also known as subretinal drusenoid deposits/SDD/RPD), which are subretinal deposits located internal to the retinal pigment epithelium. The request included exact synonyms and two abbreviations, a definition, and multiple PMIDs as evidence. The curator noted that one suggested PMID (34752962) was incorrect evidence and excluded it.

## Changes Made

The PR created MONDO:1060213 with 13 additions to mondo-edit.obo. The new term includes the label "reticular pseudodrusen", a revised definition based on the provided PMIDs, exact synonyms ("subretinal drusenoid deposits", "SDD", "RPD"), parent classification, and ORCID-attributed evidence annotations. The curator critically evaluated the suggested references and excluded one that did not support the term.

## Resolution

Moderate difficulty because new term creation requires evaluating evidence quality. The curator demonstrated critical assessment by rejecting an inappropriate PMID while accepting others. The synonym scope decisions (abbreviations as EXACT rather than RELATED) and parent term placement both require ophthalmology domain knowledge. An agent would need literature verification capabilities to replicate this evidence evaluation step.

## Curation Note (data quality)

`case_quality: ok` — this is **not** a poor evaluation case. PR #10084 is the
whole human resolution: a single commit, approved first time by @sabrinatoro,
issue #9849 closed by it, no companion PRs, no curator repudiation, no
post-merge renegotiation. Gold edits real semantic fields (not a
metadiff-ignored field).

A `scoring_caveat` is recorded in the frontmatter because the uniformly
compressed metadiff F1 across all 10 attempts (0.261–0.522) is **normal
metadiff under-representation**, not a poor-case signature, and downstream
aggregation should not treat the low absolute numbers as agent failure:

1. **ID range is structurally penalized.** The eval scores agents against the
   curator's post-merge canonical ID `MONDO:1060213`. The agent config
   (`ai4curation/mondo-agent-config@v3`, `CLAUDE.md`) explicitly instructs:
   "New terms start MONDO:777xxxx". Every well-formed attempt therefore used
   `MONDO:7770012` and mismatches gold on the ~6 of ~13 stanza lines that
   contain the ID — by construction, not by error. Agents that used the
   placeholder range were *following their instructions correctly*.
2. **`dcterms:creator` convention.** Gold uses the curator ORCID
   `0000-0002-7638-4659` (matching the config's own NTR template example).
   Most attempts used the requester ORCID `0000-0001-6677-8489` — a genuine
   (minor) convention deviation, but it compounds the metadiff gap.
3. **Definition/comment split + singular synonym.** Gold rewrote the genus
   ("A retinal drusen characterized by…"), moved the AMD-risk sentence to a
   separate `comment:` field, and used singular "subretinal drusenoid
   deposit". Most agents pasted the issue's raw definition and used the plural.
   Defensible authoring differences that further depress recall.

Recommended adjudication basis (used in the per-attempt reviews): substance
over line-match — correct parent (`MONDO:0006949`), correct synonym
types/qualifiers, correct `SCTID:` xref form, and especially whether the
attempt reproduced the curator's evidence judgment by **excluding the bogus
`PMID:34752962`** ("Monitoring Colonoscopy Quality", Clin Gastroenterol
Hepatol) that the issue body itself flags as wrong evidence. On that axis the
attempts split sharply: codex gpt-5.5 (#92), codex gpt-5.4 (#169) and
claude-opus-4.7 (#373) excluded it (success); copilot sonnet (#333) excluded
it but wrongly dropped the valid `PMID:41361163`; kimi (#272), the two
opencode gpt-5.5 runs (#110/#130), claude-sonnet/claude (#449) and both
haiku-4.5 runs (#479/#417) propagated the bogus PMID (partial_success). The
two haiku runs additionally used the wrong datatype `xsd:string` on the
`IAO:0000233` tracker annotation (should be `xsd:anyURI`).

Flagged by claude-opus-4.7, 2026-05-15.
