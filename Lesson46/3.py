def F(x,y,z,w):
    return int(((x <= y) and (y <= w)) or (z == (x or y)))


r = range(2)
print('x y z w F')
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = F(x,y,z,w)
                if not f:
                    print(x,y,z,w, f)
