#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raises an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")
