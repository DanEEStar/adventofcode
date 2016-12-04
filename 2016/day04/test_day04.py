import unittest

from day03 import handle_line


class Day03TestCase(unittest.TestCase):
    def test_intersection0(self):
        self.assertEqual(True, handle_line('owshgfarwv-bwddqtwsf-kzahhafy-216[wafhd]'))


if __name__ == "__main__":
    unittest.main()
