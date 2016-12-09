def decompress(content):
    result = 0
    i = 0
    while i < len(content):
        c = content[i]

        if c == '(':
            endmarker = content.find(')', i)
            if endmarker >= 0:
                s = content[i+1:endmarker].split('x')
                numchars = int(s[0])
                repeat = int(s[1])
                rs = content[endmarker+1:endmarker+numchars+1]
                print(rs)

                if rs.find(')') >= 0:
                    result += repeat * decompress(rs)
                else:
                    result += repeat * numchars
                i = endmarker + numchars + 1
        else:
            result += 1
            i += 1
    return result


def main():
    with open('input.txt') as input:
        content = input.read()
        print(content)

        result = decompress(content)

    print('')
    print(result)


if __name__ == '__main__':
    main()
