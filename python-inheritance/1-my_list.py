#!/usr/bin/python3
"""Defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list with a method to print its elements in ascending order."""

    def print_sorted(self):
        """Prints the list sorted in ascending order, without changing it."""
        print(sorted(self))
