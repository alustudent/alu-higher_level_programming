#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Returns the attributes of obj as a dictionary for JSON serialization."""
    return obj.__dict__
