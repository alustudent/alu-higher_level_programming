#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class."""

    def setUp(self):
        """Resets the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        """Square inherits Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_attributes(self):
        """size sets width and height."""
        s = Square(3, 1, 2, 7)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (3, 3, 3, 1, 2, 7))

    def test_ids(self):
        """Ids are automatic unless given."""
        self.assertEqual(Square(5).id, 1)
        self.assertEqual(Square(5, id=12).id, 12)

    def test_missing_size(self):
        """size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_validation(self):
        """Square uses Rectangle's validation and width messages."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "1")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 0, -1)

    def test_invalid_size_x_y(self):
        """Negative and non-integer size, x and y are rejected."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 0, -3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 0, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 0, 1.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1], 0)

    def test_save_to_file_none(self):
        """Square.save_to_file(None) writes an empty list."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        try:
            Square.save_to_file(None)
            with open("Square.json") as f:
                self.assertEqual(f.read(), "[]")
        finally:
            if os.path.exists("Square.json"):
                os.remove("Square.json")

    def test_save_and_load(self):
        """Squares survive a save and load round trip."""
        try:
            Square.save_to_file([Square(5), Square(7, 9, 1)])
            loaded = Square.load_from_file()
            self.assertEqual([str(s) for s in loaded],
                             ["[Square] (1) 0/0 - 5", "[Square] (2) 9/1 - 7"])
        finally:
            if os.path.exists("Square.json"):
                os.remove("Square.json")

    def test_size_setter(self):
        """The size setter updates and validates."""
        s = Square(5)
        s.size = 10
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_area(self):
        """area returns size squared."""
        self.assertEqual(Square(5).area(), 25)

    def test_display(self):
        """display prints the square with offsets."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            Square(2, 2, 1).display()
        self.assertEqual(buf.getvalue(), "\n  ##\n  ##\n")

    def test_str(self):
        """__str__ gives the expected format."""
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (1) 1/3 - 3")

    def test_update_args(self):
        """update assigns id, size, x and y in order."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update assigns keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        s = Square(5)
        s.update(3, size=9)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 5")

    def test_update_validates(self):
        """update uses the validating setters."""
        with self.assertRaises(ValueError):
            Square(1).update(1, -2)

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        self.assertEqual(Square(10, 2, 1).to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update(self):
        """A dictionary can update another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)


if __name__ == "__main__":
    unittest.main()
