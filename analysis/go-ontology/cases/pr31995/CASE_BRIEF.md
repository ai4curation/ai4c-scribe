# PR #31995 — Missing parent: GO:0072318 clathrin coat disassembly

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31981](https://github.com/geneontology/go-ontology/issues/31981)
- **PR**: [#31995](https://github.com/geneontology/go-ontology/pull/31995)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-04-28
- **task_type**: axiom_repair
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

GO:0072318 `clathrin coat disassembly` was missing a `part_of` relationship to `GO:0072583 clathrin-dependent endocytosis`. While its parent term GO:0072319 `vesicle uncoating` already had a `part_of` to the more general `GO:0016192 vesicle-mediated transport`, the specific connection to clathrin-dependent endocytosis was absent. This gap was identified by ValWood during a review of vesicle-mediated transport term relationships.

## Changes Made

Two lines were added to the GO:0072318 stanza in `go-edit.obo`: a `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` axiom and a `property_value: term_tracker_item` linking back to issue #31981. No existing content was modified or removed. The addition makes explicit that clathrin coat disassembly is a step within clathrin-dependent endocytosis, complementing the existing is_a parent `vesicle uncoating`.

## Resolution

Easy difficulty because this was a straightforward addition of a missing axiom with no ambiguity about the biological relationship. Clathrin coat disassembly (uncoating) is universally recognized as a step in clathrin-dependent endocytosis, occurring after the clathrin-coated vesicle has pinched off from the plasma membrane. The minimal 2-line addition reflects the surgical nature of the fix.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

## Agent Attempts (11)

### Attempt 1: claude-sonnet-4.5 / copilot

- **Eval PR**: [#493](https://github.com/ai4curation/eval-ont-agent-go/pull/493)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25888558384](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25888558384)
- **Workflow run**: [25888558384](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888558384)

#### Agent PR Comment

# Changes to GO:0072318 (clathrin coat disassembly)

## Summary
Added missing relationship and term tracker metadata to GO:0072318 as requested in issue #31981.

## Changes Made

### GO:0072318 (clathrin coat disassembly)
1. **Added relationship**: `part_of GO:0072583 ! clathrin-dependent endocytosis`
2. **Added term tracker**: `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`

## Rationale

The addition of the `part_of` relationship (rather than `is_a`) follows the established design pattern in the ontology for disassembly/uncoating processes:

- GO:0016191 (synaptic vesicle uncoating) has `part_of GO:0048488 ! synaptic vesicle endocytosis`
- GO:0072319 (vesicle uncoating, parent of GO:0072318) has `part_of GO:0016192 ! vesicle-mediated transport`

Clathrin coat disassembly is a subprocess that occurs during clathrin-dependent endocytosis after vesicle formation and before vesicle fusion, making `part_of` the appropriate relationship type. This was correctly identified by @pgaudet in the issue comments.

## Validation Checklist

- [x] PLAN: Issue analyzed and plan created
- [x] PRE-VALIDATION: N/A - validation tools not available in this environment
- [x] RESEARCH: N/A - no research needed for straightforward relationship addition
- [x] TERM-SEARCH: Both GO:0072318 and GO:0072583 confirmed to exist
- [x] DESIGN-PATTERNS: Pattern confirmed by examining similar terms (synaptic vesicle uncoating, vesicle uncoating)
- [x] EDITS: Followed checkout/checkin procedure correctly
- [x] RELATIONSHIPS: 
    - [x] Added `part_of` relationship as appropriate for subprocess
    - [x] Follows established pattern in ontology
    - [x] No over-specification of logical definitions
- [x] SPECIALIZED-EDITS: N/A - simple relationship addition
- [x] METADATA:
    - [x] Term tracker item added with correct format
    - [x] No modification of created_by/creation_date (existing term)
    - [x] Namespace preserved
- [x] AUTOMATED-VALIDATION: Could not run due to missing tools (amm, robot) in environment
- [x] REFERENCE-VALIDATION: N/A - no new references added
- [x] CHANGES-COMMITTED:
    - [x] RELEVANT-FILES: Only src/ontology/go-edit.obo modified
    - [x] ACCURACY: Change follows established ontology patterns
    - [x] ISSUE-ALIGNMENT: Directly addresses issue request
    - [x] PR created
    - [x] Communication prepared for issue and PR

## Notes

The change is minimal and follows well-established patterns in the ontology. The biological correctness is supported by:
1. The definition of GO:0072318 states it "results in stripping or removing the clathrin coat from clathrin-coated vesicles (CCV) before fusing with their targets"
2. This process is part of the clathrin-dependent endocytosis pathway
3. The pattern is consistent with how other uncoating/disassembly terms relate to their parent processes

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888558384)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Added the missing `part_of` relationship to GO:0072583 (clathrin-dependent endocytosis) as suggested by @pgaudet, along with the term tracker item property.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888558384)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#478](https://github.com/ai4curation/eval-ont-agent-go/pull/478)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25847335030](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847335030)
- **Workflow run**: [25847335030](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847335030)

#### Agent PR Comment

## Summary

Added missing parent relationship to GO:0072318 (clathrin coat disassembly) as requested in issue #31981.

## Changes Made

### GO:0072318 (clathrin coat disassembly)

Added two new annotations:
1. **Relationship**: `part_of GO:0072583 ! clathrin-dependent endocytosis`
2. **Property value**: `term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`

## Biological Rationale

The `part_of` relationship from clathrin coat disassembly to clathrin-dependent endocytosis is biologically appropriate. Clathrin-dependent endocytosis is a multi-step process:
1. Material is taken up into clathrin-coated pits
2. These pits pinch off to form clathrin-coated vesicles
3. The clathrin coat must be disassembled (uncoated) from these vesicles
4. The uncoated vesicles can then fuse with their target membranes

Clathrin coat disassembly is therefore a critical subprocess that occurs as part of the overall clathrin-dependent endocytosis pathway.

## Validation

✓ Syntax validation passed (robot convert)
✓ SPARQL queries passed:
  - non-anyURI-value-violation
  - missing-namespace-violation
  - trailing-whitespace-violation
✓ ELK reasoning completed without errors
✓ No unsatisfiable classes introduced

## Checklist

- [x] PLAN: The issue and all its context has been analyzed, the intent is clear, and a plan for addressing it has been created
- [x] PRE-VALIDATION: Current state of the ontology validates prior to any changes
- [x] RESEARCH: N/A - straightforward relationship addition based on biological knowledge
- [x] TERM-SEARCH: Relevant ontology terms consulted via obo-grep.pl
- [x] DESIGN-PATTERNS: N/A - simple relationship addition to existing term
- [x] EDITS: Correct procedure followed using checkout/checkin commands
- [x] RELATIONSHIPS: Appropriate relationships included
  - [x] part_of relationship is appropriate for this biological process
  - [x] Relationships conform to similar terms in the ontology
  - [x] is_a not over-asserted
- [x] SPECIALIZED-EDITS: N/A - no obsoletion, chemical entities, reactions, or taxon constraints involved
- [x] METADATA: The metadata for the changes is correct
  - [x] term_tracker_item property added correctly with proper formatting
  - [x] created_by and creation_date NOT modified (existing term)
- [x] AUTOMATED-VALIDATION: The ontology validates correctly after changes
- [x] REFERENCE-VALIDATION: N/A - no new references introduced
- [x] CHANGES-COMMITTED:
  - [x] RELEVANT-FILES: Only src/ontology/go-edit.obo committed
  - [x] ACCURACY: The changes made are biologically correct and accurate
  - [x] ISSUE-ALIGNMENT: The changes align with the issue request
  - [x] PR created
  - [x] Communicated on original issue
  - [x] Detailed description provided in PR

## Files Modified

- `src/ontology/go-edit.obo`: Added part_of relationship and term_tracker_item to GO:0072318

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847335030)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I've added the missing parent relationship as requested:
- Added `part_of` relationship from GO:0072318 (clathrin coat disassembly) to GO:0072583 (clathrin-dependent endocytosis)
- Added term tracker link to this issue

