"""
Reverse a string in Python using slicing.

This example shows how to get the reverse of a string using the slice
syntax `s[start:stop:step]` with a negative step value.

How it works:
- `s[::-1]` means:
  - start from the end of the string
  - go backwards one character at a time
  - stop when the beginning is reached

Time complexity:
- O(n), where n is the length of the string. Python must visit each character once.

Space complexity:
- O(n), because reversing creates a new string of the same length.

Example:
- Input  : "upskill"
- Output : "llikspu"
"""

s = "upskill"
reversed_s = s[::-1]
print(reversed_s)

# Input  : "upskill"
# Output : "llikspu"