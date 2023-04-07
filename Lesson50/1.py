def game19(x, i):
    if i > 2 or x > 37:
        return i == 2
    return any([game19(x+1, i+1), game19(x+2, i+1), game19(x*2, i+1)])


r = range(1, 38)
for s in r:
    if game19(s, 0):
        # print(s)
        break


def game20(x, i):
    if i > 3 or x > 37:
        return i == 3
    return (all if i % 2 else any)([game20(x+1, i+1), game20(x+2, i+1), game20(x*2, i+1)])


for s in r:
    if game20(s, 0):
        pass
        # print(s)


def game21(x, i):
    if i > 4 or x > 37:
        return i == 2 or i == 4
    return (all if i % 2 == 0 else any)([game21(x+1, i+1), game21(x+2, i+1), game21(x*2, i+1)])


def game21_1(x, i):
    if i > 2 or x > 37:
        return i == 2
    return (all if i % 2 == 0 else any)([game21_1(x+1, i+1), game21_1(x+2, i+1), game21_1(x*2, i+1)])


for s in r:
    if game21(s, 0) and not game21_1(s, 0):
        print(s)
        break

#19 10
#20 91617
#21 15