"""
Reverse a tuple in Python and explain the approach for new learners.

This example shows how to reverse a tuple using the built-in `reversed()`
function which returns an iterator yielding elements from last to first.
We wrap that iterator with `tuple()` to create a new tuple because tuples
are immutable (they cannot be modified in place).

How it works:
- `reversed(t)` returns an iterator over `t` in reverse order.
- `tuple(reversed(t))` consumes the iterator and returns a new tuple.

Example:
- Input  : (1, 2, 3, 4)
- Output : (4, 3, 2, 1)

Time complexity:
- O(n), where n is the number of elements. Each element is visited once.

Space complexity:
- O(n), because a new tuple of the same size is created.

Useful info:
- Tuples are immutable. If you need to reverse in-place-like, convert to a
	list first: `lst = list(t); lst.reverse(); t2 = tuple(lst)`.
- If you only need to iterate in reverse order and want to avoid creating
	a new tuple, use `reversed(t)` directly.
"""

t = (1, 2, 3, 4)
result = tuple(reversed(t))
print(result)

# Input  : (1, 2, 3, 4)
# Output : (4, 3, 2, 1)