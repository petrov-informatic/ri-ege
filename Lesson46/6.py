def F(a,b,c):
    return int((a or not c) and (not a or b or c))


r = range(2)
print('a b c F')
for a in r:
    for b in r:
        for c in r:
            print(a, b, c, eval('F(a,b,c)'))