#!/usr/bin/python3
"""Defines a function that lists the attributes of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of obj."""
    return dir(obj)
