import unittest

from day9 import distance_from_line, distance_from_route


class DistanceFromLineTestCase(unittest.TestCase):
    def test_line1(self):
        line1 = 'AlphaCentauri to Snowdin = 66'
        output = distance_from_line(line1)

        self.assertEqual(('AlphaCentauri', 'Snowdin', 66), output)


class DistanceFromRouteTestCase(unittest.TestCase):
    def test_dlb(self):
        distances = {
            ('d', 'l'): 464,
            ('b', 'l'): 518,
            ('d', 'b'): 141
        }

        d = distance_from_route(['d', 'l', 'b'], distances)
        self.assertEqual(982, d)


if __name__ == "__main__":
    unittest.main()
