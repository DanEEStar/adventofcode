import re

import numpy as np


def parse_line(line):
    r = r'\#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)'
    (num, x, y, w, h) = re.findall(r, line)[0]
    return int(num), int(x), int(y), int(w), int(h)


def parse_line_ints(line):
    r = r'-?(\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def main():
    with open('day03.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        grid = np.zeros(shape=(10000, 10000), dtype=(int, 2))

        for line in lines:
            (num, x, y, w, h) = parse_line_ints(line)
            for i in range(x, w+x):
                for j in range(y, h+y):
                    grid[i, j][0] += num
                    grid[i, j][1] = num

        for line in lines:
            (num, x, y, w, h) = parse_line_ints(line)
            ge = list(grid[x:w+x, y:h+y].flatten())
            if ge.count(ge[0]) == len(ge):
                print(num)
                break


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