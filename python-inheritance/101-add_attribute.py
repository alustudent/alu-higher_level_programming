#!/usr/bin/python3
"""Defines a function that adds an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Sets attribute name to value on obj.

    Raises a TypeError when obj can't hold new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
