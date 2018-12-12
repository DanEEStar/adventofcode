import re
from datetime import datetime

import numpy as np


def parse_line(line):
    # [1518 - 11 - 01 00: 00] Guard  # 10 begins shift
    r = r'(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)\] (.*)'
    m = re.findall(r, line)[0]
    # print(line)
    # print(m)
    d = datetime(int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]))
    return d, m[5]
    #return int(num), int(x), int(y), int(w), int(h)


serial_number = 9221


def power_level(x, y, serial_number=serial_number):
    rack_id = (x + 10)
    v = (rack_id * y + serial_number) * rack_id
    if len(str(v)) >= 3:
        h = int(str(v)[-3])
    else:
        h = 0
    return h - 5


def parse_line_ints(line):
    r = r'-?(\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def part1(input):
    #lines = input.read().split('\n')
    grid = np.zeros(shape=(300, 300), dtype=int)

    for x in range(300):
        for y in range(300):
            grid[x, y] = power_level(x, y, 9221)

    result = (-1, -1)

    for x in range(298):
        for y in range(298):
            total_power = grid[x, y] + grid[x+1, y] + grid[x+2, y] + grid[x, y+1] + grid[x+1, y+1] + grid[x+2, y+1] + grid[x, y+2] + grid[x+1, y+2] + grid[x+2, y+2]
            if total_power > result[1]:
                result = ((x, y), total_power)

    print(result)


def part2(input):
    grid = np.zeros(shape=(300, 300), dtype=int)

    for x in range(300):
        for y in range(300):
            grid[x, y] = power_level(x, y, 9221)

    result = (-1, -1, -1)

    for square in range(3, 20):
        print(square)
        for x in range(301 - square):
            for y in range(301 - square):
                total_power = np.sum(grid[x:x+square,y:y+square])

                if total_power > result[1]:
                    result = ((x, y, square), total_power)

    print(result)


def main():
    # print(neighbors4((4, 8)))
    # print(neighbors8((4, 8)))
    # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # print(X(p))

    print(power_level(3, 5))
    print(power_level(122, 79, 57))
    print(power_level(217, 196, 39))
    print(power_level(101, 153, 71))

    part2(None)



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