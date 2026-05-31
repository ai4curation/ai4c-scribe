---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 165
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.716
precision: 0.686
recall: 0.750
jaccard: 0.558
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: success
failure_modes: [over_editing]
---

## Summary

A correct, well-documented full **merge** — substantively one of the best attempts despite an F1 (0.716) below the partial-merge opencode runs. The agent executed the canonical Mondo merge SOP: reduced MONDO:0023243 to a clean obsolete stanza (`MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by: MONDO:0011274`) and transferred the historical synonyms and the Orphanet:1535 xref onto MONDO:0011274. Its PR comment shows genuine methodology: it ran `make NORM`, `robot convert`, and six targeted QC SPARQL checks, and it explicitly reasoned about each transferred/dropped item. This matches the reviewer-approved approach (gold #10106) and avoids the obsolete-only pattern @sabrinatoro repudiated in #10087.

## Strengths

- Obsolete stanza byte-identical to gold: correct `IAO:0000231 MONDO:TermsMerged` (not the generic `OMO:0001000`), correct `replaced_by: MONDO:0011274`.
- Correctly used `MONDO:equivalentObsolete` qualifier on the transferred `xref: Orphanet:1535` (not the fabricated `MONDO:obsoleteEquivalent` four lower-tier attempts used).
- Repointed the `glass-chapman-hockley syndrome` synonym evidence to literature/source (`[Orphanet:1535, PMID:20108486]`) instead of leaving owltools-injected `[MONDO:0023243]` self-reference — a genuinely good QC instinct (Mondo policy: synonyms must not cite the obsoleted ID).
- Dropped the redundant broad `is_a: MONDO:0015469 ! craniosynostosis` while keeping the more specific `MONDO:0015338 ! syndromic craniosynostosis` on Muenke — defensible classification hygiene.
- Strong, auditable methodology (NORM, robot convert, named QC queries, no `alt_id`, verified no dangling references).

## Issues

- **Defensible deviation from gold (not an error):** deliberately dropped `xref: SCTID:720814001` reasoning the SNOMED concept is retired and transferring it as equivalent would be inaccurate. Gold instead *retains* it as `MONDO:equivalentObsolete`. The agent's reasoning is sound; gold's choice (keep as obsolete-equivalent record) is also valid. This costs recall but is curatorially defensible.
- **Scope/over-editing (minor):** added `is_a: MONDO:0000426 ! autosomal dominant disease` to Muenke (transferred from the obsoleted term). Gold does not add this; whether Muenke is strictly autosomal-dominant-only is debatable, so this is borderline over-editing rather than clearly wrong.
- Kept transferred synonyms at `RELATED`/`EXACT []` where gold promotes to `EXACT [GARD:0002479]` — a scope-convention difference not derivable from the issue, and gold's incidental Muenke cleanups (`subset: inferred_rare`, `MNKES` ABBREVIATION change, deletion of "Muenke nonsyndromic coronal craniosynostosis") cap F1 below 1.0 for any well-scoped agent.

Net: success — a correct full merge with auditable QC and one defensible SCTID divergence. F1 under-represents quality.
