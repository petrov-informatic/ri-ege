def f(x,y,A):
    return y+2*x<A or x>30 or y > 20


for A in range(100):
    flag = True
    for x in range(500):
        for y in range(500):
            if not f(x,y,A):
                flag = False
    if flag:
        print(A)
        break