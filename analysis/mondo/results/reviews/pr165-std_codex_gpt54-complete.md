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
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A well-executed full **merge** with the most thorough and transparent methodology of all ten attempts (documented `make NORM`, `robot convert` syntax check, and six targeted QC SPARQL queries run). The obsoleted stanza is reduced exactly per the merge SOP and historical synonyms plus the Orphanet:1535 xref are transferred to Muenke (MONDO:0011274). It correctly implements the curator-endorsed merge (PR #10106), not the rejected obsolete-only path (PR #10087). F1=0.716 substantially **under-represents** quality; the gap from gold is mostly defensible curatorial judgment that the agent explicitly reasoned about, plus one debatable parent-cleanup.

## Strengths

- Correct, minimal obsoleted stanza: `obsolete glass-chapman-hockley syndrome`, `IAO:0000231 MONDO:TermsMerged`, issue #9798 link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — identical to gold.
- Transferred the four historical "craniosynostosis...brachydactyly" synonyms and `synonym: "glass-chapman-hockley syndrome" EXACT [Orphanet:1535, PMID:20108486]` onto Muenke, preserving lexical resolution to Muenke.
- Transferred `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` with the correct qualifier, and `is_a: MONDO:0000426 ! autosomal dominant disease`; added the issue #9798 `IAO:0000233` provenance to Muenke.
- Best-documented process: explicitly explained dropping the retired SCTID:720814001 xref, repointing the owltools-injected synonym evidence away from the bare MONDO ID, and removing obsoletion-tracking carryover — and ran the relevant QC checks (`qc-misused-replaced-by`, `qc-obsoletion-reason`, `qc-deprecated-class-reference`, `qc-xref-without-precision`, etc.).
- Used the real `MONDO:equivalentObsolete` qualifier, not the fabricated `MONDO:obsoleteEquivalent` seen in weaker attempts.

## Issues

- **Defensible deviation from gold (SCTID):** Agent deliberately dropped `xref: SCTID:720814001`, reasoning the SNOMED concept is retired and shouldn't be asserted as equivalent on Muenke. Gold instead **keeps it as `MONDO:equivalentObsolete`** (a qualifier that explicitly encodes "obsolete equivalence"), which is the more standard Mondo handling for a retired-but-historically-equivalent xref. This is the main substantive miss, but the agent's reasoning is articulate and not unreasonable.
- **Debatable parent edit:** Removed `is_a: MONDO:0015469 ! craniosynostosis` from Muenke, calling it redundant with `is_a: MONDO:0015338 ! syndromic craniosynostosis`. Gold does not touch Muenke's parents. Whether 0015469 is strictly redundant under the reasoner is not verified in the diff; per the project guideline ("do not remove existing parents unless explicitly instructed"), this is over-editing the surviving term beyond the merge.
- **Scope/style:** Transferred synonyms kept at `RELATED` (gold promotes to `EXACT`) — conservative and faithful to source, but a metadiff penalty. No `IAO:0006012`/GARD-`seeAlso` carryover (correct).
