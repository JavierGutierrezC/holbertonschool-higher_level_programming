#!/usr/bin/python3
"""
Unittest for Base.py
"""


import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """test instance, from base class"""
    def set_up(self):
        """init nb"""
        Base._Base__nb_objects = 0

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

    def empty_jason(self):
        """test for empty list"""
        lis = Base.to_json_string([])
        self.assertEqual(lis, "[]")

    def test_empty_json(self):
        """Empty dict"""
        dict = Base.to_json_string([{}])
        self.assertEqual(dict, "[{}]")

    def test_nonefile(self):
        """test for none file"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_string_set(self):
        """tests function from json"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string({1, 2})
        self.assertEqual("the JSON object must be str, not 'set'",
                         str(e.exception))

    def test_json_from_none(self):
        """test a none in a json string"""
        ans = Base.to_json_string(None)
        self.assertEqual(ans, "[]")

    def test_multi_dict_list(self):
        """test multiple dicts in a json_list"""
        ans = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(type(ans), str)

    def test_saves_empty_list_in_file(self):
        """test to save an empty list to a file"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_json_string_error(self):
        """Test for from_json_method with int."""
        with self.assertRaises(TypeError):
            Base.from_json_string(39)

    def test_json_empty_dict(self):
        """Test json with empty dict"""
        list_input = [{}]
        json_list_input = Base.to_json_string(list_input)
        listob = Base.from_json_string(json_list_input)
        self.assertEqual(listob, [{}])


if __name__ == '__main__':
    unittest.main()
