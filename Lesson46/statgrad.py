def F(x,y,z,w):
    return (x == (not y)) <= ((x and w) == (z and not w))


r = range(2)
print('x y z w F')
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if not F(x,y,z,w):
                    print(x, y, z, w, 0)