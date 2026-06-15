"""
Reverse a list in Python using slicing.

This example is written for new learners.
The slice notation `lst[::-1]` reads the list from the end to the start,
using a negative step to move backwards through the list.

How it works:
- `lst[start:stop:step]` is the general slice form.
- When `start` and `stop` are omitted, Python uses the full list.
- A `step` of `-1` means move from right to left, one item at a time.

Example:
- Input  : [10, 20, 30, 40, 50]
- Output : [50, 40, 30, 20, 10]
"""

lst = [10, 20, 30, 40, 50]
reversed_lst = lst[::-1]
print(reversed_lst)

# Input  : [10, 20, 30, 40, 50]
# Output : [50, 40, 30, 20, 10]

# Complexity:
# - Time complexity: O(n)
#   The slice operation must visit each element once to build the reversed list.
# - Space complexity: O(n)
#   A new list is created to store the reversed elements.
#
# Useful info:
# - Slicing does not modify the original list; it returns a new list.
# - To reverse the list in place, use `lst.reverse()` instead.
# - For strings, the same idea works: `s[::-1]` reverses the characters.
