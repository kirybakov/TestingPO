""" import unittest
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
    unittest.main() """

import unittest
from rootsmain import Klass 

class TestEquation(unittest.TestCase):

    def setUp(self):
        self.Klass = Klass()

    def test_PositiveDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(3, 7, -6), 121)
    
    def test_ZeroDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(4, 4, 1), 0)

    def test_NegativeDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(2, 1, 1), -7)
        
    def test_Squareroot(self):
        self.assertEqual(self.Klass.squareroot(1, 0), 0.0)
        
    def test_Squareroots(self):
        self.assertEqual(self.Klass.squareroots(1, 2, 16), [-3.0, 1])
  
if __name__ == "__main__":
    unittest.main()


