def f(x, A):
    return (x & 51 == 0) or ((x & 41 != 0) or (x & A == 0))


for A in range(100, -1, -1):
    flag = True
    for x in range(100000):
        if not f(x, A):
            flag = False
    if flag:
        print(A)
        break

