import re
from datetime import datetime


def parse_line(line):
    # [1518 - 11 - 01 00: 00] Guard  # 10 begins shift
    r = r'(\w+)'
    return re.findall(r, line)


points = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

points2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}


def calc_points(line):
    return points[line]


def part1(input):
    lines = input.read().split('\n')
    return sum(calc_points(line) for line in lines)


def part2(input):
    lines = input.read().split('\n')
    return sum(points2[line] for line in lines)


def main():
    with open('day02.txt') as input:
        print(part2(input))


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