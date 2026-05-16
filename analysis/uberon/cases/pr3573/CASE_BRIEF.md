---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3572
pr_number: 3573
issue_title: Revise esophagus and esophageal artery partonomy
pr_author: dragon-ai-agent
pr_merged_at: '2025-07-02'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: thoracic-anatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3573 — Revise esophagus and esophageal artery partonomy

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3572](https://github.com/obophenotype/uberon/issues/3572) | [PR #3573](https://github.com/obophenotype/uberon/pull/3573) | @dragon-ai-agent | merged 2025-07-02

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

The esophagus had a "located in thoracic cavity" relationship, but this is anatomically incorrect because the esophagus has cervical and abdominal portions that extend beyond the thorax. Additionally, the esophageal artery used "branching part of" instead of the correct "connecting branch of" relationship to the thoracic aorta.

## Changes Made

Removed the incorrect "located in thoracic cavity" relationship from the esophagus term (UBERON:0001043). Replaced the "branching part of" relationship with "connecting branch of" for the esophageal artery (UBERON:0035539) in relation to the thoracic aorta.

## Resolution

Medium difficulty because the agent must understand that the esophagus is a long tubular organ spanning the neck, thorax, and upper abdomen, so restricting its location to the thoracic cavity is incorrect. It also requires knowing the distinction between "branching part of" and "connecting branch of" in vascular partonomy.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

## Agent Attempts (8)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#310](https://github.com/ai4curation/eval-ont-agent-uberon/pull/310)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25878072165](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25878072165)
- **Workflow run**: [25878072165](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25878072165)

#### Agent PR Comment

# Revise esophagus and esophageal artery partonomy

This PR addresses issue #3572 by making two anatomical relationship corrections.

## Changes Made

### 1. Esophagus (UBERON:0001043)
**Removed:** `relationship: located_in UBERON:0002224 ! thoracic cavity`

**Rationale:** The esophagus is not exclusively located in the thoracic cavity. In humans and other mammals, the esophagus spans three anatomical regions:
- Cervical part (in the neck)
- Thoracic part (in the chest)
- Abdominal part (short segment in the abdomen)

The previous axiom incorrectly implied that the entire esophagus is located within the thoracic cavity, which is anatomically inaccurate.

### 2. Esophageal artery (UBERON:0035539)
**Changed:** `relationship: branching_part_of UBERON:0001515 ! thoracic aorta`
**To:** `relationship: connecting_branch_of UBERON:0001515 ! thoracic aorta`

**Rationale:** The relationship type was updated to use the more appropriate `connecting_branch_of` instead of `branching_part_of` to better represent the anatomical connection between the esophageal arteries and the thoracic aorta.

## Validation
- Both terms were checked out using `obo-checkout.pl`
- Edits were made to individual term files in the `terms/` directory
- Terms were checked back in using `obo-checkin.pl`
- Changes verified via `obo-grep.pl` and `git diff`

## Checklist
- [x] Checked out terms UBERON:0001043 and UBERON:0035539
- [x] Removed incorrect location axiom from esophagus
- [x] Updated relationship type for esophageal artery
- [x] Checked in all edits to src/ontology/uberon-edit.obo
- [x] Verified changes in git diff
- [x] Committed with clear message and signed as @dragon-ai-agent

@dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25878072165)


#### Agent Issue Comment

Changes committed in PR #<NN>. Both requested modifications have been completed:
- Removed the 'located in' thoracic cavity axiom from esophagus (UBERON:0001043)
- Changed 'branching part of' to 'connecting branch of' for esophageal artery (UBERON:0035539)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25878072165)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

### Attempt 2: claude-haiku-4.5 / claude

