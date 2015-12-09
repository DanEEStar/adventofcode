import re
from collections import namedtuple

import itertools

Dist = namedtuple('Dist', ('a', 'b', 'dist'))


def distance_from_line(line):
    m = re.match('(\w+) to (\w+) = (\d+)', line)
    a = m.group(1)
    b = m.group(2)
    dist = int(m.group(3))
    if a < b:
        return Dist(a, b, dist)
    else:
        return Dist(b, a, dist)


def subroute_distance(sub_route, distance):
    if sub_route in distance:
        return distance[sub_route]
    return distance[(sub_route[1], sub_route[0])]


def distance_from_route(route, distances):
    sub_routes = zip(route, route[1:])
    distance = 0
    for sr in sub_routes:
        distance += subroute_distance(sr, distances)

    return distance


def main():
    with open('input.txt') as input:
        locations = set()
        distances = dict()

        for line in input:
            d = distance_from_line(line)
            locations.add(d.a)
            locations.add(d.b)

            distances[(d.a,d.b)] = d.dist

        sorted_locations = sorted(list(locations))

        print(sorted(list(locations)))
        print(distances)

        routes = itertools.permutations(sorted_locations)

        longest_route = 0
        shortest_route = 10000
        for route in routes:
            route_distance = distance_from_route(route, distances)
            if route_distance > longest_route:
                print(route)
                print(route_distance)
                longest_route = route_distance
            if route_distance < shortest_route:
                print(route)
                print(route_distance)
                shortest_route = route_distance

        print(longest_route)


if __name__ == '__main__':
    main()

