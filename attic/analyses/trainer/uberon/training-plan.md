# Training Plan: dragon-ai-agent for Uberon Contributions

## Executive Summary

Analysis of 14 PRs from dragon-ai-agent to the Uberon ontology revealed a 100% eventual merge rate, but only 42.9% were merged without requiring modifications. The following training plan addresses the identified failure modes to improve first-time acceptance rate.

**Caveat:** Some "merged with mods" cases reflect process timing or automated review gates (e.g., #gogoeditdiff dependencies) rather than content errors; focus remediation on the repeatable behavioral issues below.

## Failure Mode Summary

| Failure Mode | Occurrences | Severity | PRs Affected |
|-------------|-------------|----------|--------------|
| PMID Validation Error | 1 | Medium | #3638 |
| Contributor Attribution Error | 1 | High | #3620 |
| Temporary ID Usage | 1 | Medium | #3609 |
| Incomplete Initial Submission | 2 | Low | #3603, #3633 |
| Logical Definition Scope Underestimation | 1 | Low | #3619 |
| Dependency Timing Issues | 1 | Low | #3573 |
| Over-inclusion of Request Content | 1 | Low | #3630 |

## Training Instructions

### 1. External Identifier Validation

**Problem**: Agent incorrectly rejected valid PMIDs as "out of range."

**Training Rule**:
```
NEVER validate external identifiers (PMIDs, DOIs, ORCIDs) by checking if
they fall within an expected numeric range. These identifiers are
continuously growing and have no upper limit.

DO validate:
- Format correctness (e.g., PMID:12345 pattern)
- Basic syntax

DO NOT validate:
- Numeric ranges
- "Existence" unless you have real-time API access

When maintainers provide references, trust them. If you have concerns,
proceed with submission and note the concern, rather than blocking.
```

### 2. Contributor Attribution

**Problem**: Agent used wrong contributor name/ORCID.

**Training Rule**:
```
Attribution is critical. Always:

1. Extract contributor information directly from the issue request
2. If the issue mentions a specific person by name, use THAT exact name
3. Verify ORCID lookups match the provided name exactly
4. If there are multiple people with similar names, ASK for clarification
5. Never guess or assume contributor identity

Example:
- Issue says: "Submitted by Stan Laulederkind"
- Lookup returns: "Sarah Laulederkind (similar name)"
- CORRECT ACTION: Ask for clarification or use the name from the issue
- WRONG ACTION: Use the similar name from lookup
```

### 3. Ontology ID Allocation

**Problem**: Agent used temporary placeholder IDs that required manual replacement.

**Training Rule**:
```
ID allocation varies by ontology. For Uberon:

1. Check if there's an established ID range for new terms
2. Look at recent term additions to understand the ID pattern
3. If unsure, ASK the maintainers before creating the PR
4. Consider using placeholder syntax that maintainers can easily find/replace

For new term requests:
- Review the ontology's contribution guidelines
- Check if IDs are auto-assigned or manually allocated
- When in doubt, note in PR description: "ID needs allocation"
```

### 4. Complete Initial Submissions

**Problem**: Terms added with missing attributes required follow-up PRs.

**Training Rule**:
```
Before submitting a new term, verify ALL required fields are populated:

Required for Uberon terms:
- [ ] id: Proper UBERON ID
- [ ] name: Term label
- [ ] def: Definition with proper dbxref citations
- [ ] is_a: Parent class relationship
- [ ] relationship: Relevant part_of, has_part, etc.
- [ ] xref: Cross-references to other ontologies (FMA, NCIT, etc.)
- [ ] synonym: Exact, related, narrow, broad synonyms as appropriate
- [ ] property_value: dcterms-date, term_tracker_item
- [ ] relationship: dc-contributor with ORCID
- [ ] created_by: Agent identifier

Use existing terms as templates. Compare your submission against
similar recently-added terms.
```

### 5. Logical Definition Impact Awareness

**Problem**: Changes to logical definitions triggered automated reviews due to cascading effects.

**Training Rule**:
```
When modifying logical definitions (equivalentTo, intersection_of):

1. Understand that OWL reasoners will propagate changes
2. Changing a parent class affects ALL descendants
3. Expect automated CI checks for "large-scale logical changes"
4. In PR description, document:
   - What you're changing and why
   - Expected downstream effects
   - Which terms will be affected

For Uberon specifically:
- The #gogoeditdiff bot analyzes inference changes
- "Large scale logical changes" require core team review
- This is NOT a rejection, just additional scrutiny
```

### 6. Understanding Request Context

**Problem**: Agent included administrative notes as term content.

**Training Rule**:
```
Issue requests contain multiple types of information:

INCLUDE in ontology:
- Preferred term label
- Definition text
- Synonyms
- References (PMIDs, textbooks)
- Relationships
- Cross-references

DO NOT INCLUDE in ontology:
- "Reason for addition" (administrative tracking)
- Discussion notes
- Process instructions
- Request metadata

When maintainers say "disregard X", comply exactly.
```

### 7. Dependency and Timing Awareness

**Problem**: PR submitted before prerequisite PRs were merged.

**Training Rule**:
```
Before creating a PR:

1. Check for related open PRs that might affect your work
2. If your change depends on another PR, note this dependency
3. Consider whether to:
   - Wait for the dependency to merge
   - Base your branch on the dependency branch
   - Note the dependency in your PR description

For Uberon:
- The #gogoeditdiff tool requires main branch to be current
- If bot commands fail, there may be pending dependencies
```

## Metrics for Success

Track these metrics to measure improvement:

| Metric | Current | Target |
|--------|---------|--------|
| First-time acceptance rate | 42.9% | 75%+ |
| PRs requiring attribution fixes | 7.1% | 0% |
| PRs with ID allocation issues | 7.1% | 0% |
| PRs with validation errors | 7.1% | 0% |

## Implementation Checklist

Before each PR submission, verify:

- [ ] All external identifiers (PMIDs, ORCIDs) use correct format
- [ ] Contributor attribution matches the issue request exactly
- [ ] ID allocation follows ontology conventions (or asks for help)
- [ ] All required term attributes are populated
- [ ] Logical definition changes are documented with expected effects
- [ ] Only technical content (not administrative notes) is included
- [ ] No conflicting PRs are pending that could affect this work

## Continuous Improvement

After each PR cycle:
1. If modifications were requested, analyze why
2. Update training rules if new patterns emerge
3. Track acceptance rate over time
4. Document edge cases for future reference

---

*Generated: 2025-12-20*
*Based on analysis of 14 PRs from dragon-ai-agent to obophenotype/uberon*
