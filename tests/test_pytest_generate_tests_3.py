
import pytest

# Math operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# List of operations
operations = [
    add,
    subtract,
    multiply,
    divide
]

# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    if "operation" in metafunc.fixturenames:
        metafunc.parametrize("operation", operations)


def test_math_operations(operation):
    if operation == add:
        result = operation(3, 5)
        assert result == 8
    elif operation == subtract:
        result = operation(10, 3)
        assert result == 7
    elif operation == multiply:
        result = operation(4, 6)
        assert result == 24
    elif operation == divide:
        result = operation(15, 3)
        assert result == 5
