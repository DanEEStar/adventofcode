import re
import sys
from hashlib import md5


def hexstring(base, number):
    m = md5()
    s = "{}{}".format(base, (number if number is not None else ''))
    m.update(s.encode('ascii'))
    d = m.digest()
    h = "".join("{:02x}".format(c) for c in d)
    return h


hashes = {}


def get_hash(input_string, num):
    if num not in hashes:
        h = hexstring(input_string, num)
        hashes[num] = h
    else:
        h = hashes[num]

    return h


def main():

    hashes = {}
    input_string = 'qzyelonm'

    p3 = re.compile(r'(.)\1\1')

    num_found = 0

    for x in range(100000):
        h3 = get_hash(input_string, x)
        r3 = p3.search(h3)

        if r3:
            p5 = re.compile(r3.group(1)*5)
            for y in range(1000):
                h5 = get_hash(input_string, x + y + 1)

                if p5.search(h5):
                    num_found += 1
                    print(x)
                    print(num_found)
                    print(r3.group(1))
                    print(h3)
                    print(h5)
                    print('------')
                    if num_found == 64:
                        sys.exit(0)
                    break








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
