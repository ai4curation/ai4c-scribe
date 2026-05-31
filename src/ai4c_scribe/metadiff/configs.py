"""Pre-built configurations for domain-specific diff comparison.

Provides preset configurations for common domains (OBO ontologies, Python code, etc.)
that can be passed to compare_diffs() or referenced by name in the CLI.

Example:
    >>> from ai4c_scribe.metadiff.configs import get_config
    >>> config = get_config("obo")
    >>> config.normalizer.mask_ids
    True
    >>> list_configs()
    ['generic', 'obo', 'python', 'strict']
"""

from ai4c_scribe.metadiff.models import MetadiffConfig, NormalizerConfig
from ai4c_scribe.metadiff.normalizers import (
    mask_timestamps,
    mask_version_numbers,
)


# Generic: minimal normalization
GENERIC_CONFIG = MetadiffConfig(
    name="generic",
    description="Generic diff comparison with minimal normalization",
    normalizer=NormalizerConfig(
        mask_ids=False,
        strip_whitespace=True,
        ignore_patterns=[],
        ignore_keys=[],
    ),
)

# OBO: ontology files (based on ontobench implementation)
OBO_CONFIG = MetadiffConfig(
    name="obo",
    description="OBO ontology file comparison (GO, HP, etc.)",
    normalizer=NormalizerConfig(
        mask_ids=True,  # Mask CURIE IDs: GO:0000001 -> GO:NNNNNNN
        strip_whitespace=True,
        ignore_keys=[
            "created_by",
            "creation_date",
            "property_value: dcterms-date",
            "relationship: dc-contributor",
        ],
        custom_normalizers=[mask_timestamps, mask_version_numbers],
    ),
)

# Python: code files
PYTHON_CONFIG = MetadiffConfig(
    name="python",
    description="Python code comparison",
    normalizer=NormalizerConfig(
        mask_ids=False,
        strip_whitespace=True,
        ignore_patterns=[
            r"^\s*#.*",  # Comments (full line)
            r"^\s*$",    # Empty lines
        ],
        custom_normalizers=[],
    ),
)

# OWL: ontology files in OWL functional syntax (CL, etc.)
OWL_CONFIG = MetadiffConfig(
    name="owl",
    description="OWL functional syntax ontology comparison (CL, etc.)",
    normalizer=NormalizerConfig(
        mask_ids=True,  # Mask CURIEs: obo:CL_4052071 -> obo:CL_NNNNNNN
        strip_whitespace=True,
        ignore_keys=[
            "terms:date",           # creation timestamps
            "terms:contributor",    # contributor ORCIDs
            "dc:date",             # Dublin Core dates
            "dcterms:date",        # Dublin Core terms dates
        ],
        ignore_patterns=[
            r".*xsd:dateTime.*",   # Any dateTime annotation
        ],
        custom_normalizers=[mask_timestamps, mask_version_numbers],
    ),
)

# Strict: no normalization
STRICT_CONFIG = MetadiffConfig(
    name="strict",
    description="Strict comparison with no normalization",
    normalizer=NormalizerConfig(
        mask_ids=False,
        strip_whitespace=False,
        ignore_patterns=[],
        ignore_keys=[],
        case_insensitive=False,
    ),
)

# Registry of all available configurations
CONFIG_REGISTRY = {
    "generic": GENERIC_CONFIG,
    "obo": OBO_CONFIG,
    "owl": OWL_CONFIG,
    "python": PYTHON_CONFIG,
    "strict": STRICT_CONFIG,
}


def get_config(name: str) -> MetadiffConfig:
    """Get a preset configuration by name.

    Args:
        name: Configuration name (must exist in CONFIG_REGISTRY)

    Returns:
        MetadiffConfig instance

    Raises:
        KeyError: If configuration name not found

    Example:
        >>> config = get_config("obo")
        >>> config.name
        'obo'

    Available configs:
        - 'generic': Minimal normalization
        - 'obo': OBO ontology files (masks IDs, ignores metadata)
        - 'python': Python code (ignores comments)
        - 'strict': No normalization

    """
    if name not in CONFIG_REGISTRY:
        available = ", ".join(CONFIG_REGISTRY.keys())
        raise KeyError(
            f"Unknown config '{name}'. Available: {available}"
        )

    return CONFIG_REGISTRY[name]


def list_configs() -> list[str]:
    """List all available configuration names.

    Returns:
        List of configuration names in sorted order

    Example:
        >>> configs = list_configs()
        >>> "obo" in configs
        True
        >>> len(configs) >= 3
        True
    """
    return sorted(CONFIG_REGISTRY.keys())
