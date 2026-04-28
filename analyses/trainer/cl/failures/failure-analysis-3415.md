# Failure Analysis: PR #3415

**PR:** [#3415 - Verify CL:0002042 is absent from hra_subset.owl](https://github.com/obophenotype/cell-ontology/pull/3415)

**Issue:** [#3414](https://github.com/obophenotype/cell-ontology/issues/3414)

**Status:** CLOSED (not merged)

**Closed:** 2025-10-29

## Summary

The issue requested removing CL:0002042 (a mouse-specific term) from the Human Reference Atlas subset file. The agent verified the term was already absent from the file but made unnecessary changes to the Makefile.

## What the Agent Did

1. Correctly verified that CL:0002042 was already absent from `hra_subset.owl`
2. **Incorrectly modified the Makefile** with unnecessary changes
3. After being told to only modify `hra_subset.owl`, reverted Makefile changes in a new commit

## Why It Failed

### Root Cause: Scope Creep

The agent expanded beyond the requested scope by modifying the Makefile when:
1. The issue only asked to remove a term from `hra_subset.owl`
2. The term was already absent (no changes needed)
3. No Makefile changes were requested or required

### Evidence from Comments

Caroline-99:
> "@copilot only make changes to hra_subset.owl file"

Agent response:
> "Reverted Makefile changes in commit 4bb147e. CL:0002042 is already absent from hra_subset.owl - no changes to that file were necessary."

## Failure Mode

**Category:** Scope creep / unnecessary changes

**Severity:** Low - the changes were reverted and no harm was done, but it created extra review work

## Lessons Learned

1. **Stay within requested scope**: Only modify files explicitly mentioned in the issue
2. **Don't "improve" beyond the ask**: Resist the urge to make helpful but unrequested changes
3. **Verify before modifying**: The term was already absent, so no changes were needed at all
4. **Be explicit about no-op situations**: When no changes are needed, communicate this clearly rather than finding something else to change

## Pattern Recognition

This is a common AI agent failure mode:
- Agent feels obligated to "do something" even when nothing is needed
- Agent tries to be helpful by making tangential improvements
- Result: Creates review burden and potential for introducing bugs

## Remediation

When given a task:
1. First determine if any changes are actually needed
2. If no changes needed, report that fact and close/complete without modifications
3. If changes are needed, only modify the specific files mentioned
4. Never modify build files (Makefile, pyproject.toml, etc.) unless explicitly requested

## Training Instruction

```
When an issue asks to modify a specific file:
1. Check if the requested change is already in place
2. If yes: Report "No changes needed - [reason]" and do not modify any files
3. If no: Make ONLY the requested change to ONLY the specified file(s)
4. Never modify Makefile, CI configs, or other infrastructure without explicit request
```
