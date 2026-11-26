#!/usr/bin/python3
"""Defines a function that builds an object out of a JSON string."""
import json


def from_json_string(my_str):
    """Returns the Python object represented by the JSON string my_str."""
    return json.loads(my_str)
