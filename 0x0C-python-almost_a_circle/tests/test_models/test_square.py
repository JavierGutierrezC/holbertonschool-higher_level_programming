#!/usr/bin/python3
"""Unittest for square.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):
    """tests instances, methods from square class"""
    def setUp(self):
        """sets variable to 0"""
        Base._Base__nb_objects = 0

    def test_square_inheritance(self):
        """test if square is a subclass of base"""
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_emptysquare(self):
        """Function to test empty arguments for square"""
        with self.assertRaises(TypeError):
            b = Square()

    def test_toomanyarguments(self):
        """Function to test too many arguments"""
        with self.assertRaises(TypeError):
            s = Square(10, 10, 10, 10, 10, 10, 10)

    def test_createRectangle2arg(self):
        """Function to test asign 2 arguments"""
        s1 = Square(39, 39)
        self.assertEqual(s1.id, 1)

    def test_createSquareallargs(self):
        """Function to test asign 5 arguments all inputs"""
        s1 = Square(39, 39, 39, 39)
        self.assertEqual(s1.id, 39)

    def test_error_width(self):
        """Width TypeError"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("hola", 10)
            self.assertEqual(str(e.exception), "width must be an integer")

    def test_error_x(self):
        """x TypeError"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(2, 10, "hola")
            self.assertEqual(str(e.exception), "x must be an integer")

    def test_error_y(self):
        """y TypeError"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(2, 2, "hola")
            self.assertEqual(str(e.exception), "y must be an integer")

    def test_Val_error_width(self):
        """Width ValueError"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-5, 10)
            self.assertEqual(str(e.exception), "width must be >= 0")

    def test_Val_error_x(self):
        """x ValueError"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(2, 10, -3)
            self.assertEqual(str(e.exception), "x must be >= 0")

    def test_Val_error_y(self):
        """y ValueError"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(2, 10, -4)
            self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """tests area"""
        s1 = Square(2, 2)
        self.assertEqual(s1.area(), 4)

    def test_numb_args(self):
        """tests if number of args given is correct"""
        s1 = Square(1, 2)
        with self.assertRaises(TypeError):
            self.assertEqual(s1.area(4))

if __name__ == '__main__':
    unittest.main()
