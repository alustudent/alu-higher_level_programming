#!/usr/bin/python3
"""Defines a function that prints the content of a text file."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
