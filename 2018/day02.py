from collections import Counter
from itertools import product


def main():
    with open('day02.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        twos = 0
        threes = 0

        for line in lines:
            if 2 in Counter(line).values():
                twos += 1
            if 3 in Counter(line).values():
                threes += 1

        print(twos * threes)

        min_diff = 100
        min_result = None

        plines = product(lines, lines)
        for e in plines:
            diff = sum(1 for a, b in zip(e[0], e[1]) if a != b)
            if diff == 0:
                continue
            if diff < min_diff:
                min_diff = diff
                min_result = e

        print(min_result)
        print(min_diff)

        # rmyxgdlihczskunpfijqcebtv
        # rmyxgdlihczskunpfibjqcebtv



if __name__ == '__main__':
    main()

'''
def test_intersection0():
    assert (0, 4) == intersect((0, 0), (0, 8), (-4, 4), (4, 4))


def test_intersection1():
    assert (0, 4) == intersect((0, 0), (0, 8), (4, 4), (-4, 4))


def test_intersection2():
    assert (0, 4) == intersect((-4, 4), (4, 4), (0, 0), (0, 8))


def test_intersection3():
    assert None is intersect((2, 1), (6, 1), (8, 0), (8, 3))
'''