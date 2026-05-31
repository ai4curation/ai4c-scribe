---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 84
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.667
precision: 0.667
recall: 0.667
jaccard: 0.5
outcome: success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a substantively correct new term for the TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy, using a placeholder ID `MONDO:7770736` (gold was assigned canonical `MONDO:1060216` only at merge time). The term has a correct genus-differentia definition with all 7 issue PMIDs + the ClinGen URL, the ClinGen-qualified EXACT synonym, the correct logical definition (`intersection_of MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), the asserted gene relationship, and the issue tracker annotation — matching the gold PR's curatorial intent closely. F1=0.667 is the **best of all 14 attempts and substantially under-represents quality**: it is structurally capped by the new_term canonical-ID / insertion-location artifact (agents cannot know the merge-assigned `MONDO:1060216` or the gold's curator ORCID), not by errors in the agent's work.

## Strengths

- Correct gene grounding: `TSEN2` verified to `HGNC:28422` via HGNC REST, used as `http://identifiers.org/hgnc/28422` exactly as gold.
- Logical definition matches gold byte-for-byte in substance: `intersection_of: MONDO:0700092` + `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`, plus the asserted `relationship` with ClinGen source.
- Definition opens with the correct genus-differentia stem ("Any neurodevelopmental disorder in which the cause of the disease is a variation in the TSEN2 gene...") and carries all 7 issue PMIDs and the ClinGen affiliation URL as def xrefs, matching gold.
- Reproduced the gold's distinctive ClinGen-qualified synonym verbatim: `synonym: "..." EXACT [https://clinicalgenome.org/affiliation/40069/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`.
- Good methodology: checked for the pre-existing TSEN2 term `MONDO:0012890` (pontocerebellar hypoplasia type 2B) and correctly chose not to duplicate/disturb it; ran `make NORM` and `robot convert` syntax validation; verified the next free NTR ID.
- Correctly used a placeholder `MONDO:777xxxx` ID per Mondo NTR convention — the right behavior; the gold's `MONDO:1060216` is assigned only at merge.

## Issues

- **Omission (defensible)**: did not add the second parent `is_a: MONDO:0002254` (syndromic disease) that the gold curator added. The issue requested only `MONDO:0700092` as parent, so this is a reasonable scoping decision rather than an error; the syndromic parent was curator judgment not requested by the submitter or mandated by the approving reviewer.
- **Minor scope addition**: added `is_a: MONDO:0100500 (Mendelian neurodevelopmental disorder)` and `subset: rare` which gold did not. Both are defensible (the disorder is Mendelian and rare) but are extra assertions beyond the issue ask and beyond gold; the second `is_a` to MONDO:0100500 is also redundant with the asserted `MONDO:0700092` parent.
- Used its own creator attribution rather than the human curator ORCID (unavoidable; metadiff-relevant but not a real defect).
- **Case quality note**: F1 ceiling here is an artifact of new_term ID/location normalization, not agent quality — see METADATA Curation Note.
