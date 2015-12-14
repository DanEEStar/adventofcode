import unittest

from day13 import values_from_line, distance_from_seconds


class BlaTestCase(unittest.TestCase):
    def test_line1(self):
        line1 = 'Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.'
        output = values_from_line(line1)

        self.assertEqual(('Vixen', 8, 8, 53), output)

    def tes_dist_from_seconds(self):
        line1 = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'
        output = values_from_line(line1)

        self.assertEqual(distance_from_seconds(output, 1), 14)

    def tes_dist_from_seconds2(self):
        line1 = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'
        output = values_from_line(line1)

        self.assertEqual(distance_from_seconds(output, 10), 140)

    def test_dist_from_seconds2(self):
        line1 = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'
        output = values_from_line(line1)

        self.assertEqual(distance_from_seconds(output, 1000), 1120)



if __name__ == "__main__":
    unittest.main()
