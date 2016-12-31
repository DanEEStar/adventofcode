import unittest

from day10 import parse_line, run_give_instruction, bot_set_value


class Day10TestCase(unittest.TestCase):
    def test_parse_line_with_bot(self):
        result = parse_line('bot 127 gives low to output 1 and high to bot 180')
        print(result)

    def test_parse_line_with_value(self):
        result = parse_line('value 19 goes to bot 61')
        print(result)

    def test_run_give_instruction(self):
        bots = {'1': (-1, 3), '2': (2, 5)}
        output = {}

        inst = parse_line('bot 2 gives low to bot 1 and high to bot 0')
        run_give_instruction(inst, bots, output)

        inst = parse_line('bot 1 gives low to output 1 and high to bot 0')
        run_give_instruction(inst, bots, output)

        inst = parse_line('bot 0 gives low to output 2 and high to output 0')
        run_give_instruction(inst, bots, output)

        print(bots)
        print(output)

    def test_bot_set_values(self):
        vbot = (-1, 23)

        rbot = bot_set_value(67, vbot)
        print(rbot)
        self.assertEqual((23, 67), rbot)


if __name__ == "__main__":
    unittest.main()
