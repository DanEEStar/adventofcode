from norvig import *


def part1(data):
    return max(sum(elf) for elf in data)


def part2(data):
    results = [sum(elf) for elf in data]
    return sum(sorted(results, reverse=True)[:3])


def main():
    in1 = parse(1, ints, paragraphs)
    print(part1(in1))
    print(part2(in1))


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