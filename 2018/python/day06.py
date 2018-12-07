import operator
import re
from collections import defaultdict, Counter
from datetime import datetime

from helper import X, Y, cityblock_distance


def parse_line(line):
    # [1518 - 11 - 01 00: 00] Guard  # 10 begins shift
    r = r'(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)\] (.*)'
    m = re.findall(r, line)[0]
    # # print(line)
    # # print(m)
    d = datetime(int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]))
    return d, m[5]
    #return int(num), int(x), int(y), int(w), int(h)


def parse_line_ints(line):
    r = r'-?(\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def part1(input):
    lines = input.read().split('\n')
    lines = lines[:-1]

    points = []
    for idx, line in enumerate(lines):
        (x, y) = parse_line_ints(line)
        points.append((idx, (x, y)))
    # print(points)

    xs = [X(i[1]) for i in points]
    ys = [Y(i[1]) for i in points]

    # print(xs)

    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)

    print(minx, maxx)
    print(miny, maxy)

    # grid = np.zeros(shape=(maxx + 10, maxy + 10), dtype=(int, 2))
    # grid = np.zeros(shape=(maxx, maxy), dtype=(int, 2))
    grid = {}

    for x in range(minx, maxx):
        for y in range(miny, maxy):
            d = defaultdict(lambda: 0)
            for p in points:
                d[p] = cityblock_distance((x, y), p[1])

            # print('xxxxxxxxx')
            # print(dict(d))
            # print(x,y)
            ds = list(reversed(sorted(d.items(), key=operator.itemgetter(1))))
            if ds[0][1] != ds[1][1]:
                grid[(x, y)] = min(d.items(), key=operator.itemgetter(1))[0]

    # print(grid)
    c = Counter(grid.values())
    print(c)

    grid = {}
    for x in range(0, maxx + 10):
        for y in range(0, maxy + 10):
            d = defaultdict(lambda: 0)
            for p in points:
                d[p] = cityblock_distance((x, y), p[1])

            # print('xxxxxxxxx')
            # print(dict(d))
            # print(x,y)
            ds = list(reversed(sorted(d.items(), key=operator.itemgetter(1))))
            if ds[0][1] != ds[1][1]:
                grid[(x, y)] = min(d.items(), key=operator.itemgetter(1))[0]

    c2 = Counter(grid.values())
    print(c2)

    result = {}
    for k in c:
        if c2[k] == c[k]:
            result[k] = c[k]

    print(list(reversed(sorted(result.items(), key=operator.itemgetter(1)))))


def part2(input):
    lines = input.read().split('\n')
    lines = lines[:-1]

    points = []
    for idx, line in enumerate(lines):
        (x, y) = parse_line_ints(line)
        points.append((idx, (x, y)))
    # print(points)

    xs = [X(i[1]) for i in points]
    ys = [Y(i[1]) for i in points]

    # print(xs)

    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)

    print(minx, maxx)
    print(miny, maxy)

    # grid = np.zeros(shape=(maxx + 10, maxy + 10), dtype=(int, 2))
    # grid = np.zeros(shape=(maxx, maxy), dtype=(int, 2))

    grid = {}
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            d = defaultdict(lambda: 0)
            manhattan = 0
            for p in points:
                manhattan += cityblock_distance((x, y), p[1])

            if manhattan < 10000:
                grid[(x, y)] = 'x'

    print(len(grid))


def main():
    # # print(neighbors4((4, 8)))
    # # print(neighbors8((4, 8)))
    # # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # # print(X(p))

    with open('day06.txt') as input:
        # part1(input)
        part2(input)


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