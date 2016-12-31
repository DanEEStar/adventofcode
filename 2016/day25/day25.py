import re

regs = {
    'a': 1,
    'b': 0,
    'c': 0,
    'd': 0
}


output = ''
output_len = 20


def parse_instruction(inst):
    print(inst)
    r = r'(\w+) (-?\w+).?(-?\w+)?'
    matches = re.match(r, inst)
    return matches.groups()


def check_output(output, output_len=output_len):
    for x in range(output_len + 4):
        if x >= len(output):
            return True
        if x % 2 == 0:
            if output[x] != '1':
                return False
        else:
            if output[x] != '1':
                return False
    return True


def reset_regs(avalue):
    return {
        'a': avalue,
        'b': 0,
        'c': 0,
        'd': 0
    }


def run_instruction(inst, cp, instructions):
    if inst[0] == 'cpy':
        if not inst[2].isalpha():
            return cp + 1
        try:
            v = int(inst[1])
            regs[inst[2]] = v
        except ValueError:
            regs[inst[2]] = regs[inst[1]]
        return cp + 1
    if inst[0] == 'inc':
        if not inst[1].isalpha():
            return cp + 1
        regs[inst[1]] += 1
        return cp + 1
    if inst[0] == 'dec':
        if not inst[1].isalpha():
            return cp + 1
        regs[inst[1]] -= 1
        return cp + 1
    if inst[0] == 'jnz':
        v = 0
        if inst[1].isdigit():
            v = int(inst[1])
        else:
            v = regs[inst[1]]
        if v != 0:
            try:
                v = int(inst[2])
                return cp + v
            except ValueError:
                return cp + int(regs[inst[2]])
        return cp + 1
    if inst[0] == 'mpl':
        regs['a'] = int(regs[inst[1]]) * int(regs[inst[2]])
        return cp + 1
    if inst[0] == 'out':
        #print(regs[inst[1]])
        global output
        output += str(regs[inst[1]])
        #print(output)
        if len(output) >= output_len:
            if check_output(output):
                print(output)
                print('found')
                return 99
            return 1000
        return cp + 1
    if inst[0] == 'tgl':
        v = regs[inst[1]]
        print(v)
        print(cp + v)
        if cp + v < 0 or cp + v >= len(instructions):
            return cp + 1
        i = instructions[cp+v]
        print(instructions[cp+v])
        if i[2] is None:
            if i[0] == 'inc':
                instructions[cp+v] = ('dec', i[1], None)
            else:
                instructions[cp+v] = ('inc', i[1], None)
        else:
            if i[0] == 'jnz':
                instructions[cp+v] = ('cpy', i[1], i[2])
            else:
                instructions[cp+v] = ('jnz', i[1], i[2])
        print(instructions[cp+v])
        return cp + 1
    return cp + 1


def main():
    instructions = []
    with open('input.txt') as input:
        content = input.read()
        instructions = [parse_instruction(i) for i in content.split('\n')]
        print(instructions)

    print(instructions)

    for a in xrange(10000000000):
        global regs
        global output
        regs = reset_regs(a)
        output = ''
        cp = 0
        cp = run_instruction(instructions[0], cp, instructions)
        while cp < len(instructions):
            #print(regs)
            #print(cp)
            #print(instructions[cp])
            cp = run_instruction(instructions[cp], cp, instructions)
            if cp == 99:
                print(a)
                break
            #print(cp)
            #time.sleep(0.1)

        #print(cp)
        #print(regs)


if __name__ == '__main__':
    main()
