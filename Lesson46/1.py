def F(x,y,z):
    return (x == z) or (x <= (y and z))


r = range(2)
print('x y z F')
for x in r:
    for y in r:
        for z in r:
            f = F(x,y,z)
            if not f:
                print(x, y, z, 0)