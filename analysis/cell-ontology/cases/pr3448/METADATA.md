---
repo: obophenotype/cell-ontology
issue_number: 3447
pr_number: 3448
issue_title: "improve definition of Islands of Calleja granule cell"
issue_created_at: "2025-11-18"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-11-20"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 6
    deletions: 4
  - path: src/ontology/components/hra_subset.owl
    additions: 3
    deletions: 5
scoping: tightly_scoped
task_type: other
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: neuroscience
tags:
  - text-definition
  - GABAergic
  - Islands-of-Calleja
  - label-correction
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-faceted term update requiring label correction, definition expansion, and reclassification under GABAergic neuron lineage
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extras_and_provenance
companion_prs: []
scoring_caveat: "metadiff vs #3448 is systematically deflated for all 6 attempts. The gold cl-edit.owl diff includes (a) the PR author's terms:contributor ORCID provenance line, (b) an unrelated annotation-property comment edit at line ~3638 (oboInOwl:hasDbXref label comment), and (c) auto-generated hra_subset.owl churn (OWL API version string, whitespace, taxon-subset removal) — none of which the issue asked for and none of which an agent editing cl-edit.owl could/should reproduce. Judge attempts against the issue's explicit asks (plural label, verbatim definition, retain DOI + add PMID:37898623/PMID:34795450, add GABAergic neuron axiom), not the F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Islands of Calleja granule cell (CL_4030053) had an incomplete definition and a label that did not follow CL naming conventions. Issue #3447 requested an improved textual definition that better captures the GABAergic nature of this cell type and its anatomical localization, complementing the broader label correction effort tracked in issue #3321.

## Changes Made

Updated `cl-edit.owl` with a corrected label, expanded textual definition referencing the GABAergic classification, and added a subClassOf axiom linking CL_4030053 to the GABAergic neuron hierarchy. Minor adjustments were also made to the HRA subset component file. The net change was 6 additions and 4 deletions in the edit file.

## Resolution

The PR went through one round of changes_requested review before being approved and merged. Medium difficulty because the change required domain knowledge about the neurochemical identity of Islands of Calleja granule cells and correct placement within the GABAergic neuron subhierarchy, beyond a simple text edit.

## Curation Note (data quality)

Flagged `case_quality: poor` (reason `gold_has_out_of_scope_extras_and_provenance`) by claude-opus-4.7 on 2026-05-16.

This issue (#3447) is an unusually well-specified transcription task: it gives the exact target label, the verbatim definition text, the two PMIDs to add, an explicit instruction to retain existing references, and a request for a "GABAergic neuron" axiom. It was resolved by the **single** PR #3448 (no companion PRs; #3321 is only a broad "Basal Ganglion product EPIC" tracking issue, still open). Step 3a does not apply.

However the metadiff F1 (0.429–0.522 across all 6 attempts, precision pinned at 0.375) **systematically under-represents** quality because the gold diff contains material the issue never requested and that an agent editing `cl-edit.owl` cannot/should not reproduce:

1. **Author provenance**: gold adds `AnnotationAssertion(terms:contributor obo:CL_4030053 "https://orcid.org/0000-0002-5507-2103")` — the original copilot PR author's ORCID. Not requested; no agent could produce the correct human ORCID.
2. **Unrelated foreign edit**: gold changes the annotation-property comment at line ~3638 from `# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)` to `(has cross-reference)` — a serialization/comment-regeneration artifact wholly unrelated to CL_4030053.
3. **Auto-generated component churn**: the `hra_subset.owl` hunks (OWL API version string `4.5.29` → `4.5.29.2024-05-13T12:11:03Z`, a stray whitespace line, collapse of the CL_4030053 HRA `owl:Class` block) are pipeline-generated artifacts, not authored edits responsive to the issue.

Net issue-relevant gold content in `cl-edit.owl` is exactly: plural label, verbatim definition, three xrefs (retained DOI + 2 new PMIDs), and `SubClassOf(CL_4030053 CL_0000617)`. **All six attempts reproduced this substantive core.** Substance-based grading:

- **pr72 / pr52** (gpt-5.5/opencode, blob `26c8a14`): cleanest — honored "do not replace existing" by retaining the DOI xref and adding both PMIDs; correct label + GABAergic parent; only defensible extras (IAO_0000233 tracker, CPNE4 comment plural tidy). `success`.
- **pr35** (gpt-5.5/codex), **pr78** (gpt-5.4/codex): correct core + retained DOI; paraphrased definition, IAO_0000233 tracker, EOF newline artifact; pr78 also paraphrased the CPNE4 comment losing the explicit subject. `success`.
- **pr227** (claude-sonnet-4.5): used the issue's verbatim definition text (best fidelity) and was the most tightly scoped, but **dropped the existing DOI xref**, violating the explicit "do not replace the existing ones". `partial_success`.
- **pr98** (claude-haiku-4.5): correct core but **dropped the DOI xref** and additionally **clobbered `terms:date`** (2023-06-14 → 2026-05-10), damaging provenance. `partial_success`.

Downstream scoring/aggregation should down-weight or exclude this case's F1, or re-score against the issue's explicit asks rather than the line-level gold diff.
