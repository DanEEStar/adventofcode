import math


def intersect(s1, e1, s2, e2):
    """
    returns intersection point of vertical and horizontal line
    :param s1: startpoint tuple
    :param e1: endpoint tuple
    :param s2: startpoint tuple
    :param e2: endpoint tuple
    :return: intersection point or None
    """
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


def intersectLines( pt1, pt2, ptA, ptB ):
    """ this returns the intersection of Line(pt1,pt2) and Line(ptA,ptB)

        returns a tuple: (xi, yi, valid, r, s), where
        (xi, yi) is the intersection
        r is the scalar multiple such that (xi,yi) = pt1 + r*(pt2-pt1)
        s is the scalar multiple such that (xi,yi) = pt1 + s*(ptB-ptA)
            valid == 0 if there are 0 or inf. intersections (invalid)
            valid == 1 if it has a unique intersection ON the segment    """

    DET_TOLERANCE = 0.00000001

    # the first line is pt1 + r*(pt2-pt1)
    # in component form:
    x1, y1 = pt1;   x2, y2 = pt2
    dx1 = x2 - x1;  dy1 = y2 - y1

    # the second line is ptA + s*(ptB-ptA)
    x, y = ptA;   xB, yB = ptB;
    dx = xB - x;  dy = yB - y;

    # we need to find the (typically unique) values of r and s
    # that will satisfy
    #
    # (x1, y1) + r(dx1, dy1) = (x, y) + s(dx, dy)
    #
    # which is the same as
    #
    #    [ dx1  -dx ][ r ] = [ x-x1 ]
    #    [ dy1  -dy ][ s ] = [ y-y1 ]
    #
    # whose solution is
    #
    #    [ r ] = _1_  [  -dy   dx ] [ x-x1 ]
    #    [ s ] = DET  [ -dy1  dx1 ] [ y-y1 ]
    #
    # where DET = (-dx1 * dy + dy1 * dx)
    #
    # if DET is too small, they're parallel
    #
    DET = (-dx1 * dy + dy1 * dx)

    if math.fabs(DET) < DET_TOLERANCE: return (0,0,0,0,0)

    # now, the determinant should be OK
    DETinv = 1.0/DET

    # find the scalar amount along the "self" segment
    r = DETinv * (-dy  * (x-x1) +  dx * (y-y1))

    # find the scalar amount along the input line
    s = DETinv * (-dy1 * (x-x1) + dx1 * (y-y1))

    # return the average of the two descriptions
    xi = (x1 + r*dx1 + x + s*dx)/2.0
    yi = (y1 + r*dy1 + y + s*dy)/2.0
    return ( xi, yi, 1, r, s )


def complex_to_tuple(cn):
    return cn.real, cn.imag


def main():
    N, S, E, W = 1j, -1j, 1, -1 # Unit vectors for headings
    current_direction = N
    pos = 0
    lines = []

    with open('input.txt') as input:
        coordinates = [s.strip() for s in input.read().split(',')]

        for c in coordinates:
            turn_direction = c[0]
            steps = int(c[1:])
            posstart = pos
            if turn_direction == 'L':
                current_direction *= N
            else:
                current_direction *= S

            pos += current_direction * steps

            print(pos)

            for line in lines:
                intersection = intersect(line[0], line[1], (posstart.real, posstart.imag), (pos.real, pos.imag))
                i2 = intersectLines(line[0], line[1], (posstart.real, posstart.imag), (pos.real, pos.imag))
                print(i2)
                if intersection:
                    print('----------- finished:')
                    print(line)
                    print(posstart, pos)
                    print(intersection)
                    print(intersection[0] + intersection[1])
                    return

            lines.append((complex_to_tuple(posstart), complex_to_tuple(pos)))

    print(int(pos.real + pos.imag))


if __name__ == '__main__':
    main()

