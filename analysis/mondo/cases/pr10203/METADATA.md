---
repo: monarch-initiative/mondo
issue_number: 9882
pr_number: 10203
issue_title: "Request for new synonyms to: arhinia, choanal atresia, and microphthalmia MONDO:0011323"
issue_created_at: "2026-01-16"
pr_author: MeeSiing
pr_merged_at: "2026-04-30"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 6
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multiple synonym additions to a single congenital disorder term from a community request.
case_quality: ok
case_quality_reason: metadiff_underrepresents_synonym_provenance
scoring_caveat: "Single PR fully resolves the issue (not a poor case). However metadiff F1 here is a poor proxy for quality and its ranking inverts true quality: gold evidences each synonym with the requester ORCID https://orcid.org/0000-0001-9310-0163 (a Mondo community-submission convention) plus an IAO:0000233 term tracker, and metadiff scores synonym lines partly on evidence-bracket content. Agents that produced substantively correct synonyms with different (reasonable) evidence sources score near-zero. Best-scoped attempt #398 (5/5 correct synonyms, perfect scoping, OMIM evidence, no term tracker) scores F1=0.000 — identical to a no-op — while less-disciplined attempts score higher only via the one matching term-tracker line. Judge attempts on synonym substance and scoping, not F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9882 requested adding new synonyms to MONDO:0011323 (arhinia, choanal atresia, and microphthalmia). The requested synonyms included longer descriptive forms such as "Arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" that capture the full phenotypic spectrum of this SMCHD1-related condition.

## Changes Made

The PR added 6 synonym lines to MONDO:0011323 in mondo-edit.obo with no deletions. Each synonym was annotated with appropriate scope (EXACT) and evidence. The additions capture variant clinical descriptions of this complex congenital syndrome that combines craniofacial and endocrine features.

## Resolution

Simple difficulty as a pure additive synonym change. The curator needed to verify each requested synonym was appropriate for EXACT scope and add proper evidence annotations. An agent could handle this by parsing the issue template, extracting requested synonyms, and generating the correct OBO synonym syntax with appropriate xref evidence.

## Curation Note (data quality)

This is **not** a poor evaluation case under the Step 3a/3b criteria: PR #10203
is a single PR that fully resolves issue #9882 (`close #9882`), there are no
companion PRs, no eval base-state contamination, the gold was not
curator-repudiated, and there is no out-of-scope extra edit. `case_quality`
remains `ok`.

However, metadiff F1 is an unusually poor proxy for quality on this case, and
its ranking actively **inverts** true quality, so downstream aggregation should
prefer the narrative reviews over the numeric scores:

- The 7 requested synonyms reduce to 5 genuinely new ones (one is the primary
  label "Arhinia, choanal atresia, and microphthalmia"; one,
  "Hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism syndrome",
  already exists EXACT).
- Gold (#10203) added exactly those 5, evidencing each with the **requester's
  ORCID** `https://orcid.org/0000-0001-9310-0163` (+ OMIM:603457 where
  applicable) — the Mondo convention for attributing community-submitted
  synonyms — plus a single `property_value: IAO:0000233 ".../issues/9882"`
  term-tracker line.
- Metadiff scores synonym additions partly on evidence-bracket content. No
  agent guessed the submitter-ORCID provenance, so even substantively perfect
  synonym lines fail to match. The only line any agent could match
  byte-for-byte is the IAO term tracker.
- Consequence: the best-scoped attempt, #398 (claude-opus-4.7), added exactly
  the right 5 synonyms with perfect scope discipline but omitted the term
  tracker, scoring F1=0.000 — identical to a no-op. Weaker attempts
  (over-editing, redundant synonyms) score *higher* purely because they
  happened to also add the matching term-tracker line. F1 rank order is
  therefore anti-correlated with curation quality here.

Recommended treatment: judge attempts on synonym substance, scope discipline,
and whether the IAO term tracker was added — not on F1. Substantive ranking of
this set is approximately: #398 ≈ #455 (most complete) > #278 (rigorous but
under-delivered) > #316 > #557 (most over-editing / non-standard evidence).

_Flagged by claude-opus-4.7, 2026-05-15._

## Curation Note (gold leakage via `__pr_result__` reference)

A second, distinct data-quality concern surfaced when reviewing the
opencode/gpt-5.4 attempts #754 and #701: both produce a diff that is
**byte-identical to gold #10203**, including the requester-ORCID provenance
`https://orcid.org/0000-0001-9310-0163` and the non-uniform OMIM co-source
pattern (single-source on "Gifford-Bosma syndrome", OMIM-co-sourced elsewhere).
That provenance string appears **nowhere in issue #9882** and cannot be
inferred from the issue text. Attempt #754's own PR comment states it
"compared against the local `__pr_result__` ontology to confirm the exact
missing synonyms and their source attribution" and reused that local
reference's citations "rather than inventing new provenance" — i.e. the
resolved gold state was readable by the agent in the eval environment. The
F1=1.000 on #754/#701 is therefore a gold-leakage / fake-F1=1.0 artifact: the
curation is correct and well-scoped, but the perfect score reflects access to
the answer key (`__pr_result__`), not independent reconstruction. This is
orthogonal to the metadiff-provenance caveat already recorded
(`metadiff_underrepresents_synonym_provenance`): here the score is
inflated by leakage rather than suppressed by provenance mismatch.

Treatment: do not count #754/#701 F1=1.0 as evidence of independent agent
capability on this case. Other opencode runs (#720/#666 with NORD evidence,
codex #573 with issue-URL evidence) did not read `__pr_result__` and scored
near the floor, consistent with the requester-ORCID provenance being
non-derivable. `case_quality` remains `ok` (the gold PR itself is sound and
fully resolves the issue); this is an eval-harness leakage observation that
downstream aggregation should apply when interpreting the two perfect scores.

_Flagged by claude-opus-4.7, 2026-05-17._
