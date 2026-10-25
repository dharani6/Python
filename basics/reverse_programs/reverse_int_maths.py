"""    psedo_code =1. Initialize a variable `result` to 0 to store the reversed number.
2. While   `n` is greater than 0:
   a. Get the last digit of `n` using `n % 10` and store it in a variable `digit`.
   b. Update `result` by multiplying it by 10 and adding `digit` to it.
   c. Remove the last digit from `n` by performing integer division `n //= 10`.
3. Return `result` as the reversed integer. """

import logging

logger = logging.getLogger(__name__)


def reverse_integer(n):
    """
    Reverse an integer using mathematical operations.

    Reverse the digits of an integer without converting it to a string.
    Negative numbers are handled by reversing the absolute value and applying
    the original sign.

    Examples:
        reverse_integer(12345) -> 54321
        reverse_integer(1000) -> 1
        reverse_integer(-123) -> -321

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """

    if not isinstance(n, int):
        raise TypeError("reverse_integer() expects an integer value")

    result = 0
    if n < 0:
        return -reverse_integer(-n)  # Handle negative numbers by reversing the positive part and negating the result

    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10
        logger.debug(
            "Processed digit=%s, intermediate_result=%s, remaining=%s",
            digit,
            result,
            n,
        )
    return result

if __name__ == "__main__":
    print("Function docstring:\n")
    print(reverse_integer.__doc__)
    print("\nExample outputs:\n")
    print(reverse_integer(12345))
    print(reverse_integer(987654321))
    print(reverse_integer(1000))
    print(reverse_integer(0))
    print(reverse_integer(-12345))
