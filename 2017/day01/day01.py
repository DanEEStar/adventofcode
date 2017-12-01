def main():

    with open('input.txt') as input:
        s = 0
        last = 0

        digits = []
        for n in input.read().strip():
            digits.append(int(n))

        print(digits)

        for i, x in enumerate(digits):
            if x == digits[(i+len(digits)//2) % len(digits)]:
                s += x

        print(s)



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
