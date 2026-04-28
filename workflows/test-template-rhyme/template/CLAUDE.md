# Agent Instructions

This agent writes poetry with proper rhyme schemes.

## Task Guidelines

1. Read the issue context from `__issue_context__.json`
2. Understand what poem is requested
3. Write the poem
4. **Always validate rhymes using the rhyme-validator skill**
5. Commit with a clear message

## Poetry Rules

- All poems MUST have alternating rhymes (ABAB pattern) unless otherwise specified
- Always validate poems using the rhyme-validator skill before committing
- Run: `python .skills/rhyme-validator/scripts/validate_rhyme.py poem.txt`
- If validation fails, revise the poem until it passes
