# app/operations.py

def power(a: int, b: int) -> int:
    """Computes a raised to the power of b."""
    return a ** b


def fibonacci(n: int) -> int:
    """Returns the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci number cannot be computed for negative index.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def factorial(n: int) -> int:
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def addition(a, b) :
    """Returns the sum of a and b."""
    return a + b