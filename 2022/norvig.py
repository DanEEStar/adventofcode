from collections import Counter, defaultdict, namedtuple, deque, abc
from dataclasses import dataclass
from itertools import permutations, combinations, cycle, chain
from itertools import count as count_from, product as cross_product
from typing import *
from statistics import mean, median
from math import ceil, floor, factorial, gcd, log, log2, log10, sqrt, inf

import matplotlib.pyplot as plt

import ast
import functools
import heapq
import operator
import pathlib
import re
import string
import time

current_year = 2022  # Subdirectory name for input files
lines = '\n'  # For inputs where each record is a line
paragraphs = '\n\n'  # For inputs where each record is a paragraph


def parse(day_or_text: Union[int, str], parser: Callable = str, sep: str = lines, show=6) -> tuple:
    """Split the input text into items separated by `sep`, and apply `parser` to each.
    The first argument is either the text itself, or the day number of a text file."""
    start = time.time()
    text = get_text(day_or_text)
    print_parse_items('Puzzle input', text.splitlines(), show, 'line')
    records = mapt(parser, text.rstrip().split(sep))
    if parser != str or sep != lines:
        print_parse_items('Parsed representation', records, show, f'{type(records[0]).__name__}')
    return records


def get_text(day_or_text: Union[int, str]) -> str:
    """The text used as input to the puzzle: either a string or the day number of a file."""
    if isinstance(day_or_text, int):
        return pathlib.Path(f'day{day_or_text:02d}.txt').read_text()
    else:
        return day_or_text


def print_parse_items(source, items, show: int, name: str, sep="─" * 100):
    """Print verbose output from `parse` for lines or records."""
    if not show:
        return
    count = f'1 {name}' if len(items) == 1 else f'{len(items)} {name}s'
    for line in (sep, f'{source} ➜ {count}:', sep, *items[:show]):
        print(truncate(line))
    if show < len(items):
        print('...')


def truncate(object, width=100) -> str:
    """Use elipsis to truncate `str(object)` to `width` characters, if necessary."""
    string = str(object)
    return string if len(string) <= width else string[:width - 4] + ' ...'


def parse_sections(specs: Iterable) -> Callable:
    """Return a parser that uses the first spec to parse the first section, the second for second, etc.
    Each spec is either parser or [parser, sep]."""
    specs = ([spec] if callable(spec) else spec for spec in specs)
    fns = ((lambda section: parse(section, *spec, show=0)) for spec in specs)
    return lambda section: next(fns)(section)


Char = str  # Intended as the type of a one-character string
Atom = Union[str, float, int]  # The type of a string or number


def ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))


def positive_ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'[0-9]+', text))


def digits(text: str) -> Tuple[int]:
    """A tuple of all the digits in text (as ints 0–9), ignoring non-digit characters."""
    return mapt(int, re.findall(r'[0-9]', text))


def words(text: str) -> Tuple[str]:
    """A tuple of all the alphabetic words in text, ignoring non-letters."""
    return tuple(re.findall(r'[a-zA-Z]+', text))


def atoms(text: str) -> Tuple[Atom]:
    """A tuple of all the atoms (numbers or identifiers) in text. Skip punctuation."""
    return mapt(atom, re.findall(r'[+-]?\d+\.?\d*|\w+', text))


def atom(text: str) -> Atom:
    """Parse text into a single float or int or str."""
    try:
        x = float(text)
        return round(x) if x.is_integer() else x
    except ValueError:
        return text.strip()


def mapt(function: Callable, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))


answers = {}


def answer(puzzle, correct, code: callable):
    """Verify that calling `code` computes the `correct` answer for `puzzle`.
    Record results in the dict `answers`. Prints execution time."""

    def pretty(x): return f'{x:,d}' if is_int(x) else truncate(x)

    start = time.time()
    got = code()
    secs = time.time() - start
    ans = pretty(got)
    msg = f'{secs:5.3f} seconds for ' + (
        f'correct answer: {ans}' if (got == correct) else
        f'WRONG!! ANSWER: {ans}; EXPECTED {pretty(correct)}')
    answers[puzzle] = msg
    print(msg)