#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """tests instances, methods from rectangle class"""
    def setUp(self):
        """unit setup"""
        Base._Base__nb_objects = 0

    def test_rectangle_inheritance(self):
        """test if rectangle is a subclass of base"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_emptyrect(self):
        """Function to test empty arguments for rectangle"""
        with self.assertRaises(TypeError):
            b = Rectangle()

    def test_emptyheight(self):
        """Function to test empty arguments for rectangle"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, )

    def test_toomanyarguments(self):
        """Function to test too many arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 10, 10, 10, 10, 10)

    def test_createRectangle2arg(self):
        """Function to test asign 2 arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(39, 39)
        self.assertEqual(r1.id, 6)

    def test_createRectangleallargs(self):
        """Function to test asign 5 arguments all inputs"""
        r1 = Rectangle(39, 39, 39, 39, 39)
        self.assertEqual(r1.id, 39)

    def test_error_height(self):
        """Height TypeError"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, "hola")
            self.assertEqual(str(e.exception), "height must be an integer")

    def test_error_width(self):
        """Width TypeError"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("hola", 10)
            self.assertEqual(str(e.exception), "width must be an integer")

    def test_error_x(self):
        """x TypeError"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 10, "hola")
            self.assertEqual(str(e.exception), "x must be an integer")

    def test_error_y(self):
        """y TypeError"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 10, 2, "hola")
            self.assertEqual(str(e.exception), "y must be an integer")

    def test_Val_error_height(self):
        """Height Valuerror"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, -1)
            self.assertEqual(str(e.exception), "height must be >= 0")

    def test_Val_error_width(self):
        """Width ValueError"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-13, 10)
            self.assertEqual(str(e.exception), "width must be >= 0")

    def test_Val_error_x(self):
        """x ValueError"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(2, 10, -13)
            self.assertEqual(str(e.exception), "x must be >= 0")

    def test_Val_error_y(self):
        """y ValueError"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(2, 10, 2, -13)
            self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """tests area"""
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

    def test_numb_args(self):
        """tests if number of args given is correct"""
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.assertEqual(r1.area(4))

    def test_str(self):
        """check if a strong was returned correctly"""
        r1 = Rectangle(10, 20, 28, 30, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 28/30 - 10/20")

if __name__ == '__main__':
    unittest.main()
