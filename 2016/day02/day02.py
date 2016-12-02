def function():
    return None


numpad = [
    [1,2,3], [4,5,6], [7,8,9],
]

numpad2 = [
    [-1, -1, 1, -1, -1],
    [-1, 2, 3, 4, -1],
    [5, 6, 7, 8, 9],
    [-1, 'A', 'B', 'C', -1],
    [-1, -1, 'D', -1, -1],
]


def num_to_index(num):
    if num == 1:
        return [0, 2]
    elif num == 2:
        return [1, 1]
    elif num == 3:
        return [1, 2]
    elif num == 4:
        return [1, 3]
    elif num == 5:
        return [2, 0]
    elif num == 6:
        return [2, 1]
    elif num == 7:
        return [2, 2]
    elif num == 8:
        return [2, 3]
    elif num == 9:
        return [2, 4]
    elif num == 'A':
        return [3, 1]
    elif num == 'B':
        return [3, 2]
    elif num == 'C':
        return [3, 3]
    elif num == 'D':
        return [4, 2]

    return -1


numpad2_possible = [
    [0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0],
]


def numpad2_is_possible(x, y):
    return numpad2_possible[x+1][y+1]


def get_number(start, line):
    current = num_to_index(start)
    for k in line:
        if k == 'R':
            current[1] = min(current[1] + 1, 4) if numpad2_is_possible(current[0], current[1] + 1) else current[1]
        elif k == 'L':
            current[1] = max(current[1] - 1, 0) if numpad2_is_possible(current[0], current[1] - 1) else current[1]
        elif k == 'D':
            current[0] = min(current[0] + 1, 4) if numpad2_is_possible(current[0] + 1, current[1]) else current[0]
        elif k == 'U':
            current[0] = max(current[0] - 1, 0) if numpad2_is_possible(current[0] - 1, current[1]) else current[0]
        #print(k)
        #print(current)
        #print(numpad2[current[0]][current[1]])
        #print('------')

    return numpad2[current[0]][current[1]]


def main():
    with open('input.txt') as input:
        line_start = 5
        for line in input:
            print('##########')
            print(line)
            line_start = get_number(line_start, line)
            print(line_start)
            print('##########')
        #content = input.read()
        #print(content)


if __name__ == '__main__':
    main()

