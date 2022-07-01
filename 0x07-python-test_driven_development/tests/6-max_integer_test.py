#!/usr/bin/python3
"""Unittest for max_integer([....])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tset case fot the max integer function"""

    def text_typeErrors(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.3)
        self.assertRaises(TypeError, max_integer, -3)
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, [2j, 3])
        self.assertRaises(TypeError, max_integer, [-2, "900"])

    def test_normalOperation(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([-100000, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([1, 2.9, 3.5, 4, 7, 6]), 7)
        self.assertEqual(max_integer([100, 200, 3.98, 40, 57, 69]), 200)
        self.assertEqual(max_integer([1000, 200, 3.98, 40, 57, 69]), 1000)
        self.assertEqual(max_integer([100]), 100)



