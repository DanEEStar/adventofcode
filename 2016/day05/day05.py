import hashlib

base = 'reyedfim'


def hexstring(base, number):
    m = hashlib.md5()
    s = "{}{}".format(base, (number if number is not None else ''))
    m.update(s)
    d = m.digest()
    h = "".join("{:02x}".format(ord(c)) for c in d)
    return h


def main():
    num_chars = 0
    password = ['' for _ in range(8)]
    for i in xrange(100000000):
        h = hexstring(base, i)
        if h.startswith('00000'):
            print(h, i, h[5], h[6])
            try:
                pos = int(h[5])
            except:
                pos = -1
            char = h[6]

            if pos >= 0 and pos < 8:
                if password[pos] == '':
                    print('new char')
                    password[pos] = char
                    num_chars += 1
                if num_chars >= 8:
                    break

    print(password)
    print(''.join(password))


if __name__ == "__main__":
    main()