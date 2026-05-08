#!/usr/bin/env python3
"""Validate alternating rhyme scheme (ABAB) in poems."""
import sys


def get_ending(word):
    """Get the phonetic ending of a word (simplified)."""
    word = word.lower().strip(".,!?;:'\"")
    for suffix in ['ight', 'ound', 'tion', 'ing', 'ness', 'ful', 'ous', 'ate', 'ine', 'ore', 'ue', 'ow', 'ay', 'ee', 'oo']:
        if word.endswith(suffix):
            return suffix
    return word[-3:] if len(word) >= 3 else word


def get_last_word(line):
    words = line.strip().split()
    return words[-1] if words else ""


def check_rhyme(word1, word2):
    return get_ending(word1) == get_ending(word2)


def validate_poem(text):
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    if len(lines) < 4:
        print("FAILED: Poem too short for ABAB pattern (need 4+ lines)")
        return False

    errors = []
    for i in range(0, len(lines) - 2, 2):
        w1, w2 = get_last_word(lines[i]), get_last_word(lines[i + 2])
        if not check_rhyme(w1, w2):
            errors.append(f"Lines {i + 1} and {i + 3} don't rhyme: '{w1}' / '{w2}'")

    for i in range(1, len(lines) - 2, 2):
        w1, w2 = get_last_word(lines[i]), get_last_word(lines[i + 2])
        if not check_rhyme(w1, w2):
            errors.append(f"Lines {i + 1} and {i + 3} don't rhyme: '{w1}' / '{w2}'")

    if errors:
        print("FAILED: Rhyme validation errors:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("PASSED: ABAB rhyme pattern confirmed")
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    sys.exit(0 if validate_poem(text) else 1)
