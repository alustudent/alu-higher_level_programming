#!/usr/bin/python3
"""Unittests for models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests ids and JSON helpers of the Base class."""

    def setUp(self):
        """Resets the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Removes JSON files written by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        """Ids increment automatically when none is given."""
        self.assertEqual([Base().id, Base().id, Base().id], [1, 2, 3])

    def test_given_id(self):
        """A given id is used as is and doesn't touch the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_none_id(self):
        """id=None means an automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_other_id_types(self):
        """Any value other than None is stored."""
        self.assertEqual(Base("a").id, "a")
        self.assertEqual(Base(-5).id, -5)

    def test_private_counter(self):
        """The counter is private."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_to_json_string_empty(self):
        """None and an empty list give "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """A list of dictionaries becomes a JSON string."""
        d = [{"id": 1, "width": 2}]
        s = Base.to_json_string(d)
        self.assertIsInstance(s, str)
        self.assertEqual(json.loads(s), d)

    def test_from_json_string_empty(self):
        """None and an empty string give an empty list."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        """A JSON string becomes a list of dictionaries."""
        d = [{"id": 89, "width": 10}, {"id": 7, "height": 7}]
        self.assertEqual(Base.from_json_string(json.dumps(d)), d)

    def test_json_round_trip(self):
        """to_json_string and from_json_string are inverses."""
        d = [Rectangle(1, 2, 3, 4, 5).to_dictionary()]
        self.assertEqual(Base.from_json_string(Base.to_json_string(d)), d)

    def test_save_to_file_rectangle(self):
        """save_to_file writes Rectangle.json."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json") as f:
            self.assertEqual(json.loads(f.read()), [r.to_dictionary()])

    def test_save_to_file_square(self):
        """save_to_file writes Square.json."""
        s = Square(5, 1, 2, 3)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_save_to_file_none_and_empty(self):
        """None and an empty list save "[]"."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrites(self):
        """save_to_file replaces the previous content."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        Rectangle.save_to_file([Rectangle(3, 3)])
        self.assertEqual(len(Rectangle.load_from_file()), 1)

    def test_create_rectangle(self):
        """create builds a new Rectangle with the same attributes."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """create builds a new Square with the same attributes."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_create_partial(self):
        """create keeps dummy values for missing keys."""
        r = Rectangle.create(id=89, width=4)
        self.assertEqual((r.id, r.width, r.height), (89, 4, 1))

    def test_load_from_file_missing(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """load_from_file returns new Rectangle instances."""
        rects = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(rects)
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded], [str(r) for r in rects])
        self.assertTrue(all(isinstance(r, Rectangle) for r in loaded))

    def test_load_from_file_square(self):
        """load_from_file returns new Square instances."""
        squares = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(squares)
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s) for s in squares])
        self.assertTrue(all(isinstance(s, Square) for s in loaded))


if __name__ == "__main__":
    unittest.main()
