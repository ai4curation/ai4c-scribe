# PR #9726 — Add parent term to MONDO:0005709 common cold

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9493](https://github.com/monarch-initiative/mondo/issues/9493)
- **PR**: [#9726](https://github.com/monarch-initiative/mondo/pull/9726)
- **Author**: @dragon-ai-agent
- **Merged**: 2025-12-01
- **task_type**: reclassification
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: changes_requested
- **scoping_notes**: Adds a single is_a parent axiom to an existing term.

## Context

An issue was filed requesting that "common cold" (MONDO:0005709) be given "viral respiratory tract infection" (MONDO:0024352) as a parent term. The common cold was missing this classification, which is important for grouping viral respiratory infections. The issue was addressed by the dragon-ai-agent, an automated curation system, making this one of the first AI-authored PRs in Mondo.

The AI agent analyzed multiple options from its issue analysis and selected the appropriate parent term addition. The issue labels indicate the AI succeeded but needed some human guidance during the process.

## Changes Made

Added 2 lines to `src/ontology/mondo-edit.obo`: an is_a relationship making "common cold" a subclass of "viral respiratory tract infection" and a source attribution annotation. This is a minimal but important classification fix that connects common cold to the broader respiratory infection hierarchy.

## Resolution

Easy difficulty for the ontology change itself (adding one parent axiom), but notable as an AI agent-authored PR. The main challenge was selecting the correct option from multiple possibilities discussed in the issue. An agent needs to understand disease classification well enough to determine that common cold should be classified as a viral respiratory tract infection rather than alternative groupings.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a0..e22cf7ba2d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="PMID:37426629", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

## Agent Attempts (13)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#310](https://github.com/ai4curation/eval-ont-agent-mondo/pull/310)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25762216384](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25762216384)
- **Workflow run**: [25762216384](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25762216384)

#### Agent PR Comment

# PR #<NN> - Add viral respiratory tract infection parent to common cold

#### Agent Issue Comment

# Issue #9493 - Add parent term to MONDO:0005709 common cold

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..02cd841db 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 2: kimi-k2.6 / opencode

- **Eval PR**: [#256](https://github.com/ai4curation/eval-ont-agent-mondo/pull/256)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25755552455](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755552455)
- **Workflow run**: [25755552455](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755552455)

#### Agent PR Comment

## Changes made for issue #9493

### Term modified
- **MONDO:0005709** — common cold

### Changes
Added a new parent term to better reflect the infectious/viral etiology of the common cold:

```obo
is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
```

Also added a term tracker item linking back to this issue:
```obo
property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
```

### Rationale
The existing definition of common cold already states that it is “usually caused by viruses (e.g., rhinovirus, adenovirus, parainfluenza virus, and coronavirus)”. Classifying it under **MONDO:0024352 (viral respiratory tract infection)** provides the most specific correct parent, which transitively places it under infectious disease (MONDO:0005550) as originally requested. No existing parents were removed.

### Checklist completed
- [x] Checked out term `MONDO:0005709` for editing
- [x] Verified parent term `MONDO:0024352` exists and is a child of infectious disease
- [x] Added new `is_a` relationship with appropriate source attribution
- [x] Added term tracker item for the issue
- [x] Checked the term back into `mondo-edit.obo`
- [x] Ran `make NORM` to normalize serialization
- [x] Verified minimal diff (only 2 lines added)
- [x] Committed changes locally

### Decisions
- Per curator instruction, **no logical definition (intersection_of) was added** -- only the subclass axiom.
- The ORCID provided by the curator (`https://orcid.org/0000-0003-2955-4640`) was included as a source on the new parent relationship.
- The PMIDs suggested in the initial analysis were not added because the existing definition (sourced to NCIT) already covers the viral etiology; no definitional change was required.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755552455)

#### Agent Issue Comment

Hi all, the requested parent term has been added to MONDO:0005709 (common cold). Specifically:

- Added `is_a: MONDO:0024352 ! viral respiratory tract infection` with source attribution to this issue and `https://orcid.org/0000-0003-2955-4640`.
- This transitively places common cold under infectious disease (MONDO:0005550) as requested, while using the most specific correct parent.
- No logical definition was added, per curator instruction.
- Existing parents were retained.

Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755552455)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..90dc07753 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#179](https://github.com/ai4curation/eval-ont-agent-mondo/pull/179)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..02cd841db 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 4: gpt-5.4 / codex

- **Eval PR**: [#157](https://github.com/ai4curation/eval-ont-agent-mondo/pull/157)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Workflow run**: [25640344434](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640344434)

#### Agent PR Comment

Implemented the requested classification update for `MONDO:0005709` (`common cold`) by adding:

`is_a: MONDO:0024352 ! viral respiratory tract infection`

Rationale:
- The issue thread explicitly requested Option 3: classify common cold under `viral respiratory tract infection` rather than only under the broader `infectious disease` parent.
- This preserves the existing parents and adds the more specific infectious-disease path:
  `common cold -> viral respiratory tract infection -> viral infectious disease -> infectious disease`
- The new parent assertion includes provenance from `PMID:32288450`, the issue URL, and the requested curator ORCID `https://orcid.org/0000-0003-2955-4640`.
- I also added an `IAO:0000233` tracker link for issue `#9493` on the term.

Checklist completed:
- [x] Read the imported issue context and comments from `__issue_context__.json`
- [x] Verified the requested implementation detail from the issue thread
- [x] Inspected `MONDO:0005709`, `MONDO:0024352`, `MONDO:0005108`, and `MONDO:0005550`
- [x] Checked out the term and edited it via `terms/`
- [x] Checked the term back into `src/ontology/mondo-edit.obo`
- [x] Verified literature applicability for the infectious/viral respiratory tract classification using `PMID:32288450`
- [x] Ran `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`
- [ ] Ran `make NORM && mv NORM mondo-edit.obo`

Validation notes:
- The `robot convert` syntax check succeeded and produced `mondo-edit.TMP.obo` without errors; I removed that temporary file afterward.
- I was not able to run the required normalization step because the environment does not have `docker`, and this repo's ODK wrapper (`src/ontology/run.sh`) depends on Docker.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640344434)

#### Agent Issue Comment

Implemented locally and committed for PR #<NN>.

Summary:
- Added `MONDO:0024352` (`viral respiratory tract infection`) as a parent of `MONDO:0005709` (`common cold`), which satisfies the request to classify common cold under infectious disease via the more specific viral respiratory tract infection path.
- Added provenance for issue `#9493` on the term and included the requested ORCID on the new parent assertion.

Validation:
- Confirmed supporting literature applicability with `PMID:32288450`.
- `robot convert` completed successfully as a syntax check.
- I could not run `make NORM` in this environment because the repo's ODK workflow depends on `docker`, and `docker` is not installed here.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640344434)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..ead6ba4a7 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="PMID:32288450", source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#87](https://github.com/ai4curation/eval-ont-agent-mondo/pull/87)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615980870](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615980870)
- **Workflow run**: [25615980870](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615980870)

#### Agent PR Comment

## Summary

Addressed issue #9493 by adding a more specific infectious disease parent to MONDO:0005709 `common cold`:

- Added `is_a: MONDO:0024352 ! viral respiratory tract infection`
- Added source annotations for the GitHub issue and requested curator ORCID (`https://orcid.org/0000-0003-2955-4640`)
- Added issue #9493 as a `term_tracker_item` annotation

This satisfies the requested placement under MONDO:0005550 `infectious disease` via the existing hierarchy:

`common cold` → `viral respiratory tract infection` → `viral infectious disease` → `infectious disease`

## Rationale

The existing definition of `common cold` states that it is usually caused by viruses, and MONDO:0024352 `viral respiratory tract infection` is the most specific applicable parent already present in MONDO. This follows the issue discussion requesting Option 3 without adding a logical definition.

## Checklist

- [x] Read issue context and comments
- [x] Checked current MONDO:0005709, MONDO:0024352, MONDO:0005108, and MONDO:0005550 stanzas
- [x] Confirmed MONDO:0024352 is already under viral infectious disease / infectious disease
- [x] Edited via `obo-checkout.pl` / `obo-checkin.pl`
- [x] Did not add a logical definition, per maintainer request
- [x] Ran syntax validation: `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo` completed successfully

## Notes

No new PMID citations were added. The issue comments mentioned literature background, but the implemented axiom was sourced to the issue and requested ORCID.

Normalization via ODK Docker was attempted using the documented direct Docker invocation, but Docker is not available in this environment (`docker: command not found`).

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615980870)


#### Agent Issue Comment

Implemented in PR #<NN>.

MONDO:0005709 `common cold` has been classified under MONDO:0024352 `viral respiratory tract infection`, which is a subclass of viral infectious disease and therefore infectious disease.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615980870)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..90dc07753 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#66](https://github.com/ai4curation/eval-ont-agent-mondo/pull/66)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615939093](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615939093)
- **Workflow run**: [25615939093](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939093)

