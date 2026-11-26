#!/usr/bin/python3
"""This module defines text_indentation, which splits text into paragraphs."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'.

    Spaces at the beginning and end of each printed line are removed.
    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip(), end="\n\n")
            line = ""
    print(line.strip(), end="")
