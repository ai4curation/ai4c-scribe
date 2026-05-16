---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3509
pr_number: 3515
issue_title: Definition of common hepatic artery is truncated
pr_author: ar-ibrahim
pr_merged_at: '2025-05-08'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: vascular-anatomy
best_f1: 0.5
best_model: claude-haiku-4.5
---

# PR #3515 — Definition of common hepatic artery is truncated

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3509](https://github.com/obophenotype/uberon/issues/3509) | [PR #3515](https://github.com/obophenotype/uberon/pull/3515) | @ar-ibrahim | merged 2025-05-08

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3509 reported that the text definition of the common hepatic artery was truncated, likely due to a data entry or import error. The definition was incomplete and needed to be restored to its full text.

## Changes Made

The PR made a single line change in src/ontology/uberon-edit.obo, replacing the truncated definition with the complete text for the common hepatic artery term. Despite the minimal change, three commits were needed, possibly due to formatting corrections during review.

## Resolution

Simple difficulty. This is a straightforward text correction requiring an agent to identify the truncated definition and supply the complete text. The main challenge is sourcing the correct full definition text, which could be obtained from anatomical references or the term's cross-references to other ontologies.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc9..887747153c 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine), pancreas, and gall bladder. It arises from the celiac artery and has the following branches: the hepatic artery proper, the gastroduodenal artery and the right gastric artery." [https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/common-hepatic-artery/22763, Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

## Agent Attempts (8)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#327](https://github.com/ai4curation/eval-ont-agent-uberon/pull/327)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25888670936](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25888670936)
- **Workflow run**: [25888670936](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888670936)

#### Agent PR Comment

# PR: Shorten definition of common hepatic artery (Issue #3509)

#### Agent Issue Comment

# Issue #3509: Definition of common hepatic artery is truncated

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..6ae02a3ad 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "A short blood vessel that arises from the celiac artery and supplies the liver, pylorus, duodenum, and pancreas." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#288](https://github.com/ai4curation/eval-ont-agent-uberon/pull/288)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25877953664](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25877953664)
- **Workflow run**: [25877953664](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877953664)

#### Agent PR Comment

## Summary

Fixed the truncated definition for **UBERON:0005436** (common hepatic artery) by removing the incomplete trailing sentence.

## Changes

**Before:**
```
def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:."
```

**After:**
```
def: "A short blood vessel that supplies oxygenated blood to the liver, pylorus, duodenum and pancreas. It arises from the celiac artery."
```

## Rationale

1. **Removed incomplete sentence**: The original definition ended with "and has the following branches:." which trails off without completing the thought
2. **Simplified structure**: Removed redundant "In anatomy," preamble and simplified parenthetical anatomical descriptions
3. **Maintained accuracy**: The core information about the artery's function, target organs, and origin is preserved
4. **Improved readability**: The new definition is more concise while remaining complete and informative

## Validation

✅ Term checked out using `obo-checkout.pl`  
✅ Definition edited in `terms/UBERON_0005436.obo`  
✅ Changes checked back in using `obo-checkin.pl`  
✅ Verified updated definition in main ontology file  
✅ Committed with clear message and proper attribution

Fixes #3509

@dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877953664)


#### Agent Issue Comment

The truncated definition has been fixed. Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877953664)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..139e07f5a 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "A short blood vessel that supplies oxygenated blood to the liver, pylorus, duodenum and pancreas. It arises from the celiac artery." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#269](https://github.com/ai4curation/eval-ont-agent-uberon/pull/269)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25844158890](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25844158890)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..6ae02a3ad 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "A short blood vessel that arises from the celiac artery and supplies the liver, pylorus, duodenum, and pancreas." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#242](https://github.com/ai4curation/eval-ont-agent-uberon/pull/242)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25834933215](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25834933215)
- **Workflow run**: [25834933215](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834933215)

#### Agent PR Comment

## Summary

Fixes issue #3509: the definition of `common hepatic artery` (UBERON:0005436) was truncated, ending with "and has the following branches:." without ever enumerating the branches.

## Change

**Before:**
> In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:.

**After:**
> In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery.

The trailing "and has the following branches:." was dropped (per the issue request: "Just shorten this further so it's not trailing"). The definition xref `Wikipedia:Common_hepatic_artery` was preserved and no other axioms or metadata were changed.

## Rationale

- The shortened form retains all substantive anatomical content (function, regions supplied, origin).
- Rather than try to enumerate branches (proper, gastroduodenal, etc.) from a non-authoritative source, this keeps the simpler, complete-sounding sentence, matching the issue author's stated preference.

## Checklist

- [x] Read issue #3509 and identified the precise truncation problem
- [x] Checked out UBERON:0005436 using `obo-checkout.pl` into `terms/`
- [x] Edited only the `def:` line; left synonyms, xrefs, is_a, relationships, and property_value untouched
- [x] Checked the term back in using `obo-checkin.pl`
- [x] Reserialised `src/ontology/uberon-edit.obo` with `robot convert`
- [x] Verified diff is minimal (1 line changed)
- [x] Committed on the working branch

Signed: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834933215)


#### Agent Issue Comment

Changes committed in PR #<NN>.

The trailing fragment "and has the following branches:." has been removed from the definition of `common hepatic artery` (UBERON:0005436). The definition now ends cleanly at "It arises from the celiac artery."

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834933215)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..cf7f76d0e 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 5: gemma-4-31b / opencode

