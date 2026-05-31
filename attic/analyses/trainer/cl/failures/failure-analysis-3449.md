# Failure Analysis: PR #3449

**PR:** [#3449 - Add IgD-negative marker to class switched memory B cell (CL_0000972)](https://github.com/obophenotype/cell-ontology/pull/3449)

**Issue:** [#3165](https://github.com/obophenotype/cell-ontology/issues/3165)

**Status:** CLOSED (not merged)

**Closed:** 2025-12-08

## Summary

The agent attempted to add an IgD-negative marker (`lacks_plasma_membrane_part IgD immunoglobulin complex`) to the class switched memory B cell term. The implementation was technically correct based on the issue description, but it caused a logical inconsistency in the ontology.

## What the Agent Did

1. Added logical definition: `lacks_plasma_membrane_part GO_0071738` (IgD immunoglobulin complex)
2. Updated text definition: "IgM-negative" -> "IgM/IgD-negative"
3. Added references: PMID:36617261, PMID:32741082, PMID:37254600, PMID:20839340

## Why It Failed

### Root Cause: Ontological Inconsistency Not Detected

The agent did not check for existing subclasses that would conflict with the new axiom. Specifically:

- **Conflicting subclass:** [IgD-positive CD38-positive IgG memory B cell (CL:0002106)](http://purl.obolibrary.org/obo/CL_0002106) is a subclass of class switched memory B cell
- **Logical conflict:** A parent class cannot have `lacks_plasma_membrane_part IgD` when a child class is explicitly IgD-positive
- **Resolution needed:** The hierarchy needs restructuring - possibly adding an intermediate "IgD-negative switched memory B cell" class

### Evidence from Comments

Caroline-99 (curator) explained:
> "We have the subclass IgD-positive CD38-positive IgG memory B cell, which conflicts with this axiom... If we want to keep the lacks_plasma_membrane_part axiom, we should reclassify CL:0002106 to a different parent"

dosumis proposed:
> "Suggested fix, make a new class IgD minus switched, and move the rest of the branch... under it."

## Failure Mode

**Category:** Ontological consistency / hierarchy conflict

**Severity:** Medium - the implementation was correct for the issue as stated, but didn't account for the broader ontology structure

## Lessons Learned

1. **Check subclasses before adding negative markers**: When adding `lacks_*` axioms to a class, always verify no subclasses express the opposite marker
2. **Run reasoner checks**: Use ROBOT or OWL reasoner to detect unsatisfiable classes before submitting
3. **Understand class hierarchies**: Review the full hierarchy of a term before making changes that could introduce inconsistencies
4. **Propose structural changes when needed**: If an issue request would cause inconsistencies, propose alternative approaches (like intermediate classes) rather than implementing literally

## Remediation

Before adding negative marker axioms:
```bash
# Check for subclasses with conflicting positive markers
robot query --input cl-edit.owl --query "
SELECT ?subclass ?label WHERE {
  ?subclass rdfs:subClassOf* obo:CL_0000972 .
  ?subclass rdfs:label ?label .
  FILTER(CONTAINS(LCASE(?label), 'igd-positive') || CONTAINS(LCASE(?label), 'igd positive'))
}
"
```

## Related Training

- Always validate ontological consistency before submitting changes to class hierarchies
- When issues mention adding constraints, check if existing subclasses would violate those constraints
