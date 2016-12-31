import re
from itertools import ifilter


def parse_line(line):
    if line.startswith('bot'):
        # bot 186 gives low to bot 96 and high to bot 33
        # bot 127 gives low to output 1 and high to bot 180
        r = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'
        matches = re.match(r, line)
        return matches.group(1), matches.group(2), matches.group(3), matches.group(4), matches.group(5)
    elif line.startswith('value'):
        # value 19 goes to bot 61
        r = r'value (\d+) goes to bot (\d+)'
        matches = re.match(r, line)
        return int(matches.group(1)), matches.group(2)


def bot_set_value(v, vbot):
    if v > vbot[1]:
        assert vbot[0] == -1
        vbot = (vbot[1], v)
    else:
        assert vbot[0] == -1
        vbot = (v, vbot[1])
    return vbot


def bot_two_values(bots):
    for key, value in bots.iteritems():
        if value[0] >= 0 and value[1] >= 0:
            return key, value
    return None


def run_give_instruction(inst, bots, output):
    ibot = inst[0]
    ivbot = bots[ibot]
    bots[ibot] = (-1, -1)

    o1 = inst[1]
    if o1 == 'output':
        output[inst[2]] = ivbot[0]
    else:
        vbot = bots.get(inst[2], (-1, -1))
        bots[inst[2]] = bot_set_value(ivbot[0], vbot)

    o2 = inst[3]
    if o2 == 'output':
        output[inst[4]] = ivbot[1]
    else:
        vbot = bots.get(inst[4], (-1, -1))
        bots[inst[4]] = bot_set_value(ivbot[1], vbot)


def run_give_simulation(bots):
    t = bot_two_values(bots)
    while t is not None:
        bot = t[0]
        v = t[1]
        if v == (17, 61):
            print('found: ', bot)
        inst = next(ifilter(lambda x: x[0] == bot, instructions), None)
        run_give_instruction(inst, bots, output)
        t = bot_two_values(bots)


bots = {}
output = {}
instructions = []


def main():

    with open('input.txt') as input:
        for line in input:
            inst = parse_line(line)
            instructions.append(inst)

    for inst in instructions:
        if len(inst) == 2:
            vbot = bots.get(inst[1], (-1, -1))
            v = inst[0]
            bots[inst[1]] = bot_set_value(v, vbot)

        run_give_simulation(bots)

    run_give_simulation(bots)

    print(bots)
    print(output)

    print(output['0'] * output['1'] * output['2'])


if __name__ == '__main__':
    main()
