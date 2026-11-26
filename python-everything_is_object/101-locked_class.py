#!/usr/bin/python3
"""Defines LockedClass, which only allows a first_name attribute."""


class LockedClass:
    """Allows only first_name as a dynamic instance attribute."""
    __slots__ = ["first_name"]