The part_of relationship is biologically appropriate, as clathrin coat disassembly occurs as part of the clathrin-dependent endocytosis process - after clathrin-coated vesicles form, they must be uncoated before fusing with target membranes.

All validation checks passed.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847335030)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#428](https://github.com/ai4curation/eval-ont-agent-go/pull/428)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25775199560](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775199560)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#345](https://github.com/ai4curation/eval-ont-agent-go/pull/345)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25650706473](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650706473)
- **Workflow run**: [25650706473](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650706473)

#### Agent PR Comment

## Summary

Addresses geneontology/go-ontology#31981 — adds a missing parent to `GO:0072318 clathrin coat disassembly`.

### Change

In `src/ontology/go-edit.obo`, added to `GO:0072318`:

```
relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
```

### Rationale

The issue reporter (@ValWood) requested `GO:0072583 clathrin-dependent endocytosis` as a superclass of `GO:0072318 clathrin coat disassembly`. @pgaudet observed that this should be `part_of` rather than `is_a`, which @ValWood acknowledged with a thumbs-up. `part_of` is the correct relation here: clathrin coat disassembly is a sub-process that contributes to the larger clathrin-dependent endocytosis process (occurring after the coated vesicle pinches off), not a subtype of endocytosis itself.

This is consistent with the existing `vesicle uncoating` parent (`GO:0072319`), which itself carries `part_of GO:0016192 ! vesicle-mediated transport`. The new `part_of` on `GO:0072318` is a more specific sibling pattern: a specific kind of uncoating that is part of a specific kind of vesicle-mediated transport.

