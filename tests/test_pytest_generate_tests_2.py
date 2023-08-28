
import pytest

def test_subtraction(subtraction_function, subtraction_input):
    a, b, expected = subtraction_input
    result = subtraction_function(a, b)
    assert result == expected, f"Expected {expected}, but got {result}"