- **Eval PR**: [#188](https://github.com/ai4curation/eval-ont-agent-uberon/pull/188)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25762064001](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25762064001)
- **Workflow run**: [25762064001](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25762064001)

#### Agent PR Comment

# Revise esophagus and esophageal artery partonomy

#### Agent Issue Comment

Changes committed in PR #<NN>

Both requested modifications have been completed:
1. Removed 'located_in thoracic cavity' axiom from esophagus (UBERON:0001043)
2. Changed esophageal artery (UBERON:0035539) relationship from 'branching_part_of' to 'connecting_branch_of' thoracic aorta

The changes properly reflect the anatomical reality that the esophagus extends beyond the thoracic cavity and align the artery relationship with the UBERON artery design pattern.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25762064001)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

### Attempt 3: gemma-4-31b / opencode

- **Eval PR**: [#138](https://github.com/ai4curation/eval-ont-agent-uberon/pull/138)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25710192789](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25710192789)
- **Workflow run**: [25710192789](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25710192789)

#### Agent PR Comment

## Summary of Changes
- **Esophagus (UBERON:0001043):** Removed the axiom `relationship: located_in UBERON:0002224 ! thoracic cavity`.
- **Esophageal artery (UBERON:0035539):** Changed the relationship to `thoracic aorta` (UBERON:0001515) from `branching_part_of` to `connecting_branch_of`.

## Rationale
- The `esophagus` extends beyond the thoracic cavity, having both cervical and abdominal segments, making the `located_in thoracic cavity` axiom inaccurate.
- The relationship change for the `esophageal artery` was requested to better reflect its anatomical connection to the thoracic aorta.

## Validation
- Verified the changes using `obo-grep.pl` in the `src/ontology/uberon-edit.obo` file to ensure the axioms were correctly removed/updated.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25710192789)


#### Agent Issue Comment

The requested changes have been committed in PR #<NN>.
- Removed the `located_in` relationship to `thoracic cavity` (UBERON:0002224) for `esophagus` (UBERON:0001043) because it also has cervical and abdominal parts.
- Updated the relationship for `esophageal artery` (UBERON:0035539) from `branching_part_of` to `connecting_branch_of` the `thoracic aorta` (UBERON:0001515).

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25710192789)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

### Attempt 4: claude-haiku-4.5 / claude

- **Eval PR**: [#103](https://github.com/ai4curation/eval-ont-agent-uberon/pull/103)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

### Attempt 5: gpt-5.4 / codex

- **Eval PR**: [#86](https://github.com/ai4curation/eval-ont-agent-uberon/pull/86)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640366030](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640366030)

#### Agent PR Comment

This update addresses issue #3572 by revising two axioms in `src/ontology/uberon-edit.obo`.

Changes made:
- Removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from `UBERON:0001043` (`esophagus`). The issue rationale is consistent with existing Uberon content, which already includes cervical, thoracic, and abdominal esophageal subdivisions.
- Changed `UBERON:0035539` (`esophageal artery`) from `relationship: branching_part_of UBERON:0001515 ! thoracic aorta` to `relationship: connecting_branch_of UBERON:0001515 ! thoracic aorta`. This matches the existing modeling pattern already used for many artery branch terms in Uberon.

Validation and process:
- Read the imported issue context from `__issue_context__.json`.
- Queried only `src/ontology/uberon-edit.obo` using `obo-grep.pl`, per repository instructions.
- Checked the current stanzas for `UBERON:0001043` and `UBERON:0035539`.
- Confirmed that `connecting_branch_of` is already the established relation used for comparable artery branch terms.
- Checked out the affected terms into `terms/` with `obo-checkout.pl`, edited those stanzas, and checked them back in with `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo`.
- Cleaned up incidental serializer-only reorderings so the net ontology diff is limited to the two requested axioms.

Checklist completed:
- [x] Issue context reviewed
- [x] Target terms verified in `uberon-edit.obo`
- [x] Requested parent/relation consistency checked
- [x] Edits made through checked-out term stanzas
- [x] Main OBO file reserialized
- [x] Net diff verified to contain only the requested ontology changes
- [x] Changes committed locally

Local commits:
- `afe8050` Revise esophagus and esophageal artery partonomy
- `14b89f7` Remove incidental serializer-only reorderings

Signed,
@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640366030)

#### Agent Issue Comment

Addressed locally and committed for PR #<NN>.

Changes made:
- Removed the `located_in thoracic cavity` axiom from `esophagus` (`UBERON:0001043`), since the esophagus also has cervical and abdominal parts.
- Replaced `branching_part_of thoracic aorta` with `connecting_branch_of thoracic aorta` on `esophageal artery` (`UBERON:0035539`) to match existing Uberon artery modeling.

Signed,
@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640366030)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#70](https://github.com/ai4curation/eval-ont-agent-uberon/pull/70)
- **F1**: 0.857  **Precision**: 1.000  **Recall**: 0.750  **Jaccard**: 0.750
- **Trace**: [25615971981](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615971981)
- **Workflow run**: [25615971981](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615971981)

