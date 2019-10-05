#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmaxinteger(unittest.TestCase):

    def max_at_end(self):
        self.assertEqual(max_integer([2,4,6,8]),8)

    def max_at_start(self):
        self.assertEqual(max_integer([8,4,6,3]),8)

    def max_at_middle(self):
        self.assertEqual(max_integer([2,4,9,8,6]),9)

    def negative_number_in_list(self):
        self.assertEqual(max_integer([2,-7,6,8]),8)

    def only_neg_numbers(self):
        self.assertEqual(max_integer([-2,-4,-6,-8]),-2)

    def only_one_element(self):
        self.assertEqual(max_integer([2]),2)

    def empty_list(self):
        self.assertEqual(max_integer([]),None)
