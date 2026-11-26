#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def setUp(self):
        """Resets the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Returns what func prints."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_is_base(self):
        """Rectangle inherits Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_ids(self):
        """Ids are automatic unless given."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """All attributes are stored and readable."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """The attributes are private."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_missing_arguments(self):
        """width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_type_errors(self):
        """Non-integers raise TypeError with the attribute name."""
        cases = [((1.5, 2), "width"), (("1", 2), "width"),
                 ((1, "2"), "height"), ((1, None), "height"),
                 ((1, 2, {}), "x"), ((1, 2, 1.5), "x"),
                 ((1, 2, 0, []), "y"), ((True, 2), "width")]
        for args, name in cases:
            with self.assertRaisesRegex(TypeError,
                                        name + " must be an integer"):
                Rectangle(*args)

    def test_value_errors(self):
        """Out of range values raise ValueError."""
        cases = [((0, 2), "width must be > 0"),
                 ((-1, 2), "width must be > 0"),
                 ((1, 0), "height must be > 0"),
                 ((1, 2, -1), "x must be >= 0"),
                 ((1, 2, 0, -1), "y must be >= 0")]
        for args, msg in cases:
            with self.assertRaisesRegex(ValueError, msg):
                Rectangle(*args)

    def test_validation_order(self):
        """width is validated before height, x and y."""
        with self.assertRaisesRegex(TypeError, "width"):
            Rectangle("1", "2", "3", "4")
        with self.assertRaisesRegex(ValueError, "width"):
            Rectangle(-1, -2)

    def test_setters(self):
        """Setters validate new values."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        r.width, r.height, r.x, r.y = 3, 4, 5, 6
        self.assertEqual(str(r), "[Rectangle] (1) 5/6 - 3/4")

    def test_area(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """display prints the rectangle with #."""
        self.assertEqual(self.output(Rectangle(2, 2).display), "##\n##\n")

    def test_display_offset(self):
        """display honors x and y."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_str(self):
        """__str__ gives the expected format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update assigns id, width, height, x and y in order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update assigns keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, width=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_validates(self):
        """update uses the validating setters."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.update(1, 0)
        with self.assertRaises(TypeError):
            r.update(height="2")

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 1)
        r.update(color="red")
        self.assertFalse(hasattr(r, "color"))

    def test_to_dictionary(self):
        """to_dictionary returns every attribute."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """A dictionary can update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 == r2)


if __name__ == "__main__":
    unittest.main()
