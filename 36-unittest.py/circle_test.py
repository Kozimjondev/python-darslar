import unittest
from circle import getPerimetr, getArea

class circletest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(3), 28.26)

    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(3),18.84)

unittest.main()