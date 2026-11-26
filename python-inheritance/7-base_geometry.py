#!/usr/bin/python3
"""Defines a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raises an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Booleans are rejected even though bool is a subclass of int.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
