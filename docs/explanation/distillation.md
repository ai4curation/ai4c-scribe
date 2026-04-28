# Distillation

Distillation transforms raw review cases into curated training vignettes using AI. This process removes noise, extracts lessons, and rates quality.

## Why distillation?

Raw review cases from GitHub contain:

- Noise: Unrelated discussions, typos, formatting issues
- Implicit context: Domain knowledge assumed but not stated
- Variable quality: Some reviews are more instructive than others

Distillation addresses these issues by:

- Cleaning up presentation
- Adding explanatory context
- Rating clarity and difficulty
- Flagging quality issues

## How it works

The distillation process uses an AI agent (via cyberian framework) to:

1. **Analyze the review case**: Understand the issue, code change, and feedback
2. **Extract the lesson**: What can be learned from this example?
3. **Create a narrative**: Write a clear explanation
4. **Assign ratings**: Score clarity and difficulty
5. **Note issues**: Flag any quality problems

```
┌─────────────────┐
│  Review Case    │
│  (raw JSONL)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   AI Agent      │
│   (cyberian)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Distilled      │
│  Vignette       │
│  (markdown)     │
└─────────────────┘
```

## Fresh agent per case

Each review case gets a fresh AI agent server:

- Clean context without contamination
- Independent processing
- Robust to failures (one failure doesn't affect others)

## Output structure

Each vignette is a markdown file with YAML frontmatter:

```yaml
---
pr_number: 8116
repository: monarch-initiative/mondo
linked_issue_number: 7712
first_revision_action: CHANGES_REQUESTED
num_reviews_in_first_revision: 3
clarity: 4
difficulty: 3
quality_issues: null
---

# PR Review Vignette: Merge Disease Terms

## Context

The linked issue (#7712) requested merging two disease terms that
appeared to be duplicates: "dermatitis, atopic" and "atopic eczema".

## Initial Code Change

The PR author proposed adding synonyms and cross-references to merge
the terms in the ontology...

## Review Feedback

Reviewers identified several concerns:

1. **Semantic equivalence**: The terms may not be true equivalents...
2. **Casing convention**: Synonyms should be lowercase...

## Lesson Learned

When merging ontology terms, verify semantic equivalence rather than
just lexical similarity. Domain experts should validate...
```

## Ratings

### Clarity (1-5)

How clear and self-contained is the example?

| Rating | Meaning |
|--------|---------|
| 5 | Crystal clear, self-contained |
| 4 | Clear with minor domain knowledge needed |
| 3 | Reasonably clear, some context needed |
| 2 | Somewhat confusing |
| 1 | Very confusing, needs significant explanation |

High clarity cases are better for training.

### Difficulty (1-5)

How challenging is the review pattern?

| Rating | Meaning |
|--------|---------|
| 5 | Complex edge case, subtle domain knowledge |
| 4 | Challenging with nuances |
| 3 | Standard review scenario |
| 2 | Straightforward pattern |
| 1 | Simple, obvious correction |

Difficulty affects training curriculum design.

### Quality issues

The AI may note problems:

- Missing context
- Noisy or irrelevant content
- Unclear review feedback
- Incomplete information

Use these flags to filter or re-process cases.

## Repository exploration (optional)

For deeper context, provide a git worktree:

```bash
ai4c-scribe distill cases.jsonl -o vignettes/ -r /path/to/worktree
```

The agent can then:

- Browse the codebase at the parent commit
- Understand file structure and conventions
- Reference related code

## Processing characteristics

- **Time**: ~1-2 minutes per case
- **Independence**: Cases processed sequentially, each with fresh agent
- **Incremental**: Vignettes written as completed
- **Resumable**: Safe to interrupt and resume

## Quality filtering

After distillation, filter by quality:

```bash
# High clarity cases
grep -l "clarity: [45]" vignettes/*.md

# Difficult cases
grep -l "difficulty: [45]" vignettes/*.md

# Cases without quality issues
grep -l "quality_issues: null" vignettes/*.md
```

## Training curriculum

Use ratings for curriculum design:

1. **Start simple**: Low difficulty, high clarity
2. **Progress**: Medium difficulty
3. **Advanced**: High difficulty, domain-specific

## See also

- [Distill vignettes](../how-to/distill-vignettes.md): How-to guide
- [Review cases](review-cases.md): Input format
- [Full workflow](../tutorials/full-workflow.md): End-to-end tutorial