#### Agent PR Comment

## Summary

Addresses issue #3572 by revising two partonomy axioms in `src/ontology/uberon-edit.obo`:

- Removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from `UBERON:0001043` (`esophagus`), since the esophagus is not wholly thoracic and includes cervical and abdominal portions in humans.
- Replaced `relationship: branching_part_of UBERON:0001515 ! thoracic aorta` with `relationship: connecting_branch_of UBERON:0001515 ! thoracic aorta` for `UBERON:0035539` (`esophageal artery`).
- Added `term_tracker_item` metadata linking both edited terms back to issue #3572.

## Rationale

The previous esophagus location axiom over-constrained the class to the thoracic cavity. The updated esophageal artery relation matches the requested modeling as a connecting branch of the thoracic aorta rather than a branching part.

## Checklist

- [x] Read the imported issue context from `__issue_context__.json`.
- [x] Checked the existing `esophagus` and `esophageal artery` stanzas in `src/ontology/uberon-edit.obo`.
- [x] Edited the terms via `obo-checkout.pl` / `obo-checkin.pl` workflow.
- [x] Re-serialized `src/ontology/uberon-edit.obo` with `robot convert`.
- [x] Validated OBO parsing with `robot convert -i src/ontology/uberon-edit.obo -f obo -o /tmp/uberon-edit-check.obo`.
- [x] Committed only the ontology edit file.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615971981)


#### Agent Issue Comment

Changes committed locally for PR #<NN>.

Implemented the requested partonomy updates for `esophagus` and `esophageal artery`, with issue tracker metadata added to the edited terms.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615971981)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..30e675aa0 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -11514,6 +11513,7 @@ property_value: external_definition "Anterior end of the alimentary canal lined
 property_value: external_ontology_notes "esophagus NOT part of gut in MA. part of gut in ZFA. part_of gut (via UGIT) in FMA. Consider splitting. Interspecies: The human oesophagus is 25 cm long and has a diameter of ca. 2 cm. Only little information was found on the oesophagus in rat, rabbit and pig. The oesophagus of rat (75 x 2 mm) and rabbit has no mucous glands and the cardia of the stomach has a well-developed sphincter, which prevents them from vomiting (Hebel and Stromberg, 1988; Manning et al., 1994). Morphologically the oesophagus is similar in man and pig; both are omnivores and have a non-keratinised epithelium, submucous glands and similar membrane enzymes. Like in humans, pigs can suffer from reflux oesophagitis and stress ulceration of the oesophagus. The pig oesophagus may therefore be a good model for investigation compared to the human oesophagus (Christie et al., 1995)" xsd:string {external_ontology="MA"}
 property_value: has_relational_adjective "esophageal" xsd:string
 property_value: homology_notes "The few structural specializations in (adult lampreys) pharynx include complex valves on the external gill openings that direct the tidal flow, and the division of the ancestral pharynx into an oesophagus and a respiratory pharynx.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0000450", ontology="VHOG", source="DOI:10.1111/j.1096-3642.1996.tb01658.x Mallatt J, Ventilation and the origin of jawed vertebrates: a new mouth. Zoological Journal of the Linnean Society (1996)", source="http://bgee.unil.ch/"}
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3572" xsd:anyURI
 
 [Term]
 id: UBERON:0001044
