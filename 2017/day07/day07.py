import math
import re
import urllib.request
from collections import defaultdict, namedtuple
from heapq import heappop, heappush
from itertools import combinations, islice


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

def groupby(iterable, key=lambda it: it):
    "Return a dic whose keys are key(it) and whose values are all the elements of iterable with that key."
    dic = defaultdict(list)
    for it in iterable:
        dic[key(it)].append(it)
    return dic

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


Node = namedtuple('Node', ['name', 'weight', 'children'])


class TreeNode:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def total_weight(self):
        return self.weight + sum([c.total_weight() for c in self.children])

    def print_children_weight(self):
        for c in self.children:
            print(c.total_weight())

    def get_unbalanced_node(self):
        children_weights = [w.total_weight() for w in self.children]
        if not all(x == children_weights[0] for x in children_weights):
            print(children_weights)
            print([p.weight for p in self.children])

        for c in self.children:
            c.get_unbalanced_node()

nodes = {}


def main():
    with open('input.txt') as input:
        lines = input.read().split('\n')

        p = re.compile(r'(\w+) \((\d+)\)( -> (.*))?')

        d = {}
        all_children = set()

        for line in lines:
            r = p.match(line)
            (name, weight, _, children) = r.groups()
            children = [pa.strip() for pa in children.split(',')] if children else None
            weight = int(weight)

            node = Node(name, weight, children)
            nodes[name] = node

            if children:
                all_children.update(children)
                d[name] = children

        root = (d.keys() - all_children).pop()
        print(root)

        root_node = nodes[root]
        print(root_node)

        tree_root = add_child_nodes(root_node)

        print(tree_root)
        print(tree_root.total_weight())

        tree_root.get_unbalanced_node()


def add_child_nodes(node):
    r = TreeNode(node.name, node.weight)
    if node.children:
        for node_name in node.children:
            r.children.append(add_child_nodes(nodes[node_name]))
    return r


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
