# PR #3440 — [Class hierarchy] Change CXCR3 property in CD8+ CXCR3+ alpha-beta regulatory T cell

- **Ontology**: cell-ontology
- **Repo**: obophenotype/cell-ontology
- **Issue**: [#3382](https://github.com/obophenotype/cell-ontology/issues/3382)
- **PR**: [#3440](https://github.com/obophenotype/cell-ontology/pull/3440)
- **Author**: @copilot-swe-agent
- **Merged**: 2025-11-13
- **task_type**: axiom_repair
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

CXCR3 is a chemokine receptor that resides on the plasma membrane. In the definition of CD8-positive CXCR3-positive alpha-beta regulatory T cell (CL:0001041), the relationship to CXCR3 was expressed using the generic `has_part` relation instead of the more specific `has_plasma_membrane_part`. This imprecision affects automated reasoning about cell surface markers.

## Changes Made

Changed a single OWL axiom in `cl-edit.owl`: replaced `has_part some CXCR3` with `has_plasma_membrane_part some CXCR3` for CL:0001041. One line added, one line removed.

## Resolution

Approved on first review. Simple difficulty because it is a single relation substitution, but it illustrates an important pattern: when annotating cell surface markers, the specific `has_plasma_membrane_part` relation should be used rather than the generic `has_part`, as this enables more precise reasoning about cell phenotypes.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..515bbaa71 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

## Agent Attempts (6)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#96](https://github.com/ai4curation/eval-ont-agent-cl/pull/96)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640373966](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640373966)

#### Agent PR Comment

# PR Description: Fix CXCR3 Property in CL_0001041

## Summary

This PR addresses issue #3382 by updating the logical definition of CL_0001041 (CD8-positive, CXCR3-positive, alpha-beta regulatory T cell) to more accurately represent the subcellular localization of the CXCR3 protein.

## Changes Made

**File modified:** `src/ontology/cl-edit.owl`

**Specific change (line 13384):**
- Changed from: `ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207)`
- Changed to: `ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207)`

Where:
- `BFO_0000051` = "has_part"
- `RO_0002104` = "has_plasma_membrane_part"
- `PR_000001207` = C-X-C chemokine receptor type 3 (CXCR3)

## Rationale

1. **Biological accuracy:** CXCR3 is a G-protein coupled receptor located on the plasma membrane. Using `has_plasma_membrane_part` more accurately reflects its cellular localization.

2. **Consistency:** Related terms like CL_0001051 (CD4-positive, CXCR3-negative, CCR6-negative, alpha-beta T cell) and CL_0001052 (CD8-positive, CXCR3-negative, CCR6-negative, alpha-beta T cell) use the specific plasma membrane relationship (`lacks_plasma_membrane_part` / CL_4030046) for CXCR3, suggesting that specialized membrane relationships are the standard approach in this ontology.

3. **Best practice:** Using specific subcellular localization relationships (has/lacks_plasma_membrane_part) is more precise than generic part_of relationships when the specific location of a protein is known.

## Validation

The change has been tested by:
- Verifying the syntax is correct
- Confirming that the ontology uses the expected relationship type (RO_0002104) for plasma membrane parts
- Comparing with similar terms to ensure consistency

## Checklist

- [x] Issue #3382 requirements met
- [x] Change reviewed for biological accuracy
- [x] Syntax validated
- [x] Consistency with related terms verified
- [x] Commit signed appropriately

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640373966)


#### Agent Issue Comment

## Issue Resolution

The requested change to CL_0001041 (CD8-positive, CXCR3-positive, alpha-beta regulatory T cell) has been completed and committed.

**Change made:** Updated the CXCR3 property from `has_part` (BFO_0000051) to `has_plasma_membrane_part` (RO_0002104) in the EquivalentClasses axiom.

**Rationale:** This change more accurately reflects the localization of the C-X-C chemokine receptor type 3 (CXCR3) as a plasma membrane protein, and aligns the logical definition with best practices for modeling membrane-bound proteins in the ontology.

Changes are now ready for review in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640373966)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..515bbaa71 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#61](https://github.com/ai4curation/eval-ont-agent-cl/pull/61)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615957886](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615957886)
- **Workflow run**: [25615957886](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615957886)

#### Agent PR Comment

## Summary

