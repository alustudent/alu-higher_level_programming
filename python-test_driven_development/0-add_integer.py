#!/usr/bin/python3
"""
This module defines add_integer, which adds two numbers.
Floats are cast to integers before the addition.
Any other type raises a TypeError.
"""


def add_integer(a, b=98):
    """Returns the integer sum of a and b.
    Raises TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
