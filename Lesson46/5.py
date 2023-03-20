def F(x,y,z,w):
    return int(((w <= (not x)) == (z <= y)) and (y or w))


r = range(2)
print('x y z w F')
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = F(x, y, z, w)
                if f:
                    print(x,y,z,w,f)