The existing logical definition was left untouched — it correctly captures the genus/differentia (`cellular component disassembly` that `results_in_disassembly_of` a `clathrin coat`). Adding `clathrin-dependent endocytosis` to the equivalence axiom would have been incorrect (other clathrin-coated vesicle pathways, e.g. trans-Golgi trafficking, would be excluded).

### Checklist

- [x] PLAN: Issue analyzed, intent clear (add missing parent; community thread converged on `part_of`)
- [x] PRE-VALIDATION: N/A — environment lacks `robot`; change is a single relationship to an existing term, no new IDs introduced
- [x] RESEARCH: N/A — relationship is straightforward and supported by existing definition and term thread consensus
- [x] TERM-SEARCH: Confirmed both `GO:0072318` and `GO:0072583` exist and are correctly identified
- [x] DESIGN-PATTERNS: N/A — no compositional pattern changes; the existing logical definition is preserved as-is
- [x] EDITS: Followed checkout/checkin procedure via `obo-checkout.pl` / `obo-checkin.pl`
- [x] RELATIONSHIPS: `part_of` chosen over `is_a` per pgaudet/ValWood consensus; logical definition unchanged (not over-asserted)
- [x] SPECIALIZED-EDITS: N/A — not an obsoletion, chemical-entity, reaction, or taxon-constraint change
- [x] METADATA: `term_tracker_item` added; `created_by`/`creation_date` left untouched (existing term, not new)
- [ ] AUTOMATED-VALIDATION: Skipped — `robot` is not available in this execution environment. Change is syntactically trivial (single line additions following existing patterns in the file).
- [x] REFERENCE-VALIDATION: No new references introduced
- [x] CHANGES-COMMITTED: `src/ontology/go-edit.obo` committed

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650706473)

#### Agent Issue Comment

Added `part_of GO:0072583 ! clathrin-dependent endocytosis` to GO:0072318 (clathrin coat disassembly), per @pgaudet's suggestion (acknowledged by @ValWood) that this should be a `part_of` rather than `is_a`. The `term_tracker_item` was also added pointing back to this issue.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650706473)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

### Attempt 5: kimi-k2.6 / opencode

