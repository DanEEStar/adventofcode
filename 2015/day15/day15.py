
#Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
sprinkles = (5, -1, 0, 0, 5)
#PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
peanut = (-1, 3, 0, 0, 1)
#Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
frosting = (0, -1, 4, 0, 6)
#Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
sugar = (-1, 0, 0, 2, 8)


def cookie_sum(sp, pe, fr, su):
    capacity = sprinkles[0] * sp + peanut[0] * pe + frosting[0] * fr + sugar[0] * su
    durability = sprinkles[1] * sp + peanut[1] * pe + frosting[1] * fr + sugar[1] * su
    flavor = sprinkles[2] * sp + peanut[2] * pe + frosting[2] * fr + sugar[2] * su
    texture = sprinkles[3] * sp + peanut[3] * pe + frosting[3] * fr + sugar[3] * su
    calories = sprinkles[4] * sp + peanut[4] * pe + frosting[4] * fr + sugar[4] * su

    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0 and calories == 500:
        return capacity * durability * flavor * texture
    return 0


def main():
    p = 0
    high_cookie = 0
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                for d in range(1, 100):
                    s = a + b + c + d
                    if s == 100:
                        p += 1
                        cs = cookie_sum(a, b, c, d)

                        high_cookie = max(high_cookie, cs)
    print(high_cookie)


if __name__ == '__main__':
    main()
