import unittest

from day01 import intersect


class ValuesFromLineTestCase(unittest.TestCase):
    def test_intersection0(self):
        self.assertEqual((0, 4), intersect((0, 0), (0, 8), (-4, 4), (4, 4)))

    def test_intersection1(self):
        self.assertEqual((0, 4), intersect((0, 0), (0, 8), (4, 4), (-4, 4)))

    def test_intersection2(self):
        self.assertEqual((0, 4), intersect((-4, 4), (4, 4), (0, 0), (0, 8)))

    def test_intersection3(self):
        #import ipdb; ipdb.set_trace()
        self.assertEqual(None, intersect((2, 1), (6, 1), (8, 0), (8, 3)))


if __name__ == "__main__":
    unittest.main()