- **Eval PR**: [#281](https://github.com/ai4curation/eval-ont-agent-go/pull/281)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25646710185](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646710185)
- **Workflow run**: [25646710185](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646710185)

#### Agent PR Comment

## Summary

Added the missing `part_of` relationship between **GO:0072318 clathrin coat disassembly** and **GO:0072583 clathrin-dependent endocytosis**, plus a `term_tracker_item` linking back to issue #31981.

### Why `part_of` and not `is_a`

The original issue title suggested adding a missing "parent", which typically implies an `is_a` link. However, @pgaudet correctly noted that this should be `part_of`. Clathrin coat disassembly is a discrete step *within* clathrin-dependent endocytosis (it strips the clathrin coat from clathrin-coated vesicles before they fuse with their targets), not a subtype of endocytosis itself. This is also consistent with the existing axiom on the parent term **GO:0072319 vesicle uncoating**, which is `part_of` **GO:0016192 vesicle-mediated transport**.

### Changes made

- **File edited:** `src/ontology/go-edit.obo`
- **Term affected:** `GO:0072318 clathrin coat disassembly`
- **Added:**
  - `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis`
  - `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`

### Checklist

- [x] Issue intent analyzed and clear
- [x] Relevant terms looked up in current ontology
- [x] Relationship type (`part_of`) chosen based on biological context and existing patterns
- [x] Term edited using checkout/checkin procedure (`obo-checkout.pl` / `obo-checkin.pl`)
- [x] SPARQL-QC checks passed
- [x] ELK reasoning passed with no unsatisfiable classes
- [x] Only edited file committed (`src/ontology/go-edit.obo`)

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646710185)


#### Agent Issue Comment

Hi @ValWood, @pgaudet — changes committed in PR #<NN>.

Per @pgaudet's suggestion, the missing link was added as `part_of` rather than `is_a`:
- **GO:0072318** *clathrin coat disassembly* `part_of` **GO:0072583** *clathrin-dependent endocytosis*

This reflects that clathrin coat disassembly is a step within the broader endocytic process, not a subtype of it. A term tracker item linking back to this issue has also been added.

Let me know if anything else is needed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646710185)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

### Attempt 6: gemma-4-31b / opencode

- **Eval PR**: [#248](https://github.com/ai4curation/eval-ont-agent-go/pull/248)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25646661647](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646661647)
- **Workflow run**: [25646661647](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646661647)

#### Agent PR Comment

## Summary
Added a `part_of` relationship from `GO:0072318` (clathrin coat disassembly) to `GO:0072583` (clathrin-dependent endocytosis) and added the term tracker item.

#### Agent Issue Comment

Changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646661647)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..c0cbbc2d4 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401423,6 +401423,8 @@ synonym: "clathrin-coat disassembly" EXACT [GOC:rb]
 synonym: "clathrin-coat uncoating" EXACT [GOC:rb]
 synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
 created_by: mah

```

### Attempt 7: claude-haiku-4.5 / claude

- **Eval PR**: [#215](https://github.com/ai4curation/eval-ont-agent-go/pull/215)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640389643](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640389643)

#### Agent PR Comment

## Summary

Added relationship and metadata to GO:0072318 (clathrin coat disassembly) to reflect its biological role within the broader clathrin-dependent endocytosis process.

## Changes Made

### Issue Analysis
- Issue #31981 requested adding a missing parent relationship to GO:0072318 (clathrin coat disassembly)
- Suggested parent: GO:0072583 (clathrin-dependent endocytosis)
- Comment from pgaudet clarified this should be a `part_of` relationship, not `is_a`

### Edits to GO:0072318

1. **Added relationship**: `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis`
   - Reflects the biological fact that clathrin coat disassembly is a specific step that occurs during the broader clathrin-dependent endocytosis process
   - This follows the established design pattern in GO: similar terms like GO:0016191 (synaptic vesicle uncoating) have `part_of GO:0048488` (synaptic vesicle endocytosis)
   
2. **Added metadata**: `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`
   - Provides traceability linking this term to the issue that requested the change

### Design Pattern Rationale

The `part_of` relationship is appropriate here because:
- Clathrin coat disassembly occurs as a necessary step during clathrin-dependent endocytosis
- The relationship reflects whole-part composition: coat disassembly is part of the endocytosis process
- This matches the established pattern for similar process decompositions in GO (e.g., synaptic vesicle uncoating in endocytosis)

## Checklist

- [x] PLAN: Issue analyzed, approach confirmed (part_of relationship based on pgaudet's comment)
- [x] PRE-VALIDATION: Ontology structure verified before changes
- [x] TERM-SEARCH: Found relevant terms (GO:0072318 and GO:0072583)
- [x] RELATIONSHIPS: part_of relationship follows established design patterns
- [x] METADATA: term_tracker_item added correctly
- [x] EDITS: Changes made using standard checkout/checkin procedure
- [x] CHANGES VERIFIED: Confirmed changes present in src/ontology/go-edit.obo
- [x] COMMITTED: Changes committed with detailed message

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640389643)


#### Agent Issue Comment

Changes committed in PR <NN>.

Added the requested part_of relationship from GO:0072318 (clathrin coat disassembly) to GO:0072583 (clathrin-dependent endocytosis), along with the term tracker ID linking to this issue.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640389643)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..ae07bb5e7 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,8 +401425,10 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 
 [Term]
 id: GO:0072319

```