@@ -184163,7 +184163,8 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3572" xsd:anyURI
 
 [Term]
 id: UBERON:0035542

```

### Attempt 7: claude-opus-4.7 / claude

- **Eval PR**: [#248](https://github.com/ai4curation/eval-ont-agent-uberon/pull/248)
- **F1**: 0.300  **Precision**: 1.000  **Recall**: 0.176  **Jaccard**: 0.176
- **Trace**: [25835240609](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25835240609)
- **Workflow run**: [25835240609](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835240609)

#### Agent PR Comment

# Revise esophagus and esophageal artery partonomy

Addresses [issue #3572](https://github.com/obophenotype/uberon/issues/3572).

## Summary of changes

Two targeted edits in `src/ontology/uberon-edit.obo`:

### 1. UBERON:0001043 (esophagus)

Removed the axiom:

```
relationship: located_in UBERON:0002224 ! thoracic cavity
```

**Rationale:** The esophagus is not entirely located within the thoracic cavity — in humans (and other mammals) it has a cervical part (above the thoracic inlet) and an abdominal part (below the diaphragm, between the esophageal hiatus and the gastroesophageal junction). A blanket `located_in some thoracic cavity` axiom is therefore incorrect at the class level. This matches the request in the issue.

### 2. UBERON:0035539 (esophageal artery)

Changed:

```
relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
```

to:

```
relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
```

**Rationale:** The esophageal arteries are connecting branches of the thoracic aorta (delivering blood to a distinct organ, the esophagus), not branching parts of the aorta itself. `connecting_branch_of` is the appropriate object property here and is already in widespread use in the ontology for analogous vessel relationships (e.g., branches of the celiac, superior mesenteric, internal iliac, and internal carotid arteries).

## Checklist

- [x] Read issue #3572 and identified the two specific edits requested
- [x] Inspected both terms via `obo-grep.pl` before editing
- [x] Checked out the two terms via `obo-checkout.pl` and edited them in `terms/`
- [x] Verified that `connecting_branch_of` is an established relationship in `uberon-edit.obo` (used on multiple existing artery terms)
- [x] Checked the terms back in via `obo-checkin.pl`
- [x] Reserialized `src/ontology/uberon-edit.obo` via `robot convert -f obo`
- [x] Confirmed the resulting diff contains only the two intended axiom changes plus incidental attribute-order normalizations from the robot reserialization
- [x] Committed the change, signed as `@dragon-ai-agent`

## Notes

The robot reserialization produced a handful of incidental, semantically-neutral reorderings of attributes inside `{}` annotation blocks (e.g., swapping the order of `seeAlso=...` and `source=...`). These are unavoidable side effects of running `robot convert` per the CLAUDE.md guidance and do not change ontology semantics.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835240609)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Both requested edits have been applied to `src/ontology/uberon-edit.obo`:

1. Removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from **esophagus** (UBERON:0001043).
2. Replaced `relationship: branching_part_of UBERON:0001515 ! thoracic aorta` with `relationship: connecting_branch_of UBERON:0001515 ! thoracic aorta` on **esophageal artery** (UBERON:0035539).

Please review at your convenience, @aleixpuigb.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835240609)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..74f84e11b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -930,7 +930,7 @@ intersection_of: has_quality PATO:0002236 ! aliform
 relationship: capable_of_part_of GO:0060361 ! flight
 relationship: in_taxon NCBITaxon:33213 ! Bilateria
 relationship: never_in_taxon NCBITaxon:118072 {source="bgee"} ! Coelacanthimorpha
-relationship: never_in_taxon NCBITaxon:186634 {seeAlso="Wikipedia:Flying_fish", source="bgee"} ! Otomorpha
+relationship: never_in_taxon NCBITaxon:186634 {source="bgee", seeAlso="Wikipedia:Flying_fish"} ! Otomorpha
 relationship: never_in_taxon NCBITaxon:314147 {source="bgee"} ! Glires
 relationship: never_in_taxon NCBITaxon:6231 {source="bgee"} ! Nematoda
 relationship: never_in_taxon NCBITaxon:7878 {source="bgee"} ! Dipnomorpha
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -22376,7 +22375,7 @@ relationship: preaxialmost_part_of UBERON:0002398 ! manus
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/6/64/Thumb-up.jpg" xsd:anyURI
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/2/2c/Thumbs_up.jpg" xsd:anyURI
 property_value: taxon_notes "Not present in Anurans (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012260", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012260"}
 
 [Term]
 id: UBERON:0001464
@@ -28060,7 +28059,7 @@ relationship: part_of UBERON:0010272 ! hyoid apparatus
 property_value: axiom_lost_from_external_ontology "relationship loss: part_of hyoid plate (AAO:0000664)[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO"}
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/1/1f/Gray186.png" xsd:anyURI
 property_value: external_definition "Paired processes that extend posterolaterally from the posterior margin of the hyoid plate. These processes are the ossified posteromedial processes and invest the laryngeal apparatus.[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO", source="AAO:LAP"}
-property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {seeAlso="https://github.com/obophenotype/uberon/issues/548", source="WP"}
+property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {source="WP", seeAlso="https://github.com/obophenotype/uberon/issues/548"}
 
 [Term]
 id: UBERON:0001686
@@ -38535,7 +38534,7 @@ xref: Wikipedia:Spinal_accessory_nerve
 xref: XAO:0004214
 intersection_of: UBERON:0001021 ! nerve
 intersection_of: extends_fibers_into UBERON:0020358 ! accessory XI nerve nucleus
-relationship: dubious_for_taxon NCBITaxon:8292 {seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7", source="VHOG", source="Wikipedia"} ! Amphibia
+relationship: dubious_for_taxon NCBITaxon:8292 {source="VHOG", source="Wikipedia", seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7"} ! Amphibia
 relationship: in_taxon NCBITaxon:32523 ! Tetrapoda
 relationship: innervates UBERON:0001737 ! larynx
 relationship: innervates UBERON:3010692 {gci_relation="part_of", gci_filler="NCBITaxon:8292", source="ISBN:080184780X"} ! m. cucullaris
@@ -74531,7 +74530,7 @@ relationship: part_of UBERON:5003622 ! manual digit 2 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/d/d5/Index_finger.JPG" xsd:anyURI
 property_value: has_relational_adjective "indicis" xsd:string
 property_value: taxon_notes "Anurans lack manual digit 1, so manual digit 2 is the digit after the prepollex (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012261", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012261"}
 
 [Term]
 id: UBERON:0003623
@@ -74568,7 +74567,7 @@ relationship: ambiguous_for_taxon NCBITaxon:8782 ! Aves
 relationship: part_of UBERON:0012141 {source="https://github.com/obophenotype/uberon/wiki/Inferring-part-of-relationships"} ! manual digitopodium region
 relationship: part_of UBERON:5003623 ! manual digit 3 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/f/fd/Middle_finger.jpg" xsd:anyURI
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012262", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012262"}
 
 [Term]
 id: UBERON:0003624
@@ -138779,7 +138778,7 @@ name: spleen marginal sinus
 def: "The border region surrounding the spleen B cell follicles and the periarteriolar lymphoid sheath that separates it from the marginal zone that mediates lymphocyte entry into the white pulp from the blood." [MP:MP]
 subset: pheno_slim
 synonym: "splenic marginal sinus" EXACT [MP:0002363]
-xref: EMAPA:37964 {source="MA:th", seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117"}
+xref: EMAPA:37964 {seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117", source="MA:th"}
 xref: MA:0000754
 xref: NCIT:C49776
 xref: UMLS:C1710157 {source="ncithesaurus:Splenic_Marginal_Sinus"}
@@ -151540,7 +151539,7 @@ xref: SCTID:361795009
 xref: Wikipedia:Malleolus
 is_a: UBERON:0005913 ! zone of bone organ
 relationship: part_of UBERON:0004410 ! distal epiphysis of fibula
-property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", seeAlso="UBERON:0004410", source="UBERON:skansa"}
+property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", source="UBERON:skansa", seeAlso="UBERON:0004410"}
 
 [Term]
 id: UBERON:0012292
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542
@@ -225213,8 +225212,8 @@ id: UBERON:8910024
 name: airway hillock
 def: "A region of squamous epithelium found in the tracheobronchial tree - continuous with the tracheobronchial epithelium." [DOI:10.1038/s41586-024-07377-1]
 is_a: UBERON:0006914 ! squamous epithelium
-relationship: part_of UBERON:0007196 ! tracheobronchial tree
 relationship: has_part CL:4030023 ! respiratory tract hillock cell
+relationship: part_of UBERON:0007196 ! tracheobronchial tree
 
 [Typedef]
 id: aboral_to

```

