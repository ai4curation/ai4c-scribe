# Metadiff: Deterministic Diff Comparison

Metadiff is a tool for comparing two diffs and computing standard metrics (F1, precision, recall, Jaccard similarity) with configurable, pluggable normalization for domain-specific patterns.

## Use Case

Compare human PR diffs against agent-generated PR diffs to measure how well the agent learned the repair pattern. Works particularly well for ontology files, code changes, and other structured formats.

**Example**: When evaluating an LLM agent that fixes issues in a repository:
- Original PR = human solution (gold standard)
- Agent PR = what the agent generated
- Metadiff = quantifies how similar they are

## Python API

### Basic Usage

```python
from ai4c_scribe.metadiff import compare_diffs, get_config

# Compare two diffs
diff1 = "+new_field: value\n-old_field: value"
diff2 = "+new_field: value\n-old_field: value"

result = compare_diffs(diff1, diff2, config=get_config("generic"), silent=True)

print(f"Similarity: {result.similarity:.3f}")      # Jaccard similarity
print(f"F1 Score: {result.f1_score:.3f}")          # Harmonic mean of precision/recall
print(f"Precision: {result.precision:.3f}")        # True positives / predicted positives
print(f"Recall: {result.recall:.3f}")              # True positives / actual positives
print(f"Identical: {result.identical}")            # Exact match?
```

### From Files

```python
from pathlib import Path
from ai4c_scribe.metadiff import compare_diff_files, get_config

result = compare_diff_files(
    Path("human.diff"),
    Path("agent.diff"),
    config=get_config("obo"),
    silent=False,  # Print visual diff to console
)

# Access metrics
print(f"True Positives: {result.comparison.num_changes_in_common}")
print(f"False Positives: {result.comparison.num_changes_in_diff2}")
print(f"False Negatives: {result.comparison.num_changes_in_diff1}")

# Save results
import json
with open("comparison.json", "w") as f:
    json.dump(result.model_dump(mode="json"), f, indent=2)

# Save HTML visualization
if result.comparison.visual_diff_html:
    with open("comparison.html", "w") as f:
        f.write(result.comparison.visual_diff_html)
```

### Configuration Presets

Available configurations:

```python
from ai4c_scribe.metadiff import get_config, list_configs

# List all available configs
for name in list_configs():
    config = get_config(name)
    print(f"{name}: {config.description}")
    # Output:
    # generic: Generic diff comparison with minimal normalization
    # obo: OBO ontology file comparison (GO, HP, etc.)
    # python: Python code comparison
    # strict: Strict comparison with no normalization
```

#### GENERIC_CONFIG
Minimal normalization - just whitespace handling.
```python
config = get_config("generic")
```

#### OBO_CONFIG
For ontology files (GO, HP, etc.). Masks CURIE IDs (GO:0000001 → GO:NNNNNNN) and ignores metadata fields that vary but don't affect semantics:
- created_by
- creation_date
- property_value: dcterms-date
- relationship: dc-contributor

```python
config = get_config("obo")
result = compare_diffs(human_diff, agent_diff, config=config)
```

#### PYTHON_CONFIG
For Python code. Ignores comments and empty lines.
```python
config = get_config("python")
```

#### STRICT_CONFIG
No normalization - exact comparison.
```python
config = get_config("strict")
```

### Custom Normalization

Create custom configurations by combining normalizers:

```python
from ai4c_scribe.metadiff import compare_diffs
from ai4c_scribe.metadiff.models import MetadiffConfig, NormalizerConfig
from ai4c_scribe.metadiff.normalizers import mask_timestamps, mask_version_numbers

# Custom config: mask timestamps and version numbers
config = MetadiffConfig(
    name="custom",
    normalizer=NormalizerConfig(
        mask_ids=False,
        ignore_patterns=[r"^\s*#"],  # Ignore comments
        custom_normalizers=[mask_timestamps, mask_version_numbers],
    ),
    generate_visual=True,
)

result = compare_diffs(diff1, diff2, config=config)
```

### Available Normalizers

```python
from ai4c_scribe.metadiff.normalizers import (
    mask_curie_ids,              # GO:0000001 → GO:NNNNNNN
    mask_timestamps,             # 2024-01-15T10:30:00Z → YYYY-MM-DDTHH:MM:SSZ
    mask_version_numbers,        # 1.2.3 → X.Y.Z
    normalize_whitespace,        # Multiple spaces → single space
    strip_comments,              # Remove inline comments
    mask_commit_shas,            # a1b2c3d → SHA
    mask_guids,                  # UUID → GUID
    mask_usernames,              # @alice → @REDACTED
    mask_file_paths,             # /home/user/file.txt → /PATH/TO/file.txt
)
```

