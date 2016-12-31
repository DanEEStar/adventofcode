import re


regs = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}


def parse_instruction(inst):
    r = r'(\w+) (\w+).?(-?\w+)?'
    matches = re.match(r, inst)
    return matches.groups()


def run_instruction(inst, cp):
    if inst[0] == 'cpy':
        if inst[1].isdigit():
            regs[inst[2]] = int(inst[1])
        else:
            regs[inst[2]] = regs[inst[1]]
        return cp + 1
    if inst[0] == 'inc':
        regs[inst[1]] += 1
        return cp + 1
    if inst[0] == 'dec':
        regs[inst[1]] -= 1
        return cp + 1
    if inst[0] == 'jnz':
        v = 0
        if inst[1].isdigit():
            v = int(inst[1])
        else:
            v = regs[inst[1]]
        if v != 0:
            return cp + int(inst[2])
        return cp + 1


def main():
    instructions = []
    with open('input.txt') as input:
        content = input.read()
        instructions = [parse_instruction(i) for i in content.split('\n')]
        print(instructions)

    cp = 0
    cp = run_instruction(instructions[0], cp)
    while cp < len(instructions):
        cp = run_instruction(instructions[cp], cp)

    print(cp)
    print(regs)


if __name__ == '__main__':
    main()
