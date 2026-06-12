"""reverse.py

Utility functions for reversing mutable sequences (lists).

This module focuses on clear, well-documented functions you can import
and test. Keep these functions small and focused so they map cleanly
to equivalent concepts in Go (slices and in-place swaps).
"""

from typing import List, Any


def reverse_for(s: List[Any]) -> List[Any]:
    """Reverse a list in-place using a for-style loop (two-pointer).

    Usage:
    >>> lst = [1, 2, 3]
    >>> reverse_for(lst)
    [3, 2, 1]

    Notes:
    - Operates in-place and returns the same list for convenience.
    - Works only on mutable sequences (lists). Strings are immutable.
    """

    n = len(s)
    left = 0
    right = n - 1
    for _ in range(n // 2):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def reverse_while(s: List[Any]) -> List[Any]:
    """Reverse a list in-place using a while-loop (two-pointer).

    The behavior and complexity are the same as `reverse_for` — this
    simply demonstrates an alternate loop style.
    """

    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
