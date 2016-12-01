import unittest

from day13 import values_from_line


class ValuesFromLineTestCase(unittest.TestCase):
    def test_line1(self):
        line1 = 'Carol would lose 62 happiness units by sitting next to Alice.'
        output = values_from_line(line1)

        self.assertEqual(('Carol', 'Alice', -62), output)

    def test_line2(self):
        line1 = 'David would lose 7 happiness units by sitting next to Bob.'
        output = values_from_line(line1)

        self.assertEqual(('David', 'Bob', -7), output)

    def test_line3(self):
        line1 = 'Bob would gain 83 happiness units by sitting next to Alice.'
        output = values_from_line(line1)

        self.assertEqual(('Bob', 'Alice', 83), output)


if __name__ == "__main__":
    unittest.main()