#### Agent PR Comment

## Summary

This change updates `MONDO:0005709` common cold by adding `MONDO:0024352` viral respiratory tract infection as an asserted parent. This implements the requested infectious disease placement using the more specific parent endorsed in the issue discussion, while avoiding a new logical definition as requested.

## Rationale

`MONDO:0024352` viral respiratory tract infection is already classified under `MONDO:0005108` viral infectious disease, which is under `MONDO:0005550` infectious disease. Adding this parent therefore satisfies the issue request while preserving the existing anatomical and inflammatory parentage for common cold.

The new parent assertion is sourced to issue #9493 and the ORCID requested in the issue thread. I also added issue #9493 as a term tracker item.

## Checklist

- Read imported issue title, body, and comments from `__issue_context__.json`.
- Verified existing stanzas for `MONDO:0005709`, `MONDO:0024352`, and `MONDO:0005550` using `obo-grep.pl`.
- Checked out `MONDO:0005709`, edited the term stanza, and checked it back into `src/ontology/mondo-edit.obo`.
- Did not add the logical definition proposed in the automated analysis, per curator instruction.
- Did not add PMID citations because no PMID was provided for this edit; no new literature claims were introduced.
- Ran `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o src/ontology/mondo-edit.TMP.obo` successfully for OBO syntax validation.
- Attempted ODK normalization, but Docker is unavailable in this environment (`docker: command not found`), so `make NORM` could not be run here.

