import re
import sys
from datetime import datetime


def parse_line(line):
    # [1518 - 11 - 01 00: 00] Guard  # 10 begins shift
    r = r'(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)\] (.*)'
    m = re.findall(r, line)[0]
    # print(line)
    # print(m)
    d = datetime(int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]))
    return d, m[5]
    #return int(num), int(x), int(y), int(w), int(h)


def parse_line_ints(line):
    r = r'(-?\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def print_positions(positions, index=0):
    xmin = min(p[0] for p in positions)
    ymin = min(p[1] for p in positions)
    xmax = max(p[0] for p in positions)
    ymax = max(p[1] for p in positions)

    #print(xmin, ymin, xmax, ymax)

    xys = [(p[0], p[1]) for p in positions]

    if xmax - xmin < 100 and ymax - ymin < 100:
        print(index)
        print(xmin, ymin, xmax, ymax, xmax - xmin, ymax - ymin)

        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                if (x, y) in xys:
                    sys.stdout.write('#')
                    pass
                else:
                    sys.stdout.write('.')
                    pass
            print()
        print()


def part1(input):
    lines = input.read().split('\n')
    lines = lines[:-1]

    positions = []
    for line in lines:
        positions.append(parse_line_ints(line))

    print_positions(positions)

    for x in range(11000):
        #print(x)
        for i, pos in enumerate(positions):
            pos[0] += pos[2]
            pos[1] += pos[3]
            positions[i] = pos

        print_positions(positions, x)


def part2(input):
    lines = input.read().split('\n')
    lines = lines[:-1]
    print(lines)


def main():
    # print(neighbors4((4, 8)))
    # print(neighbors8((4, 8)))
    # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # print(X(p))

    with open('day10.txt') as input:
        part1(input)


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