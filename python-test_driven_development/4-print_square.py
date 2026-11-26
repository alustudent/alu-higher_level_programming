#!/usr/bin/python3
"""This module defines print_square, which prints a square of # characters."""


def print_square(size):
    """Prints a square of side size with the character #.

    Raises TypeError if size is not an integer (including negative floats)
    and ValueError if size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
