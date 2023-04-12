#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([42, 53, 74]), 74)
        self.assertAlmostEqual(max_integer([83, 24, 332, 330]), 332)
        self.assertAlmostEqual(max_integer([-23, -43, -4]), -4)
        self.assertAlmostEqual(max_integer([20000022]), 20000022)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_non_int(self):
        self.assertRaises(TypeError, max_integer, True)
