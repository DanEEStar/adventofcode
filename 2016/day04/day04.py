import string
from collections import Counter


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def handle_line(text):
    try:
        enc = text[:-11]
        checksum = text[-6:-1]
        sector_id = int(text[-10:-7])

        letters = enc.split('-')
        counter = Counter(''.join(letters))
        freqs = sorted(counter.items(), key=lambda x: (x[1], 255 - ord(x[0])), reverse=True)

        checksum2 = ''.join([s[0] for s in freqs])[:5]

        if checksum == checksum2:
            return sector_id, caesar(enc, sector_id % 26)
        return 0, ''
    except:
        return 0, ''


def main():
    with open('input.txt') as input:
        sum = 0
        for line in input:
            sector_id, text = handle_line(line.strip())
            if sector_id > 888:
                print(text, sector_id)
            sum += sector_id

        print(sum)


if __name__ == '__main__':
    main()
