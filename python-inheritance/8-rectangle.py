#!/usr/bin/python3
"""Defines a Rectangle class that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private, validated width and height."""

    def __init__(self, width, height):
        """Initializes the rectangle with positive integer sides."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
