def f(x, A):
    return ((x % 2 == 0) <= (x % 3)) or x+A>=100


for A in range(1, 1000):
    flag = True
    for x in range(1,10000):
        if not f(x, A):
            flag = False
    if flag:
        print(A)
        break

