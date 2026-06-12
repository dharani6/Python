"""reverse01.py

Examples of reversing a sequence in-place using the two-pointer technique.

This file contains two implementations that operate on mutable sequences
(lists). The comments and docstrings include interview-style explanations
and common follow-ups a beginner might be asked.

Key ideas covered here:
- Two-pointer technique (swap from both ends and move inward)
- In-place reversal (O(1) extra space) for mutable sequences
- Handling immutable types (strings) by converting to a list first
- Complexity analysis and common interview follow-ups
"""

from typing import List, Any


def reverse_string_for(s: List[Any]) -> List[Any]:
        """Reverse a list in-place using a for-loop and two pointers.

        Parameters
        - s: a mutable sequence (list) of items. Typical interview examples use
            `List[str]` for characters or `List[int]` for numbers; this accepts any.

        Returns
        - The same list object `s`, reversed in-place.

        Why this works (short):
        - We maintain two pointers `left` and `right` at the ends of the list.
        - On each step we swap the elements at those pointers and move them
            closer. After floor(n/2) swaps the list is reversed.

        Complexity:
        - Time: O(n) — each element is moved at most once (n/2 swaps).
        - Space: O(1) extra space — swaps are done in-place.

        Interview follow-ups answered here:
        - Q: Why O(n) rather than O(n/2)? A: Big-O ignores constant factors; n/2
            is still O(n).
        - Q: Can we reverse a Python `str` this way? A: No — strings are immutable.
            Convert to a list of characters first (e.g., `list(s)`) then reverse.
        - Q: Is this stable? Stability applies to sorting; reversing preserves
            relative duplicates but 'stable' isn't meaningful here.
        """

        len_s = len(s) # let l be the length of the list
        left = 0
        right = len_s - 1
        # We only need to iterate half the list; each iteration swaps two items.
        for _ in range(len_s // 2):
                # swap values at left and right
                s[left], s[right] = s[right], s[left]
                # move pointers inward
                left += 1
                right -= 1

        return s


def reverse_string_while(s: List[Any]) -> List[Any]:
        """Reverse a list in-place using a while-loop and two pointers.

        This function shows the same two-pointer idea but uses a while loop.
        The behavior, complexity, and usage notes are the same as
        `reverse_string_for`.
        """

        len_s = len(s)
        left = 0
        right = len_s - 1
        # Continue until pointers meet or cross
        while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return s


if __name__ == "__main__":
        # Example demonstrating how to use these functions.
        # Note: strings are immutable, so convert to list first.
        s = "Dharani"
        # Convert to a list of characters to reverse in-place
        result = reverse_string_for(list(s))
        print("Value of result:", result)
        print("After joining result list:", ''.join(result))

        # reversing a list of integers works directly
        lst = [1, 2, 3, 4, 5]
        print(reverse_string_for(lst))

        print("\nTesting with while loop")
        result = reverse_string_while(list("Python"))
        print("Value of result:", result)
        print("After joining result list:", ''.join(result))
        lst = [10, 20, 30, 40, 50]
        print(reverse_string_while(lst))

        try:
            # This will raise an error because strings are immutable
            reverse_string_for("Immutable")
        except TypeError as e:
               print("Error reversing string directly:", e)
        try:
               int_values = reverse_string_for(12345)  # This will raise an error because integers are not sequences
        except TypeError as e:
               print("Error reversing integer directly:", e)

"""
FAQ / Common interview prompts (brief answers):

- Q: How would you reverse a string in-place?  
    A: You cannot for immutable strings; convert to list first or build a new
    string by joining reversed characters.

- Q: Other ways to reverse in Python?  
    A: Use slicing `s[::-1]` (creates a new sequence), `reversed()` + `join`, or
    use recursion for exercise purposes (less efficient / more stack usage).

- Q: How to reverse only a subrange?  
    A: Apply the two-pointer swap to indices `i`..`j` instead of 0..n-1.

- Q: How to check if a string is a palindrome?  
    A: Compare characters symmetrically (`s[i] == s[n-1-i]`) or check
    `s == s[::-1]` for simple cases.

Complexity summary:
| Metric  | Value |
|--------:|:-----:|
| Time    | O(n)  |
| Space   | O(1) extra (in-place) |

"""

print("********Reverse Problem Memory Trick ********")
"""
Reverse
    |
    +-- Two Pointer
    +-- Stack
    +-- Recursion
    +-- Slicing
    +-- Built-in
    +-- Loop

"""

print("********Method 1 slicing ********")
s = "Dharani"
print(s[::-1])   # slicing creates a new string in reverse order
print("********Method 2 reversed() ********")
print(''.join(reversed(s)))  # reversed() returns an iterator, join to create a new string
print("********Method 3 Two Pointer (in-place) ********")   

l, r = 0, len(s) -1
s = list(s)  # Convert string to list to allow in-place modification
while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1
print(s)  # 
print(''.join(s))
print("********Method 4 Stack ********")
s = "Dharani"
stack = []
for char in s:
      stack.append(char)
result = ''
while stack:
      result += stack.pop()
print(result)  # Remove leading space added at initialization

print("********Method 5  ********")

s = "Dharani"
def reverse_string_M5(s):
    result = ''
    for char in s:
          result = char + result  # Prepend character to result
    return result
result = reverse_string_M5(s)
result_int = reverse_string_M5(str(12345))
print(result, result_int)  
"""
if we use int This will raise an error because integers are not iterable and cannot
be reversed directly. We need to convert the integer to a string first, 
which is done in the code by using `str(12345)`.
The output will be '54321' for the string and '54321' for the integer after conversion.
"""
def reverse_string_M5_while(s):
    result = ''
    index = 0
    while index < len(s):
          result = s[index] + result  # Prepend character to result
          index += 1
    return result

print("********Method 6 Recursion ********")
s = "Dharani"
def recursive_reverse(s):
       if len(s) == 0:
                return s
       return recursive_reverse(s[1:]) + s[0]  # Move first character to the end after reversing the rest
result = recursive_reverse(s)
print(result)  # 
result_int = recursive_reverse(str(12345))
print(result_int)  #

print("********Method 7 for loop ********")

s = "Dharani"
result = ""
for i in range(len(s)-1, -1, -1):
       print(f"Index: {i}, Character: {s[i]}, Current result: '{result}'")
       result = result + s[i]  # Append characters in reverse order
print(result)  # 


print("********Testing with for forward loop********")
s = "Python"
result = ''
for char in range(len(s)):
       result = s[char] + result  # Prepend character to result
print(result)  # 

print("********Testing with while loop********")
s = "Python"
result = ''
index = 0
while index < len(s):
       result = s[index] + result  # Prepend character to result
       index += 1
print(result)  # 

print("********Testing with reduce functional programing********")

from functools import reduce
s = "Dharani"
reverse  = reduce( lambda x,y: y + x, s)
print(reverse)  #


print("******** List reverse method ********")

lst = [1, 2, 3, 4, 5]
lst.reverse()  # This modifies the list in-place
print(lst)  # Output: [5, 4, 3, 2, 1] in-place reversal
s = "Dharani"
try:
    s.reverse()
except AttributeError as e:
    print(s, "Error reversing string with list method:", e)  # 
print(s)
print("********reversed iterator using reversed() ********")
s = "Dharani"
print(list(reversed(s)))  # This returns a list of characters in reverse order
print(''.join(reversed(s)))  # This joins the reversed characters into a new string
