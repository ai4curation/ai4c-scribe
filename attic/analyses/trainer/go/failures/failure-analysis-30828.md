# Failure Analysis: PR #30828

## PR Title
Obsolete organic anion/cation transport/transporter terms

## Failure Mode
**Changes too broad / extensive for single PR**

## What Happened
1. PR attempted to obsolete 4 terms:
   - GO:0015101 organic cation transmembrane transporter activity
   - GO:0008514 organic anion transmembrane transporter activity
   - GO:0015695 organic cation transport
   - GO:0015711 organic anion transport

2. The diff was enormous - affecting hundreds of child terms
3. This cascaded through the ontology

## Scale of Changes
The PR touched relationships for:
- 100+ child terms that referenced these as parents
- Multiple transport and transporter activity terms across amino acids, nucleotides, etc.

## Root Causes
1. **Did not consider the cascading impact of obsoleting high-level terms**
2. **These terms have many children that needed their parentage adjusted**
3. **Too much change for one PR to properly review**

## Correct Approach
For high-impact obsoletions:
1. First analyze the impact - how many terms are affected?
2. Discuss on the issue to determine if obsoletion is the right approach
3. Consider alternative approaches (renaming, refactoring hierarchy)
4. If proceeding, may need to break into multiple PRs
5. Ensure all child terms are properly re-parented

## Status
Closed without merge - changes too extensive
