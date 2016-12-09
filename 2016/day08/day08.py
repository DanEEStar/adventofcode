import copy
import re
from collections import deque

import pandas as pd

W = 50
H = 6


def parse_line(line):
    if line.startswith('rect'):
        nums = line[5:].split('x')
        return rect, int(nums[0]), int(nums[1])
    elif line.startswith('rotate row'):
        r = r'rotate row y=(\d+) by (\d+)'
        matches = re.match(r, line)
        return rotate_row, int(matches.group(1)), int(matches.group(2))
    elif line.startswith('rotate column'):
        r = r'rotate column x=(\d+) by (\d+)'
        matches = re.match(r, line)
        return rotate_column, int(matches.group(1)), int(matches.group(2))


def create_display(x, y):
    return [[False for _ in range(x)] for _ in range(y)]


def rect(display, a, b):
    for x in xrange(b):
        for y in xrange(a):
            display[x][y] = True
    return display


def rotate_column(display, x, a):
    df = pd.DataFrame(data=display)
    coldata = deque(list(df[x]))
    coldata.rotate(a)
    df[x] = list(coldata)
    return df.as_matrix().tolist()


def rotate_row(display, y, b):
    display = copy.deepcopy(display)
    rowdata = deque(display[y])
    rowdata.rotate(b)
    display[y] = list(rowdata)
    return display


def print_display(display):
    output = ''
    for x in xrange(H):
        for y in xrange(W):
            if display[x][y]:
                output += '#'
            else:
                output += '.'
        output += '\n'
    print(output)


def count_pixels(display):
    pixels = 0
    for x in xrange(H):
        for y in xrange(W):
            if display[x][y]:
                pixels += 1
    return pixels


def main():
    display = create_display(W, H)
    print_display(display)

    with open('input.txt') as input:
        for line in input:
            func, x, y = parse_line(line)
            display = func(display, x, y)

    print_display(display)
    print(count_pixels(display))


if __name__ == '__main__':
    main()
