#!/usr/bin/python3
"""Defines a Square class comparable by area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size, which must be a number >= 0."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compares areas for equality."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares areas for inequality."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Returns True if this area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Returns True if this area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Returns True if this area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns True if this area is bigger or equal."""
        return self.area() >= other.area()
