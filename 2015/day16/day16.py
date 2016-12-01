import re
from collections import namedtuple

import itertools

Dist = namedtuple('Dist', ('a', 'b', 'dist'))


def values_from_line(line):
    # Sue 10: trees: 2, children: 10, samoyeds: 10
    result = re.findall('([a-z]+): (\d+)', line)

    d = {}
    for t in result:
        d[t[0]] = int(t[1])

    return d


ref = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def main():
    max_correct = 0
    best_aunt = 0

    with open('input.txt') as input:
        for aunt, line in enumerate(input, 1):
            c = 0
            aunt_data = values_from_line(line)
            for key, value in ref.iteritems():
                if key in aunt_data:
                    if key in ['cats', 'trees']:
                        if aunt_data[key] > value:
                            c += 1
                    elif key in ['pomeranians', 'goldfish']:
                        if aunt_data[key] < value:
                            c += 1
                    else:
                        if aunt_data[key] == value:
                            c += 1

            if c > max_correct:
                max_correct = c
                best_aunt = aunt

                print(c)
                print(aunt)
                print(aunt_data)



if __name__ == '__main__':
    main()