## CLI

### List Available Configs

```bash
ai4c-scribe metadiff configs
```

Output:
```
Available metadiff configurations:

  generic
    Generic diff comparison with minimal normalization
    - Mask IDs: False
    - Ignore patterns: 0
    - Ignore keys: 0

  obo
    OBO ontology file comparison (GO, HP, etc.)
    - Mask IDs: True
    - Ignore patterns: 0
    - Ignore keys: 4
    - Custom normalizers: 2
    ...
```

### Compare Two Diffs

```bash
# Basic comparison
ai4c-scribe metadiff compare human.diff agent.diff

# With specific config
ai4c-scribe metadiff compare human.diff agent.diff -c obo

# Save results as JSON
ai4c-scribe metadiff compare human.diff agent.diff -o results.json -f json

# Save results as text
ai4c-scribe metadiff compare human.diff agent.diff -o results.txt -f text

# Skip visual diff (faster)
ai4c-scribe metadiff compare human.diff agent.diff --no-visual
```

## Workflow Integration

Metadiff is automatically run when dumping workflow artifacts. For each completed workflow run, the dump includes:

```
output_dir/
├── {params_hash_prefix}/
│   ├── original-pr-{num}.diff         # Human solution
│   ├── pr-{num}.diff                  # Agent solution
│   ├── diff-comparison.json           # Comparison stats
│   └── diff-comparison.html           # Visual comparison
```

The comparison stats include:
- `similarity`: Jaccard similarity (0.0 to 1.0)
- `f1_score`: F1 score (0.0 to 1.0)
- `precision`: Precision (0.0 to 1.0)
- `recall`: Recall (0.0 to 1.0)
- `identical`: Whether diffs are exactly identical
- `changes_in_common`: Number of matching changes (true positives)
- `changes_in_diff1`: Number of changes only in original (false negatives)
- `changes_in_diff2`: Number of changes only in agent (false positives)

### Example Workflow

```bash
# Run workflows
ai4c-scribe workflows run config.yaml

# Dump artifacts with metadiff comparison
ai4c-scribe workflows dump -o ./results

# View comparison HTML in browser
open results/a1b2c3d4e5f6/diff-comparison.html

# Check comparison stats
cat results/a1b2c3d4e5f6/diff-comparison.json
```

## Metrics Explained

### Similarity (Jaccard)

Ratio of common changes to total unique changes.

```
Similarity = |A ∩ B| / |A ∪ B|
```

- 1.0 = diffs are identical (all changes match)
- 0.0 = diffs are completely different (no changes match)

**Use case**: Overall similarity assessment.

### Precision

Fraction of agent changes that match the human solution.

```
Precision = True Positives / (True Positives + False Positives)
         = |common| / |agent_changes|
```

- 1.0 = all agent changes are correct
- 0.0 = no agent changes match
- High precision = agent doesn't over-modify

**Use case**: Is the agent making unnecessary changes?

### Recall

Fraction of human changes that the agent replicated.

```
Recall = True Positives / (True Positives + False Negatives)
      = |common| / |human_changes|
```

- 1.0 = agent replicated all human changes
- 0.0 = agent missed all changes
- High recall = agent captures the full fix

**Use case**: Did the agent miss key changes?

### F1 Score

Harmonic mean of precision and recall (0.0 to 1.0).

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

- Balances precision and recall
- Better for unbalanced datasets than accuracy
- Standard metric for information retrieval

**Use case**: Overall quality metric (single number summary).

## Real-World Example

### Scenario
Evaluating an agent that fixes GitHub issues in an ontology repository.

```python
from ai4c_scribe.metadiff import compare_diff_files, get_config

# Human solution: manually fixed the issue
human_diff = Path("human-fix.diff")

# Agent solution: LLM-generated fix
agent_diff = Path("agent-fix.diff")

# Compare using OBO config (masks arbitrary IDs, ignores metadata)
result = compare_diff_files(
    human_diff,
    agent_diff,
    config=get_config("obo"),
    silent=False,  # Show visual comparison
)

# Analyze results
comparison = result.comparison

print(f"Overall similarity: {comparison.similarity:.1%}")
print(f"F1 score: {comparison.f1_score:.1%}")
print(f"Quality breakdown:")
print(f"  ✓ Matched changes: {comparison.num_changes_in_common}")
print(f"  ✗ Missing from agent: {comparison.num_changes_in_diff1}")
print(f"  ⚠ Extra from agent: {comparison.num_changes_in_diff2}")

# Interpretation:
# Similarity 95% + F1 95% = agent learned the pattern very well
# Missing 1 change = agent probably missed a subtle requirement
# Extra 0 changes = agent didn't over-modify (good!)
```

