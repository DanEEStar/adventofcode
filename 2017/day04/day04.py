from collections import Counter


def main():
    num_valid = 0
    with open('input.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        for line in lines:
            print(line)
            p_list = line.strip().split(' ')
            sorted_p_list = [''.join(sorted(a)) for a in p_list]
            c = Counter(sorted_p_list)

            if len([v for v in c.values() if v > 1]) == 0:
                num_valid += 1

        print(num_valid)


if __name__ == '__main__':
    main()
