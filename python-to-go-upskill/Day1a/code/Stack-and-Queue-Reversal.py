"""
Stack and queue reversal examples for new learners.

This file shows two common reversal techniques in Python:
- reversing a simple list used like a stack
- reversing a deque used like a queue

A stack is a last-in-first-out (LIFO) structure. The easiest reversal
for a stack-like list is using slicing with `[::-1]`.

A queue is a first-in-first-out (FIFO) structure. When using a deque,
calling `reverse()` changes the order of elements in place.
"""

# Stack reversal example
stack = [1, 2, 3, 4]
reversed_stack = stack[::-1]
print("Stack input :", stack)
print("Stack output:", reversed_stack)
# Output: [4, 3, 2, 1]

# Queue reversal example using deque
from collections import deque
q = deque([1, 2, 3, 4])
q.reverse()
print("Queue input :", deque([1, 2, 3, 4]))
print("Queue output:", q)
# Output: deque([4, 3, 2, 1])

# Complexity:
# - Stack reversal with slicing: O(n) time, O(n) space because a new list is created.
# - Deque reversal with q.reverse(): O(n) time, O(1) extra space because it reverses in place.
#
# Useful info:
# - Lists are often used like stacks in Python because append/pop work well.
# - Deques are better for queues because they are efficient at both ends.
# - Use `stack[::-1]` for a quick reversed copy; use `reversed(stack)` if you only need to iterate backwards.
# - Use `deque.reverse()` when you want to change the queue order without creating a new object.
