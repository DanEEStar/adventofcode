def main():

    digits = [4,	1,	15,	12,	0,	9,	9,	5,	5,	8,	7,	3,	14,	5,	12,	3]
    #digits = [0, 2, 7, 0]

    print(digits)

    states = {}
    state = tuple(digits)

    steps = 0

    while state not in states:
        states[state] = steps
        steps += 1

        m = max(state)
        mi = state.index(m)
        new_state = list(state)
        new_state[mi] = 0

        i = (mi + 1) % len(state)
        while m > 0:
            new_state[i] += 1
            m -= 1
            i += 1
            i %= len(new_state)

        state = tuple(new_state)

    print(steps)
    print(states[tuple([0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10])])






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