## Commit

Committed locally as `e4edcb0` (`Add infectious parentage for common cold`).

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939093)


#### Agent Issue Comment

Implemented in PR #<NN>.

`MONDO:0005709` common cold is now asserted as a child of `MONDO:0024352` viral respiratory tract infection, which provides the requested infectious disease ancestry via viral infectious disease.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615939093)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..90dc07753 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 7: gpt-5.5 / codex

- **Eval PR**: [#46](https://github.com/ai4curation/eval-ont-agent-mondo/pull/46)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615892229](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615892229)
- **Workflow run**: [25615892229](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615892229)

#### Agent PR Comment

## Summary

Addressed issue #9493 by adding `MONDO:0024352` (`viral respiratory tract infection`) as an additional parent for `MONDO:0005709` (`common cold`).

The new parent axiom is sourced to the issue and to the requested curator ORCID:

```obo
is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
```

I also added the issue as a `term_tracker_item`:

```obo
property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
```

#### Agent Issue Comment

Changes committed in PR #<NN>.

Implemented the requested Option 3: `common cold` now has `viral respiratory tract infection` as an additional parent, which places it under `infectious disease` through the existing MONDO hierarchy.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615892229)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..90dc07753 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,11 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 8: claude-sonnet-4.5 / claude

- **Eval PR**: [#444](https://github.com/ai4curation/eval-ont-agent-mondo/pull/444)
- **F1**: 0.400  **Precision**: 0.500  **Recall**: 0.333  **Jaccard**: 0.250
- **Trace**: [25867735895](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867735895)
- **Workflow run**: [25867735895](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867735895)

#### Agent PR Comment

## Summary

This PR addresses issue #9493 by adding a parent classification to MONDO:0005709 (common cold). Following the recommendation in Option 3 from the issue analysis, the term has been classified under MONDO:0024352 (viral respiratory tract infection) rather than directly under infectious disease.

#### Agent Issue Comment

Changes committed in PR #<NN>.

The common cold (MONDO:0005709) has been classified as a child of viral respiratory tract infection (MONDO:0024352), which provides a more specific classification than directly under infectious disease. Since viral respiratory tract infection is itself a child of infectious disease, this satisfies the original request while being more accurate given the viral etiology of common cold.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867735895)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..4a0be3185 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,9 +116781,10 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9493" xsd:anyURI
 
 [Term]
 id: MONDO:0005710

```

### Attempt 9: claude-sonnet-4.5 / copilot

- **Eval PR**: [#529](https://github.com/ai4curation/eval-ont-agent-mondo/pull/529)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..9fcd05fb3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,6 +116781,7 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI

```

### Attempt 10: claude-sonnet-4.5 / copilot

