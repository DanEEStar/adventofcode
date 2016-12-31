def function():
    return None

input = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
#input = '..^^.'


def is_save(index, inp):
    l = inp[index - 1] if index > 0 else '.'
    c = inp[index]
    r = inp[index + 1] if index < len(inp) - 1 else '.'

    if l == '.' and c == '.' and r == '.':
        return '.'

    if l == '.' and c == '.' and r == '^':
        return '^'

    if l == '^' and c == '.' and r == '.':
        return '^'

    if l == '^' and c == '^' and r == '.':
        return '^'

    if l == '.' and c == '^' and r == '^':
        return '^'

    return '.'


def main():
    out = input + '\n'
    line = input
    for x in range(399999):
        k = ''
        for c in range(len(line)):
            k += is_save(c, line)
        out += (k + '\n')
        line = k

    #print(out)

    #print([x for x in out if out == '.'])
    print(out.count('.'))



if __name__ == '__main__':
    main()
