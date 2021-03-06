#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([2,4,6,8]), 8)

    def test_max_at_start(self):
        self.assertEqual(max_integer([8,4,6,3]), 8)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([2,4,9,8,6]), 9)

    def test_negative_number_in_list(self):
        self.assertEqual(max_integer([2,-7,6,8]), 8)

    def test_only_neg_numbers(self):
        self.assertEqual(max_integer([-2,-4,-6,-8]), -2)

    def test_only_one_element(self):
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
