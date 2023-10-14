import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Test Class Base"""


class TestBaseId(unittest.TestCase):
    """Test ID """
    # positive nagative id

    def test_pass_id_positive(self):
        Base._Base__nb_objects = 0
        Tp0 = Base(12)
        self.assertAlmostEqual(Tp0.id, 12)
        Tp1 = Base()
        self.assertAlmostEqual(Tp1.id, 1)
        Tp2 = Base()
        self.assertAlmostEqual(Tp2.id, 2)
        Tp3 = Base()
        self.assertAlmostEqual(Tp3.id, 3)
        Tp4 = Base()
        self.assertAlmostEqual(Tp4.id, 4)
        Tp5 = Base(None)
        self.assertAlmostEqual(Tp5.id, 5)
        Tp6 = Base(None)
        self.assertAlmostEqual(Tp6.id, 6)
        Tn0 = Base(-12)
        self.assertAlmostEqual(Tn0.id, -12)
        Tn1 = Base()
        self.assertAlmostEqual(Tn1.id, 7)
        Tn2 = Base()
        self.assertAlmostEqual(Tn2.id, 8)
        Tn3 = Base()
        self.assertAlmostEqual(Tn3.id, 9)
        Tn4 = Base()
        self.assertAlmostEqual(Tn4.id, 10)
        Tn5 = Base(None)
        self.assertAlmostEqual(Tn5.id, 11)
        Tn6 = Base(None)
        self.assertAlmostEqual(Tn6.id, 12)

    def test_base_id_zero(self):
        Base._Base__nb_objects = 0
        zero1 = Base(0)
        self.assertEqual(zero1.id, 0)


class Test_ToJsonString(unittest.TestCase):
    """test to json string."""

    def test_to_Json_string(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        a = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        self.assertEqual(dictionary, a)
        self.assertEqual(type(dictionary), dict)
        b = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_dictionary, b)
        self.assertEqual(type(json_dictionary), str)

    def test_empty_Dict(self):
        empty_dic = Base.to_json_string([])
        self.assertEqual(empty_dic, "[]")

    def test_None_Dict(self):
        empty_dict = Base.to_json_string(None)
        self.assertEqual(empty_dict, "[]")

    def test_two_dict(self):
        dic1 = {"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}
        dic2 = {"x": 11, "y": 12, "id": 13, "height": 14, "width": 15}
        json_dictionary2 = Base.to_json_string([dic1, dic2])
        j_d2 = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 11, "y": 12, "id": 13, "height": 14, "width": 15}]'
        self.assertEqual(json_dictionary2, j_d2)

    def test_no_argumant(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_many_argument(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 123)
