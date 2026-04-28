"""Visual diff generation using icdiff.

Generates side-by-side colored diffs and converts ANSI colors to HTML
for web display.

Example:
    >>> from ai4c_scribe.metadiff.visual import generate_visual_diff
    >>> from ai4c_scribe.metadiff.configs import GENERIC_CONFIG
    >>> ansi, html = generate_visual_diff("+a", "+b", GENERIC_CONFIG, silent=True)
    >>> "<pre" in html
    True
"""

import re
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

from ai4c_scribe.metadiff.models import MetadiffConfig


def generate_visual_diff(
    diff1: str,
    diff2: str,
    config: MetadiffConfig,
    silent: bool = False,
) -> tuple[str, str]:
    """Generate visual diff using icdiff.

    Creates temporary files, runs icdiff subprocess, captures ANSI output,
    converts to HTML.

    Args:
        diff1: First diff as string
        diff2: Second diff as string
        config: Configuration (uses icdiff_args)
        silent: If True, don't print to console

    Returns:
        Tuple of (ansi_text, html_text)

    Side effect:
        Prints colored diff to console unless silent=True

    Example:
        >>> from ai4c_scribe.metadiff.configs import GENERIC_CONFIG
        >>> ansi, html = generate_visual_diff(
        ...     "+foo\\n-bar",
        ...     "+foo\\n-baz",
        ...     GENERIC_CONFIG,
        ...     silent=True,
        ... )
        >>> "<pre" in html
        True

    Graceful degradation:
        If icdiff not installed, returns ("icdiff not available", "")
    """
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            tmpf1 = tmpdir_path / "diff1.diff"
            tmpf2 = tmpdir_path / "diff2.diff"

            tmpf1.write_text(diff1)
            tmpf2.write_text(diff2)

            # Build icdiff command
            cmd = ["icdiff", str(tmpf1), str(tmpf2)] + config.icdiff_args

            # Run icdiff and capture output
            result = subprocess.run(
                cmd,
                check=False,
                capture_output=True,
                text=True,
            )

            ansi_output = result.stdout

            # Print to console if not silent
            if not silent:
                print(ansi_output)

            # Convert ANSI to HTML
            html_output = ansi_to_html(ansi_output)

            return ansi_output, html_output

    except FileNotFoundError:
        # icdiff not installed
        return "icdiff not available", ""
    except Exception as e:
        # Other errors
        return f"Error generating visual diff: {e}", ""


def ansi_to_html(text: str) -> str:
    """Convert ANSI escape sequences to HTML with inline styles.

    Maps ANSI color codes to CSS colors, handles bold/underline,
    and wraps in styled <pre> tag.

    Args:
        text: Text with ANSI escape codes (from icdiff output)

    Returns:
        HTML string with styled spans in <pre> wrapper

    Example:
        >>> html = ansi_to_html("\\x1b[32mgreen text\\x1b[0m")
        >>> "<pre" in html
        True
        >>> "color:" in html or "#" in html
        True

    ANSI color codes supported:
        - 30-37: Basic foreground colors
        - 90-97: Bright foreground colors
        - 40-47: Basic background colors
        - 100-107: Bright background colors
        - 1: Bold
        - 4: Underline
        - 0: Reset
    """
    # ANSI to CSS color mappings
    color_map = {
        "30": "black",
        "31": "red",
        "32": "green",
        "33": "yellow",
        "34": "blue",
        "35": "magenta",
        "36": "cyan",
        "37": "white",
        "90": "#808080",        # bright black (gray)
        "91": "#ff6b6b",        # bright red
        "92": "#51cf66",        # bright green
        "93": "#ffd43b",        # bright yellow
        "94": "#74c0fc",        # bright blue
        "95": "#f06292",        # bright magenta
        "96": "#22d3ee",        # bright cyan
        "97": "#f8f9fa",        # bright white
    }

    bg_color_map = {
        "40": "black",
        "41": "red",
        "42": "green",
        "43": "yellow",
        "44": "blue",
        "45": "magenta",
        "46": "cyan",
        "47": "white",
        "100": "#808080",       # bright black bg
        "101": "#ff6b6b",       # bright red bg
        "102": "#51cf66",       # bright green bg
        "103": "#ffd43b",       # bright yellow bg
        "104": "#74c0fc",       # bright blue bg
        "105": "#f06292",       # bright magenta bg
        "106": "#22d3ee",       # bright cyan bg
        "107": "#f8f9fa",       # bright white bg
    }

    def replace_ansi(match):
        """Replace ANSI escape code with HTML span."""
        codes = match.group(1).split(";")
        styles = []

        for code in codes:
            if code == "0" or code == "":
                # Reset
                return "</span>"
            elif code == "1":
                # Bold
                styles.append("font-weight: bold")
            elif code == "4":
                # Underline
                styles.append("text-decoration: underline")
            elif code in color_map:
                # Foreground colors
                styles.append(f"color: {color_map[code]}")
            elif code in bg_color_map:
                # Background colors
                styles.append(f"background-color: {bg_color_map[code]}")

        if styles:
            return f'<span style="{"; ".join(styles)}">'

        return ""

    # Match ANSI escape sequences: \033[...m or \x1b[...m
    ansi_pattern = r"\033\[([0-9;]*)m|\x1b\[([0-9;]*)m"
    html_text = re.sub(ansi_pattern, lambda m: replace_ansi(m), text)

    # Wrap in pre tag with dark theme
    return (
        '<pre style="background-color: #1e1e1e; '
        'color: #d4d4d4; padding: 10px; '
        'font-family: monospace; overflow-x: auto;">'
        f"{html_text}</pre>"
    )
