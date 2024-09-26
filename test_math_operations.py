# test_math_operations.py

import unittest
from math_operations import add_numbers

class TestMathOperations(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  # Test case 1
        self.assertEqual(add_numbers(-1, 1), 0)  # Test case 2
        self.assertEqual(add_numbers(0, 0), 0)  # Test case 3

    def test_add_numbers_with_negative(self):
        self.assertEqual(add_numbers(-5, -3), -8)  # Test case 4
        self.assertEqual(add_numbers(-5, 3), -2)  # Test case 5

if __name__ == '__main__':
    unittest.main()
