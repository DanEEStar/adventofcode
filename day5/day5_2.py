from collections import defaultdict


def three_substrings(s):
    return [s[i:i+3] for i in range(0, len(s))]


def prefix_count_dict(s):
    d = defaultdict(int)
    triplets = three_substrings(s)

    for triplet in triplets:
        if len(triplet) == 3:
            if triplet[0:2] != triplet[1:3]:
                d[triplet[0:2]] += 1
        elif len(triplet) == 2:
            d[triplet[0:2]] += 1

    return d


def contains_double_pair(s):
    pcd = prefix_count_dict(s)

    values = pcd.values()
    return any([v for v in values if v > 1])


def contains_repeat_letter_in_triplet(s):
    for triplet in three_substrings(s):
        if len(triplet) == 3:
            if triplet[0] == triplet[2]:
                return True
    return False


def is_nice_string(s):
    return contains_double_pair(s) and contains_repeat_letter_in_triplet(s)


def main():
    with open('input.txt') as input:
        result = []
        for line in input:
            if is_nice_string(line):
                result.append(line)
                print('nice: ' + line)
            else:
                print('naughty: ' + line)

        print('num nice strings: {}'.format(len(result)))


if __name__ == '__main__':
    main()

