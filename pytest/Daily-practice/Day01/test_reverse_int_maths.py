import logging
import time

import pytest

from basics.reverse_programs.reverse_int_maths import reverse_integer

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)


""" Write one test function for each important behavior:
   - reverse a normal positive integer
   - reverse zero
   - reverse a negative integer
   - reverse a number with trailing zeros
   - reverse a single-digit integer
   - raise TypeError for invalid input
"""

def log_test_case(value, expected, result, elapsed):
    logger.info(
        "INPUT=%r EXPECTED=%r RESULT=%r DURATION=%.6fs",
        value,
        expected,
        result,
        elapsed,
    )


def test_reverse_a_normal_positive_integer():
    value = 12345
    expected = 54321
    start = time.perf_counter()
    result = reverse_integer(value)
    duration = time.perf_counter() - start
    log_test_case(value, expected, result, duration)
    assert result == expected


def test_reverse_zero():
    value = 0
    expected = 0
    start = time.perf_counter()
    result = reverse_integer(value)
    duration = time.perf_counter() - start
    log_test_case(value, expected, result, duration)
    assert result == expected


def test_reverse_a_negative_integer():
    value = -9840288973
    expected = -3798820489
    start = time.perf_counter()
    result = reverse_integer(value)
    duration = time.perf_counter() - start
    log_test_case(value, expected, result, duration)
    assert result == expected


def test_reverse_a_number_with_trailing_zeros():
    value = 1000
    expected = 1
    start = time.perf_counter()
    result = reverse_integer(value)
    duration = time.perf_counter() - start
    log_test_case(value, expected, result, duration)
    assert result == expected


def test_reverse_single_digit_number():
    value = 7
    expected = 7
    start = time.perf_counter()
    result = reverse_integer(value)
    duration = time.perf_counter() - start
    log_test_case(value, expected, result, duration)
    assert result == expected


def test_reverse_non_integer_raises_type_error():
    value = "123"
    expected = TypeError
    start = time.perf_counter()
    with pytest.raises(TypeError):
        reverse_integer(value)
    duration = time.perf_counter() - start
    logger.info(
        "INPUT=%r EXPECTED=%s RESULT=%s DURATION=%.6fs",
        value,
        expected.__name__,
        expected.__name__,
        duration,
    )

    