#### Review by gpt-5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/215
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 215 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed geneontology/go-ontology#31981 by adding the missing process relationship for `GO:0072318` clathrin coat disassembly. The metadiff score is F1 1.0 with precision and recall both 1.0, and that accurately reflects the substantive result: the agent made the same ontology edit as the accepted human PR, with only harmless stanza-order placement of the tracker line differing in the raw diff context.


## Strengths

- Added `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318`, matching the issue's requested parent target and the human PR's biological interpretation.
- Used the correct relationship type. The issue called this a missing parent, but the human PR and agent both modeled clathrin coat disassembly as `part_of` clathrin-dependent endocytosis rather than `is_a`, which is appropriate because uncoating is a step in the endocytic process.
- Added the correct `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`, preserving traceability to the source issue.
- Kept the edit tightly scoped to the `GO:0072318` stanza and preserved the existing `is_a: GO:0072319 ! vesicle uncoating` and logical definition using `results_in_disassembly_of GO:0030118 ! clathrin coat`.


## Issues

No substantive issues. The agent's `term_tracker_item` line appears after `creation_date` rather than immediately after the new `relationship` line as in the human PR diff, but this does not change the OBO semantics and was treated as an exact metadiff match after normalization.

### Attempt 8: gpt-5.4 / codex

- **Eval PR**: [#197](https://github.com/ai4curation/eval-ont-agent-go/pull/197)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640339806](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640339806)

#### Agent PR Comment

This change updates `GO:0072318 ! clathrin coat disassembly` to add the missing link to `GO:0072583 ! clathrin-dependent endocytosis`, modeled as:

- `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis`

I did not add `GO:0072583` as an additional `is_a` parent. Existing GO precedent supports `part_of` here:

- `GO:0048212 ! Golgi vesicle uncoating` is `part_of` its transport process
- `GO:0090112 ! COPII vesicle uncoating` is `part_of` its transport process
- `GO:0016191 ! synaptic vesicle uncoating` is `part_of GO:0048488 ! synaptic vesicle endocytosis`
- `GO:0099049 ! clathrin coat assembly involved in endocytosis` is `part_of GO:0072583 ! clathrin-dependent endocytosis`

I also added:

- `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`

Validation and workflow notes:

- Used `obo-grep.pl` to inspect the affected term and comparable clathrin/uncoating terms.
- Checked the existing `cc_disassembly` design pattern and term precedent; no new logical axioms were needed.
- Used `obo-checkout.pl` / `obo-checkin.pl` rather than editing `go-edit.obo` directly.
- Ran `cd src/ontology && make travis_build` after the edit; it completed successfully.
- No new references were introduced, so additional literature research was not required.

Checklist:

- [x] PLAN: issue context reviewed and intent determined
- [x] PRE-VALIDATION: baseline validation was initiated before edits; post-edit full validation passed cleanly
- [x] RESEARCH: N/A, no new biology or references introduced
- [x] TERM-SEARCH: relevant GO terms and precedent inspected
- [x] DESIGN-PATTERNS: checked existing disassembly pattern and sibling terms
- [x] EDITS: used checkout/checkin workflow
- [x] RELATIONSHIPS: added `part_of` relation consistent with analogous transport/endocytosis terms
- [x] METADATA: added missing `term_tracker_item`; did not alter legacy creation metadata
- [x] AUTOMATED-VALIDATION: `make travis_build` passed
- [x] REFERENCE-VALIDATION: N/A, no references added
- [x] CHANGES-COMMITTED: committed local change to `src/ontology/go-edit.obo` only

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640339806)

#### Agent Issue Comment

Addressed locally and committed for PR #<NN>.

