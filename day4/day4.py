import hashlib

base = 'iwrupvqb'

def hexstring(base, number):
    m = hashlib.md5()
    s = "{}{}".format(base, (number if number is not None else ''))
    m.update(s)
    d = m.digest()
    h = "".join("{:02x}".format(ord(c)) for c in d)
    return h

def main():
    for i in range(10000000):
        h = hexstring(base, i)
        if h.startswith('000000'):
            print(h, i)
            break


if __name__ == "__main__":
    main()
