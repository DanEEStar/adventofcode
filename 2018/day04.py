import re

from helper import neighbors4, neighbors8, cityblock_distance, X


def parse_line(line):
    r = r'\#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)'
    (num, x, y, w, h) = re.findall(r, line)[0]
    return int(num), int(x), int(y), int(w), int(h)


def parse_line_ints(line):
    r = r'-?(\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def main():
    print(neighbors4((4, 8)))
    print(neighbors8((4, 8)))
    print(cityblock_distance((1,1), (4, 1)))

    p = (51, 42)
    print(X(p))

    with open('day04.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        for line in lines:
            print(parse_line_ints(line))


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