- **Eval PR**: [#113](https://github.com/ai4curation/eval-ont-agent-uberon/pull/113)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25683678795](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25683678795)
- **Workflow run**: [25683678795](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683678795)

#### Agent PR Comment

The definition of 'common hepatic artery' (UBERON:0005436) was truncated, ending with "and has the following branches:.". I have shortened the definition to remove this trailing phrase.

Checklist:
- [x] Identified the truncated definition of UBERON:0005436.
- [x] Edited the term using `obo-checkout.pl` and `obo-checkin.pl`.
- [x] Verified the change in `src/ontology/uberon-edit.obo`.
- [x] Committed the changes.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683678795)

#### Agent Issue Comment

Changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683678795)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..cf7f76d0e 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 6: gpt-5.5 / codex

- **Eval PR**: [#28](https://github.com/ai4curation/eval-ont-agent-uberon/pull/28)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615884788](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615884788)
- **Workflow run**: [25615884788](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615884788)

#### Agent PR Comment

This PR addresses issue #3509 by shortening the definition for `UBERON:0005436` (`common hepatic artery`) so it no longer ends with the incomplete phrase "has the following branches:.".

The new definition keeps the existing Wikipedia source reference and preserves the term's current hierarchy and relationships. I checked the current term stanza, reviewed the parent `systemic artery` and related `celiac artery` stanzas for consistency, checked the term out through `obo-checkout.pl`, edited the checked-out term, checked it back in, and reserialized `src/ontology/uberon-edit.obo` with `robot convert`.

Checklist completed:

- Read imported issue context from `__issue_context__.json`.
- Confirmed the affected term is `UBERON:0005436`.
- Checked the proposed existing parent and celiac artery relationship context.
- Shortened only the definition text for `common hepatic artery`.
- Preserved the existing definition xref.
- Validated OBO parsing with `robot convert -i src/ontology/uberon-edit.obo -f obo -o /tmp/uberon-edit-check.obo`.
- Committed only `src/ontology/uberon-edit.obo`.

@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615884788)


#### Agent Issue Comment

Updated UBERON:0005436 in PR #<NN> to remove the dangling trailing clause from the common hepatic artery definition.

@dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615884788)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..4aca6c259 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that arises from the celiac artery and supplies oxygenated blood to the liver, pylorus, duodenum and pancreas." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#63](https://github.com/ai4curation/eval-ont-agent-uberon/pull/63)
- **F1**: 0.400  **Precision**: 0.500  **Recall**: 0.333  **Jaccard**: 0.250
- **Trace**: [25615968931](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615968931)
- **Workflow run**: [25615968931](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615968931)

#### Agent PR Comment

## Summary

- Shortened the definition of `UBERON:0005436` (`common hepatic artery`) to remove the truncated trailing sentence ending in `has the following branches:.`.
- Added a `term_tracker_item` property linking the term to issue #3509.

## Rationale

The issue reported that the existing Wikipedia-derived definition was truncated/trailing. The updated definition preserves the useful supply-target content while removing the incomplete branch-introduction sentence and simplifying parenthetical wording.

## Validation

- Checked out and edited `UBERON:0005436` using the ontology term checkout/checkin workflow.
- Re-serialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Ran `robot convert` to a temporary output file to validate OBO syntax.
- Ran `git diff --check`.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615968931)


#### Agent Issue Comment

Updated UBERON:0005436 (`common hepatic artery`) to shorten the definition and remove the truncated trailing clause. Changes committed locally for PR #<NN>.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615968931)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..cc0a2591f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "The common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus, duodenum, and pancreas." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308
@@ -101467,6 +101467,7 @@ xref: Wikipedia:Common_hepatic_artery
 is_a: UBERON:0004573 ! systemic artery
 relationship: connecting_branch_of UBERON:0001640 ! celiac artery
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/6/65/Gray532.png" xsd:anyURI
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3509" xsd:anyURI
 
 [Term]
 id: UBERON:0005437

```

### Attempt 8: gpt-5.5 / opencode

- **Eval PR**: [#44](https://github.com/ai4curation/eval-ont-agent-uberon/pull/44)
- **F1**: 0.400  **Precision**: 0.500  **Recall**: 0.333  **Jaccard**: 0.250
- **Trace**: [25615927298](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615927298)
- **Workflow run**: [25615927298](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927298)

#### Agent PR Comment

Updated `UBERON:0005436` (`common hepatic artery`) to remove the truncated trailing phrase in the definition.

Rationale:
- The old definition ended with `and has the following branches:.`, which was grammatically incomplete.
- The revised definition keeps the same Wikipedia source and preserves the core anatomical content while shortening the wording.
- Added a `term_tracker_item` link back to issue #3509 for traceability.

Completed checklist:
- Read imported issue context from `__issue_context__.json`.
- Inspected the existing `UBERON:0005436` stanza with `obo-grep.pl`.
- Edited via the `terms/` checkout/checkin workflow.
- Verified the final diff is scoped to the target term.
- Ran `robot convert` syntax validation successfully.
- Committed the ontology change locally as `a9ee5ce`.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927298)


#### Agent Issue Comment

Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927298)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc..cc0a2591f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "The common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus, duodenum, and pancreas." [Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308
@@ -101467,6 +101467,7 @@ xref: Wikipedia:Common_hepatic_artery
 is_a: UBERON:0004573 ! systemic artery
 relationship: connecting_branch_of UBERON:0001640 ! celiac artery
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/6/65/Gray532.png" xsd:anyURI
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3509" xsd:anyURI
 
 [Term]
 id: UBERON:0005437

```
