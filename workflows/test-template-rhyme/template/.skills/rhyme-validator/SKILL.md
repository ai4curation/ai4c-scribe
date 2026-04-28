---
name: rhyme-validator
description: Validates that poems have alternating (ABAB) rhyme scheme. Use when writing poems, checking verse structure, or validating rhyme patterns.
allowed-tools: Read, Bash(python:*)
---

# Rhyme Validator

Validates poems have proper alternating rhyme scheme (ABAB pattern).

## Usage

To validate a poem file:

```bash
python scripts/validate_rhyme.py poem.txt
```

Or pipe text directly:

```bash
echo "poem text here" | python scripts/validate_rhyme.py
```

## What Gets Checked

- Lines 1, 3, 5... must rhyme with each other (A lines)
- Lines 2, 4, 6... must rhyme with each other (B lines)
- Minimum 4 lines required for ABAB pattern

## Example

Good poem (passes):
```
Roses are red
Violets are blue
I bumped my head
And lost my shoe
```

If validation fails, revise the poem and re-run until it passes.
