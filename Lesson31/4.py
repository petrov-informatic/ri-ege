def M(x):
    alf = '0123456789abcd'
    return int(f'8{alf[x]}12{alf[x]}', 14)


def N(x):
    alf = '0123456789abcd'
    return int(f'8{alf[x]}542', 14)


for A in range(1, 10000):
    for x in range(14):
        if (M(x)+A) % N(x) == 0:
            print(A)
            exit()
