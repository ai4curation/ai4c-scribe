# How to distill vignettes

This guide covers using AI to refine review cases into curated training vignettes.

## Prerequisites

The distill command requires optional AI dependencies:

```bash
pip install "ai4c-scribe[ai]"
```

This installs the [cyberian](https://github.com/ai4curation/cyberian) framework for AI agent coordination.

## Basic usage

Distill review cases into vignettes:

```bash
ai4c-scribe distill cases.jsonl -o vignettes/
```

**Required arguments:**

- Input file (positional): JSONL file from `create-review-cases`

**Optional arguments:**

- `-o, --output-dir`: Output directory for vignette markdown files
- `-f, --input-format`: Input format (`jsonl` or `markdown`)
- `-v, --verbose`: Verbose output (use `-vv` for debug)

## How distillation works

For each review case, the distill command:

1. Starts a fresh AI agent server
2. Sends the review case to the agent
3. Agent analyzes and refines the case
4. Agent assigns clarity and difficulty ratings
5. Writes a vignette markdown file
6. Stops the agent server

Each vignette is processed independently with a clean agent context.

## Output structure

Vignettes are written as markdown files with YAML frontmatter:

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

The issue requested merging two disease terms...

## Initial Code

The PR proposed changes to...

## Review Feedback

Reviewers noted...

## Lesson Learned

This case demonstrates...
```

## Ratings

### Clarity (1-5)

How clear and understandable is this review case?

- **5**: Crystal clear, self-contained, easy to understand
- **4**: Clear with minor domain knowledge needed
- **3**: Reasonably clear, requires some context
- **2**: Somewhat confusing, missing key context
- **1**: Very confusing, requires significant explanation

### Difficulty (1-5)

How challenging would it be for an LLM to learn this pattern?

- **5**: Complex edge case, subtle domain knowledge required
- **4**: Challenging pattern with nuances
- **3**: Standard review scenario
- **2**: Straightforward with clear pattern
- **1**: Simple, obvious correction

### Quality issues

Any problems the AI noted:

- Missing context
- Noisy or irrelevant content
- Unclear review feedback
- Incomplete information

## Verbose output

Use `-v` for progress information:

```bash
ai4c-scribe distill cases.jsonl -o vignettes/ -v
```

Output includes:

```
[INFO] Starting server for PR #8116
[INFO]   Port: 5200
[INFO]   Working directory: /tmp/ai4c-scribe-distill-xxx
[INFO] Running distillation for PR #8116
Wrote vignette to vignettes/pr_8116.md
```

Use `-vv` for debug output including agent communication.

## Repository exploration (advanced)

For deeper context, provide a git worktree that the agent can explore:

```bash
ai4c-scribe distill cases.jsonl -o vignettes/ -r /path/to/worktree
```

!!! warning "Destructive operation"
    The `--repo-worktree` option uses `git reset --hard` to reset the worktree
    to each PR's parent commit. Only use with dedicated worktrees created
    specifically for this purpose.

Setting up a worktree:

```bash
# Clone the repo
git clone https://github.com/owner/repo.git repo-main

# Create a worktree for distillation
cd repo-main
git worktree add ../repo-distill main
```

Then use:

```bash
ai4c-scribe distill cases.jsonl -o vignettes/ -r ../repo-distill
```

The agent can then explore the repository state at each PR's parent commit.

## Working with output

### List all vignettes

```bash
ls vignettes/
# pr_8116.md  pr_8117.md  pr_8120.md  ...
```

### Extract ratings

```bash
for f in vignettes/*.md; do
  echo -n "$f: "
  grep -E '^(clarity|difficulty):' "$f" | tr '\n' ' '
  echo
done
```

### Find high-quality cases

```bash
grep -l "clarity: 5" vignettes/*.md
```

### Find cases with quality issues

```bash
grep -l "quality_issues: [^n]" vignettes/*.md
```

## Performance considerations

- Each case starts a fresh agent server (clean context)
- Expect ~1-2 minutes per case
- Progress is saved incrementally (safe to interrupt)
- Existing vignettes are overwritten on re-run

## Troubleshooting

### "cyberian is required for distillation"

Install AI dependencies:

```bash
pip install "ai4c-scribe[ai]"
```

### Agent timeout

Increase the timeout by setting the `CYBERIAN_TIMEOUT` environment variable.

### Server won't start

Check that the port range (5200-5300) is available:

```bash
lsof -i :5200-5300
```

### Skipping cases

Cases are skipped if:

- They have no linked issue number
- The agent encounters an error (logged and continues)

## See also

- [Create review cases](create-review-cases.md): Create the input file
- [Distillation concept](../explanation/distillation.md): Understanding the process
- [Full workflow tutorial](../tutorials/full-workflow.md): End-to-end example
