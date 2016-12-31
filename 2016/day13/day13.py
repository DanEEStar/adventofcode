import numpy

import astar


def is_space(x, y, key):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += key

    b = bin(n)
    ones = len([c for c in b[2:] if c == '1'])
    return ones % 2 == 0


def make_array(w, h, key):
    result = []
    for y in range(h):
        i = []
        for x in range(w):
            if is_space(x, y, key):
                i.append(0)
            else:
                i.append(1)
        result.append(i)
    return result


def draw_cube(w, h, key):
    output = ''
    for y in range(h):
        for x in range(w):
            if is_space(x, y, key):
                output += '.'
            else:
                output += '#'
        output += '\n'
    return output


def breadth_first(max_depth=50):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),]
    w = 100
    h = 100
    m = make_array(100, 100, 1350)

    visited = {(1,1)}

    for x in range(max_depth):
        for node in visited.copy():
            for i, j in neighbors:
                neighbor = node[0] + i, node[1] + j
                if neighbor[0] < 0 or neighbor[0] >= w or neighbor[1] < 0 or neighbor[1] >= h:
                    continue
                if m[neighbor[0]][neighbor[1]] == 0:
                    visited.add(neighbor)
    print(visited)
    print(len(visited))


def main():
    print(draw_cube(100, 100, 1350))
    nmap = numpy.array(make_array(100, 100, 1350))
    print(astar.astar(nmap, (1, 1), (39, 31)))
    print(len(astar.astar(nmap, (1, 1), (39, 31))))

    breadth_first()


if __name__ == '__main__':
    main()
