"""Tests for calculator.py"""

import unittest
import math

from calculator import add, subtract, multiply, divide, exponent, logarithmic, sine, cosine, tangent


class TestCalculator(unittest.TestCase):
    """Test cases for basic arithmetic operations."""

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, -2), -5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(5, 0), 1)
        self.assertEqual(exponent(10, 0.5), math.sqrt(10))

    def test_logarithmic(self):
        self.assertEqual(logarithmic(100, 10), 2)
        self.assertAlmostEqual(logarithmic(math.e), 1)  # natural log of e
        with self.assertRaises(ValueError):
            logarithmic(0, 10)
        with self.assertRaises(ValueError):
            logarithmic(-1, 10)

    def test_trigonometric(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(tangent(0), 0)
        self.assertAlmostEqual(sine(math.pi / 2), 1, places=6)
        self.assertAlmostEqual(cosine(math.pi / 2), 0, places=6)


if __name__ == "__main__":
    unittest.main()