import unittest

from day7 import apply_operator, output_signal_from_line, operator_from_line, signals_from_line, apply_rule, step, \
    to_uint16, simulate


class ApplyOperatorTestCase(unittest.TestCase):
    def test_underflow(self):
        result = apply_operator(2**16, None, 'NOT')
        self.assertEqual(65535, result)

    def test_or(self):
        result = apply_operator(1, 2, 'OR')
        self.assertEqual(3, result)

    def test_and(self):
        result = apply_operator(1, 3, 'AND')
        self.assertEqual(1, result)

    def test_lshift(self):
        result = apply_operator(1, 4, 'LSHIFT')
        self.assertEqual(16, result)

    def test_rshift(self):
        result = apply_operator(16, 4, 'RSHIFT')
        self.assertEqual(1, result)

    def test_assign(self):
        result = apply_operator(256, None, 'ASSIGN')
        self.assertEqual(256, result)


class OutputSignalFromStringTestCase(unittest.TestCase):

    def test_ex1(self):
        output_signal = output_signal_from_line('NOT dq -> dr')
        self.assertEqual('dr', output_signal)

    def test_ex2(self):
        output_signal = output_signal_from_line('dd OR do -> dp')
        self.assertEqual('dp', output_signal)

    def test_ex3(self):
        output_signal = output_signal_from_line('44430 -> b')
        self.assertEqual('b', output_signal)


class OperatorFromLineTestCase(unittest.TestCase):

    def test_not(self):
        operator = operator_from_line('NOT dq -> dr')
        self.assertEqual('NOT', operator)

    def test_and(self):
        operator = operator_from_line('eg AND ei -> ej')
        self.assertEqual('AND', operator)

    def test_lshift(self):
        operator = operator_from_line('kf LSHIFT 15 -> kj')
        self.assertEqual('LSHIFT', operator)

    def test_assign(self):
        operator = operator_from_line('44430 -> b')
        self.assertEqual('ASSIGN', operator)


class SignalsFromLineTestCase(unittest.TestCase):
    def test_not(self):
        (signal1, signal2) = signals_from_line('NOT dq -> dr')
        self.assertEqual('dq', signal1)
        self.assertEqual(None, signal2)

    def test_assign(self):
        (signal1, signal2) = signals_from_line('44430 -> b')
        self.assertEqual('44430', signal1)
        self.assertEqual(None, signal2)

    def test_and(self):
        (signal1, signal2) = signals_from_line('jx AND jz -> ka')
        self.assertEqual('jx', signal1)
        self.assertEqual('jz', signal2)

    def test_lshift(self):
        (signal1, signal2) = signals_from_line('cd LSHIFT 15 -> ch')
        self.assertEqual('cd', signal1)
        self.assertEqual('15', signal2)


class ApplyRuleTestCase(unittest.TestCase):
    def test_assign_withUnknownSignal_setsValueToSignal(self):
        signal_state = {}
        signal_state = apply_rule(signal_state, '123 -> a')

        self.assertEqual(123, signal_state['a'])

    def test_or_withSetSignals_setsValueToSignal(self):
        signal_state = {
            'a': 1,
            'b': 2
        }

        signal_state = apply_rule(signal_state, 'a OR b -> c')
        self.assertEqual(3, signal_state['c'])

    def test_lshift(self):
        signal_state = {
            'x': 123
        }

        signal_state = apply_rule(signal_state, 'x LSHIFT 2 -> f')
        self.assertEqual(492, signal_state['f'])


class StepTestCase(unittest.TestCase):
    def test_step_withMultipleRules(self):
        signal_state = {}
        rules = [
            '123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i',
        ]

        next_state = step(signal_state, rules)

        self.assertEqual(72, next_state['d'])
        self.assertEqual(507, next_state['e'])
        self.assertEqual(492, next_state['f'])
        self.assertEqual(114, next_state['g'])
        self.assertEqual(65412, to_uint16(next_state['h']))
        self.assertEqual(65079, to_uint16(next_state['i']))
        self.assertEqual(123, next_state['x'])
        self.assertEqual(456, next_state['y'])


class SimulateTestCase(unittest.TestCase):
    def test_simulate_withMultipleRules(self):
        rules = [
            'NOT x -> h',
            'x AND y -> d',
            'x LSHIFT 2 -> f',
            '123 -> x',
            'y RSHIFT 2 -> g',
            '456 -> y',
            'x OR y -> e',
            'NOT y -> i',
        ]

        next_state = simulate(rules)

        self.assertEqual(72, next_state['d'])
        self.assertEqual(507, next_state['e'])
        self.assertEqual(492, next_state['f'])
        self.assertEqual(114, next_state['g'])
        self.assertEqual(65412, to_uint16(next_state['h']))
        self.assertEqual(65079, to_uint16(next_state['i']))
        self.assertEqual(123, next_state['x'])
        self.assertEqual(456, next_state['y'])


if __name__ == "__main__":
    unittest.main()
