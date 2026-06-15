"""
Reverse a dictionary's items in Python and explain the approach for new learners.

This example shows how to produce a new dictionary whose insertion order
is the reverse of the original dictionary's insertion order. We use
`reversed(d.items())` to iterate the key/value pairs in reverse, and
`dict(...)` to build a new dictionary from that sequence.

How it works:
- `d.items()` returns a view of the dictionary's (key, value) pairs.
- `reversed(d.items())` returns those pairs from last inserted to first.
- `dict(reversed(d.items()))` consumes the reversed pairs and constructs
	a new dictionary where iteration order matches that reversed sequence.

Example:
- Input  : {"a": 1, "b": 2, "c": 3}
- Output : {"c": 3, "b": 2, "a": 1}

Time complexity:
- O(n) where n is the number of items — each item is visited once.

Space complexity:
- O(n) because a new dictionary is created to hold the reversed items.

Useful info:
- Dictionaries preserve insertion order in Python 3.7+ (CPython 3.6 implemented it
	as an implementation detail). Relying on order in older Python versions is unsafe.
- `reversed(d)` or `reversed(d.items())` lets you iterate in reverse without
	creating a new dictionary; use that if you only need to loop over items.
- If you need an in-place reversal of order for structures that support it,
	convert to a list, reverse it, and (if needed) rebuild the dict: 
	`pairs = list(d.items()); pairs.reverse(); d2 = dict(pairs)`.
"""

d = {"a": 1, "b": 2, "c": 3}
result = dict(reversed(d.items()))
print(result)

# Input  : {"a": 1, "b": 2, "c": 3}
# Output : {"c": 3, "b": 2, "a": 1}