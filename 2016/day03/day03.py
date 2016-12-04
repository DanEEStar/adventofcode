def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in xrange(0, len(l), n))


def main():
    triangle_numbers = []
    with open('input.txt') as input:
        for line in input:
            print(line.strip())
            a, b, c = [int(s) for s in line.strip().split(' ') if s != '']

            triangle_numbers.append(a)

    with open('input.txt') as input:
        for line in input:
            print(line.strip())
            a, b, c = [int(s) for s in line.strip().split(' ') if s != '']

            triangle_numbers.append(b)

    with open('input.txt') as input:
        for line in input:
            print(line.strip())
            a, b, c = [int(s) for s in line.strip().split(' ') if s != '']

            triangle_numbers.append(c)

    sum = 0
    numbers = list(chunks(triangle_numbers, 3))
    for t in numbers:
        a, b, c = t
        if a + b > c and a + c > b and b + c > a:
            sum += 1
    print(numbers)
    print(sum)


if __name__ == '__main__':
    main()
