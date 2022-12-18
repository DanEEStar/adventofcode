
def part1(lines):
    result = 0
    current = 0

    for line in lines:
        if line:
            current += int(line)
        else:
            print(current)
            if current > result:
                result = current
            current = 0

    return result


def part2(lines):
    results = []
    current = 0

    for line in lines:
        if line:
            current += int(line)
        else:
            results.append(current)
            current = 0

    return sum(sorted(results, reverse=True)[:3])


def main():
    with open('day01.txt') as input:
        lines = input.read().split('\n')
        print(part2(lines))


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