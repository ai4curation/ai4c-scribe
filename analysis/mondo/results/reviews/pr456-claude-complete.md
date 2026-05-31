---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 456
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.615
precision: 0.545
recall: 0.706
jaccard: 0.444
outcome: partial_success
failure_modes: [under_editing, missed_requirement, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-sonnet-4.5 obsoleted MONDO:0008549 and made a partial, error-prone transfer to MONDO:0979242. The obsoletion mechanics are roughly right (`is_obsolete: true`, `replaced_by: MONDO:0979242`, `IAO:0000231 MONDO:TermsMerged`, issue link) but the content transfer contains multiple concrete errors that the higher-scoring runs avoided. F1 0.615 (precision 0.545, recall 0.706) is an accurate-to-slightly-generous reflection of the quality: this is a substantively flawed merge, not merely a stylistic divergence.

## Strengths

- Correctly set the core obsoletion fields on MONDO:0008549: `name: obsolete thoracic dysostosis, isolated`, `IAO:0000231 MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`.
- Removed `subset: obsoletion_candidate` and the merge-schedule `comment:` and `IAO:0006012` from the obsoleted stanza.
- Added the `synonym: "thoracic dysostosis, isolated"` and a MESH xref onto the survivor (the right intent, even if the evidence qualifiers are wrong — see Issues).

## Issues

- **Error — left dead content in the obsoleted stanza.** MONDO:0008549 retains `synonym: "thoracic dysostosis, isolated" EXACT []`, `xref: MESH:C566063 {source="MONDO:obsoleteEquivalent"}`, and `xref: OMIM:187750 {source="MONDO:obsoleteEquivalent"}`. An obsolete merged stanza must be reduced to id/name/IAO:0000231/IAO:0000233/is_obsolete/replaced_by (as gold and the top runs did). Synonyms and xrefs left on an obsolete term are a QC violation pattern.
- **Error — wrong xref precision qualifiers.** It rewrote `MESH:C566063` to `{source="MONDO:obsoleteEquivalent"}` (gold/correct: `MONDO:equivalentTo`) and `OMIM:187750` to `{source="MONDO:obsoleteEquivalent"}` (gold/correct: `MONDO:equivalentObsolete`). `obsoleteEquivalent` is not the right qualifier here and these xrefs were left on the wrong (obsoleted) stanza rather than transferred.
- **Error — invented a stray `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659`** on the obsoleted stanza. This ORCID appears nowhere in the source data or issue; it looks fabricated/hallucinated and is not part of gold.
- **Error — survivor synonym cites the obsolete MONDO ID.** It added `synonym: "thoracic dysostosis, isolated" EXACT [MONDO:0008549]` to MONDO:0979242. The merge SOP explicitly requires replacing the owltools `[MONDO:0008549]` self-citation with a real external xref (gold: `[OMIM:187750]`). Citing a now-obsolete MONDO ID as synonym evidence is exactly the anti-pattern the skill warns against.
- **Error — survivor xref carries an obsolete-MONDO source qualifier:** `xref: MESH:C566063 {source="MONDO:equivalentTo", source="MONDO:0008549"}` — the spurious `source="MONDO:0008549"` should not be present.
- **Omission — incomplete transfer.** The survivor did not receive `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}`, the `is_a: MONDO:0003847` parent, or the MalaCards `curated_content_resource` that gold and the top runs transferred. This drives the recall shortfall.
- Net: core obsoletion done but the merge is wrong in several concrete, QC-relevant ways (dead content on obsolete stanza, hallucinated ORCID, obsolete-ID synonym evidence, incomplete transfer). `partial_success` with failure modes under_editing, missed_requirement, wrong_pattern.
