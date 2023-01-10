import unittest
from RootsMain import Roots


class TestRoots(unittest.TestCase):

    def setUp(self):
        self.Roots = Roots()

    def test_GoodDisc(self):
        self.assertEqual(self.Roots.Discriminant(1, -8, 12), 16)

    def test_NullDisc(self):
        self.assertEqual(self.Roots.Discriminant(1, -6, 9), 0)

    def test_NotExistDisc(self):
        self.assertEqual(self.Roots.Discriminant(5, 3, 7), -131)

    def test_OneRoot(self):
        self.assertEqual(self.Roots.Oneroot(1, 12), 0.0)

    def test_TwoRoots(self):
        self.assertEqual(self.Roots.Tworoots(-1, -2, 64), [-5, 3])


if __name__ == "__main__":
    unittest.main()


