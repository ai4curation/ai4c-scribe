---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 375
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.706
precision: 0.686
recall: 0.727
jaccard: 0.545
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: success
failure_modes: []
---

## Summary

A correct, exemplary full **merge** with the most explicit and self-aware methodology in the set. The agent reduced MONDO:0023243 to a clean obsolete stanza (`name: obsolete ...`, `IAO:0000231 MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by: MONDO:0011274`) and transferred the historical synonyms plus the Orphanet:1535 xref onto MONDO:0011274, matching the reviewer-approved approach (gold #10106) and avoiding the obsolete-only pattern @sabrinatoro repudiated in #10087. The PR comment includes a per-item disposition table and a QC checklist (owltools obsolete-replace, NORM, named `robot verify` queries, no `alt_id`, no synonym citing the obsoleted ID). F1=0.706 substantially under-represents quality: the gap is gold's *issue-unrelated incidental* Muenke cleanups, not any defect here.

## Strengths

- Obsolete stanza byte-identical to gold: correct `IAO:0000231 MONDO:TermsMerged` (not the generic `OMO:0001000`), correct `replaced_by: MONDO:0011274`, def/comment/subsets/is_a/date all stripped.
- Correct `MONDO:equivalentObsolete` qualifier on the transferred `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` — exactly matching gold, and avoiding the fabricated `MONDO:obsoleteEquivalent` that the haiku/copilot/sonnet attempts used.
- Transferred all historical synonyms to Muenke, including the key `synonym: "glass-chapman-hockley syndrome" EXACT [Orphanet:1535]` — the primary lexical bridge that the obsolete-only attempts lost; merged the `Orphanet:1535/inferred` source into the existing `is_a: MONDO:0015469` line rather than duplicating the axiom.
- Explicitly justified every dropped item (retired SCTID:720814001, obsoletion-tracking subsets, owltools-injected synonym artefact, GARD seeAlso) — sound, transparent curatorial reasoning consistent with Mondo merge SOP.
- Did not cite the obsoleted MONDO ID on any transferred synonym (a real QC requirement it explicitly checked).

## Issues

- **Defensible deviation from gold (not an error):** intentionally dropped `xref: SCTID:720814001` because the SNOMED concept is retired; gold instead keeps it as `MONDO:equivalentObsolete`. The agent's reasoning is sound and it documented the choice; gold's choice is also valid. This costs recall but is curatorially correct, not a defect.
- **Scope (minor, defensible):** added `is_a: MONDO:0000426 ! autosomal dominant disease` to Muenke (transferred from the obsoleted term); gold does not. Borderline — Muenke is FGFR3-dominant so this is plausible, but it is an unrequested classification addition.
- **Metadiff under-representation (not the agent's fault):** kept transferred synonyms at the source scopes where gold promotes to `EXACT`, and did not reproduce gold's incidental `subset: inferred_rare` / `MNKES` ABBREVIATION change / deletion of "Muenke nonsyndromic coronal craniosynostosis" — none derivable from the issue. These cap F1 below 1.0 for any well-scoped agent.

Net: success — a correct, fully documented merge with one well-reasoned SCTID divergence. Among the best attempts; F1 materially under-represents quality.
