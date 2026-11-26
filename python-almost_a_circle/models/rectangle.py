#!/usr/bin/python3
"""Defines Rectangle, a shape with validated width, height and position."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a width, a height and an x/y position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle and validates every attribute."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __validate(name, value, minimum):
        """Raises if value is not an int or is lower than minimum."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < minimum:
            sign = ">" if minimum == 1 else ">="
            raise ValueError("{} must be {} 0".format(name, sign))

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width, which must be an integer > 0."""
        self.__validate("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height, which must be an integer > 0."""
        self.__validate("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """Gets the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the horizontal offset, which must be an integer >= 0."""
        self.__validate("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """Gets the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the vertical offset, which must be an integer >= 0."""
        self.__validate("y", value, 0)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with #, offset by x spaces and y lines."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns id, width, height, x and y by position or by keyword.

        Keyword arguments are ignored when positional ones are given.
        """
        names = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
