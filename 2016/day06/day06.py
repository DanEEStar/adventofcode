from collections import Counter


def function():
    return None


def main():
    with open('input.txt') as input:
        content = input.readlines()
        col0 = [s[0] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[1] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[2] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[3] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[4] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[5] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[6] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])
        col0 = [s[7] for s in content]
        counter = Counter(''.join(col0))
        print(list(reversed(counter.most_common()))[0])


if __name__ == '__main__':
    main()
