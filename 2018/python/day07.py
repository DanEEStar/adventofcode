import operator
import re
from datetime import datetime


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


def parse_line_steps(line):
    return (line[5], line[-12])


def part1(input):
    lines = input.read().split('\n')
    lines = lines[:-1]

    steps = []
    nodes = set()
    for line in lines:
        n1, n2 = parse_line_steps(line)
        steps.append((n1, n2))
        nodes.add(n1)
        nodes.add(n2)

    print(nodes)
    print(steps)

    result = ''
    while len(nodes) > 0:
        n1s = set(s[0] for s in steps)
        n2s = set(s[1] for s in steps)
        n = sorted(nodes - n2s)[0]
        result += n

        steps = [s for s in steps if s[0] not in result]
        nodes.remove(n)
        print(steps)

    print(result)


def part2(input):
    lines = input.read().split('\n')
    lines = lines[:-1]

    steps = []
    nodes = set()
    for line in lines:
        n1, n2 = parse_line_steps(line)
        steps.append((n1, n2))
        nodes.add(n1)
        nodes.add(n2)

    print(steps)

    result = ''
    seconds = 0
    workers = {}
    while len(nodes) > 0:
        n1s = set(s[0] for s in steps)
        n2s = set(s[1] for s in steps)

        next_nodes = list(sorted(nodes - n2s))

        while len(workers) < 5 and len(next_nodes) > 0:
            workers[next_nodes[0]] = ord(next_nodes[0]) - 64 + 60
            nodes.remove(next_nodes[0])
            next_nodes = next_nodes[1:]

        print(workers)

        min_node = min(workers.items(), key=operator.itemgetter(1))
        print(min_node)

        seconds += min_node[1]
        result += min_node[0]
        workers.pop(min_node[0])

        for k, v in workers.items():
            workers[k] -= min_node[1]

        print(workers)
        print(seconds)

        steps = [s for s in steps if s[0] not in result]
        print(steps)
        print(result)
        print('####################')

    print(result)
    print(seconds)


def main():
    # print(neighbors4((4, 8)))
    # # print(neighbors8((4, 8)))
    # # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # # print(X(p))

    with open('day07.txt') as input:
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