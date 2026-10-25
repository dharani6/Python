"""Pytest template for testing basics.reverse_programs.reverse_int_maths.

Pseudocode for this test module:
1. Import the function you want to test from reverse_int_maths.py.
2. Write one test function for each important behavior:
   - reverse a normal positive integer
   - reverse zero
   - reverse a negative integer
   - reverse a number with trailing zeros
3. In each test:
   a. prepare input and expected output
   b. call the function
   c. assert that the returned value equals the expected output
4. Keep test names descriptive so failures are easy to understand.

This file documents the test plan and gives a clean pytest structure.
"""

# If your test run does not find the module, you may need to add the project root to PYTHONPATH.
# Example:
# import os, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from basics.reverse_programs.reverse_int_maths import reverse_integer


def test_reverse_integer_positive_number():
    """Reverse a positive integer and compare to the expected reversed value."""
    # Arrange
    value = 12345
    expected = 54321

    # Act
    result = reverse_integer(value)

    # Assert
    assert result == expected


def test_reverse_integer_zero():
    """Reversing zero should return zero."""
    value = 0
    expected = 0

    result = reverse_integer(value)

    assert result == expected


def test_reverse_integer_negative_number():
    """Negative numbers should preserve sign after reversing digits."""
    value = -123
    expected = -321

    result = reverse_integer(value)

    assert result == expected


def test_reverse_integer_trailing_zeros():
    """Trailing zeros should disappear when the reversed value is returned."""
    value = 1000
    expected = 1

    result = reverse_integer(value)

    assert result == expected