Addresses issue #3382 by updating the logical definition of `CL_0001041` (`CD8-positive, CXCR3-positive, alpha-beta regulatory T cell`). The CXCR3 (`PR_000001207`) restriction now uses `has plasma membrane part` (`RO_0002104`) instead of the broader `has part` (`BFO_0000051`).

## Rationale

CXCR3 is a cell-surface chemokine receptor, so modeling it as a plasma membrane part is more specific and consistent with related CXCR3-positive and CXCR3-negative classes in CL, including the negative CXCR3 terms cited in the issue.

## Checklist

- [x] Reviewed issue context from `__issue_context__.json`.
- [x] Checked existing axioms for `CL_0001041` and CXCR3 (`PR_000001207`) in `src/ontology/cl-edit.owl`.
- [x] Updated only `src/ontology/cl-edit.owl`.
- [x] Confirmed the updated `CL_0001041` axiom uses `RO_0002104`.
- [x] Validated OWL functional syntax with `robot convert --input src/ontology/cl-edit.owl --output /tmp/cl-edit.ofn`.

Signed-off-by: GitHub Copilot

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615957886)


#### Agent Issue Comment

Implemented the requested hierarchy update for CL_0001041 by changing the CXCR3 restriction from `has part` to `has plasma membrane part` (`RO_0002104`). Changes committed locally for PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615957886)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..515bbaa71 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

### Attempt 3: claude-opus-4.7 / claude

- **Eval PR**: [#278](https://github.com/ai4curation/eval-ont-agent-cl/pull/278)
- **F1**: 0.800  **Precision**: 1.000  **Recall**: 0.667  **Jaccard**: 0.667

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..339c01373 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,8 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0001041 <https://github.com/obophenotype/cell-ontology/issues/3382>)
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

### Attempt 4: claude-sonnet-4.5 / claude

- **Eval PR**: [#228](https://github.com/ai4curation/eval-ont-agent-cl/pull/228)
- **F1**: 0.800  **Precision**: 1.000  **Recall**: 0.667  **Jaccard**: 0.667
- **Trace**: [25877911786](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877911786)
- **Workflow run**: [25877911786](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877911786)

#### Agent PR Comment

## Summary

This PR addresses issue #3382 by updating the logical definition of CL_0001041 (CD8-positive, CXCR3-positive, alpha-beta regulatory T cell) to use a more specific relationship property for CXCR3.

## Changes Made

- **Changed relationship property**: Updated the relationship for PR_000001207 (C-X-C chemokine receptor type 3/CXCR3) from `has part` (BFO_0000051) to `has plasma membrane part` (RO_0002104)
- **Added issue tracking**: Added IAO_0000233 annotation linking to issue #3382

## Rationale

CXCR3 is a G protein-coupled cell surface receptor that is localized to the plasma membrane. Using `has plasma membrane part` (RO_0002104) instead of the generic `has part` (BFO_0000051) more accurately reflects this subcellular localization.

This change brings CL_0001041 into consistency with other CXCR3-related terms in the ontology that use `lacks_plasma_membrane_part` for CXCR3-negative cells (e.g., CL_0001051, CL_0001052).

## Validation

- Verified that PR_000001207 is the correct identifier for CXCR3 (C-X-C chemokine receptor type 3)
- Confirmed that RO_0002104 (has plasma membrane part) is used elsewhere in the ontology for plasma membrane proteins
- Checked that the syntax and formatting match existing patterns in cl-edit.owl
- Confirmed that similar CXCR3-negative terms use the corresponding `lacks_plasma_membrane_part` relationship

## Files Modified

- `src/ontology/cl-edit.owl`: Updated logical definition for CL_0001041 (line 13384) and added issue tracker annotation (line 13384)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877911786)


#### Agent Issue Comment

Thank you for reporting this issue. I've made the requested change to CL_0001041 (CD8-positive, CXCR3-positive, alpha-beta regulatory T cell).

The relationship for C-X-C chemokine receptor type 3 (CXCR3/PR_000001207) has been updated from `has part` (BFO_0000051) to `has plasma membrane part` (RO_0002104), which more accurately reflects the localization of this cell surface receptor.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877911786)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..339c01373 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,8 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+AnnotationAssertion(obo:IAO_0000233 obo:CL_0001041 <https://github.com/obophenotype/cell-ontology/issues/3382>)
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)

