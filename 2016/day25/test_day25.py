import unittest

from day25 import parse_instruction, check_output


class Day25TestCase(unittest.TestCase):
    def test_parse_instruction1(self):
        i = 'cpy 41 a'
        values = parse_instruction('cpy 41 a')
        self.assertEqual(('cpy', '41', 'a'), values)

    def test_parse_instruction2(self):
        values = parse_instruction('inc a')
        self.assertEqual(('inc', 'a', None), values)

    def test_parse_instruction3(self):
        values = parse_instruction('dec a')
        self.assertEqual(('dec', 'a', None), values)

    def test_parse_instruction4(self):
        values = parse_instruction('jnz a -5')
        self.assertEqual(('jnz', 'a', '-5'), values)

    def test_check_output(self):
        self.assertTrue(check_output('010101010101', 12))


if __name__ == "__main__":
    unittest.main()
