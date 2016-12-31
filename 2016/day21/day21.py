import re
from collections import deque
from itertools import permutations


def parse_line(line):
    if line.startswith('swap position'):
        r = r'swap position (\d+) with position (\d+)'
        matches = re.match(r, line)
        return swap_position, int(matches.group(1)), int(matches.group(2))
    if line.startswith('swap letter'):
        r = r'swap letter (\w) with letter (\w)'
        matches = re.match(r, line)
        return swap_letters, matches.group(1), matches.group(2)
    if line.startswith('rotate left'):
        r = r'rotate left (\d+) step'
        matches = re.match(r, line)
        return rotate_left, int(matches.group(1)), None
    if line.startswith('rotate right'):
        r = r'rotate right (\d+) step'
        matches = re.match(r, line)
        return rotate_right, int(matches.group(1)), None
    if line.startswith('rotate based'):
        r = r'rotate based on position of letter (\w)'
        matches = re.match(r, line)
        return rotate_based, matches.group(1), None
    if line.startswith('reverse positions'):
        r = r'reverse positions (\d+) through (\d+)'
        matches = re.match(r, line)
        return reverse_pos, int(matches.group(1)), int(matches.group(2))
    if line.startswith('move'):
        r = r'move position (\d+) to position (\d+)'
        matches = re.match(r, line)
        return move, int(matches.group(1)), int(matches.group(2))


def swap_position(input, i1, i2):
    x = input[i1]
    y = input[i2]
    ilist = [c for c in input]
    ilist[i1] = y
    ilist[i2] = x
    return ''.join(ilist)


def swap_letters(input, c1, c2):
    def swap(c):
        if c == c1:
            return c2
        if c == c2:
            return c1
        return c

    return ''.join(map(swap, input))


def rotate_left(input, num, _):
    d = deque(input)
    d.rotate(-num)
    return ''.join(list(d))


def rotate_right(input, num, _):
    d = deque(input)
    d.rotate(num)
    return ''.join(list(d))


def rotate_based(input, c, _):
    pos = [i for i,x in enumerate(input) if x == c][0]
    d = deque(input)
    d.rotate(pos+1)
    if pos >= 4:
        d.rotate(1)
    return ''.join(list(d))


def reverse_pos(input, i1, i2):
    ilist = [x for x in input]
    ilist[i1:i2+1] = list(reversed(ilist[i1:i2+1]))
    return ''.join(ilist)


def move(input, i1, i2):
    ilist = [x for x in input]
    c = ilist[i1]
    ilist[i1] = False
    ilist = [x for x in ilist if x]
    ilist.insert(i2, c)
    return ''.join(ilist)


def f_inv(target, insts):
    for p in permutations(target):
        if solve(p, insts) == target:
            return ''.join(p)


def solve(input, insts):
    for inst in insts:
        input = inst[0](input, inst[1], inst[2])
    return input


def main():
    scrambled = 'fbgdceah'
    input = 'abcdefgh'
    insts = []
    with open('input.txt') as text:
        for line in text:
            insts.append(parse_line(line))

    print(solve(input, insts))
    print(f_inv(scrambled, insts))

if __name__ == '__main__':
    main()
