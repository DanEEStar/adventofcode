import math
import re
import urllib.request
from collections import namedtuple
from heapq import heappop, heappush
from itertools import combinations, islice, groupby


def Input(day):
    "Open this day's input file."
    filename = 'advent2016/input{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        return urllib.request.urlopen("http://norvig.com/ipython/" + filename)

def transpose(matrix): return zip(*matrix)

def first(iterable): return next(iter(iterable))

def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)

cat = ''.join

Ø   = frozenset() # Empty set
inf = float('inf')
BIG = 10 ** 999

def grep(pattern, lines):
    "Print lines that match pattern."
    for line in lines:
        if re.search(pattern, line):
            print(line)

def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items)+1):
        for c in combinations(items, r):
            yield c

# 2-D points implemented using (x, y) tuples
def X(point): return point[0]
def Y(point): return point[1]

def neighbors4(point):
    "The four neighbors (without diagonals)."
    x, y = point
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

def neighbors8(point):
    "The eight neighbors (with diagonals)."
    x, y = point
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (X+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def cityblock_distance(p, q=(0, 0)):
    "City block distance between two points."
    return abs(X(p) - X(q)) + abs(Y(p) - Y(q))

def euclidean_distance(p, q=(0, 0)):
    "Euclidean (hypotenuse) distance between two points."
    return math.hypot(X(p) - X(q), Y(p) - Y(q))

def trace1(f):
    "Print a trace of the input and output of a function on one line."
    def traced_f(*args):
        result = f(*args)
        print('{}({}) = {}'.format(f.__name__, ', '.join(map(str, args)), result))
        return result
    return traced_f

def astar_search(start, h_func, moves_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
    frontier  = [(h_func(start), start)] # A priority queue, ordered by path length, f = g + h
    previous  = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}     # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))

def Path(previous, s):
    "Return a list of states that lead to state s, according to the previous dict."
    return ([] if (s is None) else Path(previous, previous[s]) + [s])


Node = namedtuple('Node', ['name', 'children'])


class TreeNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []


nodes = {}
tree_nodes = {}
visited = set()

def cd3(p, q=(0, 0, 0)):
    return abs(X(p) - X(q)) + abs(Y(p) - Y(q)) + abs(p[2] - q[2])


def main():

    with open('input.txt') as input:
        lines = input.read().split('\n')

        test = '''p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>'''

        #lines = test.split('\n')

        p = re.compile(r'p=<(.*?)>, v=<(.*?)>, a=<(.*?)>')

        parts = []

        m = 10000000
        result = -1

        for index, line in enumerate(lines):
            result = p.match(line)

            pos = [int(i.strip()) for i in result.groups()[0].split(',')]
            v = [int(i.strip()) for i in result.groups()[1].split(',')]
            a = [int(i.strip()) for i in result.groups()[2].split(',')]

            parts.append((pos, v, a, [index, True]))

        for x in range(1000):
            for i, part in enumerate(parts):
                #print(parts)
                if parts[3][1]:
                    part[1][0] += part[2][0]
                    part[1][1] += part[2][1]
                    part[1][2] += part[2][2]

                    part[0][0] += part[1][0]
                    part[0][1] += part[1][1]
                    part[0][2] += part[1][2]

            for k, g in groupby(parts, lambda z: z[0]):
                g = list(g)
                if len(g) > 1:
                    for part in g:
                        part[3][1] = False

        for i, part in enumerate(parts):
            n = cd3(part[0])
            if n < m:
                m = n
                result = i

        living = [part for part in parts if part[3][1]]

        print(len(living))


if __name__ == '__main__':
    main()


def test_intersection0():
    assert (0, 4) == intersect((0, 0), (0, 8), (-4, 4), (4, 4))


def test_intersection1():
    assert (0, 4) == intersect((0, 0), (0, 8), (4, 4), (-4, 4))


def test_intersection2():
    assert (0, 4) == intersect((-4, 4), (4, 4), (0, 0), (0, 8))


def test_intersection3():
    assert None is intersect((2, 1), (6, 1), (8, 0), (8, 3))
