import ctypes
import re
from copy import deepcopy


def simulate(rules, start_state=None):
    if start_state is None:
        start_state = {}

    current_state = deepcopy(start_state)
    next_state = step(current_state, rules)

    while next_state != current_state:
        current_state = next_state
        next_state = step(current_state, rules)

    return next_state


def step(signal_state, rules):
    next_state = deepcopy(signal_state)
    for rule in rules:
        next_state = apply_rule(next_state, rule)

    return next_state


def to_uint16(number):
    return ctypes.c_uint16(number).value


def apply_rule(signal_state, rule):
    operator = operator_from_line(rule)
    (signal1, signal2) = signals_from_line(rule)
    output_signal = output_signal_from_line(rule)

    if signal1.isdigit():
        signal1_value = int(signal1)
    else:
        signal1_value = signal_state.get(signal1, 0)

    if signal2 and signal2.isdigit():
        signal2_value = int(signal2)
    else:
        signal2_value = signal_state.get(signal2, 0)

    result = apply_operator(signal1_value, signal2_value, operator)
    signal_state[output_signal] = result

    return signal_state


def apply_operator(signal1, signal2, operator):
    result = None
    if operator == 'NOT':
        result = to_uint16(~signal1)
    elif operator == 'AND':
        result = to_uint16(signal1 & signal2)
    elif operator == 'OR':
        result = to_uint16(signal1 | signal2)
    elif operator == 'LSHIFT':
        result = to_uint16(signal1 << signal2)
    elif operator == 'RSHIFT':
        result = to_uint16(signal1 >> signal2)
    elif operator == 'ASSIGN':
        result = to_uint16(signal1)
    else:
        raise Exception('unknown operator: {}'.format(operator))

    if result > 2**16 or result < 0:
        raise Exception('overflow: {}'.format(result))

    return result


def operator_from_line(s):
    m = re.search('[A-Z]+', s)
    if m is not None:
        return m.group(0)
    return 'ASSIGN'


def signals_from_line(s):
    m1 = re.search('(\d+|[a-z]+)', s)
    m2 = re.search('(\d+|[a-z]+) ->', s)
    if m1.group(1) != m2.group(1):
        return m1.group(1), m2.group(1)
    else:
        return m1.group(1), None


def output_signal_from_line(s):
    m = re.search('-> (\w+)', s)
    if m is not None:
        return m.group(1)
    return None


def main():
    with open('input.txt') as input:
        rules = input.readlines()
        states = simulate(rules)

        print(states)

        print(states['a'])


if __name__ == '__main__':
    main()

