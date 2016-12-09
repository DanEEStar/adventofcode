import itertools
import re


def function():
    return None


def filter_bracket_string(s):
    r = r'\[(.*?)\]'
    hyps = re.findall(r, s)
    s = re.sub(r, '      ', s)
    return s, hyps


def contains_bbannotation(s):
    matches = re.findall(r'([a-z])(.)\2\1', s)
    return any([x[0] != x[1] for x in matches])


def support_tls(s):
    s, hyps = filter_bracket_string(s)
    #print(s, hyps)
    return contains_bbannotation(s) and not any(contains_bbannotation(hyp) for hyp in hyps)


def support_ssl(s):
    r = r'\[(.*?)\]'
    hyps = re.findall(r, s)
    non_hyps = re.sub(r, ' ', s).split(' ')
    print(hyps, non_hyps)
    pos_strings = list('A'.join(x) for x in itertools.product(hyps, non_hyps))
    print(pos_strings)

    r2 = r'([a-z])(.)\1[a-z]*A[a-z]*\2\1\2'
    for s in pos_strings:
        searches = re.search(r2, s)
        if searches is not None:
            if searches.groups()[0] != searches.groups()[1]:
                return True
    return False


def main():
    counter = 0
    with open('input.txt') as input:
        for line in input:
            line = line.strip()
            if support_ssl(line):
                counter += 1

    print(counter)


if __name__ == '__main__':
    main()
