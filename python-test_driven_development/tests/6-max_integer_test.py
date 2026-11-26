#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the start of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A single element is the max."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Works with only negative numbers."""
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_mixed_signs(self):
        """Works with positive and negative numbers."""
        self.assertEqual(max_integer([-5, 0, 5, -10]), 5)

    def test_duplicates(self):
        """Duplicated max values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Works with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Works with ints and floats mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string returns its largest character."""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        """A list of strings returns the largest one."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_none(self):
        """None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Mixing numbers and strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])


if __name__ == "__main__":
    unittest.main()
