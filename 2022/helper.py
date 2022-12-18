# Python 3.x Utility Functions

import os
import random
import re
import urllib.request
from collections import defaultdict, deque, abc
from functools import lru_cache
from heapq import heappop, heappush
from itertools import (combinations, chain, islice,
                       takewhile, zip_longest)

letters = 'abcdefghijklmnopqrstuvwxyz'

cache = lru_cache(None)

cat = ''.join

Ø = frozenset()  # Empty set
inf = float('inf')
BIG = 10 ** 999


################ Functions for Input, Parsing

def Input(day, year=2017):
    "Open this day's input file."
    directory = 'advent{}/'.format(year)
    filename = directory + 'input{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        if not os.path.exists(directory):
            os.makedirs(directory)

        urllib.request.urlretrieve("https://raw.githubusercontent.com/norvig/pytudes/master/data/" + filename, filename)
        return Input(day)


def Inputstr(day, year=2017):
    "The contents of this day's input file as a str."
    return Input(day, year).read().rstrip('\n')


def Array(lines):
    "Parse an iterable of str lines into a 2-D array. If `lines` is a str, splitlines."
    if isinstance(lines, str): lines = lines.splitlines()
    return mapt(Vector, lines)


def Vector(line):
    "Parse a str into a tuple of atoms (numbers or str tokens)."
    return mapt(Atom, line.replace(',', ' ').split())


def Integers(text):
    "Return a tuple of all integers in a string."
    return mapt(int, re.findall(r'-?\b\d+\b', text))


def Atom(token):
    "Parse a str token into a number, or leave it as a str."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def error(err=RuntimeError, *args): raise err(*args)


################ Functions on Iterables

def first(iterable, default=None):
    "The first item in an iterable, or default if it is empty."
    return next(iter(iterable), default)


