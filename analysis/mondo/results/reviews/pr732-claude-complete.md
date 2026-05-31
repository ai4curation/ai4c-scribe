---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 732
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
metadata, and the issue tracker backlink. It correctly recognized that the issue's
`PMID:34752962` is wrong evidence (it explicitly noted in the PR comment that it
"resolves to an unrelated" article) — but instead of simply excluding it like the
curator did, it **substituted a different PMID (`PMID:34752916`)** that appears
nowhere in the issue and nowhere in the gold PR, and propagated this fabricated
correction into the def, all three synonyms, and the `is_a` source. The metadiff
F1=0.435 substantially under-represents structural quality (the placeholder-ID
artifact alone caps it well below 1.0), but the spurious PMID is a genuine
evidence-handling defect, so this is a partial success rather than a clean success.
This review is byte-identical in substance to eval PR #679 (same diff, same blob,
same scores) — they are duplicate runs of the same agent/model.

## Strengths

- **Correct parent placement**: Kept `MONDO:0006949 retinal drusen` exactly as the
  requester specified, with `is_a` source annotations — matches gold's parent.
- **Correct synonym scoping**: `subretinal drusenoid deposits` as EXACT and
  `SDD`/`RPD` as EXACT ABBREVIATION, matching the requested synonym types and MONDO's
  ABBREVIATION qualifier convention. All synonyms carry PMID citations (no empty `[]`).
- **Correct xref form**: Used the MONDO-standard
  `xref: SCTID:762533006 {source="MONDO:equivalentTo"}` form, exactly matching gold,
  rather than the raw `SNOMED:` prefix supplied in the issue body.
- **Compliant ID allocation**: `MONDO:7770012` is in the `MONDO:777xxxx` NTR range
  the agent config mandates; the mismatch against gold's post-merge canonical
  `MONDO:1060213` is a harness scoring artifact, not an agent error.
- **Detected the bad evidence**: Unlike kimi/opencode-gpt-5.5/claude-sonnet/haiku
  attempts that blindly propagated the bogus `PMID:34752962`, this run flagged it as
  unrelated — demonstrating the evidence-evaluation behavior the case is designed to
  probe. The PR comment documents the reasoning and a sound methodology checklist
  (existing-term search, parent verification, `robot convert` syntax check, NORM
  step skipped with a clear note that Docker was unavailable).
- **Tight scope**: Exactly one new stanza in one file; no over-editing.

## Issues

- **Fabricated PMID substitution (`wrong_term`)**: The curator's correct action was
  to *drop* `PMID:34752962` and keep the three valid PMIDs
  (`41361163`, `29859199`, `38386332`). This agent instead invented
  `PMID:34752916` as a "corrected" replacement (claiming the issue PMID was a typo)
  and inserted it into the def, all three synonyms, and the `is_a` source. That PMID
  is not in the issue, not in gold, and asserting it as evidence without it being
  curator-sanctioned introduces unverified provenance into the ontology. This is a
  more subtle failure than blindly propagating the bogus PMID, but it is still
  incorrect evidence handling — the safe action was exclusion, not substitution.
- **`dcterms:creator` deviates from config template**: Set to the requester ORCID
  `https://orcid.org/0000-0001-6677-8489`. Gold and the config's own NTR template
  use the curator ORCID `https://orcid.org/0000-0002-7638-4659` for
  `dcterms:creator`. Minor convention deviation; semantically neutral but a metadiff
  and provenance mismatch.
- **Definition style differs from gold (stylistic, not wrong)**: Folded the
  AMD-risk statement into `def:` whereas gold split it into a separate `comment:`
  field and rewrote the genus into Aristotelian "A retinal drusen characterized
  by..." form. Defensible alternative; costs metadiff recall.
- **Synonym pluralization**: Plural "subretinal drusenoid deposits" vs gold's
  singular form. Trivial; matches the issue's own wording.
- No syntax errors, no scope creep.
