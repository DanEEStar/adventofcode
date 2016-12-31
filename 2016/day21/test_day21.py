import unittest

from day21 import parse_line


class Day21TestCase(unittest.TestCase):
    def test_parse_line_with_swap_position(self):
        result = parse_line('swap position 0 with position 2')
        self.assertEqual(0, result[1])
        self.assertEqual(2, result[2])
        i = 'acefdbgh'
        r = result[0](i, result[1], result[2])
        self.assertEqual('ecafdbgh', r)

    def test_parse_line_with_swap_letter(self):
        result = parse_line('swap letter d with letter b')
        self.assertEqual('d', result[1])
        self.assertEqual('b', result[2])
        i = 'ebcda'
        r = result[0](i, result[1], result[2])
        self.assertEqual('edcba', r)

    def test_parse_line_with_swap_rotate_left(self):
        result = parse_line('rotate left 1 step')
        self.assertEqual(1, result[1])
        i = 'abcde'
        r = result[0](i, result[1], None)
        self.assertEqual('bcdea', r)

    def test_parse_line_with_swap_rotate_based(self):
        result = parse_line('rotate based on position of letter b')
        self.assertEqual('b', result[1])
        i = 'abdec'
        r = result[0](i, result[1], None)
        self.assertEqual('ecabd', r)

    def test_parse_line_with_reverse(self):
        result = parse_line('reverse positions 0 through 4')
        self.assertEqual(0, result[1])
        self.assertEqual(4, result[2])
        i = 'edcba'
        r = result[0](i, result[1], result[2])
        self.assertEqual('abcde', r)

    def test_parse_line_with_move(self):
        result = parse_line('move position 1 to position 4')
        self.assertEqual(1, result[1])
        self.assertEqual(4, result[2])
        i = 'bcdea'
        r = result[0](i, result[1], result[2])
        self.assertEqual('bdeac', r)

    def test_parse_line_with_move2(self):
        result = parse_line('move position 3 to position 0')
        self.assertEqual(3, result[1])
        self.assertEqual(0, result[2])
        i = 'bdeac'
        r = result[0](i, result[1], result[2])
        self.assertEqual('abdec', r)


if __name__ == "__main__":
    unittest.main()