### Attempt 8: gpt-5.5 / codex

- **Eval PR**: [#32](https://github.com/ai4curation/eval-ont-agent-uberon/pull/32)
- **F1**: 0.300  **Precision**: 1.000  **Recall**: 0.176  **Jaccard**: 0.176
- **Trace**: [25615887850](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615887850)
- **Workflow run**: [25615887850](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615887850)

#### Agent PR Comment

## Summary

This addresses issue #3572 by revising the requested esophagus and esophageal artery partonomy assertions in `src/ontology/uberon-edit.obo`.

Changes made:

- Removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from `UBERON:0001043` esophagus, because the issue notes that esophagus includes cervical and abdominal parts as well as a thoracic part.
- Replaced `relationship: branching_part_of UBERON:0001515 ! thoracic aorta` with `relationship: connecting_branch_of UBERON:0001515 ! thoracic aorta` on `UBERON:0035539` esophageal artery, preserving the existing `{source="FMA"}` annotation.

## Checklist

- Read `__issue_context__.json`.
- Checked the existing `UBERON:0001043` and `UBERON:0035539` stanzas with `obo-grep.pl`.
- Checked the target `UBERON:0001515` thoracic aorta term and existing `connecting_branch_of` usage for consistency.
- Edited terms via `obo-checkout.pl` / `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Validated OBO conversion with `robot convert -i src/ontology/uberon-edit.obo -f obo -o /tmp/uberon-edit-check.obo`.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615887850)


#### Agent Issue Comment

Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615887850)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..74f84e11b 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -930,7 +930,7 @@ intersection_of: has_quality PATO:0002236 ! aliform
 relationship: capable_of_part_of GO:0060361 ! flight
 relationship: in_taxon NCBITaxon:33213 ! Bilateria
 relationship: never_in_taxon NCBITaxon:118072 {source="bgee"} ! Coelacanthimorpha
-relationship: never_in_taxon NCBITaxon:186634 {seeAlso="Wikipedia:Flying_fish", source="bgee"} ! Otomorpha
+relationship: never_in_taxon NCBITaxon:186634 {source="bgee", seeAlso="Wikipedia:Flying_fish"} ! Otomorpha
 relationship: never_in_taxon NCBITaxon:314147 {source="bgee"} ! Glires
 relationship: never_in_taxon NCBITaxon:6231 {source="bgee"} ! Nematoda
 relationship: never_in_taxon NCBITaxon:7878 {source="bgee"} ! Dipnomorpha
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -22376,7 +22375,7 @@ relationship: preaxialmost_part_of UBERON:0002398 ! manus
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/6/64/Thumb-up.jpg" xsd:anyURI
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/2/2c/Thumbs_up.jpg" xsd:anyURI
 property_value: taxon_notes "Not present in Anurans (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012260", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012260"}
 
 [Term]
 id: UBERON:0001464
@@ -28060,7 +28059,7 @@ relationship: part_of UBERON:0010272 ! hyoid apparatus
 property_value: axiom_lost_from_external_ontology "relationship loss: part_of hyoid plate (AAO:0000664)[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO"}
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/1/1f/Gray186.png" xsd:anyURI
 property_value: external_definition "Paired processes that extend posterolaterally from the posterior margin of the hyoid plate. These processes are the ossified posteromedial processes and invest the laryngeal apparatus.[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO", source="AAO:LAP"}
-property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {seeAlso="https://github.com/obophenotype/uberon/issues/548", source="WP"}
+property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {source="WP", seeAlso="https://github.com/obophenotype/uberon/issues/548"}
 
 [Term]
 id: UBERON:0001686
@@ -38535,7 +38534,7 @@ xref: Wikipedia:Spinal_accessory_nerve
 xref: XAO:0004214
 intersection_of: UBERON:0001021 ! nerve
 intersection_of: extends_fibers_into UBERON:0020358 ! accessory XI nerve nucleus
-relationship: dubious_for_taxon NCBITaxon:8292 {seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7", source="VHOG", source="Wikipedia"} ! Amphibia
+relationship: dubious_for_taxon NCBITaxon:8292 {source="VHOG", source="Wikipedia", seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7"} ! Amphibia
 relationship: in_taxon NCBITaxon:32523 ! Tetrapoda
 relationship: innervates UBERON:0001737 ! larynx
 relationship: innervates UBERON:3010692 {gci_relation="part_of", gci_filler="NCBITaxon:8292", source="ISBN:080184780X"} ! m. cucullaris
@@ -74531,7 +74530,7 @@ relationship: part_of UBERON:5003622 ! manual digit 2 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/d/d5/Index_finger.JPG" xsd:anyURI
 property_value: has_relational_adjective "indicis" xsd:string
 property_value: taxon_notes "Anurans lack manual digit 1, so manual digit 2 is the digit after the prepollex (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012261", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012261"}
 
 [Term]
 id: UBERON:0003623
@@ -74568,7 +74567,7 @@ relationship: ambiguous_for_taxon NCBITaxon:8782 ! Aves
 relationship: part_of UBERON:0012141 {source="https://github.com/obophenotype/uberon/wiki/Inferring-part-of-relationships"} ! manual digitopodium region
 relationship: part_of UBERON:5003623 ! manual digit 3 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/f/fd/Middle_finger.jpg" xsd:anyURI
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012262", source="PMID:10220427", source="PhenoscapeRCN"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012262"}
 
 [Term]
 id: UBERON:0003624
@@ -138779,7 +138778,7 @@ name: spleen marginal sinus
 def: "The border region surrounding the spleen B cell follicles and the periarteriolar lymphoid sheath that separates it from the marginal zone that mediates lymphocyte entry into the white pulp from the blood." [MP:MP]
 subset: pheno_slim
 synonym: "splenic marginal sinus" EXACT [MP:0002363]
-xref: EMAPA:37964 {source="MA:th", seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117"}
+xref: EMAPA:37964 {seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117", source="MA:th"}
 xref: MA:0000754
 xref: NCIT:C49776
 xref: UMLS:C1710157 {source="ncithesaurus:Splenic_Marginal_Sinus"}
@@ -151540,7 +151539,7 @@ xref: SCTID:361795009
 xref: Wikipedia:Malleolus
 is_a: UBERON:0005913 ! zone of bone organ
 relationship: part_of UBERON:0004410 ! distal epiphysis of fibula
-property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", seeAlso="UBERON:0004410", source="UBERON:skansa"}
+property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", source="UBERON:skansa", seeAlso="UBERON:0004410"}
 
 [Term]
 id: UBERON:0012292
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542
@@ -225213,8 +225212,8 @@ id: UBERON:8910024
 name: airway hillock
 def: "A region of squamous epithelium found in the tracheobronchial tree - continuous with the tracheobronchial epithelium." [DOI:10.1038/s41586-024-07377-1]
 is_a: UBERON:0006914 ! squamous epithelium
-relationship: part_of UBERON:0007196 ! tracheobronchial tree
 relationship: has_part CL:4030023 ! respiratory tract hillock cell
+relationship: part_of UBERON:0007196 ! tracheobronchial tree
 
 [Typedef]
 id: aboral_to

```
