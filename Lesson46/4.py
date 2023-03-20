def F(x,y,z,w):
    return ((y <= x) == (x <= w)) and (z or x)


r = range(2)
print('x y z w F')
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if F(x,y,z,w):
                    print(x,y,z,w,1)