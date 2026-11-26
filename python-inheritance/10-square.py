#!/usr/bin/python3
"""Defines a Square class that inherits Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private, validated size."""

    def __init__(self, size):
        """Initializes the square with a positive integer size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
