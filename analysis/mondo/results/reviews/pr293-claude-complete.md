---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 293
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.600
precision: 0.514
recall: 0.720
jaccard: 0.429
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: failure
failure_modes: [wrong_pattern, under_editing, missed_requirement, syntax_error]
---

## Summary

The agent performed a plain **obsoletion in place** with no transfer to the surviving term — reproducing the obsolete-only pattern reviewer @sabrinatoro explicitly **repudiated** in the curator's first attempt #10087 ("If the term is the same as the other one, then it should be merged. In this case, follow the merge procedure"). The diff touches only the MONDO:0023243 stanza; MONDO:0011274 (Muenke) receives nothing. It also uses the generic obsoletion reason `OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`, fabricates the invalid qualifier `MONDO:obsoleteEquivalent`, and leaves an over-fat obsolete stanza (retained def, synonyms, xrefs). F1=0.600. This is a failure: it does not solve the issue and would require the same rejection #10087 received.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed the `subset: obsoletion_candidate` and the scheduled-obsoletion `IAO:0006012` date, which are appropriate to drop on obsoletion.
- Prefixed the definition with `OBSOLETE.` per OBO convention (though gold removes the def entirely in a merge).

## Issues

- **Wrong pattern (decisive):** this is an obsoletion, not a merge. The historical synonyms and xrefs are *kept on the obsolete term* and *nothing is added to Muenke*. @sabrinatoro's review of #10087 makes clear this is not acceptable when the terms are the same disease — a true merge transferring content to MONDO:0011274 was required.
- **Wrong obsoletion reason:** `property_value: IAO:0000231 OMO:0001000` (generic "obsoleted") instead of gold's merge-specific `MONDO:TermsMerged`. This mis-signals the obsoletion type to QC and downstream consumers.
- **Fabricated qualifier (syntax/validity error):** `xref: ... {source="...", source="MONDO:obsoleteEquivalent"}` — `MONDO:obsoleteEquivalent` is not a valid Mondo source qualifier; correct token is `MONDO:equivalentObsolete`. Same recurring error flagged in case METADATA.
- **Over-fat obsolete stanza:** retained full def, comment, multiple subsets, and both xrefs on the obsolete class — gold strips these. Also added a `dc:creator` ORCID property to the obsolete stanza, which gold does not.
- **Synonym scope tampering:** flipped `"craniosynostosis with facial dysmorphism..."` EXACT→RELATED and `"glass chapman hockley syndrome"` RELATED→EXACT with no evidence — unjustified scope edits on a term being obsoleted.

Net: failure — reproduces the repudiated #10087 obsolete-only approach with an additional invalid qualifier and wrong obsoletion reason.
