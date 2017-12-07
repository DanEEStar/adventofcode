from itertools import combinations


def main():

    checksum = 0
    with open('input.txt') as input:
        lines = input.read().split('\n')
        lines = lines[:-1]

        for line in lines:
            line_numbers = [int(n) for n in line.split('\t') if n.strip() != '']

            pairs = combinations(line_numbers, 2)
            for pair in pairs:
                if pair[0] % pair[1] == 0:
                    checksum += pair[0] / pair[1]
                elif pair[1] % pair[0] == 0:
                    checksum += pair[1] / pair[0]

    print(checksum)


if __name__ == '__main__':
    main()
