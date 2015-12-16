import re
from collections import namedtuple

import itertools

Dist = namedtuple('Dist', ('a', 'b', 'dist'))


def values_from_line(line):
    m = re.match('([A-Z]\w+) would (gain|lose) (\d+) .* next to ([A-Z]\w+)', line)
    person1 = m.group(1)
    person2 = m.group(4)
    value = 0
    gain_lose = m.group(2)
    if gain_lose == 'gain':
        value = int(m.group(3))
    else:
        value = -int(m.group(3))

    return person1, person2, value


def calc_table_setting_value(values, table_setting):
    value = 0
    neighbours = zip(table_setting, table_setting[1:])
    neighbours.append((table_setting[-1], table_setting[0]))
    for persons in neighbours:
        value += values[(persons[0], persons[1])]
        value += values[(persons[1], persons[0])]

    return value



def main():
    with open('input.txt') as input:
        values = dict()
        persons = set()

        for line in input:
            v = values_from_line(line)
            values[(v[0], v[1])] = v[2]
            persons.add(v[0])

        for person in persons:
            values[(person, 'Daniel')] = 0
            values[('Daniel', person)] = 0
        persons.add('Daniel')

        print(values)
        print(persons)

        table_settings = itertools.permutations(persons)
        happiness = 0

        for table_setting in table_settings:
            print(table_setting)
            h = calc_table_setting_value(values, table_setting)
            print(h)
            happiness = max(h, happiness)

        print(happiness)


if __name__ == '__main__':
    main()

