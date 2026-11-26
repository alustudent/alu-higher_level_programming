#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends text to a UTF8 file and returns the number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
