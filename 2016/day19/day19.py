from collections import OrderedDict

num_elves = 3001330
max_index = num_elves


def make_init(num_elves):
    d = {}
    for x in xrange(num_elves):
        d[x+1] = 1

    return OrderedDict(d)


def incr_key(current_key):
    result = current_key
    if result >= num_elves:
        result = 0
    return result + 1


def next_key(gift_dict, current_key):
    result = incr_key(current_key)

    while result not in gift_dict:
        result = incr_key(result)

    return result


def step(gift_dict, current_key):
    left_key = next_key(gift_dict, current_key)
    #print(current_key, left_key)

    if gift_dict[current_key] == 0:
        del gift_dict[current_key]
        return False

    gift_dict[current_key] += gift_dict[left_key]
    del gift_dict[left_key]

    if gift_dict[current_key] >= num_elves:
        return True
    else:
        return False


def main():
    gift_dict = make_init(num_elves)

    current_key = 1
    while True:
        #print(current_key)
        #print(gift_dict)
        finished = step(gift_dict, current_key)
        #print('')
        if finished:
            break
        current_key = next_key(gift_dict, current_key)

    print(current_key)


if __name__ == '__main__':
    main()
