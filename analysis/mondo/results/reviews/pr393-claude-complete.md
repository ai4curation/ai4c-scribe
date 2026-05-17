---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 393
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.872
precision: 0.773
recall: 1.0
jaccard: 0.773
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-opus-4.7 via the claude runtime produced a correct, clean merge of MONDO:0008549 into MONDO:0979242. The obsoleted stanza is reduced to exactly the gold six lines (`MONDO:TermsMerged`, retained `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by: MONDO:0979242`), and the survivor received the corrected synonym `[OMIM:187750]`, both transferred xrefs with proper precision qualifiers, `is_a: MONDO:0003847`, and the MalaCards `curated_content_resource`. The F1 of 0.872 (precision 0.773, recall 1.000) materially under-represents the quality: the only differences from gold are (a) the human's extra `def:` and `intersection_of` enrichment, which the merge request never asked for, and (b) this run's omission of the duplicate issue-tracker `property_value: IAO:0000233 .../9826` on the survivor — a single redundant provenance line (the obsoleted term already carried that issue link). The substantive merge is fully correct.

## Strengths

- Obsoleted MONDO:0008549 stanza is byte-equivalent to gold, including correct removal of `subset: obsoletion_candidate`, the merge-schedule `comment:`, and `IAO:0006012 "2026-03-01"` rather than leaking them onto the survivor.
- Synonym evidence correctly repaired: `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`, matching gold and avoiding the obsolete-MONDO-ID self-citation.
- Both xrefs transferred with correct precision qualifiers: `MESH:C566063 {source="MONDO:equivalentTo"}`, `OMIM:187750 {source="MONDO:equivalentObsolete"}` — identical to gold.
- Retained the `is_a: MONDO:0003847` "hereditary disease" parent on the survivor exactly as gold did (where the gpt-5.5/opencode runs dropped it) — closer to MONDO house convention.
- Issue comment is accurate and concise, correctly summarizing the OMIM:187750 → OMIM:621260 provenance and the carried-over MESH/OMIM/MalaCards content.

## Issues

- Minor omission: did not add the survivor's duplicate `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9826" xsd:anyURI`. This is the one line separating it from the gpt-5.5/codex top run (#41). It is a redundant provenance pointer (the issue link is already on the obsoleted stanza), so its absence is defensible and arguably cleaner; it nonetheless costs metadiff precision.
- Omission (not derivable from issue): no `def:` (OMIM:621260-sourced) and no `intersection_of` logical definition — the human's opportunistic curatorial enrichment, out of scope for a merge request. Correctly conservative.
- Sparse PR/issue documentation: the PR body is a one-line "Resolves ...#9826" with no validation checklist or QC evidence, unlike the codex/opencode runs which documented `make NORM` + targeted SPARQL QC. The output is correct, but the lack of recorded verification is a process weakness, not a correctness defect.
- Outcome set to `success`: the merge is fully correct; the only gap from the best run is a single redundant provenance line.
