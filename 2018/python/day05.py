import operator
import re
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
    r = r'-?(\d+)'
    result = [int(x) for x in re.findall(r, line)]
    return result


def contains_bbannotation(s):
    matches = re.findall(r'([a-z])(.)\2\1', s)
    return any([x[0] != x[1] for x in matches])


chr_lower = [chr(a) for a in range(97, 123)]
chr_upper = [s.upper() for s in chr_lower]
matches1 = ['{}{}'.format(x[0], x[1]) for x in list(zip(chr_lower, chr_upper))]
matches2 = ['{}{}'.format(x[1], x[0]) for x in list(zip(chr_lower, chr_upper))]


def react(line):
    while True:
        start = len(line)
        for m in matches1:
            line = line.replace(m, '', 1)
        for m in matches2:
            line = line.replace(m, '', 1)

        if start == len(line):
            break

    return len(line.strip())


def main():
    # print(neighbors4((4, 8)))
    # print(neighbors8((4, 8)))
    # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # print(X(p))

    with open('day05.txt') as input:
        line = input.read().strip()

        #line = 'dabAcCaCBAcCcaDA'

        #print(line)


        #print(chr_lower)
        #print(chr_upper)

        #print(matches2)
        #print(matches1)

        original = line

        print(react(original))

        solutions = {}

        for i in range(26):
            line = original
            m1 = chr_lower[i]
            m2 = chr_upper[i]
            line = line.replace(m1, '')
            line = line.replace(m2, '')

            solutions[m1] = react(line)

        print(solutions)

        print(min(solutions.items(), key=operator.itemgetter(1)))


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