```

### Attempt 5: gpt-5.4 / codex

- **Eval PR**: [#76](https://github.com/ai4curation/eval-ont-agent-cl/pull/76)
- **F1**: 0.667  **Precision**: 1.000  **Recall**: 0.500  **Jaccard**: 0.500
- **Workflow run**: [25640322475](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640322475)

#### Agent PR Comment

This change updates the logical definition of `CL_0001041` (CD8-positive, CXCR3-positive, alpha-beta regulatory T cell) so the CXCR3 restriction uses `RO_0002104` (`has plasma membrane part`) instead of `BFO_0000051` (`has part`).

Rationale:
- The issue requests that CXCR3 be modeled as a plasma membrane marker rather than a generic part.
- The neighboring comparator classes cited in the issue, `CL_0001051` and `CL_0001052`, already use the corresponding negative plasma membrane pattern via `CL_4030046`.
- Other CXCR3-positive T-cell classes in `cl-edit.owl`, including `CL_0000545` and `CL_0000917`, already model CXCR3 with `has plasma membrane part`, so this edit makes `CL_0001041` consistent with existing CL practice.

Checks completed:
- Read the imported issue context from `__issue_context__.json`.
- Inspected the target class and related comparator classes in `src/ontology/cl-edit.owl`.
- Confirmed the intended pattern in `docs/patterns/cellHasPlasmaMembranePartX.md`.
- Ran `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit.ofn` to verify the edited ontology parses cleanly.

Files changed:
- `src/ontology/cl-edit.owl`

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640322475)


#### Agent Issue Comment

Addressed locally and committed for PR #<NN>.

Updated `CL_0001041` so the CXCR3 marker is modeled with `has plasma membrane part` (`RO_0002104`) instead of `has part`, bringing it into line with the existing CXCR3 positive/negative marker pattern used for related T-cell classes.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640322475)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..0ddaa1dfd 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)
@@ -35308,4 +35308,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```

### Attempt 6: gpt-5.5 / codex

- **Eval PR**: [#21](https://github.com/ai4curation/eval-ont-agent-cl/pull/21)
- **F1**: 0.667  **Precision**: 1.000  **Recall**: 0.500  **Jaccard**: 0.500
- **Trace**: [25615861589](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615861589)
- **Workflow run**: [25615861589](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861589)

#### Agent PR Comment

Updated CL_0001041 (`CD8-positive, CXCR3-positive, alpha-beta regulatory T cell`) so that its CXCR3 (`PR_000001207`) restriction uses `RO_0002104` (`has plasma membrane part`) instead of `BFO_0000051` (`has part`).

Rationale:
- The issue requested this specific relation change for CXCR3 localization.
- Existing CXCR3-positive T cell logical definitions use `RO_0002104` for `PR_000001207`.
- The cited CXCR3-negative comparison terms, CL_0001051 and CL_0001052, use `CL_4030046` (`lacks_plasma_membrane_part`) for `PR_000001207`, so this keeps the positive term aligned with that pattern.

Checklist completed:
- Read the imported issue context from `__issue_context__.json`.
- Checked the CL_0001041 logical definition.
- Checked the proposed parent and nearby CXCR3 positive/negative patterns in `src/ontology/cl-edit.owl`.
- Made the scoped ontology edit only in `src/ontology/cl-edit.owl`.
- Validated functional syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit-issue-3382.owl`.

Signed-off-by: GitHub Copilot

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861589)


#### Agent Issue Comment

Implemented the requested CL_0001041 hierarchy update; changes committed in PR #<NN>.

I changed the CXCR3 restriction from `has part` to `has plasma membrane part`, matching the existing CXCR3 positive/negative T cell patterns. The broader note about other PR terms may need separate review if a wider modeling cleanup is desired.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615861589)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c97c97462..0ddaa1dfd 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -13381,7 +13381,7 @@ AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T-lymphocyte")
 AnnotationAssertion(rdfs:comment obo:CL_0001041 "These cells may be the human equivalent of murine CD8-positive, CD122-positive alpha-beta regulatory T cell. They are also found in the CD45RA-negative and CD62L-positive fraction.")
 AnnotationAssertion(rdfs:label obo:CL_0001041 "CD8-positive, CXCR3-positive, alpha-beta regulatory T cell")
-EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
+EquivalentClasses(obo:CL_0001041 ObjectIntersectionOf(obo:CL_0000795 ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001207) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032613) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0032689) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0042130)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0001041 obo:CL_0000795)
 
 # Class: obo:CL_0001042 (T-helper 22 cell)
@@ -35308,4 +35308,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```