I added the missing link for `GO:0072318 ! clathrin coat disassembly`, but modeled it as `part_of GO:0072583 ! clathrin-dependent endocytosis` rather than a new superclass. That follows the ontology precedent for uncoating/transport subprocesses and matches the review comment in the issue thread.

I also added the missing `term_tracker_item` for this issue.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640339806)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

#### Review by gpt-5-codex

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/197
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 197 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed geneontology/go-ontology#31981 by adding the requested parentage for `GO:0072318` "clathrin coat disassembly". The metadiff score is F1 1.0 with precision and recall both 1.0, and in this simple axiom-repair case that exactly reflects the substantive quality: the agent diff matches the human PR line for line.


## Strengths

- Added `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318`, matching the requested superclass from the issue and the accepted human PR.
- Preserved the existing logical definition for `GO:0072318`, including `intersection_of: GO:0022411` and `intersection_of: results_in_disassembly_of GO:0030118`, while adding the missing process relationship.
- Added the correct `term_tracker_item` pointing to `https://github.com/geneontology/go-ontology/issues/31981`, matching the human solution and providing traceability for the edit.
- Kept the edit narrowly scoped to the affected term; there were no unrelated ontology changes.


## Issues

No issues found. The agent's change is identical to the human PR and fully satisfies the issue request.

### Attempt 9: gpt-5.5 / opencode

- **Eval PR**: [#97](https://github.com/ai4curation/eval-ont-agent-go/pull/97)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615948280](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615948280)
- **Workflow run**: [25615948280](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615948280)

#### Agent PR Comment

## Summary

Addressed geneontology/go-ontology issue #31981 by updating `GO:0072318 clathrin coat disassembly`.

Changes made:

- Added `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis`.
- Added the term tracker link: `https://github.com/geneontology/go-ontology/issues/31981`.

#### Agent Issue Comment

Implemented the requested update for `GO:0072318 clathrin coat disassembly`: added `part_of GO:0072583 clathrin-dependent endocytosis` and the issue tracker link.

Validated with `cd src/ontology && make travis_build`.

Changes committed locally for PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615948280)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/97
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 97 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed issue #31981 by making the same edit as the merged human PR: adding `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318 clathrin coat disassembly`, plus the issue tracker property. The metadiff score of 1.0 accurately reflects the substantive result here: the agent diff is an exact match to the human diff and stays tightly scoped to the requested axiom repair.


## Strengths

- Correctly identified the requested target term, `GO:0072318 clathrin coat disassembly`, and added the requested parentage to `GO:0072583 clathrin-dependent endocytosis`.
- Used the appropriate `part_of` relationship rather than forcing an `is_a` superclass. This matches the human PR and is ontologically sensible because clathrin coat disassembly is a subprocess within clathrin-dependent endocytosis, not a subtype of it.
- Preserved the existing logical definition structure for `GO:0072318`, including `is_a: GO:0072319 ! vesicle uncoating` and `intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat`.
- Added the expected `term_tracker_item` property pointing to `https://github.com/geneontology/go-ontology/issues/31981`.
- Kept the change minimal: one ontology stanza, two added lines, no unrelated edits.


## Issues

No substantive issues. The agent's diff matches the human PR exactly and satisfies the source issue without under-editing or scope creep.

### Attempt 10: gpt-5.5 / opencode

