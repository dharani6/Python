# This file contains simple pytest tests demonstrating how assert statements work.
# Each test function name starts with "test_" so pytest will discover and run it.

def test_numbers():
    # Simple numeric comparisons
    assert 10 > 5          # True because 10 is greater than 5
    assert 7 != 8          # True because 7 is not equal to 8
    assert 4 + 6 == 10     # True because the sum of 4 and 6 equals 10
    assert not (3 > 5)     # True because 3 > 5 is False, so not False is True

def test_truth_value():
    # Truthiness of different values in Python
    assert True            # True is truthy
    assert 1               # non-zero integers are truthy
    assert not 0           # 0 is falsy, so not 0 is True
    assert bool("hello") # non-empty strings are truthy
    assert not bool("")  # empty string is falsy

def test_precedence():
    # Operator precedence in arithmetic expressions
    assert 3 - 1 * 4 / 2 == 1.0    # multiplication and division happen before subtraction
    assert (3 - 1) * (4 / 2) == 4.0 # parentheses change the order of evaluation
    assert (3 - 1) * 4 / 2 == 4.0   # left-to-right evaluation after parentheses
    assert 3 - 1 * 2 / 1 == 1.0     # multiplication and division first, then subtraction

def test_strings():
    # String comparisons and membership checks
    assert "abc" != "abcd"                        # strings with different lengths/content are not equal
    assert "py" in "the test is pytest"           # substring membership is True
    assert "put" not in "the test is pytest"      # substring does not appear in the string
    assert "test" in "this is a test"             # the word "test" is present
    assert "rdh" in "dharani"                     # substring match in a string

def test_divmod():
    # Using divmod() to return quotient and remainder
    assert divmod(9, 5) == (1, 4)   # 9 // 5 is 1, 9 % 5 is 4
    assert divmod(10, 3) == (3, 1)  # 10 // 3 is 3, 10 % 3 is 1
    assert divmod(8, 4) == (2, 0)   # 8 divides evenly by 4
    assert divmod(8, 3) == (2, 1)   # remainder is 1 for 8 divided by 3