def f(x,A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(100000):
    flag = 1
    for x in range(10000):
        if not f(x,A):
            flag = 0
    if flag:
        print(A)
        break
