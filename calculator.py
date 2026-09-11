"""Calculator program with basic arithmetic, exponent, logarithmic, and trigonometric functions."""


import math


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def exponent(base: float, exp: float) -> float:
    """Return base raised to the power of exp."""
    return base ** exp


def logarithmic(value: float, base: float = math.e) -> float:
    """Return the logarithm of value with the given base (default: natural log).

    Raises:
        ValueError: If value is less than or equal to 0.
        ValueError: If base is less than or equal to 0 or equal to 1.
    """
    if value <= 0:
        raise ValueError("Value must be greater than 0 for logarithm.")
    if base <= 0 or base == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1.")
    return math.log(value, base)


def sine(angle: float) -> float:
    """Return the sine of angle (in radians)."""
    return math.sin(angle)


def cosine(angle: float) -> float:
    """Return the cosine of angle (in radians)."""
    return math.cos(angle)


def tangent(angle: float) -> float:
    """Return the tangent of angle (in radians)."""
    return math.tan(angle)


if __name__ == "__main__":
    # Demo the functions
    print("=== Calculator Demo ===")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"divide(6, 3) = {divide(6, 3)}")
    print(f"exponent(2, 3) = {exponent(2, 3)}")
    print(f"logarithmic(100, 10) = {logarithmic(100, 10)}")
    print(f"ln(1) = {logarithmic(1)}")
    print(f"sine(0) = {sine(0)}")
    print(f"cosine(0) = {cosine(0)}")
    print(f"tangent(0) = {tangent(0)}")