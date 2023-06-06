#!/usr/bin/python3


"""
This module contains a function that adds two numbers.
"""


def add_integer(a, b=98):
    """Add two integer or float numbers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number. Defaults to 98.

    Returns:
        The sum of the two numbers.

    Raises:
        TypeError: If a or b are not integer or float numbers.

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b

