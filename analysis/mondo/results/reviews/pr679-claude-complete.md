---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 679
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes:
  - wrong_term
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
case_quality: ok
case_quality_reason: clean_single_pr_but_id_scoring_caveat
scoring_caveat: "Gold #10084 is the complete single-PR human resolution. Metadiff F1 systematically under-represents agent quality: eval scores against the curator post-merge canonical ID MONDO:1060213 while mondo-agent-config@v3 instructs agents to use the MONDO:777xxxx placeholder range, so ~6 of ~13 stanza lines mismatch on the ID alone for every well-formed attempt. Judge on substance (parent, synonym types, xref form, PMID evidence judgment)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-17
---

## Summary

The agent created a substantively well-formed new term for reticular pseudodrusen
under the requested parent `MONDO:0006949 retinal drusen`, with a literature-backed
definition, the three requested synonyms (`subretinal drusenoid deposits` EXACT,
`SDD`/`RPD` EXACT ABBREVIATION), the SNOMED-equivalent xref in canonical form, creator
metadata, and the issue tracker backlink. The diff is byte-identical to eval PR #732
(same blob `1f4ac96`, same F1=0.435/P=0.417/R=0.455) — they are duplicate runs of the
same opencode gpt-5.4 agent. As in #732, the agent correctly recognized that the
issue's `PMID:34752962` is bad evidence, but rather than excluding it as the curator
did, it **substituted a fabricated `PMID:34752916`** and propagated that unverified
correction into the def, all three synonyms, and the `is_a` source. The metadiff
F1=0.435 substantially under-represents structural quality (the placeholder-ID
artifact alone caps achievable F1 well below 1.0), but the spurious PMID is a real
evidence-handling defect, making this a partial success.

## Strengths

- **Correct parent placement**: Kept `MONDO:0006949 retinal drusen` as the requester
  specified, with `is_a` source annotations — matches gold's parent.
- **Correct synonym scoping**: `subretinal drusenoid deposits` as EXACT and
  `SDD`/`RPD` as EXACT ABBREVIATION, matching the requested synonym types and MONDO's
  ABBREVIATION qualifier convention. All synonyms carry PMID citations (no empty `[]`).
- **Correct xref form**: Used the MONDO-standard
  `xref: SCTID:762533006 {source="MONDO:equivalentTo"}`, exactly matching gold,
  rather than the raw `SNOMED:` prefix from the issue body.
- **Compliant ID allocation**: `MONDO:7770012` is in the mandated `MONDO:777xxxx`
  NTR range; the mismatch against gold's canonical `MONDO:1060213` is a harness
  scoring artifact, not an agent error.
- **Detected the bad evidence**: Recognized that the issue's `PMID:34752962` is
  unrelated to reticular pseudodrusen — the evidence-evaluation behavior this case
  is designed to probe — placing it ahead of the attempts that blindly propagated
  the bogus PMID.
- **Tight scope**: Exactly one new stanza in one file; no over-editing.

## Issues

- **Fabricated PMID substitution (`wrong_term`)**: The curator's correct action was
  to *drop* `PMID:34752962` and keep the three valid PMIDs
  (`41361163`, `29859199`, `38386332`). This run instead invented `PMID:34752916`
  as a "corrected" replacement and inserted it into the def, all three synonyms, and
  the `is_a` source. That PMID is absent from both the issue and gold; asserting it
  as ontology evidence without curator sanction introduces unverified provenance.
  The safe and correct action was exclusion, not substitution. This is the
  defining defect for this run (and its #732 twin).
- **`dcterms:creator` deviates from config template**: Used the requester ORCID
  `https://orcid.org/0000-0001-6677-8489`; gold and the config NTR template use the
  curator ORCID `https://orcid.org/0000-0002-7638-4659`. Minor convention
  deviation; semantically neutral but a metadiff/provenance mismatch.
- **Definition style differs from gold (stylistic, not wrong)**: Folded the
  AMD-risk statement into `def:` whereas gold split it into a separate `comment:`
  and rewrote the genus into Aristotelian form. Defensible; costs metadiff recall.
- **Synonym pluralization**: Plural "subretinal drusenoid deposits" vs gold's
  singular. Trivial; matches the issue's wording.
- This attempt file (`pr679.md`) contains only the diff, no PR/issue comment, so
  the methodology narrative is inferred from the identical #732 run rather than
  independently documented here.
- No syntax errors, no scope creep.