def first_true(iterable, pred=None, default=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true."""
    # first_true([a,b,c], default=x) --> a or b or c or x
    # first_true([a,b], fn, x) --> a if fn(a) else b if fn(b) else x
    return next(filter(pred, iterable), default)


def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)


def upto(iterable, maxval):
    "From a monotonically increasing iterable, generate all the values <= maxval."
    # Why <= maxval rather than < maxval? In part because that's how Ruby's upto does it.
    return takewhile(lambda x: x <= maxval, iterable)


identity = lambda x: x


def groupby(iterable, key=identity):
    "Return a dict of {key(item): [items...]} grouping all items in iterable by keys."
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return groups


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks:
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def overlapping(iterable, n):
    """Generate all (overlapping) n-element subsequences of iterable.
    overlapping('ABCDEFG', 3) --> ABC BCD CDE DEF EFG"""
    if isinstance(iterable, abc.Sequence):
        yield from (iterable[i:i + n] for i in range(len(iterable) + 1 - n))
    else:
        result = deque(maxlen=n)
        for x in iterable:
            result.append(x)
            if len(result) == n:
                yield tuple(result)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return overlapping(iterable, 2)


def sequence(iterable, type=tuple):
    "Coerce iterable to sequence: leave alone if already a sequence, else make it `type`."
    return iterable if isinstance(iterable, abc.Sequence) else type(iterable)


def join(iterable, sep=''):
    "Join the items in iterable, converting each to a string first."
    return sep.join(map(str, iterable))


def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield c


def quantify(iterable, pred=bool):
    "Count how many times the predicate is true."
    return sum(map(pred, iterable))


def length(iterable):
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)


def shuffled(iterable):
    "Create a new list out of iterable, and shuffle it."
    new = list(iterable)
    random.shuffle(new)
    return new


flatten = chain.from_iterable


################ Functional programming

def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def map2d(fn, grid):
    "Apply fn to every element in a 2-dimensional grid."
    return tuple(mapt(fn, row) for row in grid)


def repeat(n, fn, arg, *args, **kwds):
    "Repeat arg = fn(arg) n times, return arg."
    return nth(repeatedly(fn, arg, *args, **kwds), n)


def repeatedly(fn, arg, *args, **kwds):
    "Yield arg, fn(arg), fn(fn(arg)), ..."
    yield arg
    while True:
        arg = fn(arg, *args, **kwds)
        yield arg


def compose(f, g):
    "The function that computes f(g(x))."
    return lambda x: f(g(x))


################ Making immutable objects

class Set(frozenset):
    "A frozenset, but with a prettier printer."

    def __repr__(self): return '{' + join(sorted(self), ', ') + '}'


def canon(items, typ=None):
    "Canonicalize these order-independent items into a hashable canonical form."
    typ = typ or (cat if isinstance(items, str) else tuple)
    return typ(sorted(items))


################ Math Functions

def transpose(matrix): return tuple(zip(*matrix))


def isqrt(n):
    "Integer square root (rounds down)."
    return int(n ** 0.5)


def ints(start, end, step=1):
    "The integers from start to end, inclusive: range(start, end+1)"
    return range(start, end + 1, step)


def floats(start, end, step=1.0):
    "Yield floats from start to end (inclusive), by increments of step."
    m = (1.0 if step >= 0 else -1.0)
    while start * m <= end * m:
        yield start
        start += step


def multiply(numbers):
    "Multiply all the numbers together."
    result = 1
    for n in numbers:
        result *= n
    return result


import operator as op

operations = {'>': op.gt, '>=': op.ge, '==': op.eq,
              '<': op.lt, '<=': op.le, '!=': op.ne,
              '+': op.add, '-': op.sub, '*': op.mul,
              '/': op.truediv, '**': op.pow}


################ 2-D points implemented using (x, y) tuples

def X(point): return point[0]


def Y(point): return point[1]


origin = (0, 0)
HEADINGS = UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


def turn_right(heading): return HEADINGS[HEADINGS.index(heading) - 1]


def turn_around(heading): return HEADINGS[HEADINGS.index(heading) - 2]


def turn_left(heading):  return HEADINGS[HEADINGS.index(heading) - 3]


def add(A, B):
    "Element-wise addition of two n-dimensional vectors."
    return mapt(sum, zip(A, B))


def neighbors4(point):
    "The four neighboring squares."
    x, y = point
    return ((x, y - 1),
            (x - 1, y), (x + 1, y),
            (x, y + 1))


def neighbors8(point):
    "The eight neighboring squares."
    x, y = point
    return ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))


def cityblock_distance(P, Q=origin):
    "Manhatten distance between two points."
    return sum(abs(p - q) for p, q in zip(P, Q))


def distance(P, Q=origin):
    "Straight-line (hypotenuse) distance between two points."
    return sum((p - q) ** 2 for p, q in zip(P, Q)) ** 0.5


def king_distance(P, Q=origin):
    "Number of chess King moves between two points."
    return max(abs(p - q) for p, q in zip(P, Q))


################ Debugging

def trace1(f):
    "Print a trace of the input and output of a function on one line."

    def traced_f(*args):
        result = f(*args)
        print('{}({}) = {}'.format(f.__name__, ', '.join(map(str, args)), result))
        return result

    return traced_f


def grep(pattern, iterable):
    "Print lines from iterable that match pattern."
    for line in iterable:
        if re.search(pattern, line):
            print(line)


class Struct:
    "A structure that can have any fields defined."

    def __init__(self, **entries): self.__dict__.update(entries)

    def __repr__(self):
        fields = ['{}={}'.format(f, self.__dict__[f])
                  for f in sorted(self.__dict__)]
        return 'Struct({})'.format(', '.join(fields))


################ A* and Breadth-First Search (tracking states, not actions)

def always(value): return (lambda *args: value)


def Astar(start, moves_func, h_func, cost_func=always(1)):
    "Find a shortest sequence of states from start to a goal state (where h_func(s) == 0)."
    frontier = [(h_func(start), start)]  # A priority queue, ordered by path length, f = g + h
    previous = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}  # The cost of the best path to a state.
    Path = lambda s: ([] if (s is None) else Path(previous[s]) + [s])
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(s)
        for s2 in moves_func(s):
            g = path_cost[s] + cost_func(s, s2)
            if s2 not in path_cost or g < path_cost[s2]:
                heappush(frontier, (g + h_func(s2), s2))
                path_cost[s2] = g
                previous[s2] = s


def bfs(start, moves_func, goals):
    "Breadth-first search"
    goal_func = (goals if callable(goals) else lambda s: s in goals)
    return Astar(start, moves_func, lambda s: (0 if goal_func(s) else 1))
