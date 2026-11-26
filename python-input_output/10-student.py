#!/usr/bin/python3
"""Defines a Student class with filtered dictionary descriptions."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student's names and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of the student's attributes.

        When attrs is a list of strings, only those attributes are kept.
        """
        if (isinstance(attrs, list) and
                all(isinstance(name, str) for name in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
