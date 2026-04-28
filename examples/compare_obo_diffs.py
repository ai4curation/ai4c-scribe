#!/usr/bin/env python3
"""
Example script: Compare OBO ontology diffs using metadiff.

Shows different ways to:
1. Use the built-in OBO config
2. Load custom config from JSON/YAML files
3. Compare diffs from files or strings
4. Access and interpret metrics
"""

from pathlib import Path
from ai4c_scribe.metadiff import compare_diffs, compare_diff_files, get_config
from ai4c_scribe.metadiff.models import MetadiffConfig, NormalizerConfig
import json
import sys


def example_1_builtin_config():
    """Example 1: Use built-in OBO config from registry."""
    print("=" * 70)
    print("Example 1: Built-in OBO Config")
    print("=" * 70)

    # Get the built-in OBO config
    obo_config = get_config("obo")
    print(f"Config: {obo_config.name}")
    print(f"Description: {obo_config.description}")
    print()

    # Sample diffs: same term, different IDs
    human_diff = """+[Term]
+id: GO:0000001
+name: biological_process
+def: "Process related to biology"
+created_by: alice
"""

    agent_diff = """+[Term]
+id: GO:0000999
+name: biological_process
+def: "Process related to biology"
+created_by: bob
"""

    result = compare_diffs(human_diff, agent_diff, config=obo_config, silent=True)

    print("Human diff (ID: GO:0000001, author: alice):")
    print(human_diff)
    print("\nAgent diff (ID: GO:0000999, author: bob):")
    print(agent_diff)
    print("\nMetrics:")
    print(f"  Similarity:  {result.similarity:.1%}")
    print(f"  F1 Score:    {result.f1_score:.1%}")
    print(f"  Identical:   {result.identical}")
    print(f"  Common:      {result.num_changes_in_common} changes")
    print(f"  Only in 1:   {result.num_changes_in_diff1} changes")
    print(f"  Only in 2:   {result.num_changes_in_diff2} changes")
    print("\nInterpretation:")
    print("  ✓ Similarity = 100% because:")
    print("    - IDs masked: GO:0000001 → GO:NNNNNNN")
    print("    - Metadata ignored: created_by (author difference)")
    print("    - Content identical: name and def match")
    print()


def example_2_load_from_json():
    """Example 2: Load custom OBO config from JSON file."""
    print("=" * 70)
    print("Example 2: Load Config from JSON File")
    print("=" * 70)

    config_file = Path(".metadiff-obo-config.json")
    if not config_file.exists():
        print(f"Note: {config_file} not found (created at root of repo)")
        return

    # Load JSON config
    with open(config_file) as f:
        config_dict = json.load(f)

    # Convert to MetadiffConfig object
    config = MetadiffConfig(**config_dict)

    print(f"Loaded config from: {config_file}")
    print(f"Config name: {config.name}")
    print(f"Description: {config.description}")
    print(f"Mask IDs: {config.normalizer.mask_ids}")
    print(f"Ignore keys: {len(config.normalizer.ignore_keys)}")
    print(f"Custom normalizers: {len(config.normalizer.custom_normalizers)}")
    print()


def example_3_load_from_yaml():
    """Example 3: Load custom OBO config from YAML file."""
    print("=" * 70)
    print("Example 3: Load Config from YAML File")
    print("=" * 70)

    try:
        import yaml
    except ImportError:
        print("Note: PyYAML not installed. Install with: uv add pyyaml")
        return

    config_file = Path("metadiff-obo-config.yaml")
    if not config_file.exists():
        print(f"Note: {config_file} not found (created at root of repo)")
        return

    # Load YAML config
    with open(config_file) as f:
        config_dict = yaml.safe_load(f)

    # Remove comments and convert to MetadiffConfig
    # (filter out keys starting with _)
    filtered = {k: v for k, v in config_dict.items() if not k.startswith("_")}
    config = MetadiffConfig(**filtered)

    print(f"Loaded config from: {config_file}")
    print(f"Config name: {config.name}")
    print(f"Description: {config.description[:100]}...")
    print()


