#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes text to a UTF8 file, overwriting it, and returns the count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
