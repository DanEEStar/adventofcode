import operator
import re
from collections import defaultdict
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


def main():
    # print(neighbors4((4, 8)))
    # print(neighbors8((4, 8)))
    # print(cityblock_distance((1, 1), (4, 1)))

    p = (51, 42)
    # print(X(p))

    with open('day04.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        lines = sorted(lines)

        guard = 0
        fall = 60
        sleep = defaultdict(lambda: 0)
        sleep_times = defaultdict(lambda: [])
        sleep_times_minutes = defaultdict(lambda: 0)

        for line in lines:
            d, s = parse_line(line)
            if s.endswith('begins shift'):
                guard = parse_line_ints(s)[0]
                # print(guard)
            if s.endswith('falls asleep'):
                fall = d.minute
            if s.endswith('wakes up'):
                sleep[guard] += d.minute - fall
                sleep_times[guard].append((fall, d.minute))
                for x in range(fall, d.minute):
                    sleep_times_minutes[(guard, x)] += 1

        # print(sleep)
        # print(sleep_times)
        print(sleep_times_minutes)

        guard_max = max(sleep.items(), key=operator.itemgetter(1))[0]
        max_sleep_times = sleep_times[guard_max]

        counter = defaultdict(lambda: 0)
        for x in range(60):
            for s1, s2 in max_sleep_times:
                if x in range(s1, s2):
                    counter[x] += 1
        # # print(counter)
        minute = max(counter.items(), key=operator.itemgetter(1))[0]

        # print(minute * guard_max)

        print(max(sleep_times_minutes.items(), key=operator.itemgetter(1)))





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