def example_4_compare_files():
    """Example 4: Compare diff files using OBO config."""
    print("=" * 70)
    print("Example 4: Compare Diff Files")
    print("=" * 70)

    # Create sample diff files
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        human_file = tmpdir / "human-ontology.diff"
        agent_file = tmpdir / "agent-ontology.diff"

        human_file.write_text("""+[Term]
+id: GO:1000001
+name: new_process
+def: "A newly defined biological process"
+is_a: GO:0008150 ! biological_process
+created_by: jane
+creation_date: 2024-01-15
""")

        agent_file.write_text("""+[Term]
+id: GO:9999999
+name: new_process
+def: "A newly defined biological process"
+is_a: GO:0008150 ! biological_process
+created_by: agent
+creation_date: 2024-01-20
""")

        result = compare_diff_files(
            human_file,
            agent_file,
            config=get_config("obo"),
            silent=True,
        )

        print(f"Compared: {human_file.name} vs {agent_file.name}")
        print(f"Config: {result.config_name}")
        print()
        print(f"Similarity:  {result.comparison.similarity:.1%}")
        print(f"F1 Score:    {result.comparison.f1_score:.1%}")
        print(f"Precision:   {result.comparison.precision:.1%}")
        print(f"Recall:      {result.comparison.recall:.1%}")
        print()


def example_5_custom_obo_config():
    """Example 5: Create and use a custom OBO config."""
    print("=" * 70)
    print("Example 5: Custom OBO Config")
    print("=" * 70)

    from ai4c_scribe.metadiff.normalizers import (
        mask_timestamps,
        mask_version_numbers,
    )

    # Create custom config for strict OBO comparison
    # (also ignores relationship line order changes)
    custom_config = MetadiffConfig(
        name="obo_strict",
        description="Strict OBO comparison: ignore author/date but NOT definitions",
        normalizer=NormalizerConfig(
            mask_ids=True,
            ignore_keys=[
                "created_by",
                "creation_date",
                "property_value: dcterms-date",
            ],
            ignore_patterns=[
                r"^relationship:.*dc-contributor",  # Ignore contributor relationships
            ],
            custom_normalizers=[mask_timestamps, mask_version_numbers],
        ),
        generate_visual=True,
    )

    print(f"Custom config: {custom_config.name}")
    print(f"Description: {custom_config.description}")
    print(f"Mask IDs: {custom_config.normalizer.mask_ids}")
    print(f"Ignore keys: {custom_config.normalizer.ignore_keys}")
    print(f"Ignore patterns: {custom_config.normalizer.ignore_patterns}")
    print()


def example_6_interpret_metrics():
    """Example 6: Understand what the metrics mean."""
    print("=" * 70)
    print("Example 6: Understanding Metrics")
    print("=" * 70)

    # Create a partially matching diff
    human_diff = """+term1
+term2
+term3
-old_term
"""

    agent_diff = """+term1
+term2
+new_term
-old_term
"""

    result = compare_diffs(human_diff, agent_diff, silent=True)

    print("Human diff:  +term1, +term2, +term3, -old_term")
    print("Agent diff:  +term1, +term2, +new_term, -old_term")
    print()
    print("Metrics breakdown:")
    print(f"  Changes in common: {result.num_changes_in_common}")
    print(f"  Changes only in human: {result.num_changes_in_diff1}")
    print(f"  Changes only in agent: {result.num_changes_in_diff2}")
    print()
    print(f"  Similarity (Jaccard):  {result.similarity:.1%}")
    print(f"    = common / total unique")
    print(f"    = {result.num_changes_in_common} / {result.num_changes_in_common + result.num_changes_in_diff1 + result.num_changes_in_diff2}")
    print()
    print(f"  Precision:  {result.precision:.1%}")
    print(f"    = common / agent changes")
    print(f"    = {result.num_changes_in_common} / {result.num_changes_in_common + result.num_changes_in_diff2}")
    print(f"    = 'How many of agent's changes were correct?'")
    print()
    print(f"  Recall:     {result.recall:.1%}")
    print(f"    = common / human changes")
    print(f"    = {result.num_changes_in_common} / {result.num_changes_in_common + result.num_changes_in_diff1}")
    print(f"    = 'How many of human's changes did agent replicate?'")
    print()
    print(f"  F1 Score:   {result.f1_score:.1%}")
    print(f"    = Harmonic mean of precision and recall")
    print(f"    = Good overall quality metric")
    print()


def main():
    """Run all examples."""
    examples = [
        ("1", "Built-in OBO Config", example_1_builtin_config),
        ("2", "Load Config from JSON", example_2_load_from_json),
        ("3", "Load Config from YAML", example_3_load_from_yaml),
        ("4", "Compare Diff Files", example_4_compare_files),
        ("5", "Custom OBO Config", example_5_custom_obo_config),
        ("6", "Interpret Metrics", example_6_interpret_metrics),
    ]

    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        for num, title, func in examples:
            if num == example_num:
                func()
                return
        print(f"Unknown example: {example_num}")
        print(f"Usage: python {sys.argv[0]} [1-6]")
        sys.exit(1)

    # Run all examples
    for num, title, func in examples:
        try:
            func()
            print()
        except Exception as e:
            print(f"Error in {title}: {e}")
            print()


if __name__ == "__main__":
    main()
