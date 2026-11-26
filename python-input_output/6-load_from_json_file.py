#!/usr/bin/python3
"""Defines a function that creates an object out of a JSON file."""
import json


def load_from_json_file(filename):
    """Returns the Python object stored as JSON in filename."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