## Integration with PR Mining

Metadiff works naturally with ai4c-scribe's PR mining functionality:

```python
from ai4c_scribe.pr_mining import mine_pr
from ai4c_scribe.metadiff import compare_diffs, get_config

# Mine human PR (solution)
human_pr = mine_pr("monarch-initiative/mondo", 8116)
human_diff = "\n".join(human_pr.diff.final_diff)

# Mine agent PR (attempt)
agent_pr = mine_pr("monarch-initiative/mondo", 8117)
agent_diff = "\n".join(agent_pr.diff.final_diff)

# Compare with OBO configuration
result = compare_diffs(
    human_diff,
    agent_diff,
    config=get_config("obo"),
    silent=True,
)

# Print metrics
print(f"Similarity: {result.similarity:.3f}")
print(f"F1 Score: {result.f1_score:.3f}")
```

## Advanced: Creating Custom Configurations

For domain-specific comparisons, create custom configs:

```python
from ai4c_scribe.metadiff.models import MetadiffConfig, NormalizerConfig
from ai4c_scribe.metadiff.normalizers import (
    mask_timestamps,
    mask_version_numbers,
    normalize_whitespace,
)

# Config for database migration files
migration_config = MetadiffConfig(
    name="sql_migrations",
    description="SQL migration file comparison",
    normalizer=NormalizerConfig(
        mask_ids=False,
        ignore_patterns=[
            r"^--\s",                # Ignore SQL comments
            r"^\s*--\s",
        ],
        custom_normalizers=[
            mask_timestamps,         # Ignore timestamps in metadata
            mask_version_numbers,    # Ignore version bumps
            normalize_whitespace,    # Normalize spacing
        ],
    ),
    generate_visual=True,
)

# Use the custom config
from ai4c_scribe.metadiff import compare_diffs
result = compare_diffs(
    migration_human,
    migration_agent,
    config=migration_config,
    silent=False,
)
```

## Performance Notes

- **Speed**: Typically completes in < 100ms for diffs with 100s of changes
- **Memory**: O(n) where n = number of changes in diffs
- **Visual diff**: Requires `icdiff` binary (~100ms overhead, gracefully skipped if not installed)
- **HTML generation**: Included in visual diff cost

## Troubleshooting

### Issue: Visual diff not showing

**Cause**: `icdiff` not installed

**Solution**:
```bash
# icdiff is installed as part of metadiff dependencies
# If missing, install it:
pip install icdiff
# Or via brew on macOS:
brew install icdiff
```

### Issue: Similarity too low for very similar diffs

**Cause**: Not using appropriate normalization config

**Solution**:
```python
# Use OBO config for ontology files
result = compare_diffs(diff1, diff2, config=get_config("obo"))

# Or create custom config that ignores your domain-specific variations
```

### Issue: "icdiff not available" in HTML output

**Cause**: `icdiff` command not in PATH

**Solution**: Metadiff gracefully falls back to text-only comparison. Install `icdiff` to get HTML.

## Testing

Run the test suite:

```bash
# All metadiff tests
just pytest tests/metadiff/

# With doctests
just doctest src/ai4c_scribe/metadiff/

# Type checking
just mypy src/ai4c_scribe/metadiff/

# Full test suite including metadiff
just test
```

## Contributing

To add a new normalizer:

1. Add function to `src/ai4c_scribe/metadiff/normalizers.py`
2. Include comprehensive docstring with examples
3. Add tests to `tests/metadiff/test_normalizers.py` (create file if needed)
4. Use in a config or as custom normalizer

Example:
```python
def mask_ip_addresses(line: str) -> str:
    """Mask IPv4 and IPv6 addresses.

    Example:
        >>> mask_ip_addresses("server: 192.168.1.1")
        'server: IP_ADDRESS'
    """
    import re
    line = re.sub(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP_ADDRESS", line)
    return line
```

## References

- **Jaccard similarity**: https://en.wikipedia.org/wiki/Jaccard_index
- **F1 score**: https://en.wikipedia.org/wiki/F-score
- **Precision and Recall**: https://en.wikipedia.org/wiki/Precision_and_recall
- **icdiff**: https://www.jefftk.com/icdiff
