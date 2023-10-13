from unittest import TestCase, mock
from models.square import Square
from models.base import Base
from io import StringIO
"""Test my class Square"""


class Test_Square_task_10(TestCase):
    """test pass arguent and display and str"""

    def test_empty_pass(self):
        with self.assertRaises(TypeError):
            Square()

    def test_with_argument(self):
        Base._Base__nb_objects = 0
        # with size.
        t = Square(4)
        self.assertEqual(str(t), "[Square] (1) 0/0 - 4")
        self.assertAlmostEqual(t.area(), 16)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t.display()
            self.assertEqual(op.getvalue(), "####\n####\n####\n####\n")

        # with size and x
        t1 = Square(2, 2)
        self.assertEqual(str(t1), "[Square] (2) 2/0 - 2")
        self.assertAlmostEqual(t1.area(), 4)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t1.display()
            self.assertEqual(op.getvalue(), "  ##\n  ##\n")

        # with size and x and y
        t2 = Square(3, 1, 2)
        self.assertEqual(str(t2), "[Square] (3) 1/2 - 3")
        self.assertAlmostEqual(t2.area(), 9)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t2.display()
            self.assertEqual(op.getvalue(), "\n\n ###\n ###\n ###\n")

        # with size, and x and y and id
        t3 = Square(5, 2, 1, 10)
        self.assertEqual(str(t3), "[Square] (10) 2/1 - 5")
        self.assertAlmostEqual(t3.area(), 25)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t3.display()
            test = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
            self.assertEqual(op.getvalue(), test)

    def test_to_many_argument(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def testPassNone(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_getter_setter(self):
        t = Square(4)
        self.assertAlmostEqual(t.size, 4)

        with self.assertRaises(AttributeError):
            t.__width

        t.size = 22
        self.assertAlmostEqual(t.size, 22)
        # cal area pass size
        self.assertAlmostEqual(t.area(), 484)
        # str Square pass size
        self.assertAlmostEqual(str(t), "[Square] (2) 0/0 - 22")
        # get height
        self.assertAlmostEqual(t.height, 22)
        # get width
        self.assertAlmostEqual(t.width, 22)

        # set value
        t = Square(3, 4, 5, 6)
        # get x
        self.assertAlmostEqual(t.x, 4)
        # get y
        self.assertAlmostEqual(t.y, 5)
        # get id
        self.assertAlmostEqual(t.id, 6)


class Test_Square_values_Type_Error(TestCase):
    """test ValueError and TypeError"""
    No_valide_types = [
        None,
        1024.44,
        3j,
        "test",
        ["test", "me"],
        ("test", "me"),
        {"test": 12, "me": 13},
        {"test", "me"},
        True,
        False
    ]

    # TypeError
    def test_size_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "width must be an integer"):
                    Square(T)

    def test_x_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Square(6, T)

    def test_y_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Square(6, 10, T)

    # ValueError
    def test_size_negative_or_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(12, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(11, -55)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(12, 11, -6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(100, 11, -123)


class Test_Square_area(TestCase):
    """ Test method area """

    def test_area(self):
        self.assertAlmostEqual(Square(2, 0, 0, 1).area(), 4)
        self.assertAlmostEqual(Square(6, 0, 0, 1).area(), 36)

    def test_area_pass_argu(self):
        with self.assertRaises(TypeError):
            Square(1, 0, 0, 1).area("test")


class Test_Square_display(TestCase):
    """Test method display """

    def test_display_size(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(3, 0, 0, 12).display()
            self.assertEqual(op.getvalue(), "###\n###\n###\n")

    def test_display_with_x(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(4, 2, 0, 12).display()
            self.assertEqual(op.getvalue(), "  ####\n  ####\n  ####\n  ####\n")

    def test_display_with_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(2, 0, 2, 12).display()
            self.assertEqual(op.getvalue(), "\n\n##\n##\n")

    def test_display_with_x_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(3, 3, 2, 12).display()
            self.assertEqual(
                op.getvalue(), "\n\n   ###\n   ###\n   ###\n")

    def test_display_with_pass_argument(self):
        with self.assertRaises(TypeError):
            Square(3, 0, 2, 12).display(5)
