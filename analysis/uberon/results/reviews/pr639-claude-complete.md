---
ontology: uberon
issue_number: 3629
pr_number: 3630
eval_repo_pr: 639
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
case_quality: ok
case_quality_reason: gold_verbatim_issue_text_with_metadiff_scoring_artifacts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent reproduced the curated gold solution exactly (blob `6ba9f78`), scoring a perfect F1=1.000 / precision=1.000 / recall=1.000. It added `UBERON:9900000 carotid artery intima-media region` with the issue-specified definition, synonym, genus, differentia relations, provenance, and — critically — serialized the disjointness axiom on the *partner* `UBERON:0005734` stanza exactly as the curator's robot-reserialized gold does. Here the F1 is fully representative: this is a clean, complete success.

## Strengths

- Both gold hunks present and byte-faithful: the new-term stanza at the tracheobronchial-tree insertion point, and the reciprocal `disjoint_from: UBERON:9900000 ! carotid artery intima-media region` line inside the `UBERON:0005734` ("tunica adventitia of blood vessel") stanza. This is the documented serialization-side artifact that every other attempt got wrong — this agent got it right.
- Canonical ID `UBERON:9900000` (matches gold; not the `9900001` placeholder used by sonnet/haiku/kimi).
- Curator-preferred primitive shape: `is_a: UBERON:0000481` plus explicit `relationship: has_part UBERON:0002522`, `relationship: has_part UBERON:0002523`, `relationship: part_of UBERON:0005396` — no `intersection_of`, matching the curator's "Remove equivalentTo" refactor directly without a correction round.
- Definition and synonym verbatim-correct with single `[PMID:39416432]` xref (no spurious DOI).
- Full metadata: `dc-contributor` ORCID with correct ` ! Aleix Puig-Barbé` label, `dcterms-date`, `term_tracker_item` (`property_value ... xsd:anyURI`), `created_by: dragon-ai-agent`.
- PR comment shows sound methodology: verified PMID via PubMed, checked existing IDs, ran `robot convert` and ELK reasoning, and explicitly noted ROBOT serialized the disjointness reciprocally.

## Issues

None. The agent matched the curated gold exactly, used the canonical ID, and landed the disjoint-axiom serialization side correctly — the single discriminator that separated this from all lower-scoring attempts. Tightly scoped to the one ontology file.
