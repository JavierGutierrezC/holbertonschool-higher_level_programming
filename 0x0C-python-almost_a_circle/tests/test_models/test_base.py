#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
import sys
from models.base import Base


class test_Base(unittest.TestCase):
    """test for base.py"""
    def set_up(self):
        """init nb"""
        Base._Base__objects = 0

    def test_exit(self):
        """Test if class exists"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")

    def test_create_base(self):
        """assigned id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual((b1.id), 1)
        self.assertEqual((b2.id), 2)
        self.assertEqual((b3.id), 3)
        self.assertEqual((b4.id), 12)

    def test_Base_zero(self):
        """test zero number"""
        b1 = Base(0)
        self.assertEqual((b1.id), 0)

    def test_Base_negative(self):
        """test negative numbers"""
        b1 = Base(-3)
        self.assertEqual((b1.id), -3)

    def test_Base_negfloat(self):
        """test negative float"""
        b1 = Base(-1.3)
        self.assertEqual((b1.id), -1.3)

    def test_Base_str(self):
        """test with string"""
        b1 = Base("Hola")
        self.assertEqual((b1.id), "Hola")

    def test_Base_tup(self):
        """test tuples"""
        b1 = Base((1, 2))
        self.assertEqual((b1.id), (1, 2))

    def test_Base_list(self):
        """test list"""
        b1 = Base([1, 2, 3])
        self.assertEqual((b1.id), [1, 2, 3])

    def test_Base_dir(self):
        """test directory"""
        b1 = Base({"arg": 1, "arg": 2})
        self.assertEqual((b1.id), {"arg": 1, "arg": 2})

    def test_args(self):
        """test with more than 1 arg"""
        with self.assertRaises(TypeError) as e:
            b1 = Base(12, 23)

if __name__ == '__main__':
    unittest.main()
