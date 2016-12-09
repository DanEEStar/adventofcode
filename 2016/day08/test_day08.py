import unittest

from day08 import parse_line


class Day08TestCase(unittest.TestCase):
    def test_parse_line_with_rect(self):
        result = parse_line('rect 2x1')
        print(result)
        self.assertEqual(2, result[1])
        self.assertEqual(1, result[2])

    def test_parse_line_with_rotate_row(self):
        result = parse_line('rotate row y=2 by 35')
        print(result)
        self.assertEqual(2, result[1])
        self.assertEqual(35, result[2])

    def test_parse_line_with_rotate_column(self):
        result = parse_line('rotate column x=25 by 1')
        print(result)
        self.assertEqual(25, result[1])
        self.assertEqual(1, result[2])


if __name__ == "__main__":
    unittest.main()
