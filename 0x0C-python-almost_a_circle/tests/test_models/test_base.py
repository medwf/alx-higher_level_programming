import unittest
from models.base import Base


class TestBaseId(unittest.TestCase):
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
        zero2 = Base(0)
        self.assertEqual(zero2.id, 0)

    @unittest.expectedFailure
    def test_Raise_Failure(self):
        """ test_Raise_Failure """
        id = "100"
        with self.assertRaises(TypeError):
            Base(id)

    @unittest.expectedFailure
    def test_Raise_Failure1(self):
        """ test_Raise_Failure """
        id = (1, 2, 3)
        with self.assertRaises(TypeError):
            Base(id)

    @unittest.expectedFailure
    def test_Raise_Failure2(self):
        """ test_Raise_Failure """
        id = [1, 2, 3]
        with self.assertRaises(TypeError):
            Base(id)
