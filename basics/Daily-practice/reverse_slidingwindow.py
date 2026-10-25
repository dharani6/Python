"""Reverse a string using slicing and explain the technique.

This example shows how to reverse text with Python slice notation.
It also contains a reusable function, detailed comments, and a docstring
so the concept is easier to remember later.
"""

from __future__ import annotations


def reverse_string(text: str) -> str:
    """Return a reversed copy of the given string.

    Uses Python slice notation with a step of -1 to traverse the string
    from the end back to the beginning.

    Args:
        text: The original string to reverse.

    Returns:
        The reversed string.

    Complexity:
        Time: O(n) because the slice operation iterates through all n
            characters of the input string once.
        Space: O(n) because slicing creates a new string of the same length
            as the original.
    """
    # [start:stop:step] with step=-1 means "iterate backwards".
    # Since start and stop are omitted, Python reads the entire string in reverse.
    return text[::-1]


if __name__ == "__main__":
    sample = "UPSKILL"
    reversed_sample = reverse_string(sample)

    print("Original string:", sample)
    print("Reversed string:", reversed_sample)
