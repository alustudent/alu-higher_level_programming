#!/usr/bin/python3
"""Defines Square, a Rectangle whose width and height are always equal."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, stored as a Rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square with a size used as width and height."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets width then height to value, with Rectangle's validation."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns id, size, x and y by position or by keyword.

        Keyword arguments are ignored when positional ones are given.
        """
        names = ("id", "size", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
