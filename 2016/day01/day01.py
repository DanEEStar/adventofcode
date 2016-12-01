def intersect(s1, e1, s2, e2):
    if abs(s1[0]) == abs(e1[0]) and abs(s2[1]) == abs(e2[1]):
        if min(s2[0], e2[0]) < min(s1[0], e1[0]) and max(s2[0], e2[0]) > max(s1[0], e1[0]) and \
                        min(s1[1], e1[1]) < min(s2[1], e2[1]) and max(s1[1], e1[1]) > max(s2[1], e2[1]):
            return (s1[0], s2[1])
    if abs(s1[1]) == abs(e1[1]) and abs(s2[0]) == abs(e2[0]):
        # intersect((2, 1), (6, 1), (8, 0), (8, 3)))
        if min(s2[1], e2[1]) < min(s1[1], e1[1]) and max(s2[1], e2[1]) > max(s1[1], e1[1]) and \
                        min(s1[0], e1[0]) < min(s2[0], e2[0]) and max(s1[0], e1[0]) > max(s2[0], e2[0]):
            return (s2[0], s1[1])
    return None


def main():
    directions = ['N', 'E', 'S', 'W']
    current_direction_index = 0
    pos = (0, 0)
    lines = []

    with open('input.txt') as input:
        coordinates = [s.strip() for s in input.read().split(',')]

        for c in coordinates:
            turn_direction = c[0]
            steps = int(c[1:])

            if turn_direction == 'L':
                current_direction_index = (current_direction_index - 1) % 4
            else:
                current_direction_index = (current_direction_index + 1) % 4

            posstart = pos
            if directions[current_direction_index] == 'N':
                pos = (pos[0] + steps, pos[1])
            elif directions[current_direction_index] == 'S':
                pos = (pos[0] - steps, pos[1])
            elif directions[current_direction_index] == 'E':
                pos = (pos[0], pos[1] + steps)
            elif directions[current_direction_index] == 'W':
                pos = (pos[0], pos[1] - steps)
            posend = pos

            print(posstart, posend)

            for line in lines:
                intersection = intersect(line[0], line[1], posstart, posend)
                if intersection:
                    print('----------- finished:')
                    print(line)
                    print(posstart, posend)
                    print(intersection)
                    print(intersection[0] + intersection[1])
                    return

            lines.append((posstart, posend))


if __name__ == '__main__':
    main()

