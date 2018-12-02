from itertools import cycle


def main():
    with open('day01.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        visited = set()

        sum = 0
        for number in cycle(lines):
            sum += int(number)
            if sum in visited:
                print(sum)
                break
            visited.add(sum)

        print(sum)


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