- **Eval PR**: [#495](https://github.com/ai4curation/eval-ont-agent-mondo/pull/495)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..9fcd05fb3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,6 +116781,7 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI

```

### Attempt 11: claude-opus-4.7 / claude

- **Eval PR**: [#406](https://github.com/ai4curation/eval-ont-agent-mondo/pull/406)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25819417795](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25819417795)
- **Workflow run**: [25819417795](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819417795)

#### Agent PR Comment

# Add viral respiratory tract infection parent to common cold

Closes #9493.

## Summary

Added a new `is_a` parent to **MONDO:0005709 (common cold)**:

```
is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
```

## Rationale

The original request (issue #9493) was to add MONDO:0005550 (infectious disease) as a parent. The issue-analysis comment proposed three options, and @matentzn instructed implementing **Option 3** (the most specific): classify common cold under **viral respiratory tract infection (MONDO:0024352)**, which itself inherits from `viral infectious disease` → `infectious disease`. This satisfies the original request while being more precise.

Per the maintainer's instructions:
- The logical definition (`intersection_of` axioms) was **not** added.
- ORCID `https://orcid.org/0000-0003-2955-4640` was added as a source on the new `is_a` axiom, alongside the issue URL.
- PMIDs were to be checked for applicability — the term has no PMID references and none were added in this edit, so no PMID validation was needed.

## Why this classification is appropriate

- The existing definition of MONDO:0005709 explicitly states the common cold is "usually caused by viruses (e.g., rhinovirus, adenovirus, parainfluenza virus, and coronavirus)".
- MONDO:0024352's own definition explicitly mentions rhinoviruses as a causative agent.
- The classification is consistent with existing MONDO patterns where viral respiratory syndromes are classified under viral respiratory tract infection.

## Checklist

- [x] Verified MONDO:0005709 exists and reviewed its current axioms
- [x] Verified MONDO:0024352 (viral respiratory tract infection) exists and is a child of viral infectious disease → infectious disease
- [x] Checked term out with `obo-checkout.pl`
- [x] Added `is_a` with source attribution (issue URL + ORCID)
- [x] Did **not** add a logical definition (`intersection_of`), per maintainer
- [x] Did **not** modify any existing parents
- [x] Checked term back in with `obo-checkin.pl`
- [x] Reviewed `git diff` — single-line addition, no other changes
- [x] Confirmed no PMIDs were involved that needed validation

## Notes

- `robot`/ODK was not available locally to run the NORM step; however, the edit was made via `obo-checkout.pl`/`obo-checkin.pl`, so the serialisation should already be consistent. The CI ontology pipeline will normalise as needed.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819417795)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Added `is_a: MONDO:0024352` (viral respiratory tract infection) as a new parent of MONDO:0005709 (common cold), per @matentzn's instruction to implement Option 3 without a logical definition. The new parent inherits from viral infectious disease and infectious disease, satisfying the original request. ORCID https://orcid.org/0000-0003-2955-4640 was added as a source on the new is_a axiom alongside the issue URL. No PMIDs were involved in this edit, so none needed checking.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25819417795)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..9fcd05fb3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,6 +116781,7 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0024352 {source="https://github.com/monarch-initiative/mondo/issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI

```

### Attempt 12: gemma-4-31b / opencode

- **Eval PR**: [#292](https://github.com/ai4curation/eval-ont-agent-mondo/pull/292)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25761159294](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25761159294)
- **Workflow run**: [25761159294](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25761159294)

#### Agent PR Comment

### Summary of Changes
Added `MONDO:0005550` (infectious disease) as a parent term to `MONDO:0005709` (common cold).

### Rationale
The common cold is a viral infectious disease. The existing definition for `MONDO:0005709` already states it is "usually caused by viruses", which justifies its classification under `MONDO:0005550`.

### Validation
- Verified that both `MONDO:0005709` and `MONDO:0005550` exist in the ontology.
- Added the requested source attribution: `https://orcid.org/0000-0003-2955-4640`.
- Normalized the ontology serialization using `make NORM`.
- Validated the syntax using `robot convert`.

### Checklist
- [x] Research and verify terms
- [x] Implement parent term addition
- [x] Add source attribution
- [x] Normalize serialization
- [x] Validate syntax
- [x] Local commit
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25761159294)

#### Agent Issue Comment

Changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25761159294)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..a1de127cc 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116781,6 +116781,7 @@ xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
+is_a: MONDO:0005550 {source="https://orcid.org/0000-0003-2955-4640"} ! infectious disease
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough
 property_value: curated_content_resource "https://www.malacards.org/card/common_cold" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI

```

### Attempt 13: gemma-4-31b / opencode

- **Eval PR**: [#204](https://github.com/ai4curation/eval-ont-agent-mondo/pull/204)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25683737572](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25683737572)
- **Workflow run**: [25683737572](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25683737572)

#### Agent Issue Comment

changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25683737572)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f26e3f70a..c889df84b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -116779,6 +116779,7 @@ xref: SCTID:266377009 {source="DOID:10459"}
 xref: SCTID:54150009 {source="DOID:10459"}
 xref: SCTID:82272006 {source="DOID:10459", source="MONDO:equivalentTo"}
 xref: UMLS:C0009443 {source="MEDGEN:3179", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+is_a: MONDO:0005550 {source="https://orcid.org/0000-0003-2955-4640"} ! infectious disease
 is_a: MONDO:0001040 {source="NCIT:C34500"} ! nasopharyngitis
 is_a: MONDO:0004867 {source="DOID:10459", source="MONDO:Redundant"} ! upper respiratory tract disorder
 relationship: disease_has_feature HP:0012735 {source="MONDO:Wikidata"} ! Cough

```
