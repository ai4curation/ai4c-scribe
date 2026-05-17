---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 262
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.571
precision: 0.667
recall: 0.500
jaccard: 0.400
outcome: partial_success
failure_modes:
  - wrong_term
  - instruction_violation
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent produced an ontologically sound and well-attributed `'uterine
fundus'` term — correct `is_a`/`part_of` structure, both synonyms, gold's
confirmed PMIDs, and a richer (expanded) definition — but assigned the **wrong
ID** `UBERON:1200003` instead of the config-mandated `UBERON:99xxxxx` range
(gold: `UBERON:9900001`) and added three extra xrefs the issue did not request.
F1 0.571 (P 0.667 / R 0.500) is the lowest of the five and *under-represents*
the substantive curation quality, which is arguably the most thorough of the
attempts; the score is dominated by the ID mismatch and the extra-xref recall
penalty.

## Strengths

- Both expected synonyms present: `fundus uteri` EXACT with `[PMID:39112955]`
  and `fundus of uterus` EXACT (with `[FMA:17561]` provenance).
- Correct asserted structure: `is_a: UBERON:0000064 ! organ part` and
  `relationship: part_of UBERON:0000995 ! uterus` — matches the gold pattern
  (no over-strong equivalence axiom, unlike the haiku/codex attempts).
- Uses gold's confirmed reference PMIDs `[PMID:40653088, PMID:41204538]`; the
  issue comment shows the agent re-verified them and corrected its own earlier
  doubt — good epistemic behavior.
- Definition is an enriched superset of gold ("...located above the openings of
  the uterine tubes"), an anatomically accurate and arguably superior
  description.
- Full provenance: `dc-contributor ! Aleix Puig-Barbé`, `dcterms-date`,
  `term_tracker_item` (typed `property_value ... xsd:anyURI`), `created_by`.
- Cross-references to FMA:17561, NCIT:C12315, SCTID:27485007 are all genuine
  external classes for "fundus of uterus" — defensible enrichment.

## Issues

- **Wrong term ID / instruction violation:** used `UBERON:1200003` rather than
  the canonical `UBERON:99xxxxx` NTR range required by the agent config (gold:
  `UBERON:9900001`). This is the dominant metadiff penalty and an instruction
  violation, not a placeholder-vs-canonical metadiff artifact — the rule was
  explicit in CLAUDE.md.
- **Over-editing (scope):** three xrefs (FMA:17561, NCIT:C12315, SCTID:27485007)
  beyond what the issue or gold asked for. Defensible but unrequested; they
  lower recall vs the minimal gold and add mappings a curator did not vet.
- Definition text diverges from gold's verbatim wording (expanded clause);
  better content, but a metadiff mismatch and technically beyond the literal
  issue text.
- Term inserted at a different file location (near UBERON:3629) than gold;
  cosmetic for metadiff. Eval PR #262 behaves as the standard closed shadow PR.
