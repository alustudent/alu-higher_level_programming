#!/usr/bin/python3
"""Defines MyInt, an int with inverted == and != operators."""


class MyInt(int):
    """A rebel int whose == and != operators are swapped."""

    def __eq__(self, other):
        """Returns True when the values differ."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Returns True when the values are equal."""
        return int.__eq__(self, other)