- **Eval PR**: [#80](https://github.com/ai4curation/eval-ont-agent-go/pull/80)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615904046](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615904046)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/80
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 80 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue #31981 by adding the missing parentage axiom for `GO:0072318` (`clathrin coat disassembly`) and adding the term tracker provenance. The metadiff score (`f1=1.0`, precision and recall both `1.0`) accurately reflects the substantive result: the agent PR diff is identical to the human PR diff.


## Strengths

- Added `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318`, matching the requested new parent from the source issue.
- Used the appropriate `part_of` relationship rather than an `is_a` parent, which is ontologically consistent with clathrin coat disassembly being a step within clathrin-dependent endocytosis rather than a subtype of endocytosis.
- Preserved the existing logical definition for `GO:0072318`, including `intersection_of: GO:0022411 ! cellular component disassembly` and `intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat`, so the edit was narrowly scoped to the missing process context.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`, matching the human PR's provenance update.
- Made no unrelated ontology edits; the agent's two-line change in `src/ontology/go-edit.obo` exactly matches the human solution.


## Issues

- No significant issues. The only caveat is procedural: the public agent PR does not expose much reasoning beyond the diff and PR metadata, but the final ontology edit is correct and complete for this simple missing-parent task.

### Attempt 11: gpt-5.5 / codex

- **Eval PR**: [#57](https://github.com/ai4curation/eval-ont-agent-go/pull/57)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25615856700](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25615856700)
- **Workflow run**: [25615856700](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615856700)

#### Agent PR Comment

## Summary

Updated `GO:0072318 clathrin coat disassembly` to add the missing process relationship requested in issue #31981:

```obo
relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
```

The issue discussion asked whether the requested superclass should instead be modeled as `part_of`. I used `part_of` because clathrin coat disassembly is a subprocess of clathrin-dependent endocytosis, not a type of endocytosis. This is consistent with existing local precedent for `GO:0099049 clathrin coat assembly involved in endocytosis`, which is also `part_of GO:0072583`.

## Validation

- Pre-change validation: `cd src/ontology && make travis_build` passed.
- Post-change validation: `cd src/ontology && make travis_build` passed.
- `git diff --check -- src/ontology/go-edit.obo` passed.

The Rhea filtering warnings emitted during validation were present in the baseline run and were not introduced by this change.

## Checklist

- [x] PLAN: Issue context and comments analyzed; intent was clear.
- [x] PRE-VALIDATION: Current ontology validated before edits.
- [x] RESEARCH: N/A; no new biological claims or references were introduced.
- [x] TERM-SEARCH: Checked `GO:0072318`, `GO:0072583`, `GO:0072319`, and related clathrin/endocytosis precedent in `go-edit.obo`.
- [x] DESIGN-PATTERNS: Consulted `cc_disassembly` pattern and existing terms; no logical definition changes were needed.
- [x] EDITS: Used `obo-checkout.pl`, edited `terms/GO_0072318.obo`, and checked the stanza back in with `obo-checkin.pl`.
- [x] RELATIONSHIPS: Added `part_of GO:0072583`; did not add an `is_a` superclass because that would incorrectly classify a subprocess as an endocytosis process.
- [x] SPECIALIZED-EDITS: N/A; no obsoletion, CHEBI, catalytic activity, mapping, or taxon constraint changes.
- [x] METADATA: Added the required `term_tracker_item` for issue #31981; did not alter legacy creation metadata.
- [x] AUTOMATED-VALIDATION: Full `make travis_build` passed after edits.
- [x] REFERENCE-VALIDATION: N/A; no new references were introduced.
- [x] CHANGES-COMMITTED: Committed only `src/ontology/go-edit.obo`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615856700)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I added `part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318 clathrin coat disassembly` and added the term tracker link for this issue.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25615856700)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

#### Review by gpt-5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31981
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31995
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/57
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31981 --repo geneontology/go-ontology
    gh pr diff 31995 --repo geneontology/go-ontology
    gh pr diff 57 --repo ai4curation/eval-ont-agent-go
-->

## Summary
The agent fully addressed issue #31981 by adding `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` to `GO:0072318 clathrin coat disassembly`, along with the `term_tracker_item` for the issue. This exactly matches the human PR diff, so the metadiff score of F1 1.0 / precision 1.0 / recall 1.0 accurately reflects the substantive quality of the result. The modeling choice is also appropriate: clathrin coat disassembly is a step within clathrin-dependent endocytosis, not an `is_a` subtype of endocytosis.



## Strengths
- Correctly edited the requested term, `GO:0072318 clathrin coat disassembly`.
- Used the same relationship as the human solution: `part_of GO:0072583 ! clathrin-dependent endocytosis`.
- Added the required tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`.
- Preserved the existing `is_a: GO:0072319 ! vesicle uncoating` parent and logical definition axioms involving `GO:0022411 cellular component disassembly` and `GO:0030118 clathrin coat`.
- Kept the change tightly scoped to the issue with no unrelated ontology edits.



## Issues
- No substantive issues found. The agent diff is identical to the merged human PR diff for this task.
