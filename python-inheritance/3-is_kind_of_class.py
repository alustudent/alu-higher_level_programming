#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or of a subclass."""
    return isinstance(obj, a_class)
