import re
from collections import namedtuple

import itertools

Dist = namedtuple('Dist', ('a', 'b', 'dist'))


def values_from_line(line):
    # Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
    m = re.match('([A-Z]\w+) can fly (\d+) km/s for (\d+) seconds, .* (\d+) seconds.', line)
    deer = m.group(1)
    speed = int(m.group(2))
    duration = int(m.group(3))
    rest = int(m.group(4))

    return deer, speed, duration, rest


def distance_from_seconds(reindeer, seconds):
    r = seconds % (reindeer[2] + reindeer[3])
    v = seconds / (reindeer[2] + reindeer[3])

    d = v * reindeer[1] * reindeer[2] + min(r, reindeer[2]) * reindeer[1]

    return d


def main():
    with open('input.txt') as input:
        reindeers = []
        score = {}
        for line in input:
            r = values_from_line(line)
            reindeers.append(r)
            score[r[0]] = 0

        for x in range(1, 2504):
            d = 0
            m = None
            for r in reindeers:
                n = distance_from_seconds(r, x)
                if n > d:
                    m = r[0]
                    d = n
            score[m] += 1

    print(score)


if __name__ == '__main__':
    main()

