import re
from collections import defaultdict

message_queue = {0: [], 1: [], 'num_sends': 0}
ips = [0, 0]

num_sends = 0


def processor(lines, program_id):
    regs = defaultdict(int)
    p = re.compile(r'(\w+) (\w) ?(.*)?')

    regs['p'] = program_id

    for i in range(10000000000):
        if ips[program_id] >= len(lines):
            #print('finished')
            break
        line = lines[ips[program_id]]
        result = p.match(line)
        (inst, reg, regnum) = result.groups()

        try:
            val2 = int(regnum)
        except ValueError:
            val2 = regs[regnum]

        #print(program_id, inst, reg, val2)

        if inst == 'set':
            regs[reg] = val2
        elif inst == 'add':
            regs[reg] += val2
        elif inst == 'mul':
            regs[reg] *= val2
        elif inst == 'mod':
            regs[reg] %= val2
        elif inst == 'snd':
            #print(program_id, 'lock acquired')
            values = message_queue[program_id]
            if reg.isdigit():
                values.append(int(reg))
            else:
                values.append(regs[reg])
            print(program_id, len(values))

            if program_id == 1:
                message_queue['num_sends'] += 1
                #print(message_queue['num_sends'])

            #print(program_id, 'lock released')
        elif inst == 'rcv':
            queue_index = (program_id + 1) % 2
            #print(program_id, queue_index)
            values = message_queue[(program_id + 1) % 2]
            if len(values) > 0:
                regs[reg] = values.pop()
                message_queue[(program_id + 1) % 2] = values
            else:
                return True
        elif inst == 'jgz':
            v = regs[reg]
            if v > 0:
                ips[program_id] += val2
                continue

        ips[program_id] += 1

    return False


def main():
    with open('input.txt') as input:
        lines = input.read().split('\n')
        lastsound = 0
        rsnd = 0

        test = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

        test = '''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''

        #lines = test.split('\n')

        while True:
            if not processor(lines, 0): break
            if not processor(lines, 1): break
            if len(message_queue[0])==0 and len(message_queue[1])==0: break


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
